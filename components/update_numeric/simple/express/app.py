from shiny import reactive, render
from shiny.express import input, ui

# Create a Shiny app that demonstrates update_numeric()
ui.page_opts(title="Update Numeric Input Demo")

# Sidebar with controls
with ui.sidebar():
    # Initial numeric input
    ui.input_numeric("base_number", "Base Number", value=50, min=0, max=100)

    # Buttons to modify the numeric input
    ui.input_action_button("double_btn", "Double the Number")
    ui.input_action_button("halve_btn", "Halve the Number")
    ui.input_action_button("reset_btn", "Reset to Original")


# Display the current value
@reactive.effect
@reactive.event(input.double_btn)
def _():
    # Double the number, ensuring it doesn't exceed max
    new_value = min(input.base_number() * 2, 100)
    ui.update_numeric("base_number", value=new_value)


@reactive.effect
@reactive.event(input.halve_btn)
def _():
    # Halve the number, ensuring it doesn't go below min
    new_value = max(input.base_number() // 2, 0)
    ui.update_numeric("base_number", value=new_value)


@reactive.effect
@reactive.event(input.reset_btn)
def _():
    # Reset to the original value
    ui.update_numeric("base_number", value=50)


# Display the current value
@render.text
def show_current_value():
    return f"Current Number: {input.base_number()}"
