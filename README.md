# Shiny Test Generator

`shiny-test-generator` is a Python tool that uses LLMs (Anthropic Claude or OpenAI GPT) to automatically generate `pytest` tests for [Shiny for Python](https://shiny.posit.co/py/) apps. It supports both CLI and library usage, and includes a quality evaluation suite with [`inspect-ai`](https://inspect.aisi.org.uk/).

## Features

- **Automated Test Generation**: Create `pytest`+`playwright` tests from your Shiny app code or file.
- **Multi-Provider LLMs**: Use Anthropic (Claude) or OpenAI (GPT) models.
- **Built-in Quality Checks**: Evaluate test quality with `inspect-ai`.

## Installation

Set your API keys as environment variables or in a `.env` file:

```bash
export ANTHROPIC_API_KEY=your_anthropic_api_key
export OPENAI_API_KEY=your_openai_api_key
```

Or in `.env`:

```bash
ANTHROPIC_API_KEY=your_anthropic_api_key
OPENAI_API_KEY=your_openai_api_key
```

Install the package:

```bash
pip install -e ".[test]"
```

## Usage

### CLI

```bash
shiny-test-generator path/to/app.py
shiny-test-generator path/to/app.py --provider openai --model gpt-4.1
shiny-test-generator path/to/app.py --output-dir tests/ --model sonnet
```

> [!TIP]
> For optimal performance, we recommend using the Anthropic `sonnet` model—it consistently outperforms OpenAI’s models for generating tests.

### Library

```python
# using openai models
from shiny_test_generator import ShinyTestGenerator

gen = ShinyTestGenerator(provider="openai")
test_code, test_path = gen.generate_test_from_file("app.py", model="gpt-4.1")
```

```python
# using anthropic models
from shiny_test_generator import ShinyTestGenerator

gen = ShinyTestGenerator(provider="anthropic")
test_code, test_path = gen.generate_test_from_file("app.py", model="sonnet")
```

## Model Aliases

- **Anthropic**: `haiku3`, `haiku3.5`, `sonnet`
- **OpenAI**: `gpt-4.1`, `o3-mini`, `o4-mini`, `gpt-4.1-nano`

## File Output

- `app.py` → `test_app.py` (same dir by default, or custom dir)

## Configuration

- API keys via env vars, `.env`, or as `api_key` argument to `ShinyTestGenerator`.

For more, see docstrings and CLI `--help`.

## Running inspect-ai evaluations

To run the quality evaluation suite using `inspect-ai`, you can use the provided GitHub Actions workflow or run it locally:

```bash
# generate test metadata
python evals/create_test_metadata.py
# run the evaluation
inspect eval evals/evaluation.py@shiny_test_evaluation --log-dir results/ --log-format json
```
