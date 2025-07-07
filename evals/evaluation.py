from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import model_graded_qa
from inspect_ai.solver import generate, self_critique
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
        "test_app_09_plots_app": """
        For this basic histogram app, focus on:
        - Testing slider input validation and range handling
        - Verifying histogram generation with different bin counts
        - Checking plot output updates when inputs change
        - Testing with edge cases like minimum/maximum slider values
        - Validating that the histogram displays correctly with different datasets
        """,
        
        "test_app_07_modules_app": """
        For this data exploration app, focus on:
        - Testing file upload functionality and format validation
        - Verifying data table display and filtering capabilities
        - Testing column selection and data type handling
        - Checking summary statistics calculations
        - Validating download functionality for processed data
        """,
        
        "test_app_03_slider_app": """
        For this interactive dashboard app, focus on:
        - Testing multiple input controls and their interactions
        - Verifying that charts update synchronously across panels
        - Testing filtering and data subset functionality
        - Checking responsive layout across different screen sizes
        - Validating export functionality for visualizations
        """,
        
        "test_app_06_R_shiny_app": """
        For this real-time monitoring app, focus on:
        - Testing automatic data refresh mechanisms
        - Verifying alert systems and threshold notifications
        - Testing pause/resume functionality for live updates
        - Checking data buffer management and memory usage
        - Validating time-series chart updates and performance
        """,
        
        "test_app_10_complex_layout_app": """
        For this form validation app, focus on:
        - Testing all input validation rules and error messages
        - Verifying form submission and data processing
        - Testing field dependencies and conditional logic
        - Checking user feedback and error handling
        - Validating data sanitization and security measures
        """,
        
        "test_app_02_express_basic_app": """
        For this chart building app, focus on:
        - Testing chart type selection and customization options
        - Verifying data binding and axis configuration
        - Testing color schemes and styling options
        - Checking chart export functionality in different formats
        - Validating interactive features like zoom and pan
        """,
        
        "test_app_08_navigation_app": """
        For this table editor app, focus on:
        - Testing cell editing and data validation
        - Verifying add/delete row functionality
        - Testing sorting and filtering capabilities
        - Checking undo/redo operations
        - Validating data persistence and save functionality
        """,
        
        "test_app_04_custom_app_name_app_input_checkbox_group": """
        For this plot gallery app, focus on:
        - Testing plot type switching and rendering
        - Verifying parameter controls for each plot type
        - Testing data source selection and loading
        - Checking plot customization options
        - Validating thumbnail generation and gallery navigation
        """,
        
        "test_app_01_core_basic_app": """
        For this statistical analysis app, focus on:
        - Testing statistical test selection and parameter validation
        - Verifying calculation accuracy and result interpretation
        - Testing data preprocessing and transformation options
        - Checking report generation and result export
        - Validating assumption checking and diagnostic plots
        """,
        
        "test_app_05_streamlit_app": """
        For this user authentication app, focus on:
        - Testing login/logout functionality and session management
        - Verifying user role permissions and access control
        - Testing password validation and security measures
        - Checking user registration and profile management
        - Validating secure data handling and privacy protection
        """
    }
    
    return app_instructions.get(app_name, "")


def create_test_specific_instructions(test_data: dict) -> str:
    """
    Create specific grading instructions based on the test and app characteristics.

    Args:
        test_data: Dictionary containing test metadata

    Returns:
        Formatted instructions for model grading
    """
    app_name = test_data["app_name"]
    app_specific_guidance = get_app_specific_instructions(app_name)

    base_instructions = f"""
    You are evaluating a Shiny application test for the app: {app_name}

    Please assess the test quality based on the following criteria:

    1. **Test Coverage**: Does the test cover the main functionality of the Shiny app?
    2. **Code Quality**: Is the test code well-structured and maintainable?

    Context about the app:
    - App location: {test_data['app_path']}
    - This is a Shiny application that may include UI components, server logic, and reactive elements

    **App-Specific Testing Focus:**
    {app_specific_guidance}

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
        app_specific_guidance = get_app_specific_instructions(data["app_name"])

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

        # Create app-specific target answer
        if app_specific_guidance:
            target_answer = f"A high-quality test for {data['app_name']} should address the following points:{app_specific_guidance}"
        else:
            target_answer = f"A high-quality test for {data['app_name']} should score 7-10 points with comprehensive coverage of app functionality, proper handling of app-specific features, and robust test assertions."

        sample = Sample(
            input=prompt,
            target=target_answer,
            metadata={
                "test_name": test_name,
                "app_name": data["app_name"],
                "app_path": data["app_path"],
                "custom_instructions": instructions,
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

    # Create a custom scorer that uses the app-specific instructions
    def custom_scorer_instructions(sample):
        return sample.metadata.get("custom_instructions", "")

    scorer = model_graded_qa(
        instructions="""
        You are an expert in Shiny application testing. If its any other framework (e.g. Shiny for R, Streamlit, Dash), Test code should be empty.

        Use the specific instructions provided for each app to focus your evaluation on the most 
        relevant aspects of that particular application type.
        """
    )

    return Task(
        dataset=samples,
        # solver=[generate(), self_critique()],
        scorer=scorer,
        # max_messages=10,
    )
