from shiny import reactive
from shiny.express import input, render, ui

# Sample data
fruits = ["Apple", "Banana", "Orange", "Mango"]
colors = ["Red", "Yellow", "Orange", "Green"]

# Main UI
ui.page_opts(title="Radio Button Update Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_radio_buttons(
            "fruit_selector", "Select a Fruit:", choices=fruits, selected="Apple"
        )

        ui.input_radio_buttons(
            "color_selector", "Color Options:", choices=colors, selected="Red"
        )

    # Main panel content
    @render.text
    def selection_text():
        return f"You selected {input.fruit_selector()} and {input.color_selector()}"


# Update color options based on fruit selection
@reactive.effect
@reactive.event(input.fruit_selector)
def _():
    if input.fruit_selector() == "Apple":
        ui.update_radio_buttons(
            "color_selector",
            label="Apple Colors:",
            choices=["Red", "Green", "Yellow"],
            selected="Red",
        )
    elif input.fruit_selector() == "Banana":
        ui.update_radio_buttons(
            "color_selector",
            label="Banana Colors:",
            choices=["Yellow"],
            selected="Yellow",
        )
    elif input.fruit_selector() == "Orange":
        ui.update_radio_buttons(
            "color_selector",
            label="Orange Colors:",
            choices=["Orange"],
            selected="Orange",
        )
    else:  # Mango
        ui.update_radio_buttons(
            "color_selector",
            label="Mango Colors:",
            choices=["Green", "Yellow", "Orange"],
            selected="Green",
        )
