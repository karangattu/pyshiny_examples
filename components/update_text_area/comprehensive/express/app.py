from shiny import reactive
from shiny.express import input, render, ui

# Page options
ui.page_opts(title="Text Area Update Demo", fillable=True)

# Layout with sidebar
with ui.layout_sidebar():
    with ui.sidebar():
        # Controls for updating text area
        ui.input_text("new_label", "New Label", value="Updated Text Area Label")
        ui.input_text_area(
            "new_value",
            "New Value",
            value="This is some new content for the text area.",
        )
        ui.input_text(
            "new_placeholder", "New Placeholder", value="Enter your text here..."
        )
        ui.input_action_button("update", "Update Text Area", class_="btn-primary")

        ui.hr()
        ui.markdown(
            """
        ### Instructions
        1. Modify any of the inputs above
        2. Click 'Update Text Area' to see changes
        3. Watch how the text area updates dynamically
        """
        )

    # Main content area
    with ui.card():
        ui.card_header("Text Area Demo")

        # The text area we'll be updating
        ui.input_text_area(
            "target_textarea",
            "Original Text Area Label",
            value="This is the original content.\nTry updating it using the controls in the sidebar!",
            placeholder="Original placeholder text",
            height="200px",
        )

        # Display current text area value
        @render.text
        def current_value():
            return f"Current Value: {input.target_textarea()}"


# Effect to handle updates
@reactive.effect
@reactive.event(input.update)
def _():
    ui.update_text_area(
        id="target_textarea",
        label=input.new_label(),
        value=input.new_value(),
        placeholder=input.new_placeholder(),
    )
    # Show notification when updated
    ui.notification_show("Text Area Updated!", type="message", duration=3)


# Add some explanatory text
with ui.card():
    ui.card_header("About this Demo")
    ui.markdown(
        """
    This demo showcases all parameters of `update_text_area`:
    
    * **id**: The ID of the text area to update ("target_textarea")
    * **label**: The new label text
    * **value**: The new content for the text area
    * **placeholder**: The new placeholder text
    * **session**: (handled automatically in express mode)
    
    Try experimenting with different values in the sidebar controls!
    """
    )
