import importlib.resources
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


__all__ = [
    "ShinyTestGenerator",
]


class ShinyTestGenerator:
    MODEL_CONFIGS = {
        "claude-3-5-haiku-20241022": {
            "name": "claude-3-5-haiku-20241022",
            "cache_creation_input_cost": 0.00000125,
            "cache_read_input_cost": 0.00000010,
            "input_cost": 0.00000100,
            "output_cost": 0.00000500,
        },
        "claude-sonnet-4-20250514": {
            "name": "claude-sonnet-4-20250514",
            "cache_creation_input_cost": 0.00000375,
            "cache_read_input_cost": 0.00000030,
            "input_cost": 0.00000300,
            "output_cost": 0.00001500,
        },
        "claude-3-haiku-20240307": {
            "name": "claude-3-haiku-20240307",
            "cache_creation_input_cost": 0.0000003,
            "cache_read_input_cost": 0.00000003,
            "input_cost": 0.00000025,
            "output_cost": 0.00000125,
        },
    }

    MODEL_ALIASES = {
        "haiku3": "claude-3-haiku-20240307",
        "haiku3.5": "claude-3-5-haiku-20241022",
        "sonnet": "claude-sonnet-4-20250514",
    }

    def __init__(self, api_key: str = None, log_file: str = "anthropic.log", setup_logging: bool = True):
        """
        Initialize the ShinyTestGenerator.
        
        Args:
            api_key: Anthropic API key. If None, will use environment variable.
            log_file: Path to log file. Defaults to "anthropic.log".
            setup_logging: Whether to setup logging. Defaults to True.
        """
        self.client = Anthropic(api_key=api_key) if api_key else Anthropic()
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
        """Load documentation for the specified app type."""
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

    def read_system_prompt(self) -> List[Dict]:
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
            return messages
        except Exception as e:
            logging.error(f"Error getting LLM response: {e}")
            raise

    @staticmethod
    def extract_test(response: str) -> str:
        """Extract Python test code block from LLM response."""
        code_match = re.search(r"```python(.*?)```", response, re.DOTALL)
        return code_match.group(1).strip() if code_match else ""

    def _create_test_prompt(self, app_text: str) -> str:
        """Create a prompt for generating tests for a Shiny app."""
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
    ) -> str:
        """
        Generate a test for a Shiny app.
        
        Args:
            app_code: The source code of the app to generate a test for
            model: Model to use for generation
            
        Returns:
            The generated test code
        """
        # Resolve model alias
        model = self.MODEL_ALIASES.get(model, model)
        
        system_prompt = self.read_system_prompt()
        user_prompt = self._create_test_prompt(app_code)
        messages = self.get_llm_response(user_prompt, system_prompt, model)
        return self.extract_test(messages.content[0].text)


def cli():
    if len(sys.argv) != 2:
        print("Usage: shiny-test-generator <path_to_app_file>")
        sys.exit(1)

    app_file_path = Path(sys.argv[1])
    if not app_file_path.is_file():
        print(f"Error: File not found at {app_file_path}")
        sys.exit(1)

    app_code = app_file_path.read_text()

    generator = ShinyTestGenerator()
    test_code = generator.generate_test_for_app(app_code)
    print(test_code)