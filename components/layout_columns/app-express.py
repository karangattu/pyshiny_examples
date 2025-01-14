from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Layout Columns Demo", fillable=True)

# Example using layout_columns parameters
with ui.layout_columns(
    col_widths={
        "sm": (6, 6),  # On small screens: 2 equal columns
        "lg": (4, 8),  # On large screens: 4 and 8 units
    },
    gap="1rem",  # Gap between columns
    class_="my-layout",  # Custom CSS class
):
    # First column
    with ui.card(height="300px"):
        ui.card_header("Card 1")
        "This is content for card 1"

        @render.text
        def card1_content():
            return "Dynamic content for card 1"

    # Second column
    with ui.card(height="300px"):
        ui.card_header("Card 2")
        "This is content for card 2"

        @render.text
        def card2_content():
            return "Dynamic content for card 2"


# Another row of columns with different settings
with ui.layout_columns(
    col_widths={
        "sm": (4, 4, 4),  # On small screens: 3 equal columns
        "lg": (3, 6, 3),  # On large screens: 3, 6, 3 units
    },
    gap="1rem",
):
    # First column
    with ui.card(height="200px"):
        ui.card_header("Card 3")
        "This is content for card 3"

        @render.text
        def card3_content():
            return "Dynamic content for card 3"

    # Second column
    with ui.card(height="200px"):
        ui.card_header("Card 4")
        "This is content for card 4"

        @render.text
        def card4_content():
            return "Dynamic content for card 4"

    # Third column
    with ui.card(height="200px"):
        ui.card_header("Card 5")
        "This is content for card 5"

        @render.text
        def card5_content():
            return "Dynamic content for card 5"
