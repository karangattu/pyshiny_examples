from shiny import reactive
from shiny.express import input, render, ui

ui.page_opts(title="Radio Buttons Update Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        # Initial radio buttons with basic choices
        ui.input_radio_buttons(
            "radio_group",
            "Original Radio Buttons",
            choices=["Option A", "Option B", "Option C"],
            selected="Option A",
            inline=False,
        )

        # Button to trigger updates
        ui.input_action_button(
            "update_btn", "Update Radio Buttons", class_="btn-primary"
        )

    # Main panel content
    with ui.card():
        ui.card_header("Radio Button Selection")

        @render.text
        def selection():
            return f"Current selection: {input.radio_group()}"


# Effect to update radio buttons when button is clicked
@reactive.effect
@reactive.event(input.update_btn)
def _():
    ui.update_radio_buttons(
        id="radio_group",
        label="Updated Radio Buttons",
        choices=["New Option 1", "New Option 2", "New Option 3"],
        selected="New Option 2",
        inline=True,
    )
