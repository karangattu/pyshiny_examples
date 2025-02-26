from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fluid(
    # Add a container for better spacing
    ui.div(
        # Simple button to trigger modal
        ui.input_action_button("show", "Show modal dialog", class_="btn btn-primary"),
        ui.output_text("txt", class_="mt-3"),
        class_="container mt-5",
    )
)


# Define the server
def server(input, output, session):
    # Create a reactive effect to show modal when button is clicked
    @reactive.effect
    @reactive.event(input.show)
    def show_modal():
        # Create a modal with various content types
        m = ui.modal(
            ui.p("This is the main content of the modal."),
            ui.tags.br(),
            ui.tags.p("Here's a paragraph with some details."),
            ui.div(ui.input_text("modal_input", "Enter some text:"), class_="mb-3"),
            # Modal title
            title="Comprehensive Modal Example",
            # Footer with buttons
            footer=ui.div(
                ui.modal_button("Close", class_="btn-secondary me-2"),
                ui.modal_button("Save", class_="btn-primary"),
            ),
            # Modal size - can be 's', 'm', 'l', 'xl'
            size="m",
            # Allow closing by clicking outside or pressing Escape
            easy_close=True,
            # Enable fade animation
            fade=True,
        )

        # Show the modal
        ui.modal_show(m)

    # Add some text to show the app is still responsive
    @output
    @render.text
    def txt():
        return "The main app remains interactive while modal is shown"


# Create and return the app
app = App(app_ui, server)
