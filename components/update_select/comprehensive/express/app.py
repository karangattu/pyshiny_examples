import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
departments = ["Sales", "Marketing", "Engineering", "Finance", "HR"]
job_levels = ["Entry", "Mid", "Senior", "Executive"]
locations = ["New York", "San Francisco", "Chicago", "Boston", "Austin"]

# Create a DataFrame with synthetic employee data
employee_data = pd.DataFrame(
    {
        "name": [f"Employee {i}" for i in range(1, 101)],
        "department": np.random.choice(departments, 100),
        "job_level": np.random.choice(job_levels, 100),
        "location": np.random.choice(locations, 100),
        "salary": np.random.randint(50000, 200000, 100),
    }
)

# Page setup
ui.page_opts(title="Update Select Demonstration", fillable=True)

# Sidebar with various controls
with ui.sidebar():
    # Initial select input with grouped choices
    ui.input_select(
        "initial_select",
        "Initial Select Input",
        {
            "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
            "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
            "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
        },
    )

    # Buttons to demonstrate different update scenarios
    ui.input_action_button("update_choices", "Update Choices")
    ui.input_action_button("update_label", "Update Label")
    ui.input_action_button("update_selected", "Update Selected")
    ui.input_action_button("reset", "Reset")

# Create a section to show the current state
ui.h4("Current Select Input State")

# Reactive counter to track updates
update_count = reactive.value(0)


# Render the current state of the select input
@render.text
def select_state():
    return f"""
    Current Selection: {input.initial_select()}
    Update Count: {update_count.get()}
    """


# Effect to update choices
@reactive.effect
@reactive.event(input.update_choices)
def _():
    # Demonstrate updating choices with different formats
    update_count.set(update_count.get() + 1)

    ui.update_select(
        "initial_select",
        choices={
            "Tech": {"GOOG": "Google", "MSFT": "Microsoft", "AMZN": "Amazon"},
            "Finance": {
                "JPM": "JP Morgan",
                "BAC": "Bank of America",
                "GS": "Goldman Sachs",
            },
        },
    )


# Effect to update label
@reactive.effect
@reactive.event(input.update_label)
def _():
    update_count.set(update_count.get() + 1)

    ui.update_select(
        "initial_select", label=f"Updated Label (Update {update_count.get()})"
    )


# Effect to update selected value
@reactive.effect
@reactive.event(input.update_selected)
def _():
    update_count.set(update_count.get() + 1)

    # Dynamically select a value
    new_selection = np.random.choice(["GOOG", "MSFT", "JPM"])

    ui.update_select("initial_select", selected=new_selection)


# Effect to reset to original state
@reactive.effect
@reactive.event(input.reset)
def _():
    update_count.set(0)

    ui.update_select(
        "initial_select",
        label="Initial Select Input",
        choices={
            "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
            "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
            "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
        },
        selected="NY",
    )


# Render a table to show employee data based on selection
@render.data_frame
def employee_table():
    # Filter employees based on current selection
    if input.initial_select():
        return employee_data[employee_data["department"] == input.initial_select()]
    return employee_data
