from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import model_graded_qa
from inspect_ai.solver import generate, self_critique
import json
from pathlib import Path


def create_test_specific_instructions(test_data: dict) -> str:
    """
    Create specific grading instructions based on the test and app characteristics.

    Args:
        test_data: Dictionary containing test metadata

    Returns:
        Formatted instructions for model grading
    """
    app_name = test_data["app_name"]

    base_instructions = f"""
    You are evaluating a Shiny application test for the app: {app_name}

    Please assess the test quality based on the following criteria:

    1. **Test Coverage**: Does the test cover the main functionality of the Shiny app?
    2. **Code Quality**: Is the test code well-structured and maintainable?
    3. **Edge Cases**: Does the test handle potential edge cases and error conditions?
    4. **Assertions**: Are the test assertions meaningful and comprehensive?
    5. **Readability**: Is the test code clear and easy to understand?

    Context about the app:
    - App location: {test_data['app_path']}
    - This is a Shiny application that may include UI components, server logic, and reactive elements

    Rate the test on a scale of 1-10 and provide specific feedback on areas for improvement.
    """

    return base_instructions.strip()


def create_inspect_ai_samples(test_data: dict) -> list[Sample]:
    """
    Create Inspect AI samples from the generated test data.

    Args:
        test_data: Dictionary containing test metadata for all generated tests

    Returns:
        List of Sample objects for Inspect AI evaluation
    """
    samples = []

    for test_name, data in test_data.items():
        instructions = create_test_specific_instructions(data)

        prompt = f"""
        Original Shiny App Code:
        ```python
        {data['app_code']}
        ```

        Generated Test Code:
        ```python
        {data['test_code']}
        ```

        Please evaluate this test code according to the provided instructions.
        """

        target_answer = "A high-quality test should score 7-10 points with comprehensive coverage of app functionality."

        sample = Sample(
            input=prompt,
            target=target_answer,
            metadata={
                "test_name": test_name,
                "app_name": data["app_name"],
                "app_path": data["app_path"],
            },
        )

        samples.append(sample)

    return samples


@task
def shiny_test_evaluation() -> Task:
    """
    Inspect AI task for evaluating generated Shiny tests.
    """
    # Load test data from the JSON file
    repo_root = Path(__file__).parent.parent  # Go up from evals/ to repo root
    metadata_file = repo_root / "evals" / "test_metadata.json"
    with open(metadata_file, "r") as f:
        test_data = json.load(f)

    samples = create_inspect_ai_samples(test_data)

    scorer = model_graded_qa(
        instructions="""
        You are an expert in Shiny application testing. Evaluate the quality of the provided test code 
        based on coverage, maintainability, and effectiveness. Provide a score from 1-10 and detailed feedback.

        Focus on:
        - How well the test exercises the app's functionality
        - Quality of test assertions and expectations
        - Code structure and clarity
        - Handling of edge cases
        - Overall test robustness
        """
    )

    return Task(
        dataset=samples,
        solver=[generate(), self_critique()],
        scorer=scorer,
        max_messages=10,
    )
