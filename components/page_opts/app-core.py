from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    # Note: window_title and lang would need to be set via ui.tags.head if needed
    ui.panel_title("Page Options Demo"),
    ui.h2("Main Content"),
    # Layout columns
    ui.layout_columns(
        ui.card(
            ui.h3("Card 1"),
            "This is a card demonstrating the layout",
            ui.input_slider("n", "Number", min=0, max=100, value=20),
            ui.output_text("txt1"),
        ),
        ui.card(
            ui.h3("Card 2"),
            "This is another card showing the full width layout",
            ui.input_numeric("num", "Enter a number", value=10),
            ui.output_text("txt2"),
        ),
    ),
    # Markdown content
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
    ),
)


# Define the server
def server(input, output, session):
    @output
    @render.text
    def txt1():
        return f"You selected: {input.n()}"

    @output
    @render.text
    def txt2():
        return f"You entered: {input.num()}"


# Create the app
app = App(app_ui, server)
