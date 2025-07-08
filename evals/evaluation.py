from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import model_graded_qa
from inspect_ai.solver import generate
import json
from pathlib import Path


def get_app_specific_instructions(app_name: str) -> str:
    """
    Get specific grading instructions for each app based on its unique characteristics.

    Args:
        app_name: Name of the Shiny app

    Returns:
        App-specific grading instructions
    """
    app_instructions = {
        "app_09_plots": """
        For this plot app tests, focus on:
        - Whether the test creates an instance of the InputSlider controller with id "my_plot_module-n_points"
        - Ensure that the slider component is verified for its label, min, max, and value attributes.
        - Ensure that the test checks by moving the slider to different values and verify the slider values accordingly
        """,
        "app_07_modules": """
        For this module-based app, focus on:
        - Whether the test creates instances of the InputText controller with ids "module_instance_1-text_input_1" and "module_instance_1-text_input_2"
        - Whether the test creates an instance of the OutputText controller with id "module_instance_1-text_output"
        - Ensure that the text inputs are verified for their labels and initial values.
        - Ensure that the test checks the text output for correct concatenation of input values.
        - Check that the test verifies the module's reactivity by changing input values and checking output
        """,
        "app_03_slider": """
        For this slider app, focus on:
        - Whether the test creates an instance of the InputSlider controller with id "slider1"
        - Ensure that the slider component is verified for its label, min, max, and value attributes.
        - Ensure that the test checks by moving the slider to different values and verify the slider values accordingly.
        - Whether the test creates an instance of the InputSliderRange controller with id "slider3"
        - Ensure that the range slider component is verified for its label, min, max, and initial range values.
        - Ensure that the test checks by moving the range slider to different values and verify the range values accordingly.
        
        """,
        "app_06_R_shiny": """
        For this app, focus on:
        - The test code should be empty since the app code was not a Shiny for Python app.
        """,
        "app_10_complex_layout": """
        For this app, focus on:
        - Whether the test creates an instance of the InputActionButton controller with id "action_button"
        - Ensure that the action button component is verified for its label and click functionality.
        - Whether the test creates an instance of the InputCheckbox controller with id "checkbox"
        - Ensure that the checkbox component is verified for its label and checked state.
        - Ensure that the test checks the checkbox state changes and verifies the output text accordingly.
        - Whether the test creates an instance of the InputDate controller with id "date_selector"
        - Ensure that the date selector component is verified for its label and selected date.
        - Ensure that the test checks the date selector state changes and verifies the output text accordingly.
        - Whether the test creates an instance of the InputNumeric controller with id "numeric_input"
        - Ensure that the numeric input component is verified for its label and value.
        - Ensure that the test checks the numeric input state changes and verifies the output text accordingly.
        - Whether the test creates an instance of the InputRadioButtons controller with id "radio_buttons"
        - Ensure that the radio buttons component is verified for its label, choices, and selected value.
        - Ensure that the test checks the radio buttons state changes and verifies the output text accordingly.
        - Whether the test creates an instance of the InputText controller with id "text_input"
        - Ensure that the text input component is verified for its label and initial value.
        - Ensure that the test checks the text input state changes and verifies the output text accordingly.
        - Whether the test creates an instance of the OutputText controller with id "action_button_value", "checkbox_value", "date_selector_value", "numeric_input_value", "radio_buttons_value", and "text_input_value"
        - Ensure that the output text components are verified for their initial values and updated values based on user interactions.
        - Ensure that the Output Data Frame controller with id "data_table" is created and verified for its initial state.
        """,
        "app_02_express_basic": """
        For this shiny express basic app, focus on:
        - Ensure that the test creates an instance of the InputActionButton controller with id "btn1"
        - Ensure that the action button component is verified for its label and click functionality.
        - Ensure that the test checks the action button state changes and verifies the output text accordingly.
        - Ensure that the test creates an instance of the OutputText controller with id "click_counts"
        - Ensure that the output text component is verified for its initial value and updated values based on button clicks.
        - Ensure that the test checks the click counts for each button and verifies the output text accordingly.
        - Ensure that the test creates instances of the InputActionButton controller with ids "btn2" and "btn3"
        - Ensure that the disabled button with icon is verified for its label and icon.
        - Ensure that the styled button is verified for its label and custom styles.
        - Ensure that the test checks the click counts for each button and verifies the output text accordingly
        """,
        "app_08_navigation": """
        For this app, focus on:
        - Whether the test creates an instance of the NavsetTab controller with id "navset_Tab"
        - Ensure that the navset tab component is verified for its titles and active state.
        - Ensure that the test checks the navigation between tabs and verifies the active state of each tab
        - Ensure that the test verifies the content of each tab, including input components and output displays
        - Ensure that the test checks the functionality of input components in each tab, such as text inputs, sliders, and action buttons
        - 
        """,
        "app_04_custom_app_name": """
        For this app, focus on:
        - Ensure that the create_app_ficture is called with the correct app file. In this case, it should be "app_input_checkbox_group.py"
        - Ensure that the test creates an instance of the InputCheckboxGroup controller with id "colors"
        - Ensure that the checkbox group component is verified for its label, choices, selected values, inline state, and width.
        - Ensure that the test checks the checkbox group state changes and verifies the output text accordingly.
        - Ensure that the test creates an instance of the OutputText controller with id "selected_colors"
        - Ensure that the output text component is verified for its initial value and updated values based on checkbox selections.
        """,
        "app_01_core_basic": """
        For this app, focus on:
        - Ensure that the test creates an instance of the InputActionButton controller with id "btn1"
        - Ensure that the action button component is verified for its label and click functionality.
        - Ensure that the test checks the action button state changes and verifies the output text accordingly.
        - Ensure that the test creates an instance of the OutputText controller with id "click_counts"
        - Ensure that the test creates instances of the InputActionButton controller with ids "btn2" and "btn3"
        """,
        "app_05_streamlit": """
        For this app, focus on:
        - The test code should be empty since the app code was not a Shiny for Python app.
        """,
    }

    return app_instructions.get(app_name, "")


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
        app_specific_guidance = get_app_specific_instructions(data["app_name"])

        # The question should be clear about what we're evaluating
        question = f"""Evaluate the quality of this Shiny test code for app {data['app_name']}.

App Code:
```python
{data['app_code']}
```

Test Code to Evaluate:
```python
{data['test_code']}
```"""

        # For non-Shiny apps, expect empty test code
        if data["app_name"] in ["app_06_R_shiny", "app_05_streamlit"]:
            target_answer = "CORRECT: The test code should be empty since this is not a Shiny for Python app."
        elif app_specific_guidance:
            target_answer = f"CORRECT: A comprehensive test that meets all specified criteria.\n{app_specific_guidance.strip()}"
        else:
            target_answer = "CORRECT: A comprehensive test that meets all specified criteria."

        sample = Sample(
            input=question,
            target=target_answer,
            metadata={
                "test_name": test_name,
                "app_name": data["app_name"],
                "app_path": data["app_path"],
                "criterion": app_specific_guidance,
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

    # Use the default template but with custom instructions and grade pattern
    scorer = model_graded_qa(
        instructions="""
        You are an expert in Shiny application testing. Evaluate the test code quality based on the provided criteria.

        For non-Shiny frameworks (R Shiny, Streamlit, etc.), the test code should be empty.
        For Shiny for Python apps, use the specific criteria provided in the criterion section.

        Provide your evaluation in the following format:
        GRADE: [C/P/I]
        - C: Complete/Correct - All or nearly all criteria met comprehensively
        - P: Partial - Most criteria met, some minor gaps  
        - I: Incomplete - Major criteria missing or significant issues

        Explanation: [Brief explanation of the grade]
        """,
        grade_pattern=r"GRADE:\s*([CPI])",
    )

    return Task(
        dataset=samples,
        solver=[generate()],
        scorer=scorer,
    )
