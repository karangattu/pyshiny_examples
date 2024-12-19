from shiny import reactive
from shiny.express import input, ui, render

# Sample data (dictionary mapping choices to labels)
choices = {
    "red": ui.span("Red", style="color: #FF0000;"),
    "green": ui.span("Green", style="color: #00AA00;"),
    "blue": ui.span("Blue", style="color: #0000AA;"),
}

# Title for the app
ui.page_opts(title="Checkbox Demo")

# Create a checkbox group with colored labels
ui.input_checkbox_group(
    "colors",
    "Choose your favorite colors:",
    choices=choices,
    selected=["red"],  # Pre-select red by default
)


# Show the selected values
@render.text
def selected_colors():
    if not input.colors():
        return "No colors selected"
    return f"You selected: {', '.join(input.colors())}"


# Show count of selections
@render.text
def selection_count():
    count = len(input.colors()) if input.colors() else 0
    return f"Number of colors selected: {count}"
