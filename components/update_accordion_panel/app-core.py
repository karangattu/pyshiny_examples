from shiny import App, reactive, render, ui

# Create the UI
app_ui = ui.page_fluid(
    # Add Font Awesome CSS in head
    ui.tags.head(
        ui.tags.link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css",
        )
    ),
    # Create a container for better layout
    ui.layout_column_wrap(
        ui.input_action_button(
            "update_btn", "Update Panel Content", class_="btn-primary mb-3"
        ),
        # Create an accordion with a panel
        ui.accordion(
            ui.accordion_panel(
                "Original Title",
                ui.markdown("This is the original content"),
                value="panel1",
            ),
            id="acc1",
            open=True,
        ),
        # Show current state
        ui.output_text("current_state"),
        width=1,
    ),
)


# Define server logic
def server(input, output, session):

    @output
    @render.text
    def current_state():
        return f"Current accordion state: {input.acc1()}"

    @reactive.effect
    @reactive.event(input.update_btn)
    def _():
        ui.update_accordion_panel(
            id="acc1",
            target="panel1",
            title="Updated Title",
            value="new_value",
            icon=ui.tags.i(class_="fa-solid fa-star"),
            show=True,
        )


# Create and return the app
app = App(app_ui, server)
