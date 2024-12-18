from shiny import reactive
from shiny.express import input, render, ui

# Create a simple app demonstrating update_numeric
ui.page_opts(title="Update Numeric Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_slider("controller", "Controller", min=0, max=20, value=10)
        ui.input_numeric("inNumber", "Input number", 0)
        ui.input_numeric("inNumber2", "Input number 2", 0)

    with ui.card():
        ui.card_header("Demonstration of update_numeric")

        @render.text
        def txt():
            return f"Controller value is: {input.controller()}"


@reactive.effect
def _():
    x = input.controller()
    # Update first numeric input to match controller value
    ui.update_numeric("inNumber", value=x)

    # Update second numeric with modified label and range based on controller
    ui.update_numeric(
        "inNumber2", label=f"Number label {x}", value=x, min=x - 5, max=x + 5, step=1
    )
