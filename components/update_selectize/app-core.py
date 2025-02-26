from shiny import App, reactive, render, ui

# Sample data for choices
states = {
    "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
    "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
}

app_ui = ui.page_fillable(
    ui.card(
        ui.card_header("Selectize Input Demo"),
        # Initial selectize input
        ui.input_selectize(
            id="state",
            label="Choose a state:",
            choices=states,
            selected="NY",
            multiple=True,
        ),
        # Control buttons for demonstrating different update scenarios
        ui.layout_column_wrap(
            ui.input_action_button(id="update_label", label="Update Label"),
            ui.input_action_button(id="update_choices", label="Update Choices"),
            ui.input_action_button(id="update_selected", label="Update Selected"),
            ui.input_action_button(id="update_options", label="Update Options"),
            ui.input_action_button(id="reset", label="Reset"),
            width=1 / 2,
        ),
        # Display current selection
        ui.output_text("current_selection"),
    )
)


def server(input, output, session):
    # Render current selection
    @output
    @render.text
    def current_selection():
        return f"Current selection: {input.state()}"

    # Effect to update label
    @reactive.effect
    @reactive.event(input.update_label)
    def update_label():
        ui.update_selectize(id="state", label="Updated State Selection Label:")

    # Effect to update choices
    @reactive.effect
    @reactive.event(input.update_choices)
    def update_choices():
        new_choices = {"Mountain": {"CO": "Colorado", "MT": "Montana", "WY": "Wyoming"}}
        ui.update_selectize(id="state", choices=new_choices, selected="CO")

    # Effect to update selected
    @reactive.effect
    @reactive.event(input.update_selected)
    def update_selected():
        ui.update_selectize(id="state", selected=["NY", "CA"])

    # Effect to update options
    @reactive.effect
    @reactive.event(input.update_options)
    def update_options():
        ui.update_selectize(
            id="state",
            options={
                "placeholder": "Select your states...",
                "maxItems": 3,
                "plugins": ["remove_button"],
            },
        )

    # Effect to reset to initial state
    @reactive.effect
    @reactive.event(input.reset)
    def reset():
        ui.update_selectize(
            id="state",
            label="Choose a state:",
            choices=states,
            selected="NY",
            options=None,
        )


app = App(app_ui, server)
