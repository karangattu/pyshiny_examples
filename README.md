# Shiny Test Generator

This repository contains a Python package, `shiny-test-generator`, that automates the creation of `pytest` tests for [Shiny for Python](https://shiny.posit.co/py/) applications. Leveraging the power of Large Language Models (LLMs), this tool reads the source code of a Shiny app and generates a corresponding test file, helping to streamline the development workflow and improve test coverage.

A key feature of this project is its focus on reliability. It includes a comprehensive evaluation suite built with [`inspect-ai`](https://rstudio.github.io/inspect-ai/) that continuously measures the quality and correctness of the generated tests against a diverse set of sample applications.

## Key Features

*   **Automated Test Generation**: Provide your Shiny app's source code and receive a complete `pytest` test file that uses `playwright` for browser interaction.
*   **Reusable Python Package**: Easily install the tool via `pip` and use the `ShinyTestGenerator` class programmatically in your own scripts and workflows.
*   **Simple Command-Line Interface**: Generate tests on the fly directly from your terminal.
*   **Built-in Quality Evaluation**: A robust evaluation pipeline using `inspect-ai` and GitHub Actions allows for ongoing, data-driven assessment of the test generation quality.

## Installation

### Prerequisites

You'll need an Anthropic API key to use this tool. Set it as an environment variable:

```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

Or create a `.env` file in your project directory:

```
ANTHROPIC_API_KEY=your_api_key_here
```

### Install the Package

```bash
pip install .
```

## Usage

### As a Library

```python
from shiny_test_generator import ShinyTestGenerator

# Initialize the generator
generator = ShinyTestGenerator()

# Method 1: Generate test from an app file
test_code, test_file_path = generator.generate_test_from_file(
    app_file_path="path/to/your/app.py",
)

# Method 2: Generate test from app code string
app_code = """
from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.input_text("name", "Enter your name:", ""),
    ui.output_text("greeting")
)

def server(input, output, session):
    @render.text
    def greeting():
        return f"Hello, {input.name()}!"

app = App(app_ui, server)
"""

test_code, test_file_path = generator.generate_test_from_code(
    app_code=app_code,
    app_name="my_app",
    output_dir="tests/"  # Optional: specify output directory
)

# Method 3: Flexible generate_test_for_app method
test_code, test_file_path = generator.generate_test_for_app(
    app_code=app_code,  # Can pass code directly
    app_file_path="path/to/your/app.py",  # Or specify file path
    model="sonnet",  # Options: "haiku3", "haiku3.5", "sonnet"
    output_file="custom_test_name.py",  # Optional: custom output filename
)

print(f"Test file generated: {test_file_path}")
print(f"Test code:\n{test_code}")
```

### As a CLI Tool

```bash
# Basic usage - generates test_<app_name>.py in the same directory
shiny-test-generator path/to/your/app.py

# Specify output directory
shiny-test-generator path/to/your/app.py --output-dir tests/
```

### Model Options

The tool supports several Claude models via aliases:

- `"haiku3"` - Claude 3 Haiku (fastest, most economical)
- `"haiku3.5"` - Claude 3.5 Haiku (balanced performance)
- `"sonnet"` - Claude Sonnet 4 (highest quality, default)

You can also specify the full model name directly (e.g., `"claude-sonnet-4-20250514"`).

### File Organization

The tool automatically generates test files following Python testing conventions:

- If your app is `app.py`, the test file will be `test_app.py`
- If your app is `my_dashboard.py`, the test file will be `test_my_dashboard.py`
- Tests are saved in the same directory as the app file by default, or in a custom directory if specified

## Configuration

### API Key Setup

The tool uses the Anthropic API and requires an API key. You can provide it in several ways:

1. **Environment variable** (recommended):
   ```bash
   export ANTHROPIC_API_KEY="your_api_key_here"
   ```

2. **`.env` file** in your project directory:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

3. **Programmatically** when initializing the generator:
   ```python
   generator = ShinyTestGenerator(api_key="your_api_key_here")
   ```

### Logging

The tool automatically sets up logging to `anthropic.log` in your current directory. You can disable this by setting `setup_logging=False` when initializing the generator.

## Evaluation

This repository includes an evaluation suite built with `inspect-ai` to measure the quality of the generated tests. The evaluation is defined in `eval.yml` and can be run using the following command:

```bash
inspect eval eval.yml
```

The evaluation runs against a set of sample applications located in the `evaluation_apps` directory. The results of the evaluation are scored using the `scorer.py` script, which runs `pytest` on the generated tests and checks for passing or failing tests.

### GitHub Action

A GitHub Action is configured to run the evaluation automatically. You can trigger it manually from the "Actions" tab in the repository. The results of the evaluation are uploaded as an artifact.
