from shiny import App, reactive, render, ui

app_ui = ui.page_fillable(
    # First row of columns
    ui.layout_columns(
        ui.card(
            ui.card_header("Card 1"),
            "This is content for card 1",
            ui.output_text("card1_content"),
            height="300px",
        ),
        ui.card(
            ui.card_header("Card 2"),
            "This is content for card 2",
            ui.output_text("card2_content"),
            height="300px",
        ),
        col_widths={
            "sm": (6, 6),  # On small screens: 2 equal columns
            "lg": (4, 8),  # On large screens: 4 and 8 units
        },
        gap="1rem",  # Gap between columns
        class_="my-layout",  # Custom CSS class
    ),
    # Second row of columns
    ui.layout_columns(
        ui.card(
            ui.card_header("Card 3"),
            "This is content for card 3",
            ui.output_text("card3_content"),
            height="200px",
        ),
        ui.card(
            ui.card_header("Card 4"),
            "This is content for card 4",
            ui.output_text("card4_content"),
            height="200px",
        ),
        ui.card(
            ui.card_header("Card 5"),
            "This is content for card 5",
            ui.output_text("card5_content"),
            height="200px",
        ),
        col_widths={
            "sm": (4, 4, 4),  # On small screens: 3 equal columns
            "lg": (3, 6, 3),  # On large screens: 3, 6, 3 units
        },
        gap="1rem",
    ),
)


def server(input, output, session):
    @output
    @render.text
    def card1_content():
        return "Dynamic content for card 1"

    @output
    @render.text
    def card2_content():
        return "Dynamic content for card 2"

    @output
    @render.text
    def card3_content():
        return "Dynamic content for card 3"

    @output
    @render.text
    def card4_content():
        return "Dynamic content for card 4"

    @output
    @render.text
    def card5_content():
        return "Dynamic content for card 5"


app = App(app_ui, server)
