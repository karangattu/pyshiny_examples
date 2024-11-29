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

load_dotenv()

logging.basicConfig(
    filename="anthropic.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# get argument to python script
if len(sys.argv) < 2:
    print("Usage: python create_apps_using_llm.py app_type")
    sys.exit(1)
else:
    app_type = sys.argv[1]
    if app_type not in ["express", "core"]:
        print("Invalid app type. Use 'express' or 'core'.")
        sys.exit(1)


client = Anthropic()

total_cache_creation_input_tokens = 0
total_cache_read_input_tokens = 0
total_input_tokens = 0
total_output_tokens = 0


def calculate_total_cost(
    cache_creation_input_tokens, cache_read_input_tokens, input_tokens, output_tokens
):
    """
    Calculate the total cost of the API call based on the usage of tokens.
    """
    # pricing based on Haiku 3 model - https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching#tracking-cache-performance:~:text=Claude%203%20Haiku,%241.25%20/%20MTok
    cost_per_cache_creation_input_token = 0.0000003
    cost_per_cache_read_input_token = 0.00000003
    cost_per_input_token = 0.00000025
    cost_per_output_token = 0.00000125
    total_cost = (
        cache_creation_input_tokens * cost_per_cache_creation_input_token
        + cache_read_input_tokens * cost_per_cache_read_input_token
        + output_tokens * cost_per_input_token
        + input_tokens * cost_per_output_token
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
            print(f"Error: Port {port} is already in use.")
        return False, f"Port {port} is already in use."

    process, process_created = start_shiny_app(script_path, port)
    if not process_created:
        if verbose:
            print("Failed to start Shiny app process.")
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
        print(f"Error starting Shiny app: {e}")
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
                        print(f"STREAM: {line.strip()}")
                else:
                    time.sleep(0.1)
            except ValueError:
                break
            except Exception as e:
                if verbose:
                    print(f"Exception in read_output thread: {e}")
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
                    print("Shiny app started successfully within timeout.")
                startup_successful = True

                time.sleep(success_timeout)
                if verbose:
                    print("Terminating app after successful startup...")
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
            print("Terminating app after timeout...")
        try:
            process.terminate()
            process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            if verbose:
                print("App did not terminate gracefully, killing...")
            process.kill()
            process.wait()

    if not startup_successful:
        error_message = ""
        for line in stderr_lines:
            error_message += line + "\n"
        if verbose:
            print("Error starting Shiny app:")
            print(error_message)
    else:
        error_message = ""

    if verbose:
        print("\n--- App Termination Summary ---")
        print("Exit Code:", process.returncode)
        print("--- Captured STDOUT ---")
        for line in stdout_lines:
            print(line)
        print("--- Captured STDERR ---")
        for line in stderr_lines:
            print(line)

    return (startup_successful, error_message)


def analyze_pyright_results(results):
    error_list = []
    if results["summary"]["errorCount"] > 1:
        for i in results["generalDiagnostics"][1:]:
            error_list.append(
                f'Line number: {i["range"]["start"]["line"]} has error: {i["message"]}'
            )
        return error_list

    print("\nNo type errors found!")
    return error_list


def extract_code_and_description(response):
    """
    Extracts the Python code block and the description from the response string.
    """
    code_match = re.search(r"```python(.*?)```", response, re.DOTALL)
    code = code_match.group(1).strip() if code_match else ""
    description = re.sub(r"```python.*?```", "", response, flags=re.DOTALL).strip()
    return code, description


def create_app_files(file_dir, code, description):
    """
    Creates app.py and DESCRIPTION.md files with the extracted code and description.
    """
    # Create or overwrite app.py in file_dir
    with open(f"{file_dir}/app.py", "w") as f:
        f.write(code)

    # Create or overwrite DESCRIPTION.md
    with open(f"{file_dir}/DESCRIPTION.md", "w") as f:
        f.write(description)


# read the contents of documentation_core.json
with open(f"documentation_{app_type}.json", "r") as f:
    documentation = f.read()

system_prompt = """
You are an expert Python developer specializing in Shiny for Python application development. Your primary objective is to generate high-quality, production-ready Shiny for Python applications with the following comprehensive guidelines:

Purpose and Scope:
- Generate production-ready Shiny for Python applications
- Demonstrate deep understanding of Shiny for Python's capabilities and best practices

Technical Constraints:
1. Library Adherence
   - Use ONLY official Shiny for Python library functions
   - Validate all code against current function reference documentation
   - Avoid R-to-Python direct translations

2. Code Generation Principles
   - Generate complete, runnable applications
   - Include comprehensive error handling
   - Optimize for readability and maintainability

3. Data Handling
   - Generate realistic synthetic datasets using faker or make random datasets matching application context

4. Visualization and Interactivity
   - Create responsive, accessible interfaces
   - Use Plotly or Altair for advanced visualizations
   - Use font Awesome for icons
   To use Font Awesome icons, ensure you've added the Font Awesome CSS file to your HTML head:
```Python
app_ui = ui.page_fluid(
    ui.head_content(
        ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">')
    ),
    ...
)
```
   - Use https://picsum.photos/200/300 for placeholder images

5. Performance Considerations
   - Implement efficient reactive programming patterns
   - Use lazy loading and caching where applicable

Deliverable Specification:
- Include concise comments explaining complex logic
- List all required package dependencies

Prohibited Practices:
- No placeholder or stub code
- Avoid speculative or hypothetical implementations
- Do not include unimplemented features
- No external API calls without explicit request
- No hardcoded credentials or sensitive information
- No unnessary imports or dependencies
- Do not use external files for accessing data, make up some data for use in the app

Verification Criteria:
- Code must be syntactically correct
- All dependencies must be pip-installable
- User interface should be intuitive and self-explanatory

Response Format:
1. Comprehensive code artifact
2. Brief technical description
3. Installation and execution instructions
4. Package dependencies list

Context Awareness:
- Adapt implementation to specific user requirements
- Infer unstated but logical application needs
- Provide pragmatic, real-world solutions

Output Quality Metrics:
- 100% functional code
- Clean, PEP 8 compliant implementation
- Minimal external dependencies
"""

for directory in os.listdir():
    if os.path.isdir(directory):
        prompt_file = Path(f"{directory}/PROMPT.md")
        if prompt_file.is_file():
            with open(prompt_file, "r") as f:
                prompt = f.read()
            if not os.path.exists(f"{directory}/app.py"):
                print(f"Directory: {directory}")
                system_prompt = [
                    {
                        "type": "text",
                        "text": f"Here is the function reference documentation for Shiny for Python: {documentation}",
                        "cache_control": {"type": "ephemeral"},
                    },
                ]
                maximum_tokens = 4096
                moderate_temperature = 0.2
                claude_model_used = "claude-3-haiku-20240307"
                user_prompt = f"""
Leverage Shiny for Python function reference documentation and make a Shiny for Python app for the following requirements: {prompt}. Please do not use external files for accessing data, make up some data for use in the app.
"""
                messages = client.beta.prompt_caching.messages.create(
                    model=claude_model_used,
                    max_tokens=maximum_tokens,
                    system=system_prompt,
                    temperature=moderate_temperature,
                    messages=[
                        {
                            "role": "user",
                            "content": user_prompt,
                        }
                    ],
                )
                logging.info("==========")
                logging.info(f"Directory: {directory}")
                logging.info(
                    f"Cache creation input tokens used: {messages.usage.cache_creation_input_tokens}"
                )
                logging.info(
                    f"Cache read input tokens used: {messages.usage.cache_read_input_tokens}"
                )
                logging.info(f"Output tokens used: {messages.usage.output_tokens}")
                logging.info(f"Input tokens used: {messages.usage.input_tokens}")
                logging.info("==========")
                total_cache_creation_input_tokens += (
                    messages.usage.cache_creation_input_tokens
                )
                total_cache_read_input_tokens += messages.usage.cache_read_input_tokens
                total_input_tokens += messages.usage.input_tokens
                total_output_tokens += messages.usage.output_tokens
                print(
                    f"Incurred costs till now: ${calculate_total_cost(total_cache_creation_input_tokens, total_cache_read_input_tokens, total_input_tokens, total_output_tokens)}"
                )
                response = messages.content[0].text
                code, description = extract_code_and_description(response)
                create_app_files(directory, code, description)

                success, error_message = run_shiny_app(
                    f"{directory}/app.py", port=8000, timeout=5, success_timeout=5
                )
                if not success:
                    logging.info(
                        f"App did not run hence prompting the LLM to fix it for {directory}"
                    )
                    # if app resulted in an error during startup, prompt the LLM to fix it
                    user_prompt_error = f"Running this code for Shiny for Python: \n {code} \n resulted in an error: {error_message}. Please fix it to make it work. Provide complete code for the same"
                    messages = client.beta.prompt_caching.messages.create(
                        model=claude_model_used,
                        max_tokens=maximum_tokens,
                        system=system_prompt,
                        temperature=moderate_temperature,
                        messages=[
                            {
                                "role": "user",
                                "content": user_prompt_error,
                            }
                        ],
                    )
                    logging.info("==========")
                    logging.info(f"Directory when debugging error: {directory}")
                    logging.info(
                        f"Cache creation input tokens used: {messages.usage.cache_creation_input_tokens}"
                    )
                    logging.info(
                        f"Cache read input tokens used: {messages.usage.cache_read_input_tokens}"
                    )
                    logging.info(f"Output tokens used: {messages.usage.output_tokens}")
                    logging.info(f"Input tokens used: {messages.usage.input_tokens}")
                    logging.info("==========")
                    total_cache_creation_input_tokens += (
                        messages.usage.cache_creation_input_tokens
                    )
                    total_cache_read_input_tokens += (
                        messages.usage.cache_read_input_tokens
                    )
                    total_input_tokens += messages.usage.input_tokens
                    total_output_tokens += messages.usage.output_tokens
                    print(
                        f"Incurred costs till now: ${calculate_total_cost(total_cache_creation_input_tokens, total_cache_read_input_tokens, total_input_tokens, total_output_tokens)}"
                    )
                    response = messages.content[0].text
                    # save the modified app code now
                    code, description2 = extract_code_and_description(response)
                    create_app_files(directory, code, description)
