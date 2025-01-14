from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(
    title="Page Options Demo",  # Title shown on the page
    window_title="Browser Window Title",  # Browser window title
    lang="en",  # Language code for HTML
    fillable=True,  # Make page fillable
    full_width=True,  # Use full width layout
)

# Add some content to demonstrate the layout
ui.h2("Main Content")

with ui.layout_columns():
    with ui.card():
        ui.h3("Card 1")
        "This is a card demonstrating the layout"
        ui.input_slider("n", "Number", min=0, max=100, value=20)

        @render.text
        def txt1():
            return f"You selected: {input.n()}"

    with ui.card():
        ui.h3("Card 2")
        "This is another card showing the full width layout"
        ui.input_numeric("num", "Enter a number", value=10)

        @render.text
        def txt2():
            return f"You entered: {input.num()}"


# Add some text to show the fillable layout
ui.markdown(
    """
### About this app

This app demonstrates various page options:
* Custom page title
* Custom window title
* Fillable layout
* Full width layout
* Multiple cards in columns
"""
)
