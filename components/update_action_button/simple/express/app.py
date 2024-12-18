from shiny import reactive
from shiny.express import input, ui, render  # Added render import

# Create a reactive value to track the number of clicks
click_count = reactive.value(0)

# Page title and description
ui.page_opts(title="Update Action Button Demo")

# Sidebar with buttons
with ui.sidebar():
    # Initial action button
    ui.input_action_button("main_button", "Click Me!", class_="btn-primary")

    # Buttons to modify the main button
    ui.input_action_button("disable_button", "Toggle Button State")
    ui.input_action_button("change_label_button", "Change Button Label")

# Main content area to display current state
with ui.card():
    ui.card_header("Button Interaction")

    # Display current click count
    @render.text
    def click_display():
        return f"Button has been clicked {click_count.get()} times"


# Reactive effect to increment click count when main button is clicked
@reactive.effect
@reactive.event(input.main_button)
def _():
    click_count.set(click_count.get() + 1)


# Reactive effect to toggle button state
@reactive.effect
@reactive.event(input.disable_button)
def _():
    # Toggle between enabled and disabled states
    is_disabled = input.main_button() % 2 == 1
    ui.update_action_button("main_button", disabled=not is_disabled)


# Reactive effect to change button label
@reactive.effect
@reactive.event(input.change_label_button)
def _():
    # Cycle through different labels
    labels = ["Click Me!", "Press Here!", "Go!", "Do Something!"]
    current_label_index = input.main_button() % len(labels)
    ui.update_action_button("main_button", label=labels[current_label_index])
