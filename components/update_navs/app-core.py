from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    # Title is set in page_fillable since page_opts isn't available in core
    title="Update Navs Demo",
    
    # Create sidebar with controls
    ui.sidebar(
        ui.h4("Navigation Controls"),
        ui.input_action_button(
            "goto1", "Go to Panel 1", 
            class_="btn-primary w-100 mb-2"
        ),
        ui.input_action_button(
            "goto2", "Go to Panel 2", 
            class_="btn-primary w-100 mb-2"
        ),
        ui.input_action_button(
            "goto3", "Go to Panel 3", 
            class_="btn-primary w-100 mb-2"
        ),
        ui.hr(),
        ui.output_text("current_panel"),
    ),

    # Main content area with navset
    ui.navset_tab(
        ui.nav_panel(
            "Panel 1",
            ui.card(
                ui.card_header("Panel 1"),
                "This is the content for Panel 1"
            ),
            value="panel1"
        ),
        ui.nav_panel(
            "Panel 2", 
            ui.card(
                ui.card_header("Panel 2"),
                "This is the content for Panel 2"
            ),
            value="panel2"
        ),
        ui.nav_panel(
            "Panel 3",
            ui.card(
                ui.card_header("Panel 3"),
                "This is the content for Panel 3"
            ),
            value="panel3"
        ),
        id="inTabset"
    ),
)

# Define the server
def server(input, output, session):
    # Display current panel
    @output
    @render.text
    def current_panel():
        return f"Currently selected: {input.inTabset()}"

    # Effects to handle button clicks
    @reactive.effect
    @reactive.event(input.goto1)
    def _():
        ui.update_navs("inTabset", selected="panel1")

    @reactive.effect
    @reactive.event(input.goto2)
    def _():
        ui.update_navs("inTabset", selected="panel2")

    @reactive.effect
    @reactive.event(input.goto3)
    def _():
        ui.update_navs("inTabset", selected="panel3")

# Create and return the app
app = App(app_ui, server)