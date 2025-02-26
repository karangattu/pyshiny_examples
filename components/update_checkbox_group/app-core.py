from shiny import App, reactive, render, ui

# Initial choices
CHOICES = ["Item A", "Item B", "Item C", "Item D"]

app_ui = ui.page_fluid(
    # Create the first checkbox group that will be updated
    ui.input_checkbox_group(
        "checkbox_group",
        "Checkbox Group (will be updated)",
        choices=CHOICES,
        selected=["Item A"],
        inline=False,
    ),
    # Controls to demonstrate all update parameters
    ui.input_text("new_label", "New Label", value="Updated Label"),
    ui.input_checkbox("inline_toggle", "Toggle Inline Display", value=False),
    # Multi-select for new choices
    ui.input_selectize(
        "new_choices",
        "Select New Choices",
        choices=CHOICES,
        selected=CHOICES[:2],
        multiple=True,
    ),
    # Multi-select for new selected values
    ui.input_selectize(
        "new_selected",
        "Select New Values",
        choices=CHOICES,
        selected=["Item A"],
        multiple=True,
    ),
    # Button to trigger the update
    ui.input_action_button("update", "Update Checkbox Group"),
    # Display current state
    ui.output_text("current_value"),
)


def server(input, output, session):
    @reactive.effect
    @reactive.event(input.update)
    def _():
        # Update the checkbox group with all possible parameters
        ui.update_checkbox_group(
            id="checkbox_group",
            label=input.new_label(),
            choices=input.new_choices(),
            selected=input.new_selected(),
            inline=input.inline_toggle(),
        )

    @output
    @render.text
    def current_value():
        return f"Current selection: {input.checkbox_group()}"


app = App(app_ui, server)
