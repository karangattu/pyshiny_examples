from shiny import reactive
from shiny.express import input, render, ui

# Create sample data
fruit_choices = ["Apple", "Banana", "Orange", "Mango", "Grape"]
veggie_choices = ["Carrot", "Broccoli", "Spinach", "Tomato", "Cucumber"]

# First checkbox group controls the second one
ui.input_checkbox_group(
    "fruits", "Select fruits:", choices=fruit_choices, selected=["Apple", "Banana"]
)

ui.input_checkbox_group("veggies", "Select vegetables:", choices=veggie_choices)


@reactive.effect
def _():
    # Get selected fruits
    selected_fruits = input.fruits()

    # Update the veggies checkbox group based on number of selected fruits
    ui.update_checkbox_group(
        "veggies",
        label=f"Select vegetables (you picked {len(selected_fruits) if selected_fruits else 0} fruits):",
        choices=veggie_choices,
        selected=veggie_choices[: len(selected_fruits) if selected_fruits else 0],
    )


# Display selections
@render.text
def show_selections():
    fruits = input.fruits()
    veggies = input.veggies()
    return f"""
    Selected fruits: {', '.join(fruits) if fruits else 'None'}
    Selected veggies: {', '.join(veggies) if veggies else 'None'}
    """
