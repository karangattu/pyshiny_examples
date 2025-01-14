from shiny import reactive
from shiny.express import input, ui, render

# Page title
ui.page_opts(title="Notification Demo", fillable=True)

# Create a card to contain the buttons
with ui.card():
    ui.card_header("Notification Examples")

    # Create buttons to trigger different notification types
    with ui.layout_column_wrap(width="200px"):
        ui.input_action_button("show_default", "Show Default", class_="mb-2")
        ui.input_action_button("show_message", "Show Message", class_="mb-2")
        ui.input_action_button("show_warning", "Show Warning", class_="mb-2")
        ui.input_action_button("show_error", "Show Error", class_="mb-2")
        ui.input_action_button("show_action", "Show Action", class_="mb-2")
        ui.input_action_button("show_persistent", "Show Persistent", class_="mb-2")
        ui.input_action_button("show_id", "Show ID Based", class_="mb-2")


# Effect for default notification
@reactive.effect
@reactive.event(input.show_default)
def show_default():
    ui.notification_show("This is a default notification", duration=3)


# Effect for message notification
@reactive.effect
@reactive.event(input.show_message)
def show_message():
    ui.notification_show("This is a message notification", type="message", duration=3)


# Effect for warning notification
@reactive.effect
@reactive.event(input.show_warning)
def show_warning():
    ui.notification_show("This is a warning notification", type="warning", duration=3)


# Effect for error notification
@reactive.effect
@reactive.event(input.show_error)
def show_error():
    ui.notification_show("This is an error notification", type="error", duration=3)


# Effect for notification with action
@reactive.effect
@reactive.event(input.show_action)
def show_action():
    ui.notification_show(
        "Notification with action",
        action=ui.a("Click me!", href="https://shiny.posit.co/", target="_blank"),
        duration=3,
    )


# Effect for persistent notification
@reactive.effect
@reactive.event(input.show_persistent)
def show_persistent():
    ui.notification_show(
        "This is a persistent notification (no auto-close)",
        duration=None,
        close_button=True,
    )


# Counter for ID notifications
notification_counter = reactive.value(0)


# Effect for notification with ID (replacing previous)
@reactive.effect
@reactive.event(input.show_id)
def show_id():
    current = notification_counter.get()
    notification_counter.set(current + 1)
    ui.notification_show(
        f"Notification #{current + 1} (replaces previous)",
        id="replaceable_notification",
        duration=None,
        close_button=True,
    )


# Add some instructions
with ui.card(class_="mt-3"):
    ui.card_header("Instructions")
    ui.markdown(
        """
    - Click any button to show different types of notifications
    - Default notifications auto-close after 3 seconds
    - Persistent notifications require manual closing
    - ID-based notifications replace previous ones with the same ID
    - Action notifications include a clickable link
    """
    )
