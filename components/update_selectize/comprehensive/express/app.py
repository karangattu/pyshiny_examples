import random
import string

from shiny import reactive
from shiny.express import input, render, ui


# Generate synthetic data
def generate_random_string(length=5):
    return "".join(random.choices(string.ascii_uppercase, k=length))


def generate_nested_choices():
    return {
        "Fruits": {"apple": "Apple", "banana": "Banana", "cherry": "Cherry"},
        "Vegetables": {
            "carrot": "Carrot",
            "broccoli": "Broccoli",
            "spinach": "Spinach",
        },
    }


# Set page options using page_opts from shiny.express.ui
ui.page_opts(title="Selectize Update Demonstration", fillable=True)

# Sidebar with various input controls
with ui.sidebar():
    # Initial selectize input
    ui.input_selectize(
        "main_selectize",
        "Main Selectize Input",
        choices=generate_nested_choices(),
        multiple=True,
        options={"placeholder": "Select items", "maxItems": 3},
    )

    # Controls for updating selectize
    ui.input_checkbox("update_label", "Update Label")
    ui.input_checkbox("update_choices", "Update Choices")
    ui.input_checkbox("update_selected", "Update Selected")
    ui.input_checkbox("update_options", "Update Options")
    ui.input_checkbox("update_server", "Toggle Server-side")


# Main panel to show current state
@render.text
def selectize_state():
    return f"""
    Current Selectize State:
    - Selected: {input.main_selectize()}
    - Server-side: {input.update_server()}
    """


# Reactive effect to update selectize based on checkboxes
@reactive.effect
def update_selectize():
    # Prepare choices and options
    new_choices = {
        "New Fruits": {
            f"{generate_random_string()}": f"New {generate_random_string()} Fruit"
            for _ in range(3)
        },
        "New Vegetables": {
            f"{generate_random_string()}": f"New {generate_random_string()} Vegetable"
            for _ in range(3)
        },
    }

    new_options = {
        "placeholder": "Updated placeholder",
        "maxItems": 5 if input.update_options() else 3,
    }

    # Update selectize with various parameters
    ui.update_selectize(
        "main_selectize",
        # Conditionally update label
        label="Updated Selectize" if input.update_label() else None,
        # Conditionally update choices
        choices=new_choices if input.update_choices() else None,
        # Conditionally update selected
        selected=(
            list(new_choices.get("New Fruits", {}).keys())
            if input.update_selected()
            else None
        ),
        # Conditionally update options
        options=new_options if input.update_options() else None,
        # Conditionally toggle server-side loading
        server=input.update_server(),
    )
