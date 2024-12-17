from shiny import reactive
from shiny.express import input, ui, render

# Create synthetic data for demonstration
states = {
    "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
    "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
    "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
}

# Page title and description
ui.page_opts(title="Selectize Update Demo")

# Initial selectize input with predefined choices
ui.input_selectize("initial_states", "Initial States Selection", states, multiple=True)

# Button to trigger update
ui.input_action_button("update_btn", "Update Selectize")


# Render the current selection
@reactive.effect
def _():
    # When the button is clicked, update the selectize input
    input.update_btn()

    ui.update_selectize(
        "initial_states",
        # Dynamically generate choices based on some logic
        choices={"New Regions": {"TX": "Texas", "FL": "Florida", "CO": "Colorado"}},
        # Select a subset of the new choices
        selected=["TX", "FL"],
        # Update the label to show something changed
        label=f"Updated States (Clicked {input.update_btn()} times)",
    )


# Render the current selection
@render.text
def show_selection():
    return f"Current Selection: {input.initial_states()}"
