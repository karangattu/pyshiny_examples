# Shiny Test Generator

This repository contains a Python package, `shiny-test-generator`, that automates the creation of `pytest` tests for [Shiny for Python](https://shiny.posit.co/py/) applications. Leveraging the power of Large Language Models (LLMs), this tool reads the source code of a Shiny app and generates a corresponding test file, helping to streamline the development workflow and improve test coverage.

A key feature of this project is its focus on reliability. It includes a comprehensive evaluation suite built with [`inspect-ai`](https://rstudio.github.io/inspect-ai/) that continuously measures the quality and correctness of the generated tests against a diverse set of sample applications.

## Key Features

*   **Automated Test Generation**: Provide your Shiny app's source code and receive a complete `pytest` test file that uses `playwright` for browser interaction.
*   **Reusable Python Package**: Easily install the tool via `pip` and use the `ShinyTestGenerator` class programmatically in your own scripts and workflows.
*   **Simple Command-Line Interface**: Generate tests on the fly directly from your terminal.
*   **Built-in Quality Evaluation**: A robust evaluation pipeline using `inspect-ai` and GitHub Actions allows for ongoing, data-driven assessment of the test generation quality.

## Installation

```bash
pip install .
```

## Usage

### As a Library

```python
from shiny_test_generator import ShinyTestGenerator

# Initialize the generator
generator = ShinyTestGenerator()

# Read the app code from a file
app_file_path = "path/to/your/app.py"
with open(app_file_path, "r") as f:
    app_code = f.read()

# Generate the test file (test_<app_file_name>.py will be created automatically)
generator.generate_test_for_app(app_code, app_file_path=app_file_path)

# Or, specify a custom output file name
# generator.generate_test_for_app(app_code, output_file="my_test_file.py")
```

### As a CLI Tool

```bash
shiny-test-generator path/to/your/app.py
```

This will generate a test file named `test_<app_file_name>.py` in the same directory as your app file.

```

## Evaluation

This repository includes an evaluation suite built with `inspect-ai` to measure the quality of the generated tests. The evaluation is defined in `eval.yml` and can be run using the following command:

```bash
inspect eval eval.yml
```

The evaluation runs against a set of sample applications located in the `evaluation_apps` directory. The results of the evaluation are scored using the `scorer.py` script, which runs `pytest` on the generated tests and checks for passing or failing tests.

### GitHub Action

A GitHub Action is configured to run the evaluation automatically. You can trigger it manually from the "Actions" tab in the repository. The results of the evaluation are uploaded as an artifact.
