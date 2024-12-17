import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
data = pd.DataFrame(
    {
        "name": [
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Frank",
            "Grace",
            "Henry",
            "Ivy",
            "Jack",
        ],
        "age": np.random.randint(20, 65, 10),
        "salary": np.random.randint(30000, 120000, 10),
        "department": [
            "HR",
            "IT",
            "Sales",
            "Marketing",
            "Finance",
            "HR",
            "IT",
            "Sales",
            "Marketing",
            "Finance",
        ],
        "experience": np.random.randint(1, 20, 10),
    }
)

# Page options and title
ui.page_opts(title="Checkbox Group Showcase", fillable=True)

# Sidebar with various checkbox group configurations
with ui.sidebar():
    # Basic checkbox group with simple list of choices
    ui.input_checkbox_group(
        "basic_choices", "Basic Choices", ["Option A", "Option B", "Option C"]
    )

    # Checkbox group with dictionary mapping (HTML labels)
    ui.input_checkbox_group(
        "html_choices",
        "HTML Choices",
        {
            "red": ui.span("Red", style="color: red;"),
            "green": ui.span("Green", style="color: green;"),
            "blue": ui.span("Blue", style="color: blue;"),
        },
    )

    # Checkbox group with initial selection
    ui.input_checkbox_group(
        "initial_selection",
        "Initial Selection",
        ["Apple", "Banana", "Cherry", "Date"],
        selected=["Apple", "Cherry"],
    )

    # Inline checkbox group
    ui.input_checkbox_group(
        "inline_choices",
        "Inline Choices",
        ["Option 1", "Option 2", "Option 3"],
        inline=True,
    )

    # Department selection with width control
    ui.input_checkbox_group(
        "department_filter",
        "Filter Departments",
        data["department"].unique().tolist(),
        width="300px",
    )

# Main content area with results
with ui.layout_columns():
    # Display selected basic choices
    with ui.card():
        ui.card_header("Basic Choices")

        @render.text
        def basic_choices_output():
            return f"Selected: {input.basic_choices() or 'None'}"

    # Display selected HTML choices
    with ui.card():
        ui.card_header("HTML Choices")

        @render.text
        def html_choices_output():
            return f"Selected: {input.html_choices() or 'None'}"

    # Display initial selection
    with ui.card():
        ui.card_header("Initial Selection")

        @render.text
        def initial_selection_output():
            return f"Selected: {input.initial_selection() or 'None'}"

    # Display inline choices
    with ui.card():
        ui.card_header("Inline Choices")

        @render.text
        def inline_choices_output():
            return f"Selected: {input.inline_choices() or 'None'}"


# Data table filtered by selected departments
@render.data_frame
def filtered_data():
    departments = input.department_filter()
    if not departments:
        return data
    return data[data["department"].isin(departments)]
