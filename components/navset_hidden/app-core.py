from shiny import App, reactive, ui

# Define the UI
app_ui = ui.page_fillable(
    # Sidebar with controller
    ui.sidebar(
        ui.input_radio_buttons(
            "controller",
            "Select Panel",
            choices=["panel1", "panel2", "panel3"],
            selected="panel1",
        )
    ),
    # navset_hidden with panels
    ui.navset_hidden(
        # Panel 1
        ui.nav_panel(
            None,
            ui.h3("Panel 1"),
            ui.p("This is the content for Panel 1"),
            ui.card("Some card content in Panel 1"),
            value="panel1",
        ),
        # Panel 2
        ui.nav_panel(
            None,
            ui.h3("Panel 2"),
            ui.p("This is the content for Panel 2"),
            ui.card("Some card content in Panel 2", full_screen=True),
            value="panel2",
        ),
        # Panel 3
        ui.nav_panel(
            None,
            ui.h3("Panel 3"),
            ui.p("This is the content for Panel 3"),
            ui.card("Some card content in Panel 3"),
            value="panel3",
        ),
        id="hidden_nav",
    ),
)


# Define the server
def server(input, output, session):
    # Effect to update selected panel based on radio input
    @reactive.effect
    def _():
        ui.update_navs("hidden_nav", selected=input.controller())


# Create the app
app = App(app_ui, server)
