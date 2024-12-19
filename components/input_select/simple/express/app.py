from shiny import reactive
from shiny.express import input, ui, render

# Generate some sample data as a dictionary
states = {
    "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
    "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
    "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
}

# Set page title
ui.page_opts(title="State Selector Demo")

# Create select input grouped by region
ui.input_select("state", "Choose a state:", states, selected="NY")


# Show the selected value
@render.text
def selected_state():
    return f"You selected: {input.state()}"
