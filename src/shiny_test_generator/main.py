import importlib.resources
from pathlib import Path
import logging
import re
import sys
from dataclasses import dataclass
from typing import Optional, Tuple
from chatlas import ChatAnthropic
from dotenv import load_dotenv


__all__ = [
    "ShinyTestGenerator",
]


@dataclass
class Config:
    """Configuration class for ShinyTestGenerator"""
    MODEL_ALIASES = {
        "haiku3": "claude-3-haiku-20240307",
        "haiku3.5": "claude-3-5-haiku-20241022",
        "sonnet": "claude-sonnet-4-20250514",
    }
    DEFAULT_MODEL = "claude-sonnet-4-20250514"
    MAX_TOKENS = 64000
    LOG_FILE = "anthropic.log"
    COMMON_APP_PATTERNS = ["app.py", "app_*.py"]


class ShinyTestGenerator:
    # Pre-compiled regex pattern for better performance
    CODE_PATTERN = re.compile(r"```python(.*?)```", re.DOTALL)
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        log_file: str = Config.LOG_FILE,
        setup_logging: bool = True,
    ):
        # Lazy loading - initialize expensive resources only when needed
        self._client = None
        self._documentation = None
        self._system_prompt = None
        self.api_key = api_key
        self.log_file = log_file
        
        if setup_logging:
            self.setup_logging()

    @property
    def client(self) -> ChatAnthropic:
        """Lazy-loaded ChatAnthropic client"""
        if self._client is None:
            self._client = ChatAnthropic(api_key=self.api_key) if self.api_key else ChatAnthropic()
        return self._client

    @property
    def documentation(self) -> str:
        """Lazy-loaded documentation"""
        if self._documentation is None:
            self._documentation = self._load_documentation()
        return self._documentation

    @property
    def system_prompt(self) -> str:
        """Lazy-loaded system prompt"""
        if self._system_prompt is None:
            self._system_prompt = self._read_system_prompt()
        return self._system_prompt

    @staticmethod
    def setup_logging():
        load_dotenv()
        logging.basicConfig(
            filename=Config.LOG_FILE,
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    def _load_documentation(self) -> str:
        """Load documentation from package resources"""
        try:
            doc_path = (
                importlib.resources.files("shiny_test_generator")
                / "data"
                / "docs"
                / "documentation_testing.json"
            )
            with doc_path.open("r") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(
                "Documentation file not found for app type: testing"
            )

    def _read_system_prompt(self) -> str:
        """Read and combine system prompt with documentation"""
        try:
            prompt_path = (
                importlib.resources.files("shiny_test_generator")
                / "data"
                / "prompts"
                / "SYSTEM_PROMPT_testing.md"
            )
            with prompt_path.open("r") as f:
                system_prompt_file = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(
                "System prompt file not found for app type: testing"
            )

        return f"{system_prompt_file}\n\nHere is the function reference documentation for Shiny for Python: {self.documentation}"

    def get_llm_response(self, prompt: str, model: str) -> str:
        """Get response from LLM - reuses client instance instead of creating new one"""
        try:
            # Reuse existing client instead of creating new ChatAnthropic instance
            chat = ChatAnthropic(
                model=model,
                system_prompt=self.system_prompt,
                max_tokens=Config.MAX_TOKENS,
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

    def extract_test(self, response: str) -> str:
        """Extract test code using pre-compiled regex pattern"""
        match = self.CODE_PATTERN.search(response)
        return match.group(1).strip() if match else ""

    def _create_test_prompt(self, app_text: str, app_file_name: str) -> str:
        """Create test generation prompt with app file name"""
        return (
            f"Given this Shiny for Python app code from file '{app_file_name}':\n{app_text}\n"
            "Please only add controllers for components that already have an ID in the shiny app.\n"
            "Do not add tests for ones that do not have an existing ids since controllers need IDs to locate elements.\n"
            "and server functionality of this app. Include appropriate assertions \n"
            "and test cases to verify the app's behavior.\n"
            f"IMPORTANT: Use the exact app file name '{app_file_name}' in the create_app_fixture call like this:\n"
            f"app = create_app_fixture([\"{app_file_name}\"])\n"
            "IMPORTANT: Only output the Python test code in a single code block. Do not include any explanation, justification, or extra text."
        )

    def _infer_app_file_path(
        self, app_code: Optional[str] = None, app_file_path: Optional[str] = None
    ) -> Path:
        """
        Infer the app file path from various sources.
        Priority: explicit path > code analysis > current directory search
        """
        if app_file_path:
            return Path(app_file_path)

        current_dir = Path.cwd()
        
        found_files = []
        for pattern in Config.COMMON_APP_PATTERNS:
            found_files.extend(current_dir.glob(pattern))

        if found_files:
            return found_files[0]

        # If we have app_code but no file path, create a temporary name
        if app_code:
            return Path("inferred_app.py")

        raise FileNotFoundError(
            "Could not infer app file path. Please provide app_file_path parameter."
        )

    def _generate_test_file_path(
        self, app_file_path: Path, output_dir: Optional[Path] = None
    ) -> Path:
        """
        Generate test file path following the test_*.py naming convention.
        Uses pathlib consistently.
        """
        output_dir = output_dir or app_file_path.parent
        test_file_name = f"test_{app_file_path.stem}.py"
        return output_dir / test_file_name

    def generate_test(
        self,
        app_code: Optional[str] = None,
        app_file_path: Optional[str] = None,
        app_name: str = "app",
        model: str = Config.DEFAULT_MODEL,
        output_file: Optional[str] = None,
        output_dir: Optional[str] = None,
    ) -> Tuple[str, Path]:
        """
        Consolidated method to generate test code for a Shiny app.
        Handles all scenarios: from file, from code, or auto-detection.

        Args:
            app_code: The app code as a string. If None, will be read from app_file_path
            app_file_path: Path to the app file
            app_name: Name for the app (used in test file naming when generating from code)
            model: The model to use for generation
            output_file: Explicit output file path (overrides automatic naming)
            output_dir: Directory to save the test file (defaults to app file directory)

        Returns:
            tuple: (test_code, test_file_path)
        """
        model = Config.MODEL_ALIASES.get(model, model)

        if app_code and not app_file_path:
            inferred_app_path = Path(f"{app_name}.py")
        else:
            inferred_app_path = self._infer_app_file_path(app_code, app_file_path)

        if app_code is None:
            if not inferred_app_path.exists():
                raise FileNotFoundError(f"App file not found: {inferred_app_path}")
            app_code = inferred_app_path.read_text(encoding='utf-8')

        # Pass the app file name to the prompt
        user_prompt = self._create_test_prompt(app_code, inferred_app_path.name)
        response = self.get_llm_response(user_prompt, model)
        test_code = self.extract_test(response)

        # Determine output file path using pathlib
        if output_file:
            test_file_path = Path(output_file)
        else:
            output_dir_path = Path(output_dir) if output_dir else None
            test_file_path = self._generate_test_file_path(
                inferred_app_path, output_dir_path
            )

        # Write test file
        test_file_path.parent.mkdir(parents=True, exist_ok=True)
        test_file_path.write_text(test_code, encoding='utf-8')

        return test_code, test_file_path

    def generate_test_from_file(
        self,
        app_file_path: str,
        model: str = Config.DEFAULT_MODEL,
        output_file: Optional[str] = None,
        output_dir: Optional[str] = None,
    ) -> Tuple[str, Path]:
        """Generate test code from an app file."""
        return self.generate_test(
            app_file_path=app_file_path,
            model=model,
            output_file=output_file,
            output_dir=output_dir,
        )

    def generate_test_from_code(
        self,
        app_code: str,
        app_name: str = "app",
        model: str = Config.DEFAULT_MODEL,
        output_file: Optional[str] = None,
        output_dir: Optional[str] = None,
    ) -> Tuple[str, Path]:
        """Generate test code from app code string."""
        return self.generate_test(
            app_code=app_code,
            app_name=app_name,
            model=model,
            output_file=output_file,
            output_dir=output_dir,
        )


def cli():
    """Command line interface"""
    if len(sys.argv) < 2:
        print(
            "Usage: shiny-test-generator <path_to_app_file> [--output-dir <dir>]"
        )
        sys.exit(1)

    app_file_path = Path(sys.argv[1])
    if not app_file_path.is_file():
        print(f"Error: File not found at {app_file_path}")
        sys.exit(1)

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
        output_dir=output_dir,
    )
