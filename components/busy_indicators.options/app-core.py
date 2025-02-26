import time
from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    # Add Font Awesome CSS for icons
    ui.head_content(
        ui.HTML(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">'
        )
    ),
    # Layout with buttons
    ui.layout_column_wrap(
        ui.input_action_button(
            "compute", "Start Long Computation", class_="btn-primary mb-3"
        ),
        ui.input_action_button(
            "compute2", "Another Long Task", class_="btn-success mb-3"
        ),
        ui.output_text("result"),
        ui.output_text("result2"),
        width="400px",
    ),
)


# Define the server
def server(input, output, session):
    # First computation
    @output
    @render.text
    @reactive.event(input.compute)
    def result():
        # Simulate a long computation
        time.sleep(5)
        return "First computation completed!"

    # Second computation
    @output
    @render.text
    @reactive.event(input.compute2)
    def result2():
        # Simulate another long computation
        time.sleep(3)
        return "Second computation completed!"

    # Progress indicator
    @reactive.effect
    @reactive.event(input.compute)
    def show_progress():
        with ui.Progress(min=1, max=10) as p:
            p.set(message="Calculation in progress", detail="This may take a while...")

            for i in range(1, 11):
                p.set(i, message=f"Step {i} of 10")
                time.sleep(0.5)

    # Notification for completion
    @reactive.effect
    @reactive.event(input.compute2)
    def show_notification():
        time.sleep(3)
        ui.notification_show(
            "Task Complete!", duration=3, type="message", close_button=True
        )


# Create and return the app
app = App(app_ui, server)
