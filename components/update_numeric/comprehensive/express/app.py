from shiny import reactive
from shiny.express import input, ui, render

# Page title and layout options
ui.page_opts(title="update_numeric Demo", fillable=True)

# Main layout with sidebar
with ui.layout_sidebar():
    with ui.sidebar():
        ui.h4("Control Panel")

        # Input to control label
        ui.input_text("new_label", "New Label", value="Updated Number")

        # Input to control value
        ui.input_slider("new_value", "New Value", min=0, max=100, value=50)

        # Inputs to control min/max
        ui.input_slider("new_min", "New Minimum", min=-100, max=0, value=-50)
        ui.input_slider("new_max", "New Maximum", min=0, max=200, value=100)

        # Input to control step
        ui.input_slider("new_step", "New Step Size", min=0.1, max=10, value=1, step=0.1)

        # Button to trigger update
        ui.input_action_button("update", "Update Numeric Input", class_="btn-primary")

        # Button to reset
        ui.input_action_button("reset", "Reset to Default", class_="btn-secondary")

    # Main panel
    ui.h3("Numeric Input Demo")

    # The numeric input we'll be updating
    ui.input_numeric(
        "target_numeric", "Target Numeric Input", value=25, min=0, max=100, step=1
    )

    # Display current settings
    with ui.card():
        ui.card_header("Current Settings")

        @render.ui
        def show_settings():
            return ui.tags.div(
                ui.tags.p(f"Value: {input.target_numeric()}"),
                ui.tags.p(f"Min: {input.new_min()}"),
                ui.tags.p(f"Max: {input.new_max()}"),
                ui.tags.p(f"Step: {input.new_step()}"),
            )


# Effect to handle the update button
@reactive.effect
@reactive.event(input.update)
def _():
    ui.update_numeric(
        "target_numeric",
        label=input.new_label(),
        value=input.new_value(),
        min=input.new_min(),
        max=input.new_max(),
        step=input.new_step(),
    )
    ui.notification_show("Numeric input updated!", type="message")


# Effect to handle the reset button
@reactive.effect
@reactive.event(input.reset)
def _():
    ui.update_numeric(
        "target_numeric", label="Target Numeric Input", value=25, min=0, max=100, step=1
    )
    ui.notification_show("Numeric input reset to default!", type="warning")
