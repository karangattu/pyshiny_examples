import os
import sys

from inspect_ai import eval

from evals.create_test_metadata import generate_shiny_test_metadata
from evals.evaluation import shiny_test_evaluation

script_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(script_dir, os.pardir))
if project_root not in sys.path:
    sys.path.insert(0, project_root)



def main():
    print("Step 1: Generating Shiny test metadata...")
    generate_shiny_test_metadata()
    print("Test metadata generation complete.")

    print("\nStep 2: Running Inspect AI evaluation...")
    # You can specify the model here, e.g., --model openai/gpt-4
    # For simplicity, we'll assume a default model is configured or passed via CLI args to inspect eval
    eval(shiny_test_evaluation)
    print("Inspect AI evaluation complete.")


if __name__ == "__main__":
    main()
