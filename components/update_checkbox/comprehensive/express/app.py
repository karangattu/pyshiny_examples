from shiny import reactive
from shiny.express import input, ui, render

# Page title
ui.page_opts(title="Update Checkbox Demo", fillable=True)

with ui.layout_columns(col_widths=[6, 6]):
    # Column 1: Controls to update checkbox
    with ui.card():
        ui.card_header("Control Panel")

        # Input to update label
        ui.input_text(
            "new_label",
            "New Label for Checkbox:",
            value="Default Checkbox Label",
            placeholder="Enter new label",
        )

        # Input to update value
        ui.input_radio_buttons(
            "new_value",
            "New Value for Checkbox:",
            choices=["True", "False"],
            selected="False",
        )

        # Button to trigger update
        ui.input_action_button("update_btn", "Update Checkbox", class_="btn-primary")

    # Column 2: Target checkbox and status
    with ui.card():
        ui.card_header("Target Checkbox")

        # The checkbox we'll update
        ui.input_checkbox("target_checkbox", "Original Label", value=False)

        # Display current checkbox state
        @render.text
        def checkbox_status():
            return f"""
            Current Status:
            - Value: {str(input.target_checkbox())}
            - Label: {input.target_checkbox.label}
            """


# Effect to handle checkbox updates
@reactive.effect
@reactive.event(input.update_btn)
def _():
    # Convert string "True"/"False" to boolean
    new_value = input.new_value() == "True"

    # Update the checkbox with new values
    ui.update_checkbox(id="target_checkbox", label=input.new_label(), value=new_value)

    # Show notification of update
    ui.notification_show(
        f"Checkbox updated with label: '{input.new_label()}' and value: {new_value}",
        duration=3,
    )


# Add some helpful instructions
with ui.card():
    ui.card_header("Instructions")
    ui.markdown(
        """
    This demo shows all parameters of the `update_checkbox` function:
    
    * **id**: The ID of the checkbox to update (fixed as "target_checkbox")
    * **label**: The new label text for the checkbox
    * **value**: The new boolean value (True/False) for the checkbox
    
    Try changing the values in the control panel and click 'Update Checkbox' to see the changes.
    """
    )
