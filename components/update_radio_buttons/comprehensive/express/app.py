from shiny import reactive
from shiny.express import input, render, ui

# Page options and styling
ui.page_opts(title="Radio Buttons Demo", fillable=True)

with ui.layout_columns(col_widths=[6, 6]):
    # Original radio buttons
    with ui.card(full_screen=True):
        ui.card_header("Original Radio Buttons")
        ui.input_radio_buttons(
            "radio1",
            "Select an option:",
            choices=["Option A", "Option B", "Option C"],
            selected="Option A",
            inline=False,
        )

    # Controls to update the radio buttons
    with ui.card(full_screen=True):
        ui.card_header("Control Panel")

        # Label control
        ui.input_text(
            "new_label",
            "New Label:",
            value="Select an option:",
            placeholder="Enter new label",
        )

        # Choices control
        ui.input_text_area(
            "new_choices",
            "New Choices (one per line):",
            value="Choice 1\nChoice 2\nChoice 3",
            height="100px",
        )

        # Selected value control
        ui.input_text("new_selected", "New Selected Value:", value="Choice 1")

        # Inline display control
        ui.input_checkbox("new_inline", "Display inline", value=False)

        ui.input_action_button(
            "update_btn", "Update Radio Buttons", class_="btn-primary"
        )

# Display current state
with ui.card():
    ui.card_header("Current Selection")

    @render.text
    def current_selection():
        return f"Currently selected: {input.radio1()}"


# Update radio buttons when the update button is clicked
@reactive.effect
@reactive.event(input.update_btn)
def _():
    # Convert text area input to list of choices
    choices = [x.strip() for x in input.new_choices().split("\n") if x.strip()]

    # Update the radio buttons with all available parameters
    ui.update_radio_buttons(
        id="radio1",
        label=input.new_label(),
        choices=choices,
        selected=input.new_selected(),
        inline=input.new_inline(),
    )

    # Show a notification
    ui.notification_show("Radio buttons updated!", type="message", duration=3)
