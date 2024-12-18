import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
departments = ["Sales", "Marketing", "Engineering", "Finance", "HR"]
employee_data = pd.DataFrame(
    {
        "name": [f"{dept} Employee {i}" for dept in departments for i in range(1, 6)],
        "department": [dept for dept in departments for _ in range(5)],
        "salary": np.random.randint(50000, 150000, 25),
        "years_experience": np.random.randint(1, 20, 25),
        "performance_rating": np.random.uniform(2.0, 5.0, 25).round(1),
    }
)

# Page options
ui.page_opts(title="Input Select Showcase", fillable=True)

# Sidebar with various select input configurations
with ui.sidebar():
    # Basic select input
    ui.input_select(
        "basic_select", "Basic Select", choices=["Option A", "Option B", "Option C"]
    )

    # Select input with dictionary choices
    ui.input_select(
        "dict_select",
        "Select with Dictionary Choices",
        choices={"opt1": "Option One", "opt2": "Option Two", "opt3": "Option Three"},
    )

    # Grouped select input
    ui.input_select(
        "grouped_select",
        "Grouped Select",
        choices={
            "Tech": {"eng": "Engineering", "it": "IT"},
            "Business": {"sales": "Sales", "marketing": "Marketing"},
        },
    )

    # Multiple select input
    ui.input_select(
        "multiple_select", "Multiple Select", choices=departments, multiple=True
    )

    # Selectize input with custom options
    ui.input_select(
        "selectize_select",
        "Selectize Select",
        choices=departments,
        selectize=True,
        multiple=True,
        options={"placeholder": "Select departments", "maxItems": 3},
    )

    # Select input with width and size
    ui.input_select(
        "width_size_select",
        "Width and Size Select",
        choices=list(range(1, 11)),
        width="300px",
        size=5,
    )

# Main content area to display selected values
with ui.layout_columns():
    # Display basic select input
    with ui.card():
        ui.card_header("Basic Select")

        @render.text
        def basic_select_output():
            return f"Selected: {input.basic_select()}"

    # Display dictionary select input
    with ui.card():
        ui.card_header("Dictionary Select")

        @render.text
        def dict_select_output():
            return f"Selected: {input.dict_select()}"

    # Display grouped select input
    with ui.card():
        ui.card_header("Grouped Select")

        @render.text
        def grouped_select_output():
            return f"Selected: {input.grouped_select()}"

    # Display multiple select input
    with ui.card():
        ui.card_header("Multiple Select")

        @render.text
        def multiple_select_output():
            return f"Selected: {input.multiple_select()}"

    # Display selectize select input
    with ui.card():
        ui.card_header("Selectize Select")

        @render.text
        def selectize_select_output():
            return f"Selected: {input.selectize_select()}"

    # Display width and size select input
    with ui.card():
        ui.card_header("Width and Size Select")

        @render.text
        def width_size_select_output():
            return f"Selected: {input.width_size_select()}"


# Optional: Add a data table to show context
@render.data_frame
def employee_table():
    # Filter table based on selected departments in multiple select
    if input.multiple_select():
        return employee_data[employee_data["department"].isin(input.multiple_select())]
    return employee_data
