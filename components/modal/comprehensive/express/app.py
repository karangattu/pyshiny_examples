from shiny import reactive
from shiny.express import input, ui, render
import random
import pandas as pd
import numpy as np

# Synthetic data generation
np.random.seed(42)
data = pd.DataFrame(
    {
        "Name": [f"Person {i}" for i in range(1, 51)],
        "Age": np.random.randint(18, 65, 50),
        "Salary": np.random.randint(30000, 120000, 50),
        "Department": random.choices(
            ["HR", "IT", "Sales", "Marketing", "Finance"], k=50
        ),
    }
)

# Page configuration
ui.page_opts(title="Modal Showcase", fillable=True)

# Add Font Awesome CSS
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.0/css/all.min.css">'
    )
)

# Sidebar with modal configuration options
with ui.sidebar():
    ui.input_checkbox_group(
        "modal_options",
        "Modal Configuration",
        {
            "easy_close": "Easy Close",
            "fade": "Fade Animation",
            "full_screen": "Full Screen",
        },
    )

    ui.input_select("modal_size", "Modal Size", ["s", "m", "l", "xl"])

    ui.input_action_button("show_modal", "Show Modal", class_="btn-primary")
    ui.input_action_button("show_info_modal", "Show Info Modal", class_="btn-info")


# Main content area with data table
@render.data_frame
def employee_table():
    return data


# Modal generation function
@reactive.effect
@reactive.event(input.show_modal)
def _():
    # Dynamically configure modal based on user selections
    m = ui.modal(
        ui.h3("Employee Details"),
        ui.p(f"Total Employees: {len(data)}"),
        ui.p(f"Departments: {', '.join(data['Department'].unique())}"),
        # Conditional footer based on checkboxes
        footer=(
            ui.modal_button("Close")
            if "easy_close" not in input.modal_options()
            else None
        ),
        # Modal configuration parameters
        title="Employee Information",
        size=input.modal_size(),
        easy_close="easy_close" in input.modal_options(),
        fade="fade" in input.modal_options(),
        full_screen="full_screen" in input.modal_options(),
    )
    ui.modal_show(m)


# Info Modal with different configuration
@reactive.effect
@reactive.event(input.show_info_modal)
def _():
    m = ui.modal(
        ui.tags.div(
            ui.tags.i(
                class_="fas fa-chart-pie", style="font-size: 3rem; color: #007bff;"
            ),
            ui.h4("Department Distribution"),
            ui.p(data["Department"].value_counts().to_string()),
            style="text-align: center; padding: 20px;",
        ),
        title="Department Insights",
        size="s",  # Small size
        easy_close=True,
        fade=True,
    )
    ui.modal_show(m)
