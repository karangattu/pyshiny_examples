from shiny import reactive
from shiny.express import input, ui, render

# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

# Page title and description
ui.page_opts(title="Notification Demo", fillable=True)

with ui.layout_columns():
    # Column 1: Basic Notifications
    with ui.card():
        ui.card_header("Basic Notifications")
        ui.input_action_button("show_basic", "Show Basic Notification")
        ui.input_action_button("show_long", "Show Long Duration")
        ui.input_action_button("show_no_close", "Show Without Close Button")

    # Column 2: Notification Types
    with ui.card():
        ui.card_header("Notification Types")
        ui.input_action_button("show_message", "Show Message Type")
        ui.input_action_button("show_warning", "Show Warning Type")
        ui.input_action_button("show_error", "Show Error Type")

    # Column 3: Actions and IDs
    with ui.card():
        ui.card_header("Actions and IDs")
        ui.input_action_button("show_action", "Show With Action")
        ui.input_action_button("show_replace", "Show Replaceable")
        ui.input_action_button("show_replace_update", "Update Replaceable")


# Event handlers for basic notifications
@reactive.effect
@reactive.event(input.show_basic)
def _():
    ui.notification_show("This is a basic notification", duration=3)


@reactive.effect
@reactive.event(input.show_long)
def _():
    ui.notification_show("This notification stays for 10 seconds", duration=10)


@reactive.effect
@reactive.event(input.show_no_close)
def _():
    ui.notification_show(
        "This notification has no close button", close_button=False, duration=5
    )


# Event handlers for notification types
@reactive.effect
@reactive.event(input.show_message)
def _():
    ui.notification_show(
        ui.HTML(
            '<i class="fa-solid fa-circle-info"></i> This is a message type notification'
        ),
        type="message",
    )


@reactive.effect
@reactive.event(input.show_warning)
def _():
    ui.notification_show(
        ui.HTML(
            '<i class="fa-solid fa-triangle-exclamation"></i> This is a warning type notification'
        ),
        type="warning",
    )


@reactive.effect
@reactive.event(input.show_error)
def _():
    ui.notification_show(
        ui.HTML(
            '<i class="fa-solid fa-circle-xmark"></i> This is an error type notification'
        ),
        type="error",
    )


# Event handlers for actions and IDs
@reactive.effect
@reactive.event(input.show_action)
def _():
    ui.notification_show(
        "Notification with action",
        action=ui.a("Click me!", href="#", onclick="alert('Action clicked!')"),
        duration=None,  # Stays until closed
    )


@reactive.effect
@reactive.event(input.show_replace)
def _():
    ui.notification_show(
        "This is a replaceable notification", id="replaceable", duration=None
    )


@reactive.effect
@reactive.event(input.show_replace_update)
def _():
    ui.notification_show(
        "This notification replaced the previous one",
        id="replaceable",
        type="message",
        duration=3,
    )
