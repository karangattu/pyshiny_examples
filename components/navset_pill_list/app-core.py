from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    ui.layout_column_wrap(
        ui.navset_pill_list(
            # First nav panel
            ui.nav_panel(
                "Panel A",
                ui.card(
                    ui.card_header("Panel A Content"),
                    "This is the content for Panel A",
                    ui.input_text("text_a", "Enter text for Panel A", ""),
                ),
            ),
            # Second nav panel
            ui.nav_panel(
                "Panel B",
                ui.card(
                    ui.card_header("Panel B Content"),
                    "This is the content for Panel B",
                    ui.input_slider("slider_b", "Slider for Panel B", 0, 100, 50),
                ),
            ),
            # Nav menu with additional panels
            ui.nav_menu(
                "More Options",
                ui.nav_panel(
                    "Panel C",
                    ui.card(
                        ui.card_header("Panel C Content"),
                        "This is the content for Panel C",
                        ui.input_numeric("num_c", "Number input for Panel C", 0),
                    ),
                ),
                ui.nav_panel(
                    "Panel D",
                    ui.card(
                        ui.card_header("Panel D Content"),
                        "This is the content for Panel D",
                        ui.input_checkbox("check_d", "Checkbox for Panel D", False),
                    ),
                ),
            ),
            id="selected_pill_list",
            selected="Panel A",
            well=True,
            widths=(3, 9),
        ),
        # Card showing selection status
        ui.card(ui.card_header("Selection Status"), ui.output_text("selected_panel")),
        width=1,
    )
)


# Define the server
def server(input, output, session):
    @output
    @render.text
    def selected_panel():
        return f"Currently selected panel: {input.selected_pill_list()}"


# Create the Shiny app
app = App(app_ui, server)
