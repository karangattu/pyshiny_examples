import json
import logging
import os
import re
import socket
import subprocess
import sys
import threading
import time
from pathlib import Path

import requests
from anthropic import Anthropic
from dotenv import load_dotenv
from lzstring import LZString


def setup_logging():
    load_dotenv()
    logging.basicConfig(
        filename="anthropic.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def parse_command_line_args():
    if len(sys.argv) < 2 or sys.argv[1] not in ["express", "core"]:
        print(
            "Usage: python create_apps_using_llm.py [express|core] [haiku3|haiku3.5|sonnet]"
        )
        sys.exit(1)

    # Map user-friendly names to actual model names
    model_mapping = {
        "haiku3": "claude-3-haiku-20240307",
        "haiku3.5": "claude-3-5-haiku-20241022",
        "sonnet": "claude-3-5-sonnet-20241022",
    }

    if len(sys.argv) == 3:
        user_model = sys.argv[2].lower()
        if user_model in model_mapping:
            model_type = model_mapping[user_model]
        else:
            print(f"Invalid model type. Choose from: {', '.join(model_mapping.keys())}")
            sys.exit(1)

    return sys.argv[1], model_type


def load_documentation(app_type):
    with open(f"documentation_{app_type}.json", "r") as f:
        documentation = f.read()
    return documentation


def read_system_prompt(app_type):
    with open(f"SYSTEM_PROMPT_{app_type}.md", "r") as f:
        system_prompt_file_contents = f.read()

    documentation = load_documentation(app_type)
    system_prompt = [
        {
            "type": "text",
            "text": system_prompt_file_contents,
        },
        {
            "type": "text",
            "text": f"Here is the function reference documentation for Shiny for Python: {documentation}",
            "cache_control": {"type": "ephemeral"},
        },
    ]
    return system_prompt


def calculate_total_cost(
    cache_creation_input_tokens,
    cache_read_input_tokens,
    input_tokens,
    output_tokens,
    model="claude-3-haiku-20240307",
):
    """
    Calculate the total cost of the API call based on the usage of tokens and model.

    Args:
        cache_creation_input_tokens: Number of tokens used for cache creation
        cache_read_input_tokens: Number of tokens read from cache
        input_tokens: Number of input tokens
        output_tokens: Number of output tokens
        model: Model name (default: claude-3-haiku-20240307)
    """
    # Pricing per model from https://docs.anthropic.com/en/docs/about-claude/models
    model_prices = {
        "claude-3-5-haiku-20241022": {
            "cache_creation_input": 0.00000125,
            "cache_read_input": 0.00000010,
            "input": 0.00000100,
            "output": 0.00000500,
        },
        "claude-3-5-sonnet-20241022": {
            "cache_creation_input": 0.00000375,
            "cache_read_input": 0.00000030,
            "input": 0.00000300,
            "output": 0.00001500,
        },
        "claude-3-haiku-20240307": {
            "cache_creation_input": 0.0000003,
            "cache_read_input": 0.00000003,
            "input": 0.00000025,
            "output": 0.00000125,
        },
    }

    if model not in model_prices:
        raise ValueError(
            f"Unknown model: {model}. Available models: {list(model_prices.keys())}"
        )

    prices = model_prices[model]
    total_cost = (
        cache_creation_input_tokens * prices["cache_creation_input"]
        + cache_read_input_tokens * prices["cache_read_input"]
        + input_tokens * prices["input"]
        + output_tokens * prices["output"]
    )
    return total_cost


def run_pyright(file_path):
    try:
        # Run pyright with JSON output
        result = subprocess.run(
            ["pyright", file_path, "--outputjson"],
            capture_output=True,
            text=True,
            check=False,
        )

        # Parse the JSON output
        try:
            pyright_output = json.loads(result.stdout)
        except json.JSONDecodeError:
            # If JSON parsing fails, create a custom error dictionary
            return {
                "error": "Failed to parse pyright output",
                "raw_output": result.stdout,
                "raw_error": result.stderr,
            }

        return pyright_output

    except FileNotFoundError:
        # Handle case where pyright is not installed
        return {
            "error": "Pyright is not installed. Please install it using: pip install pyright"
        }
    except Exception as e:
        # Catch any other unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}


def run_shiny_app(
    script_path,
    port=8000,
    timeout=8,
    success_timeout=5,
    verbose=True,
):
    if is_port_in_use(port):
        if verbose:
            logging.info(f"Error: Port {port} is already in use.")
        return False, f"Port {port} is already in use."

    process, process_created = start_shiny_app(script_path, port)
    if not process_created:
        if verbose:
            logging.info("Failed to start Shiny app process.")
        return False, "Failed to start Shiny app process."

    return monitor_app_logs(process, timeout, success_timeout, verbose)


def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0


def start_shiny_app(script_path, port=8000):
    try:
        process = subprocess.Popen(
            ["shiny", "run", script_path, "--port", str(port)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return process, True
    except Exception as e:
        logging.info(f"Error starting Shiny app: {e}")
        return None, False


def monitor_app_logs(process, timeout, success_timeout, verbose):
    if not process:
        return False, "No process found"

    stdout_lines = []
    stderr_lines = []
    startup_successful = False
    monitor_active = threading.Event()
    monitor_active.set()

    def read_output(stream, lines_list):
        while monitor_active.is_set():
            try:
                line = stream.readline()
                if line:
                    lines_list.append(line.strip())
                    if verbose:
                        logging.info(f"STREAM: {line.strip()}")
                else:
                    time.sleep(0.1)
            except ValueError:
                break
            except Exception as e:
                if verbose:
                    logging.info(f"Exception in read_output thread: {e}")
                break

    stdout_thread = threading.Thread(
        target=read_output, args=(process.stdout, stdout_lines)
    )
    stderr_thread = threading.Thread(
        target=read_output, args=(process.stderr, stderr_lines)
    )

    stdout_thread.daemon = True
    stderr_thread.daemon = True

    stdout_thread.start()
    stderr_thread.start()

    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(f"http://localhost:{8000}", timeout=5)
            if response.status_code == 200:
                if verbose:
                    logging.info("Shiny app started successfully within timeout.")
                startup_successful = True

                time.sleep(success_timeout)
                if verbose:
                    logging.info("Terminating app after successful startup...")
                process.terminate()
                process.wait(timeout=2)
                break
        except requests.exceptions.RequestException:
            time.sleep(0.1)

    monitor_active.clear()
    stdout_thread.join()
    stderr_thread.join()

    if process.poll() is None:
        if verbose:
            logging.info("Terminating app after timeout...")
        try:
            process.terminate()
            process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            if verbose:
                logging.info("App did not terminate gracefully, killing...")
            process.kill()
            process.wait()

    if not startup_successful:
        error_message = ""
        for line in stderr_lines:
            error_message += line + "\n"
        if verbose:
            logging.info("Error starting Shiny app:")
            logging.info(error_message)
    else:
        error_message = ""

    if verbose:
        logging.info("\n--- App Termination Summary ---")
        logging.info(f"Exit Code: {process.returncode}")
        logging.info("--- Captured STDOUT ---")
        for line in stdout_lines:
            logging.info(line)
        logging.info("--- Captured STDERR ---")
        for line in stderr_lines:
            logging.info(line)

    return (startup_successful, error_message)


def analyze_pyright_results(results):
    error_list = []
    if results["summary"]["errorCount"] > 1:
        for i in results["generalDiagnostics"][1:]:
            error_list.append(
                f'Line number: {i["range"]["start"]["line"]} has error: {i["message"]}'
            )
        return error_list

    logging.info("\nNo type errors found!")
    return error_list


def extract_code_and_description(response):
    """
    Extracts the Python code block and the description from the response string.
    """
    code_match = re.search(r"```python(.*?)```", response, re.DOTALL)
    code = code_match.group(1).strip() if code_match else ""
    description = re.sub(r"```python.*?```", "", response, flags=re.DOTALL).strip()
    return code, description


def python_app_to_shinylive_url(app_text: str) -> str:
    # Create a JSON object with the application details
    app_data = [
        {
            "name": "app.py",
            "content": app_text,
        },
        {
            "name": "requirements.txt",
            "content": """
matplotlib
numpy
pandas
plotly
seaborn

            """,
        },
    ]

    json_string = json.dumps(app_data)
    compressed_app = LZString.compressToEncodedURIComponent(json_string)

    # Construct the final URL
    url = f"https://shinylive.io/py/app/#h=0&code={compressed_app}"

    return url


def create_app_files(file_dir, code, description):
    """
    Creates app.py and DESCRIPTION.md files with the extracted code and description.
    """
    # Create or overwrite app.py in file_dir
    with open(f"{file_dir}/app.py", "w") as f:
        f.write(code)

    # create a requirements.txt file in file_dir
    with open(f"{file_dir}/requirements.txt", "w") as f:
        f.write(
            """
altair
folium
matplotlib
numpy
pandas
plotly
plotnine
requests
seaborn
shinywidgets
"""
        )

    # Create or overwrite DESCRIPTION.md
    with open(f"{file_dir}/DESCRIPTION.md", "w") as f:
        f.write(description)

    # append a line to the DESCRIPTION.md file
    with open(f"{file_dir}/DESCRIPTION.md", "a") as f:
        f.write(
            f"""
## Preview the app on [Shinylive]({python_app_to_shinylive_url(code)})
"""
        )


def process_directory(directory, system_prompt, model):
    """Process a single directory to create and validate a Shiny app."""
    prompt_file = Path(f"{directory}/PROMPT.md")
    if not (os.path.isdir(directory) and prompt_file.is_file()):
        return

    if os.path.exists(f"{directory}/app.py"):
        return

    logging.info(f"Processing directory: {directory}")
    with open(prompt_file, "r") as f:
        prompt = f.read()

    # Generate initial app
    code, description = generate_shiny_app(prompt, system_prompt, model)
    create_app_files(directory, code, description)

    # Test and fix if needed
    success, error_message = run_shiny_app(
        f"{directory}/app.py", port=8000, timeout=5, success_timeout=5
    )
    if not success:
        logging.info(f"App failed to run in {directory}, attempting fix")
        code, description_2 = fix_shiny_app(code, error_message, system_prompt, model)
        create_app_files(directory, code, description)


def generate_shiny_app(prompt, system_prompt, model):
    """Generate a Shiny app using the LLM."""
    user_prompt = f"""
    Leverage Shiny for Python function reference documentation and make a Shiny for Python app for the following requirements: {prompt}. 
    Please do not use external files for accessing data, make up some data for use in the app.
    """

    messages = get_llm_response(user_prompt, system_prompt, model)
    update_token_counts(messages.usage, model)
    return extract_code_and_description(messages.content[0].text)


def fix_shiny_app(code, error_message, system_prompt, model):
    """Fix a failing Shiny app using the LLM."""
    user_prompt = f"Running this code for Shiny for Python: \n {code} \n resulted in an error: {error_message}. Please fix it to make it work. Provide complete code for the same"

    messages = get_llm_response(user_prompt, system_prompt, model)
    update_token_counts(messages.usage, model)
    return extract_code_and_description(messages.content[0].text)


def get_llm_response(prompt, system_prompt, model):
    """Get response from the LLM."""
    # start script here
    client = Anthropic()

    messages = client.beta.prompt_caching.messages.create(
        model=model,
        max_tokens=4096,
        system=system_prompt,
        temperature=0.5,
        messages=[{"role": "user", "content": prompt}],
    )
    return messages


def update_token_counts(usage, model):
    """Update global token counts and log usage."""
    global total_cache_creation_input_tokens, total_cache_read_input_tokens, total_input_tokens, total_output_tokens

    total_cache_creation_input_tokens += usage.cache_creation_input_tokens
    total_cache_read_input_tokens += usage.cache_read_input_tokens
    total_input_tokens += usage.input_tokens
    total_output_tokens += usage.output_tokens

    logging.info("==========")
    logging.info(f"Cache creation input tokens: {usage.cache_creation_input_tokens}")
    logging.info(f"Cache read input tokens: {usage.cache_read_input_tokens}")
    logging.info(f"Output tokens: {usage.output_tokens}")
    logging.info(f"Input tokens: {usage.input_tokens}")
    logging.info("==========")

    cost = calculate_total_cost(
        total_cache_creation_input_tokens,
        total_cache_read_input_tokens,
        total_input_tokens,
        total_output_tokens,
        model=model,
    )
    print(f"Incurred costs till now: ${cost}")


total_cache_creation_input_tokens = 0
total_cache_read_input_tokens = 0
total_input_tokens = 0
total_output_tokens = 0

setup_logging()
app_type, model = parse_command_line_args()
system_prompt = read_system_prompt(app_type=app_type)

for directory in os.listdir():
    process_directory(directory, system_prompt, model)
