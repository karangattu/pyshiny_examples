from shiny import reactive
from shiny.express import input, render, ui

# Sample data for selectize inputs
states = {
    "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
    "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
    "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
}

# Set page options
ui.page_opts(title="Selectize Update Demo", fillable=True)

# Create a sidebar with controls
with ui.sidebar():
    ui.h4("Control Panel")
    ui.input_action_button("update_label", "Update Label")
    ui.input_action_button("update_choices", "Update Choices")
    ui.input_action_button("update_selected", "Update Selected")
    ui.input_action_button("update_options", "Update Options")
    ui.input_action_button("reset", "Reset All")

# Main content
with ui.layout_column_wrap(width=1 / 2):
    # First selectize input - single selection
    with ui.card():
        ui.card_header("Single Selection Selectize")
        ui.input_selectize(
            "single_select", "Select a state:", choices=states, selected="NY"
        )

    # Second selectize input - multiple selection
    with ui.card():
        ui.card_header("Multiple Selection Selectize")
        ui.input_selectize(
            "multi_select",
            "Select multiple states:",
            choices=states,
            multiple=True,
            selected=["NY", "CA"],
        )

# Display current values
with ui.card():
    ui.card_header("Current Selections")

    @render.text
    def show_selections():
        return (
            f"Single Select: {input.single_select()}\n"
            f"Multi Select: {input.multi_select()}"
        )


# Update functions for different parameters
@reactive.effect
@reactive.event(input.update_label)
def _():
    ui.update_selectize(
        "single_select",
        label=f"Updated Label (clicked: {input.update_label()})",
    )
    ui.update_selectize(
        "multi_select",
        label=f"Updated Multi Label (clicked: {input.update_label()})",
    )


@reactive.effect
@reactive.event(input.update_choices)
def _():
    # New choices with different structure
    new_choices = {
        "Mountains": {"CO": "Colorado", "MT": "Montana", "WY": "Wyoming"},
        "Islands": {"HI": "Hawaii", "PR": "Puerto Rico"},
    }
    ui.update_selectize("single_select", choices=new_choices)
    ui.update_selectize("multi_select", choices=new_choices)


@reactive.effect
@reactive.event(input.update_selected)
def _():
    ui.update_selectize("single_select", selected="CA")
    ui.update_selectize("multi_select", selected=["WA", "OR"])


@reactive.effect
@reactive.event(input.update_options)
def _():
    # Demonstrate different selectize.js options
    options = {
        "placeholder": "Choose your states...",
        "plugins": ["remove_button"],
        "maxItems": 3,
        "closeAfterSelect": True,
    }
    ui.update_selectize("single_select", options=options)
    ui.update_selectize("multi_select", options=options)


@reactive.effect
@reactive.event(input.reset)
def _():
    # Reset everything to initial state
    ui.update_selectize(
        "single_select",
        label="Select a state:",
        choices=states,
        selected="NY",
        options=None,
    )
    ui.update_selectize(
        "multi_select",
        label="Select multiple states:",
        choices=states,
        selected=["NY", "CA"],
        options=None,
    )
