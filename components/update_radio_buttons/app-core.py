from shiny import App, reactive, render, ui

app_ui = ui.page_fillable(
    ui.layout_sidebar(
        ui.sidebar(
            # Initial radio buttons with basic choices
            ui.input_radio_buttons(
                "radio_group",
                "Original Radio Buttons",
                choices=["Option A", "Option B", "Option C"],
                selected="Option A",
                inline=False,
            ),
            # Button to trigger updates
            ui.input_action_button(
                "update_btn", "Update Radio Buttons", class_="btn-primary"
            ),
        ),
        # Main panel content
        ui.card(
            ui.card_header("Radio Button Selection"),
            ui.output_text("selection"),
        ),
    )
)


def server(input, output, session):
    @output
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


app = App(app_ui, server)
