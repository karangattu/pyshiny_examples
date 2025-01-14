from shiny import reactive
from shiny.express import input, ui, render

# Set page title
ui.page_opts(title="Update Checkbox Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        # Controls for updating the checkbox
        ui.input_text(
            "new_label", "Enter new label for checkbox", value="Updated checkbox label"
        )
        ui.input_checkbox("new_value", "Set checkbox value to", value=True)
        ui.input_action_button("update_btn", "Update Checkbox", class_="btn-primary")

    # Main panel content
    ui.h3("Checkbox Update Demo")

    # The checkbox we'll be updating
    ui.input_checkbox("my_checkbox", "Initial checkbox label", value=False)

    ui.hr()

    # Display current state
    @render.text
    def current_state():
        return f"Current checkbox state: {input.my_checkbox()}"


# Effect to handle the update
@reactive.effect
@reactive.event(input.update_btn)
def _():
    ui.update_checkbox(
        id="my_checkbox", label=input.new_label(), value=input.new_value()
    )
