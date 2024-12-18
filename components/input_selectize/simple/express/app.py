from shiny import reactive
from shiny.express import input, render, ui

# Generate synthetic data
states = {
    "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
    "West Coast": {"CA": "California", "OR": "Oregon", "WA": "Washington"},
    "Midwest": {"IL": "Illinois", "MI": "Michigan", "OH": "Ohio"},
}

# Page options
ui.page_opts(title="Selectize Input Demonstration")

# Sidebar with selectize inputs
with ui.sidebar():
    # Basic selectize input with optgroups
    ui.input_selectize("state", "Choose a state:", states, multiple=False)

    # Selectize input with multiple selections allowed
    ui.input_selectize("multi_state", "Choose multiple states:", states, multiple=True)

    # Selectize input with custom options
    ui.input_selectize(
        "custom_state",
        "Selectize with custom options:",
        states,
        multiple=True,
        options={
            "placeholder": "Select states...",
            "maxItems": 3,  # Limit to 3 selections
        },
    )

# Main content area to display selections
with ui.layout_columns():
    # Display single state selection
    @render.text
    def single_state_output():
        return f"You selected: {input.state() or 'No state selected'}"

    # Display multiple state selections
    @render.text
    def multi_state_output():
        selected = input.multi_state()
        return f"You selected: {selected or 'No states selected'}"

    # Display custom selectize selections
    @render.text
    def custom_state_output():
        selected = input.custom_state()
        return f"You selected: {selected or 'No states selected'}"
