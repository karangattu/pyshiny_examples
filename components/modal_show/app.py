from shiny import reactive
from shiny.express import input, render, ui

ui.page_opts(title="Modal Dialog Example")

# Add a container for better spacing
with ui.div(class_="container mt-5"):
    # Simple button to trigger modal
    ui.input_action_button("show", "Show modal dialog", class_="btn btn-primary")

    ui.output_text("txt", class_="mt-3")


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
@render.text
def txt():
    return "The main app remains interactive while modal is shown"
