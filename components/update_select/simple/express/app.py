from shiny import reactive
from shiny.express import input, render, ui

# Sample data - dictionary with grouped choices
choices = {
    "Fruits": {"apple": "Apple", "banana": "Banana", "orange": "Orange"},
    "Vegetables": {"carrot": "Carrot", "celery": "Celery", "lettuce": "Lettuce"},
}

# Input checkbox group to control select input
ui.input_checkbox_group(
    "food_types",
    "Select food types to show:",
    choices=["Fruits", "Vegetables"],
    selected=["Fruits", "Vegetables"],
)

# Select input that will be updated
ui.input_select("foods", "Select foods:", choices=choices)


# Show the current selection
@render.text
def selected_food():
    return f"You selected: {input.foods()}"


# Update select input based on checkbox selections
@reactive.effect
def _():
    # Get selected food types
    selected_types = input.food_types()

    # Build new choices dictionary based on selections
    new_choices = {k: v for k, v in choices.items() if k in selected_types}

    # Update the select input
    ui.update_select("foods", choices=new_choices)
