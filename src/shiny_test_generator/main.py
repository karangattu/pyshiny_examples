import importlib.resources
from pathlib import Path
import logging
import re
import sys
from chatlas import ChatAnthropic, token_usage
from dotenv import load_dotenv


__all__ = [
    "ShinyTestGenerator",
]


class ShinyTestGenerator:
    MODEL_ALIASES = {
        "haiku3": "claude-3-haiku-20240307",
        "haiku3.5": "claude-3-5-haiku-20241022",
        "sonnet": "claude-sonnet-4-20250514",
    }

    def __init__(
        self,
        api_key: str = None,
        log_file: str = "anthropic.log",
        setup_logging: bool = True,
    ):
        if api_key:
            self.client = ChatAnthropic(api_key=api_key)
        else:
            self.client = ChatAnthropic()

        self.log_file = log_file
        if setup_logging:
            self.setup_logging()

    @staticmethod
    def setup_logging():
        load_dotenv()
        logging.basicConfig(
            filename="anthropic.log",
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    @staticmethod
    def load_documentation() -> str:
        try:
            with (
                importlib.resources.files("shiny_test_generator")
                / "data"
                / "docs"
                / "documentation_testing.json"
            ).open("r") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Documentation file not found for app type: testing"
            )

    def read_system_prompt(self) -> str:
        try:
            with (
                importlib.resources.files("shiny_test_generator")
                / "data"
                / "prompts"
                / "SYSTEM_PROMPT_testing.md"
            ).open("r") as f:
                system_prompt_file = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(
                f"System prompt file not found for app type: testing"
            )

        documentation = self.load_documentation()

        combined_prompt = f"{system_prompt_file}\n\nHere is the function reference documentation for Shiny for Python: {documentation}"

        return combined_prompt

    def get_llm_response(self, prompt: str, system_prompt: str, model: str):
        try:
            chat = ChatAnthropic(
                model=model,
                system_prompt=system_prompt,
                max_tokens=64000,
            )

            response = chat.chat(prompt)

            if hasattr(response, "content"):
                return response.content
            elif hasattr(response, "text"):
                return response.text
            else:
                return str(response)
        except Exception as e:
            logging.error(f"Error getting LLM response: {e}")
            raise

    @staticmethod
    def extract_test(response: str) -> str:
        code_match = re.search(r"```python(.*?)```", response, re.DOTALL)
        return code_match.group(1).strip() if code_match else ""

    def _create_test_prompt(self, app_text: str) -> str:
        return (
            f"Given this Shiny for Python app code:\n{app_text}\n"
            "Please only add controllers for components that already have an ID in the shiny app.\n"
            "Do not add tests for ones that do not have an existing ids since controllers need IDs to locate elements.\n"
            "and server functionality of this app. Include appropriate assertions \n"
            "and test cases to verify the app's behavior.\n"
            "IMPORTANT: Only output the Python test code in a single code block. Do not include any explanation, justification, or extra text."
        )

    def _infer_app_file_path(
        self, app_code: str = None, app_file_path: str = None
    ) -> Path:
        """
        Infer the app file path from various sources.
        Priority: explicit path > code analysis > current directory search
        """
        if app_file_path:
            return Path(app_file_path)

        # Try to find app files in current directory
        current_dir = Path.cwd()

        # Common Shiny app file patterns
        common_patterns = [
            "app.py",
            "app_*.py",
        ]

        found_files = []
        for pattern in common_patterns:
            found_files.extend(current_dir.glob(pattern))

        # If we found potential app files, use the first one
        if found_files:
            return found_files[0]

        # If we have app_code but no file path, create a temporary name
        if app_code:
            return Path("inferred_app.py")

        raise FileNotFoundError(
            "Could not infer app file path. Please provide app_file_path parameter."
        )

    def _generate_test_file_path(
        self, app_file_path: Path, output_dir: Path = None
    ) -> Path:
        """
        Generate test file path following the test_*.py naming convention.
        """
        if output_dir is None:
            output_dir = app_file_path.parent

        app_name = app_file_path.stem
        test_file_name = f"test_{app_name}.py"

        return output_dir / test_file_name

    def generate_test_for_app(
        self,
        app_code: str = None,
        model: str = "claude-sonnet-4-20250514",
        output_file: str = None,
        show_token_usage: bool = False,
        app_file_path: str = None,
        output_dir: str = None,
    ) -> tuple[str, Path]:
        """
        Generate test code for a Shiny app.

        Args:
            app_code: The app code as a string. If None, will be read from app_file_path
            model: The model to use for generation
            output_file: Explicit output file path (overrides automatic naming)
            show_token_usage: Whether to print token usage
            app_file_path: Path to the app file
            output_dir: Directory to save the test file (defaults to app file directory)

        Returns:
            tuple: (test_code, test_file_path)
        """
        model = self.MODEL_ALIASES.get(model, model)

        # Infer app file path if not provided
        inferred_app_path = self._infer_app_file_path(app_code, app_file_path)

        # Read app code if not provided
        if app_code is None:
            if not inferred_app_path.exists():
                raise FileNotFoundError(f"App file not found: {inferred_app_path}")
            app_code = inferred_app_path.read_text()

        # Generate test code
        system_prompt = self.read_system_prompt()
        user_prompt = self._create_test_prompt(app_code)
        response = self.get_llm_response(user_prompt, system_prompt, model)
        test_code = self.extract_test(response)

        # Determine output file path
        if output_file:
            test_file_path = Path(output_file)
        else:
            output_dir_path = Path(output_dir) if output_dir else None
            test_file_path = self._generate_test_file_path(
                inferred_app_path, output_dir_path
            )

        # Write test file
        test_file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(test_file_path, "w") as f:
            f.write(test_code)

        if show_token_usage:
            usage = token_usage()
            print(f"Token usage: {usage}")

        return test_code, test_file_path

    def generate_test_from_file(
        self,
        app_file_path: str,
        model: str = "claude-sonnet-4-20250514",
        output_file: str = None,
        show_token_usage: bool = False,
        output_dir: str = None,
    ) -> tuple[str, Path]:
        """
        Generate test code from an app file.

        Args:
            app_file_path: Path to the app file
            model: The model to use for generation
            output_file: Explicit output file path (overrides automatic naming)
            show_token_usage: Whether to print token usage
            output_dir: Directory to save the test file (defaults to app file directory)

        Returns:
            tuple: (test_code, test_file_path)
        """
        return self.generate_test_for_app(
            app_file_path=app_file_path,
            model=model,
            output_file=output_file,
            show_token_usage=show_token_usage,
            output_dir=output_dir,
        )

    def generate_test_from_code(
        self,
        app_code: str,
        app_name: str = "app",
        model: str = "claude-sonnet-4-20250514",
        output_file: str = None,
        show_token_usage: bool = False,
        output_dir: str = None,
    ) -> tuple[str, Path]:
        """
        Generate test code from app code string.

        Args:
            app_code: The app code as a string
            app_name: Name for the app (used in test file naming)
            model: The model to use for generation
            output_file: Explicit output file path (overrides automatic naming)
            show_token_usage: Whether to print token usage
            output_dir: Directory to save the test file (defaults to current directory)

        Returns:
            tuple: (test_code, test_file_path)
        """
        # Create a virtual app path for naming purposes
        virtual_app_path = Path(f"{app_name}.py")

        return self.generate_test_for_app(
            app_code=app_code,
            app_file_path=str(virtual_app_path),
            model=model,
            output_file=output_file,
            show_token_usage=show_token_usage,
            output_dir=output_dir,
        )

    def get_token_usage(self):
        return token_usage()


def cli():
    if len(sys.argv) < 2:
        print(
            "Usage: shiny-test-generator <path_to_app_file> [--show-tokens] [--output-dir <dir>]"
        )
        sys.exit(1)

    app_file_path = Path(sys.argv[1])
    if not app_file_path.is_file():
        print(f"Error: File not found at {app_file_path}")
        sys.exit(1)

    show_tokens = "--show-tokens" in sys.argv

    # Parse output directory if provided
    output_dir = None
    if "--output-dir" in sys.argv:
        try:
            output_dir_index = sys.argv.index("--output-dir")
            output_dir = sys.argv[output_dir_index + 1]
        except (IndexError, ValueError):
            print("Error: --output-dir requires a directory path")
            sys.exit(1)

    generator = ShinyTestGenerator()
    test_code, test_file_path = generator.generate_test_from_file(
        str(app_file_path),
        show_token_usage=show_tokens,
        output_dir=output_dir,
    )

    print(f"Test file generated: {test_file_path}")
