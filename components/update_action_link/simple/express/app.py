from shiny import reactive
from shiny.express import input, render, ui

# Page title
ui.page_opts(title="update_action_link Demo")

# Layout with sidebar
with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_action_button("update", "Update link label and icon")
        ui.br()
        ui.br()
        ui.input_text("custom_label", "Custom link label", value="Click me!")

    # Main content area
    ui.h2("Demo of update_action_link")
    ui.markdown(
        """
        Click the button in the sidebar to update the action link below.
        You can also customize the label using the text input.
    """
    )

    ui.hr()

    # The action link that will be updated
    ui.input_action_link("demo_link", "Original Label")

    ui.br()
    ui.br()

    # Display counter of link clicks
    @render.text
    def click_counter():
        return f"Link has been clicked {input.demo_link()} times"


# Counter to track icon changes
icon_state = reactive.value(0)


# Effect to update the action link when the update button is clicked
@reactive.effect
@reactive.event(input.update)
def _():
    # Get current icon state and increment
    current_state = icon_state.get()
    icon_state.set((current_state + 1) % 3)

    # Choose icon based on state
    icons = ["⭐", "🌟", "💫"]
    current_icon = icons[current_state]

    # Update the action link with new label and icon
    ui.update_action_link("demo_link", label=input.custom_label(), icon=current_icon)
