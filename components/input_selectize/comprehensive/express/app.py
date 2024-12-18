from shiny import reactive
from shiny.express import input, ui, render

# Sample data for different examples
states = {
    "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
    "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
    "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
}

# Page options
ui.page_opts(title="Selectize Input Demo", fillable=True)

with ui.layout_columns(col_widths=[6, 6]):
    # Basic single selection
    ui.input_selectize(
        "select1",
        "Basic Single Selection",
        choices=list(states["East Coast"].values()),
        selected="New York",
    )

    # Multiple selection
    ui.input_selectize(
        "select2",
        "Multiple Selection",
        choices=list(states["West Coast"].values()),
        multiple=True,
        selected=["Washington", "Oregon"],
    )

    # Grouped options with optgroup
    ui.input_selectize("select3", "Grouped Options", choices=states, selected="NY")

    # With placeholder and custom options
    ui.input_selectize(
        "select4",
        "With Placeholder and Custom Options",
        choices=list(states["Midwest"].values()),
        options={
            "placeholder": "Choose a state...",
            "plugins": ["clear_button"],
        },
    )

    # Multiple selection with remove button
    ui.input_selectize(
        "select5",
        "Multiple Selection with Remove Button",
        choices=list(states["East Coast"].values()),
        multiple=True,
        remove_button=True,
    )

    # Custom rendering of options
    ui.input_selectize(
        "select6",
        "Custom Rendered Options",
        choices={
            "NY": "New York (Population: 19.8M)",
            "CA": "California (Population: 39.5M)",
            "TX": "Texas (Population: 29.1M)",
        },
        options={
            "render": ui.js_eval(
                """{
                    option: function(item, escape) {
                        return '<div><strong>' + escape(item.label) + '</strong></div>';
                    }
                }"""
            )
        },
    )

# Display selected values
with ui.card():
    ui.card_header("Selected Values")

    @render.ui
    def show_selections():
        return ui.tags.div(
            ui.tags.p(f"Basic Single Selection: {input.select1()}"),
            ui.tags.p(f"Multiple Selection: {input.select2()}"),
            ui.tags.p(f"Grouped Options: {input.select3()}"),
            ui.tags.p(f"With Placeholder: {input.select4()}"),
            ui.tags.p(f"With Remove Button: {input.select5()}"),
            ui.tags.p(f"Custom Rendered: {input.select6()}"),
        )


# Add a button to demonstrate updating selectize inputs
ui.input_action_button("update_btn", "Update Selectize Inputs", class_="btn-primary")


@reactive.effect
@reactive.event(input.update_btn)
def _():
    # Update various selectize inputs to demonstrate dynamic updates
    ui.update_selectize(
        "select1", choices=list(states["Midwest"].values()), selected="Minnesota"
    )

    ui.update_selectize(
        "select2",
        choices=list(states["East Coast"].values()),
        selected=["New York", "New Jersey"],
    )

    ui.update_selectize(
        "select4",
        label="Updated Label",
        choices=list(states["West Coast"].values()),
        options={"placeholder": "Updated placeholder..."},
    )
