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
                max_tokens=190000,
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
            "and test cases to verify the app's behavior."
        )

    def generate_test_for_app(
        self,
        app_code: str,
        model: str = "claude-sonnet-4-20250514",
        output_file: str = None,
        show_token_usage: bool = False,
    ) -> str:
        model = self.MODEL_ALIASES.get(model, model)

        system_prompt = self.read_system_prompt()
        user_prompt = self._create_test_prompt(app_code)
        response = self.get_llm_response(user_prompt, system_prompt, model)

        test_code = self.extract_test(response)

        if output_file:
            with open(output_file, "w") as f:
                f.write(test_code)

        if show_token_usage:
            usage = token_usage()
            print(f"Token usage: {usage}")

    def get_token_usage(self):
        return token_usage()


def cli():
    if len(sys.argv) < 2:
        print("Usage: shiny-test-generator <path_to_app_file> [--show-tokens]")
        sys.exit(1)

    app_file_path = Path(sys.argv[1])
    if not app_file_path.is_file():
        print(f"Error: File not found at {app_file_path}")
        sys.exit(1)

    show_tokens = "--show-tokens" in sys.argv

    app_code = app_file_path.read_text()

    test_file_path = app_file_path.with_name(f"test_{app_file_path.name}")

    generator = ShinyTestGenerator()
    generator.generate_test_for_app(
        app_code, output_file=test_file_path, show_token_usage=show_tokens
    )

    print(f"Test file generated: {test_file_path}")
