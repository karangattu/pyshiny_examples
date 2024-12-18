from shiny import reactive
from shiny.express import input, ui

# Create synthetic data for demonstration
phrases = [
    "Hello, World!",
    "Shiny is awesome!",
    "Python rocks!",
    "Interactive apps are fun!",
    "Learning never stops!",
]

ui.page_opts(title="Tooltip Update Demo")

# Buttons to interact with tooltip
ui.input_action_button("btn_show", "Show Tooltip", class_="mt-3 me-3")
ui.input_action_button("btn_close", "Close Tooltip", class_="mt-3 me-3")
ui.input_action_button(
    "btn_update", "Update Tooltip Phrase (and show tooltip)", class_="mt-3 me-3"
)

# Create a tooltip
with ui.tooltip(id="tooltip_id"):
    ui.input_action_button(
        "btn_w_tooltip",
        "A button with a tooltip",
        class_="btn-primary mt-5",
    )
    "A default message"


# Reactive effect to show tooltip
@reactive.effect
@reactive.event(input.btn_show)
def _():
    ui.update_tooltip("tooltip_id", show=True)


# Reactive effect to close tooltip
@reactive.effect
@reactive.event(input.btn_close)
def _():
    ui.update_tooltip("tooltip_id", show=False)


# Reactive effect to update tooltip content
@reactive.effect
@reactive.event(input.btn_update)
def _():
    # Select a random phrase based on button click count
    content = phrases[input.btn_update() % len(phrases)]

    # Update tooltip content and show it
    ui.update_tooltip("tooltip_id", content, show=True)


# Reactive effect for button click notification
@reactive.effect
@reactive.event(input.btn_w_tooltip)
def _():
    ui.notification_show("Button clicked!", duration=3, type="message")
