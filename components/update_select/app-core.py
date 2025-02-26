from shiny import App, reactive, render, ui

# Initial data setup
states = {
    "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
    "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
    "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
}

# Define UI
app_ui = ui.page_fillable(
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_action_button("update", "Update Select Input", class_="mb-3"),
            # The select input we'll be updating
            ui.input_select("state", "Choose a state:", choices=states, selected="NY"),
        ),
        ui.card(
            ui.card_header("Current Selection"),
            ui.output_text("current_selection"),
            ui.output_text("update_count"),
        ),
    )
)


# Define server
def server(input, output, session):
    @output
    @render.text
    def current_selection():
        return f"Current selection: {input.state()}"

    @output
    @render.text
    def update_count():
        return f"Number of updates: {input.update()}"

    # Effect to demonstrate update_select
    @reactive.effect
    @reactive.event(input.update)
    def _():
        # Update the select input with new choices and selection
        ui.update_select(
            id="state",
            label=f"Updated State Selection (Click #{input.update()})",
            choices={
                "Southern States": {"FL": "Florida", "TX": "Texas", "AZ": "Arizona"}
            },
            selected="TX",
        )


# Create and return app
app = App(app_ui, server)
