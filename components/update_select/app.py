from shiny import reactive
from shiny.express import input, ui, render

# Initial data setup
states = {
    "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
    "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
    "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
}

# Page setup
ui.page_opts(title="Update Select Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_action_button("update", "Update Select Input", class_="mb-3")

        # The select input we'll be updating
        ui.input_select("state", "Choose a state:", choices=states, selected="NY")

    with ui.card():
        ui.card_header("Current Selection")

        @render.text
        def current_selection():
            return f"Current selection: {input.state()}"

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
        choices={"Southern States": {"FL": "Florida", "TX": "Texas", "AZ": "Arizona"}},
        selected="TX",
    )
