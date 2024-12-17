import random
import pandas as pd
from shiny import reactive
from shiny.express import input, ui, render

# Create synthetic data
states = {
    "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
    "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
    "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
}

# Create a DataFrame to simulate some additional data
df = pd.DataFrame(
    {
        "state_code": list(
            sum([list(region.keys()) for region in [states[k] for k in states]], [])
        ),
        "population": [random.randint(500000, 10000000) for _ in range(9)],
        "area_sq_miles": [random.randint(5000, 300000) for _ in range(9)],
    }
)

# Page options
ui.page_opts(title="State Selection Demo", fillable=True)

# Sidebar with input controls
with ui.sidebar():
    # First select input for region
    ui.input_select(
        "region", "Choose a Region", list(states.keys()), selected="East Coast"
    )

    # Second select input for state (will be dynamically updated)
    ui.input_select("state", "Choose a State", [])

# Main content area
with ui.card():
    ui.card_header("State Details")

    @render.text
    def state_info():
        # Require both region and state to be selected
        if not input.region() or not input.state():
            return "Please select a region and state"

        # Find the selected state details
        state_code = input.state()
        state_name = states[input.region()][state_code]

        # Get population and area from DataFrame
        state_data = df[df["state_code"] == state_code].iloc[0]

        return f"""
        State: {state_name} ({state_code})
        Population: {state_data['population']:,}
        Area: {state_data['area_sq_miles']:,} sq miles
        """


# Reactive effect to update state selection based on region
@reactive.effect
def _():
    # Get the currently selected region
    region = input.region()

    # Update the state select input with states from the selected region
    ui.update_select(
        "state",
        choices=list(states[region].keys()),
        selected=list(states[region].keys())[0],  # Default to first state in region
    )
