from shiny import reactive
from shiny.express import input, render, ui

# Sample data
states = {
    "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
    "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
    "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
}

ui.page_opts(title="Selectize Example")

with ui.sidebar():
    ui.input_action_button("update", "Update Choices")
    ui.input_selectize("state", "Choose states:", states, multiple=True)


@render.text
def selected_states():
    return f"You selected: {input.state()}"


@reactive.effect
@reactive.event(input.update)
def _():
    # Update with new choices and select some values
    ui.update_selectize(
        "state",
        label="Updated state choices:",
        choices={"Selected": {"CA": "California", "NY": "New York"}},
        selected=["CA"],
    )
