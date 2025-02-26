from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    # Create navset with underlined navigation
    ui.navset_underline(
        # Panel A
        ui.nav_panel(
            "Panel A",
            ui.card(
                ui.card_header("Panel A Content"),
                "This is the content for Panel A",
                ui.input_text("text_a", "Enter text for Panel A", "Sample text"),
            ),
        ),
        # Panel B
        ui.nav_panel(
            "Panel B",
            ui.card(
                ui.card_header("Panel B Content"),
                "This is the content for Panel B",
                ui.input_numeric("num_b", "Enter number for Panel B", 42),
            ),
            value="panel_b",
        ),
        # Panel C
        ui.nav_panel(
            "Panel C",
            ui.card(
                ui.card_header("Panel C Content"),
                "This is the content for Panel C",
                ui.input_slider("slider_c", "Slide in Panel C", 0, 100, 50),
            ),
        ),
        # Dropdown menu for additional panels
        ui.nav_menu(
            "More Options",
            ui.nav_panel(
                "Panel D",
                ui.card(
                    ui.card_header("Panel D Content"),
                    "This is the content for Panel D",
                    ui.input_checkbox("check_d", "Check this in Panel D"),
                ),
            ),
            ui.nav_panel(
                "Panel E",
                ui.card(
                    ui.card_header("Panel E Content"),
                    "This is the content for Panel E",
                    ui.input_radio_buttons(
                        "radio_e",
                        "Choose in Panel E",
                        choices=["Option 1", "Option 2", "Option 3"],
                    ),
                ),
            ),
        ),
        id="nav_id",
    ),
    # Card showing current panel
    ui.card(ui.card_header("Navigation Status"), ui.output_text("selected_panel")),
    # Card showing input values
    ui.card(ui.card_header("Input Values"), ui.output_text("panel_values")),
)


# Define the server
def server(input, output, session):
    @output
    @render.text
    def selected_panel():
        return f"Currently selected panel: {input.nav_id()}"

    @output
    @render.text
    def panel_values():
        return (
            f"Text from Panel A: {input.text_a()}\n"
            f"Number from Panel B: {input.num_b()}\n"
            f"Slider value from Panel C: {input.slider_c()}\n"
            f"Checkbox state from Panel D: {input.check_d()}\n"
            f"Radio selection from Panel E: {input.radio_e()}"
        )


# Create and return the app
app = App(app_ui, server)
