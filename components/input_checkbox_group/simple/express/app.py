from shiny import reactive
from shiny.express import input, render, ui

# Sample data as a dictionary mapping values to labels
choices = {
    "red": ui.span("Red", style="color: #FF0000;"),
    "green": ui.span("Green", style="color: #00AA00;"),
    "blue": ui.span("Blue", style="color: #0000AA;"),
}

# Set page title
ui.page_opts(title="Checkbox Group Demo")

# Create checkbox group input
ui.input_checkbox_group(
    "colors",  # input id
    "Choose your favorite colors:",  # label
    choices=choices,
    selected=["red"],  # pre-select red
)


# Display the selected values
@render.text
def selected_colors():
    if not input.colors():
        return "No colors selected"
    return f"You selected: {', '.join(input.colors())}"


# Show count of selected colors
@render.text
def color_count():
    count = len(input.colors()) if input.colors() else 0
    return f"Number of colors selected: {count}"
