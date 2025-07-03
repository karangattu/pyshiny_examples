# Shiny Test Generator

This package provides a `ShinyTestGenerator` class that can be used to generate tests for Shiny for Python applications using LLMs.

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
with open("path/to/your/app.py", "r") as f:
    app_code = f.read()

# Generate the test
test_code = generator.generate_test_for_app(app_code)

# Print the generated test
print(test_code)
```

### As a CLI Tool

```bash
shiny-test-generator path/to/your/app.py
```