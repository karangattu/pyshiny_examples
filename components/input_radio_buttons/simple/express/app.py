from shiny import reactive
from shiny.express import input, render, ui

# Sample data as a dictionary mapping values to labels
choices = {
    "red": ui.span("Red", style="color: #FF0000;"),
    "green": ui.span("Green", style="color: #00AA00;"),
    "blue": ui.span("Blue", style="color: #0000AA;"),
}

ui.page_opts(title="Radio Button Demo", fillable=True)

with ui.layout_columns():
    # Radio buttons with colored text labels
    ui.input_radio_buttons(
        "color", "Choose your favorite color:", choices=choices, selected="red"
    )

    @render.text
    def selected_color():
        return f"You selected: {input.color()}"
