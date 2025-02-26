from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    # Create a sidebar with an id (required for update_sidebar)
    ui.sidebar(
        ui.h4("Sidebar Content"),
        ui.markdown("This sidebar can be controlled using the buttons below."),
        id="demo_sidebar",
        open="always",
    ),
    # Main content area
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Sidebar Controls"),
            ui.layout_column_wrap(
                ui.input_action_button(
                    "show_sidebar", "Show Sidebar", class_="btn-success w-100"
                ),
                ui.input_action_button(
                    "hide_sidebar", "Hide Sidebar", class_="btn-danger w-100"
                ),
                width=1 / 2,
            ),
            ui.hr(),
            ui.output_text("sidebar_state"),
        ),
        width="100%",
    ),
)


# Define the server
def server(input, output, session):
    # Render text showing sidebar state
    @output
    @render.text
    def sidebar_state():
        return f"Current sidebar state: {input.demo_sidebar()}"

    # Effect to show the sidebar
    @reactive.effect
    @reactive.event(input.show_sidebar)
    def show_sidebar():
        ui.update_sidebar("demo_sidebar", show=True)

    # Effect to hide the sidebar
    @reactive.effect
    @reactive.event(input.hide_sidebar)
    def hide_sidebar():
        ui.update_sidebar("demo_sidebar", show=False)


# Create and return the app
app = App(app_ui, server)
