from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="Notification Demo", fillable=True)

with ui.card():
    ui.card_header("Notification Types Demo")

    with ui.layout_column_wrap():
        ui.input_action_button("show_default", "Show Default", class_="btn-secondary")
        ui.input_action_button("show_message", "Show Message", class_="btn-info")
        ui.input_action_button("show_warning", "Show Warning", class_="btn-warning")
        ui.input_action_button("show_error", "Show Error", class_="btn-danger")


# Show a default notification
@reactive.effect
@reactive.event(input.show_default)
def _():
    ui.notification_show("This is a default notification", duration=3)


# Show a message notification (blue)
@reactive.effect
@reactive.event(input.show_message)
def _():
    ui.notification_show("This is a message notification", duration=3, type="message")


# Show a warning notification (yellow)
@reactive.effect
@reactive.event(input.show_warning)
def _():
    ui.notification_show("This is a warning notification!", duration=3, type="warning")


# Show an error notification (red)
@reactive.effect
@reactive.event(input.show_error)
def _():
    ui.notification_show("This is an error notification!", duration=3, type="error")
