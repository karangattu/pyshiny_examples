from shiny import reactive
from shiny.express import input, ui
import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Synthetic Data Generation
np.random.seed(42)
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry"]
departments = ["Sales", "Marketing", "Engineering", "Finance", "HR"]

employee_data = pd.DataFrame(
    {
        "Name": names,
        "Department": np.random.choice(departments, len(names)),
        "Salary": np.random.randint(50000, 150000, len(names)),
        "Hire Date": [
            datetime.now() - timedelta(days=random.randint(100, 3000)) for _ in names
        ],
    }
)

# Page Setup
ui.page_opts(title="Modal Showcase", fillable=True)

# Sidebar with Modal Interaction Controls
with ui.sidebar():
    ui.input_radio_buttons(
        "modal_type",
        "Modal Type",
        [
            "Basic Modal",
            "Modal with Footer",
            "Large Modal",
            "Modal with Easy Close",
            "Modal with Custom Content",
        ],
    )
    ui.input_checkbox("fade_effect", "Fade Effect", value=True)

# Main Content Area
with ui.card():
    ui.card_header("Modal Demonstration")
    ui.input_action_button("show_modal", "Show Modal")


# Modal Rendering Logic
@reactive.effect
@reactive.event(input.show_modal)
def _():
    # Different Modal Types based on Radio Button Selection
    if input.modal_type() == "Basic Modal":
        m = ui.modal(
            "This is a basic modal with simple content.",
            title="Basic Modal",
            fade=input.fade_effect(),
        )
        ui.modal_show(m)

    elif input.modal_type() == "Modal with Footer":
        m = ui.modal(
            "This modal demonstrates footer functionality.",
            title="Modal with Footer",
            footer=ui.modal_button("Close"),
            fade=input.fade_effect(),
        )
        ui.modal_show(m)

    elif input.modal_type() == "Large Modal":
        m = ui.modal(
            "This is a large modal showcasing the size parameter.",
            title="Large Modal",
            size="l",  # Large size
            fade=input.fade_effect(),
        )
        ui.modal_show(m)

    elif input.modal_type() == "Modal with Easy Close":
        m = ui.modal(
            "This modal can be closed by clicking outside or pressing ESC.",
            title="Easy Close Modal",
            easy_close=True,
            fade=input.fade_effect(),
        )
        ui.modal_show(m)

    elif input.modal_type() == "Modal with Custom Content":
        # Randomly select an employee for demonstration
        employee = employee_data.sample(1).iloc[0]

        m = ui.modal(
            ui.tags.div(
                ui.tags.h3(f"Employee Details: {employee['Name']}"),
                ui.tags.p(f"Department: {employee['Department']}"),
                ui.tags.p(f"Salary: ${employee['Salary']:,}"),
                ui.tags.p(f"Hire Date: {employee['Hire Date'].strftime('%Y-%m-%d')}"),
            ),
            title="Employee Information",
            size="m",
            fade=input.fade_effect(),
            footer=ui.modal_button("Close"),
        )
        ui.modal_show(m)


# Optional: Display current modal type selection
@reactive.effect
def _():
    ui.notification_show(
        f"Selected Modal Type: {input.modal_type()}", duration=2, type="message"
    )
