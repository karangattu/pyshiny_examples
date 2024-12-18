from shiny import reactive
from shiny.express import input, render, ui

# Add page title
ui.page_opts(title="Checkbox Update Demo")

# Create a slider to control checkbox state
ui.input_slider("controller", "Controller", min=0, max=1, value=0, step=1)

# Create a checkbox that will be controlled
ui.input_checkbox("my_checkbox", "Controlled Checkbox")

# Add some explanatory text
ui.markdown(
    """
This demo shows how to use `update_checkbox`:
* Move the slider to control the checkbox
* When slider is at 0, checkbox will be unchecked
* When slider is at 1, checkbox will be checked
"""
)


# Create a reactive effect to update the checkbox based on slider value
@reactive.effect
def _():
    # True if controller is 1, False if 0
    is_checked = input.controller() == 1
    ui.update_checkbox("my_checkbox", value=is_checked)


# Display current state
@render.text
def current_state():
    return f"""
    Current States:
    - Slider value: {input.controller()}
    - Checkbox value: {input.my_checkbox()}
    """
