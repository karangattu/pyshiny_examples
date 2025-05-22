from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, List, Tuple
import json
import logging
import re
import socket
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests
from anthropic import Anthropic
from dotenv import load_dotenv


class AppType(Enum):
    EXPRESS = "express"
    CORE = "core"
    TESTING = "testing"
    CORE2EXPRESS = "core2express"
    EXPRESS2CORE = "express2core"


@dataclass
class ModelConfig:
    name: str
    cache_creation_input_cost: float
    cache_read_input_cost: float
    input_cost: float
    output_cost: float


@dataclass
class TokenUsage:
    cache_creation_input_tokens: int = 0
    cache_read_input_tokens: int = 0
    input_tokens: int = 0
    output_tokens: int = 0

    def update(self, usage):
        self.cache_creation_input_tokens += usage.cache_creation_input_tokens
        self.cache_read_input_tokens += usage.cache_read_input_tokens
        self.input_tokens += usage.input_tokens
        self.output_tokens += usage.output_tokens


class ShinyAppGenerator:
    MODEL_CONFIGS = {
        "claude-3-5-haiku-20241022": ModelConfig(
            "claude-3-5-haiku-20241022",
            0.00000125,
            0.00000010,
            0.00000100,
            0.00000500,
        ),
        "claude-sonnet-4-20250514": ModelConfig(
            "claude-sonnet-4-20250514",
            0.00000375,
            0.00000030,
            0.00000300,
            0.00001500,
        ),
        "claude-3-haiku-20240307": ModelConfig(
            "claude-3-haiku-20240307",
            0.0000003,
            0.00000003,
            0.00000025,
            0.00000125,
        ),
    }

    MODEL_ALIASES = {
        "haiku3": "claude-3-haiku-20240307",
        "haiku3.5": "claude-3-5-haiku-20241022",
        "sonnet": "claude-sonnet-4-20250514",
    }

    def __init__(self):
        self.token_usage = TokenUsage()
        self.client = Anthropic()
        self.setup_logging()

    @staticmethod
    def setup_logging():
        load_dotenv()
        logging.basicConfig(
            filename="anthropic.log",
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    @classmethod
    def parse_command_line_args(cls) -> Tuple[AppType, str]:
        if len(sys.argv) < 2 or not any(
            sys.argv[1] == app_type.value for app_type in AppType
        ):
            print(
                "Usage: python create_apps_using_llm.py [express|core|testing|core2express|express2core] [haiku3|haiku3.5|sonnet]"
            )
            sys.exit(1)

        model_type = cls.MODEL_ALIASES.get(
            sys.argv[2].lower() if len(sys.argv) > 2 else "haiku3"
        )
        if not model_type:
            print(
                f"Invalid model type. Choose from: {', '.join(cls.MODEL_ALIASES.keys())}"
            )
            sys.exit(1)

        return AppType(sys.argv[1]), model_type

    @staticmethod
    def load_documentation(app_type: AppType) -> str:
        return Path("docs", f"documentation_{app_type.value}.json").read_text()

    def read_system_prompt(self, app_type: AppType) -> List[Dict]:
        system_prompt_file = Path(
            "prompts", f"SYSTEM_PROMPT_{app_type.value}.md"
        ).read_text()
        documentation = self.load_documentation(app_type)

        return [
            {
                "type": "text",
                "text": system_prompt_file,
            },
            {
                "type": "text",
                "text": f"Here is the function reference documentation for Shiny for Python: {documentation}",
                "cache_control": {"type": "ephemeral"},
            },
        ]

    def calculate_cost(self, model: str) -> float:
        if model not in self.MODEL_CONFIGS:
            raise ValueError(f"Unknown model: {model}")

        config = self.MODEL_CONFIGS[model]
        return (
            self.token_usage.cache_creation_input_tokens
            * config.cache_creation_input_cost
            + self.token_usage.cache_read_input_tokens * config.cache_read_input_cost
            + self.token_usage.input_tokens * config.input_cost
            + self.token_usage.output_tokens * config.output_cost
        )

    @staticmethod
    def run_pyright(file_path: Path) -> Dict:
        try:
            result = subprocess.run(
                ["pyright", str(file_path), "--outputjson"],
                capture_output=True,
                text=True,
                check=False,
            )
            return json.loads(result.stdout)
        except json.JSONDecodeError:
            return {
                "error": "Failed to parse pyright output",
                "raw_output": result.stdout,
                "raw_error": result.stderr,
            }
        except FileNotFoundError:
            return {
                "error": "Pyright is not installed. Please install it using: pip install pyright"
            }
        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}

    @staticmethod
    def is_port_in_use(port: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(("localhost", port)) == 0

    def run_shiny_app(
        self,
        script_path: Path,
        port: int = 8000,
        timeout: int = 8,
        success_timeout: int = 5,
        verbose: bool = True,
    ) -> Tuple[bool, str]:
        if self.is_port_in_use(port):
            return False, f"Port {port} is already in use."

        try:
            process = subprocess.Popen(
                ["shiny", "run", str(script_path), "--port", str(port)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        except Exception as e:
            return False, f"Failed to start Shiny app: {e}"

        return self._monitor_app_process(
            process, port, timeout, success_timeout, verbose
        )

    def _monitor_app_process(
        self,
        process: subprocess.Popen,
        port: int,
        timeout: int,
        success_timeout: int,
        verbose: bool,
    ) -> Tuple[bool, str]:
        monitor_active = threading.Event()
        monitor_active.set()
        output_lines = {"stdout": [], "stderr": []}

        with ThreadPoolExecutor(max_workers=2) as executor:
            stdout_future = executor.submit(
                self._read_output_stream,
                process.stdout,
                output_lines["stdout"],
                monitor_active,
                verbose,
            )
            stderr_future = executor.submit(
                self._read_output_stream,
                process.stderr,
                output_lines["stderr"],
                monitor_active,
                verbose,
            )

            startup_successful = self._wait_for_app_startup(
                process, port, timeout, success_timeout, verbose
            )

        monitor_active.clear()
        stdout_future.result()
        stderr_future.result()

        return startup_successful, (
            "\n".join(output_lines["stderr"]) if not startup_successful else ""
        )

    @staticmethod
    def _read_output_stream(
        stream,
        lines_list: List[str],
        monitor_active: threading.Event,
        verbose: bool,
    ) -> None:
        while monitor_active.is_set():
            try:
                line = stream.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                lines_list.append(line.strip())
                if verbose:
                    logging.info(f"STREAM: {line.strip()}")
            except (ValueError, Exception) as e:
                if verbose:
                    logging.info(f"Exception in read_output thread: {e}")
                break

    def _wait_for_app_startup(
        self,
        process: subprocess.Popen,
        port: int,
        timeout: int,
        success_timeout: int,
        verbose: bool,
    ) -> bool:
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                response = requests.get(f"http://localhost:{port}", timeout=5)
                if response.status_code == 200:
                    if verbose:
                        logging.info("Shiny app started successfully")
                    time.sleep(success_timeout)
                    return True
            except requests.exceptions.RequestException:
                time.sleep(0.1)

        process.terminate()
        try:
            process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
        return False

    def analyze_pyright_results(self, results: Dict) -> List[str]:
        error_list = []
        if results["summary"]["errorCount"] > 1:
            for i in results["generalDiagnostics"][1:]:
                error_list.append(
                    f'Line number: {i["range"]["start"]["line"]} has error: {i["message"]}'
                )
            return error_list

        logging.info("\nNo type errors found!")
        return error_list

    @staticmethod
    def extract_code_and_description(response: str) -> Tuple[str, str]:
        """Extract Python code block and description from LLM response."""
        code_match = re.search(r"```python(.*?)```", response, re.DOTALL)
        code = code_match.group(1).strip() if code_match else ""
        description = re.sub(r"```python.*?```", "", response, flags=re.DOTALL).strip()
        return code, description

    @staticmethod
    def extract_test(response: str) -> str:
        """Extract Python test code block from LLM response."""
        code_match = re.search(r"```python(.*?)```", response, re.DOTALL)
        return code_match.group(1).strip() if code_match else ""

    def get_llm_response(self, prompt: str, system_prompt: List[Dict], model: str):
        """Get response from the LLM with error handling."""
        try:
            messages = self.client.messages.create(
                model=model,
                max_tokens=4096,
                system=system_prompt,
                temperature=0.5,
                messages=[{"role": "user", "content": prompt}],
            )
            self.token_usage.update(messages.usage)
            self._log_token_usage(model)
            return messages
        except Exception as e:
            logging.error(f"Error getting LLM response: {e}")
            raise

    def _log_token_usage(self, model: str) -> None:
        """Log token usage and cost."""
        logging.info("==========")
        logging.info(
            f"Cache creation input tokens ✎: {self.token_usage.cache_creation_input_tokens}"
        )
        logging.info(
            f"Cache read input tokens 🗒: {self.token_usage.cache_read_input_tokens}"
        )
        logging.info(f"Output tokens ⇣: {self.token_usage.output_tokens}")
        logging.info(f"Input tokens ⇡: {self.token_usage.input_tokens}")
        logging.info("==========")

        cost = self.calculate_cost(model)
        print(f"Incurred costs till now: ${cost:.6f}")

    def process_testing_directory(
        self, directory: Path, system_prompt: List[Dict], model: str
    ) -> None:
        """Process directory for testing app generation."""
        app_files = self._find_app_files_without_tests(directory)
        for dir_path, app_file in app_files:
            test_file = dir_path / f"test_{dir_path.name}.py"
            if test_file.exists():
                continue
            app_text = app_file.read_text()
            user_prompt = self._create_test_prompt(app_text)
            messages = self.get_llm_response(user_prompt, system_prompt, model)
            code = self.extract_test(messages.content[0].text)
            self._create_test_files(dir_path, code)

    def process_conversion_directory(
        self, directory: Path, app_type: AppType, system_prompt: List[Dict], model: str
    ) -> None:
        """Process directory for app conversion."""
        app_files = self._find_app_files(directory)
        for dir_path, app_file in app_files:
            app_text = app_file.read_text()
            code, _ = self.generate_converted_shiny_app(app_text, system_prompt, model)

            output_file = dir_path / f"app-{app_type.value.split('2')[1]}.py"
            output_file.write_text(code)

    def process_directory(
        self, directory: Path, system_prompt: List[Dict], model: str, app_type: AppType
    ) -> None:
        """Process directory for standard app generation."""
        prompt_files = self._find_prompt_files(directory, app_type)
        for dir_path, prompt_file in prompt_files:
            if not dir_path.is_dir():
                continue

            logging.info(f"Processing directory: {dir_path}")
            prompt = prompt_file.read_text()
            code, description = self.generate_shiny_app(prompt, system_prompt, model)

            # Create app files
            self._create_app_files(dir_path, code, description, app_type)

            # # Test and fix if needed
            # success, error_message = self.run_shiny_app(
            #     dir_path / "app.py", port=8000, timeout=5, success_timeout=5
            # )
            # if not success:
            #     logging.info(f"App failed to run in {dir_path}, attempting fix")
            #     code, _ = self.fix_shiny_app(code, error_message, system_prompt, model)
            #     self._create_app_files(dir_path, code, description, app_type)

    def _find_prompt_files(
        self, base_dir: Path, app_type: AppType
    ) -> List[Tuple[Path, Path]]:
        """Find all PROMPT.md files without corresponding app files."""
        result = []
        for path in base_dir.rglob("PROMPT.md"):
            dir_path = path.parent
            # Determine the expected app file name based on app type
            if app_type == AppType.CORE:
                app_file_name = "app-core.py"
            elif app_type == AppType.EXPRESS:
                app_file_name = "app-express.py"
            else:
                # For other types, use the existing logic
                app_file_name = f"app{'-' + app_type.value if app_type.value != 'core' else ''}.py"
            
            # Check if the specific app file already exists
            if not (dir_path / app_file_name).exists():
                result.append((dir_path, path))
        return result

    def _find_app_files(self, base_dir: Path) -> List[Tuple[Path, Path]]:
        """Find all app files in order of preference."""
        result = []
        # Exclude certain directories that shouldn't contain app files
        excluded_dirs = {"docs", "scripts", "prompts", ".git", "__pycache__", ".venv", "venv"}
        
        for root in base_dir.rglob("*"):
            if not root.is_dir():
                continue
            
            # Skip excluded directories
            if any(part in excluded_dirs for part in root.parts):
                continue
                
            for app_file in ["app-express.py", "app-core.py"]:
                file_path = root / app_file
                if file_path.exists() and file_path.is_file():
                    result.append((root, file_path))
                    break
        return result

    def _find_app_files_without_tests(self, base_dir: Path) -> List[Tuple[Path, Path]]:
        """Find all app files that don't have corresponding test files, by checking file existence only."""
        result = []
        for root, app_file in self._find_app_files(base_dir):
            test_file = root / f"test_{root.name}.py"
            if not test_file.is_file():
                result.append((root, app_file))
        return result

    @staticmethod
    def _create_test_files(dir_path: Path, code: str) -> None:
        """Create test files in the specified directory."""
        test_name = dir_path.name
        test_file = dir_path / f"test_{test_name}.py"
        test_file.write_text(code)

    @staticmethod
    def _create_app_files(
        dir_path: Path, code: str, description: str, app_type: AppType
    ) -> None:
        """Create app files and requirements in the specified directory."""
        # Write app file
        app_file = dir_path / f"app-{app_type.value}.py"
        app_file.write_text(code)

        # Write requirements
        requirements = """
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
        (dir_path / "requirements.txt").write_text(requirements)

    def generate_shiny_app(
        self, prompt: str, system_prompt: List[Dict], model: str
    ) -> Tuple[str, str]:
        """Generate a new Shiny app using the LLM."""
        user_prompt = (
            f"Leverage Shiny for Python function reference documentation and make a "
            f"Shiny for Python app for the following requirements: {prompt}. "
            f"Please do not use external files for accessing data, make up some data for use in the app."
        )
        messages = self.get_llm_response(user_prompt, system_prompt, model)
        return self.extract_code_and_description(messages.content[0].text)

    def generate_converted_shiny_app(
        self, app_text: str, system_prompt: List[Dict], model: str
    ) -> Tuple[str, str]:
        """Generate a converted version of an existing Shiny app."""
        user_prompt = (
            f"Given this shiny app code: {app_text}, please convert it using the reference documentation. "
            f"Please provide complete code for the same."
        )
        messages = self.get_llm_response(user_prompt, system_prompt, model)
        return self.extract_code_and_description(messages.content[0].text)

    def fix_shiny_app(
        self, code: str, error_message: str, system_prompt: List[Dict], model: str
    ) -> Tuple[str, str]:
        """Fix a failing Shiny app using the LLM."""
        user_prompt = (
            f"Running this code for Shiny for Python: \n {code} \n resulted in an error: "
            f"{error_message}. Please fix it to make it work. Please provide complete code for the same"
        )
        messages = self.get_llm_response(user_prompt, system_prompt, model)
        return self.extract_code_and_description(messages.content[0].text)

    def _create_test_prompt(self, app_text: str) -> str:
        """Create a prompt for generating tests for a Shiny app."""
        return (
            f"Given this Shiny for Python app code:\n{app_text}\n"
            "Please only add controllers for components that already have an ID in the shiny app.\n"
            "Do not add tests for ones that do not have an existing ids since controllers need IDs to locate elements.\n"
            "and server functionality of this app. Include appropriate assertions \n"
            "and test cases to verify the app's behavior."
        )


def main():
    generator = ShinyAppGenerator()
    app_type, model = generator.parse_command_line_args()
    system_prompt = generator.read_system_prompt(app_type)

    timer_start = time.perf_counter()

    for directory in Path().iterdir():
        if not directory.is_dir():
            continue

        if app_type == AppType.TESTING:
            generator.process_testing_directory(directory, system_prompt, model)
        elif app_type in (AppType.CORE2EXPRESS, AppType.EXPRESS2CORE):
            generator.process_conversion_directory(
                directory, app_type, system_prompt, model
            )
        else:
            generator.process_directory(directory, system_prompt, model, app_type)

        timer_current = time.perf_counter()
        logging.info(
            f"Time taken for directory {directory}: {timer_current - timer_start:.2f} seconds"
        )

    timer_end = time.perf_counter()
    minutes, seconds = divmod(timer_end - timer_start, 60)
    print(f"Total time taken: {int(minutes)} minutes and {seconds:.2f} seconds")


if __name__ == "__main__":
    main()
