from shiny import reactive
from shiny.express import input, ui, render

# Page options for basic styling
ui.page_opts(title="Update Popover Demo", fillable=True)

with ui.layout_column_wrap(width="400px"):
    # A button with a popover that we'll update
    with ui.card():
        ui.card_header("Popover Demo")

        with ui.popover(id="demo_popover"):
            ui.input_action_button(
                "main_btn", "Click me (I have a popover)!", class_="btn-primary"
            )
            "Initial popover content"

    # Control buttons card
    with ui.card():
        ui.card_header("Control Buttons")
        with ui.layout_column_wrap():
            ui.input_action_button(
                "update_content", "Update content", class_="btn-secondary mb-2"
            )
            ui.input_action_button(
                "update_title", "Update title & content", class_="btn-secondary mb-2"
            )
            ui.input_action_button(
                "show_popover", "Show popover", class_="btn-success mb-2"
            )
            ui.input_action_button(
                "hide_popover", "Hide popover", class_="btn-danger mb-2"
            )

    # Status card
    with ui.card():
        ui.card_header("Current State")

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
