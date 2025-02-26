from shiny import App, reactive, render, ui

app_ui = ui.page_fillable(
    # Create a navset_card_underline with all possible parameters
    ui.navset_card_underline(
        ui.nav_panel(
            "Panel 1",
            ui.h4("Content for Panel 1"),
            ui.markdown(
                """
                This is the content for Panel 1. You can add any UI elements here.
                - Item 1
                - Item 2
                - Item 3
                """
            ),
            value="panel1",
        ),
        ui.nav_panel(
            "Panel 2",
            ui.h4("Content for Panel 2"),
            ui.card(
                "This is a card inside Panel 2",
                ui.input_text("txt", "Enter some text", ""),
            ),
            value="panel2",
        ),
        ui.nav_menu(
            "More Panels",
            ui.nav_panel(
                "Panel 3",
                ui.h4("Content for Panel 3"),
                ui.input_slider("n", "N", 0, 100, 20),
                value="panel3",
            ),
            ui.nav_panel(
                "Panel 4",
                ui.h4("Content for Panel 4"),
                ui.input_numeric("num", "Enter a number", 0),
                value="panel4",
            ),
        ),
        id="nav_id",
        selected="panel2",
    ),
    ui.output_text("selected_panel"),
    ui.output_text("txt_out"),
    ui.output_text("num_out"),
    ui.output_text("slider_out"),
)


def server(input, output, session):
    @output
    @render.text
    def selected_panel():
        return f"Currently selected panel: {input.nav_id()}"

    @output
    @render.text
    def txt_out():
        return f"Text input value: {input.txt()}" if input.txt() else ""

    @output
    @render.text
    def num_out():
        return f"Numeric input value: {input.num()}"

    @output
    @render.text
    def slider_out():
        return f"Slider value: {input.n()}"


app = App(app_ui, server)
