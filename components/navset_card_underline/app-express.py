from shiny import reactive
from shiny.express import input, render, ui

# Set page options
ui.page_opts(title="Navset Card Underline Demo", fillable=True)

# Create a navset_card_underline with all possible parameters
with ui.navset_card_underline(
    id="nav_id",  # Optional id for tracking selected panel
    selected="panel2",  # Initially selected panel
):
    with ui.nav_panel("Panel 1", value="panel1"):
        ui.h4("Content for Panel 1")
        ui.markdown(
            """
        This is the content for Panel 1. You can add any UI elements here.
        - Item 1
        - Item 2
        - Item 3
        """
        )

    with ui.nav_panel("Panel 2", value="panel2"):
        ui.h4("Content for Panel 2")
        with ui.card():
            "This is a card inside Panel 2"
            ui.input_text("txt", "Enter some text", "")

    with ui.nav_menu("More Panels"):
        with ui.nav_panel("Panel 3", value="panel3"):
            ui.h4("Content for Panel 3")
            ui.input_slider("n", "N", 0, 100, 20)

        with ui.nav_panel("Panel 4", value="panel4"):
            ui.h4("Content for Panel 4")
            ui.input_numeric("num", "Enter a number", 0)


# Show which panel is currently selected
@render.text
def selected_panel():
    return f"Currently selected panel: {input.nav_id()}"


# Show the value of text input when it changes
@render.text
def txt_out():
    return f"Text input value: {input.txt()}" if input.txt() else ""


# Show the value of numeric input when it changes
@render.text
def num_out():
    return f"Numeric input value: {input.num()}"


# Show the value of slider when it changes
@render.text
def slider_out():
    return f"Slider value: {input.n()}"
