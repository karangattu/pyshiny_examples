from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    ui.panel_title("Update Popover Demo"),
    ui.layout_column_wrap(
        # A button with a popover that we'll update
        ui.card(
            ui.card_header("Popover Demo"),
            ui.popover(
                ui.input_action_button(
                    "main_btn", "Click me (I have a popover)!", class_="btn-primary"
                ),
                "Initial popover content",
                id="demo_popover",
            ),
        ),
        # Control buttons card
        ui.card(
            ui.card_header("Control Buttons"),
            ui.layout_column_wrap(
                ui.input_action_button(
                    "update_content", "Update content", class_="btn-secondary mb-2"
                ),
                ui.input_action_button(
                    "update_title",
                    "Update title & content",
                    class_="btn-secondary mb-2",
                ),
                ui.input_action_button(
                    "show_popover", "Show popover", class_="btn-success mb-2"
                ),
                ui.input_action_button(
                    "hide_popover", "Hide popover", class_="btn-danger mb-2"
                ),
            ),
        ),
        # Status card
        ui.card(
            ui.card_header("Current State"),
            ui.output_text("state"),
        ),
        width="400px",
    ),
)


# Define the server
def server(input, output, session):
    # Render state text
    @output
    @render.text
    def state():
        return (
            f"Main button clicks: {input.main_btn() or 0}\n"
            f"Content updates: {input.update_content() or 0}\n"
            f"Title updates: {input.update_title() or 0}"
        )

    # Effect to update content only
    @reactive.effect
    @reactive.event(input.update_content)
    def _():
        click_count = input.update_content()
        ui.update_popover("demo_popover", f"Content updated {click_count} times!")

    # Effect to update both title and content
    @reactive.effect
    @reactive.event(input.update_title)
    def _():
        click_count = input.update_title()
        ui.update_popover(
            "demo_popover",
            f"Content with title update #{click_count}",
            title=f"Updated Title #{click_count}",
        )

    # Effect to show the popover
    @reactive.effect
    @reactive.event(input.show_popover)
    def _():
        ui.update_popover("demo_popover", show=True)

    # Effect to hide the popover
    @reactive.effect
    @reactive.event(input.hide_popover)
    def _():
        ui.update_popover("demo_popover", show=False)

    # Effect to show notification when main button is clicked
    @reactive.effect
    @reactive.event(input.main_btn)
    def _():
        ui.notification_show(
            f"Main button clicked! (Click count: {input.main_btn()})", duration=2
        )


# Create and return the app
app = App(app_ui, server)
