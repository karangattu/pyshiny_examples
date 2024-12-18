from shiny import reactive
from shiny.express import input, ui, render

# Create a simple app to demonstrate update_action_link
ui.page_opts(title="Update Action Link Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_action_button("update", "Update Link")
        ui.input_radio_buttons("icon_choice", "Choose Icon", ["🌟", "🚀", "🎉", "🌈"])

    # Initial action link
    ui.input_action_link("demo_link", "Click me!", icon="🌟")

    # Render a text output to show current link details
    @render.text
    def link_details():
        return f"Current link clicks: {input.demo_link()}"


# Reactive effect to update the action link
@reactive.effect
@reactive.event(input.update)
def _():
    # Dynamically update the link's label and icon
    ui.update_action_link(
        "demo_link",
        label=f"Clicked {input.demo_link()} times",
        icon=input.icon_choice(),
    )
