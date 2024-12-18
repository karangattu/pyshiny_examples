from shiny import reactive
from shiny.express import input, ui

# Create initial accordion panels
ui.input_action_button("add_panel", "Add random panel", class_="mt-3 mb-3")

with ui.accordion(id="acc", multiple=True):
    # Initial panels with sample data
    with ui.accordion_panel("Sales Data"):
        "Revenue: $1.2M"
        "Growth: 25%"
        "Customers: 5,000"

    with ui.accordion_panel("Marketing Data"):
        "Ad Spend: $250K"
        "Leads: 2,500"
        "Conversion Rate: 12%"

    with ui.accordion_panel("Operations Data"):
        "Employees: 125"
        "Offices: 5"
        "Countries: 3"

# Counter for new panel IDs
panel_counter = reactive.value(1)


@reactive.effect
@reactive.event(input.add_panel)
def _():
    # Increment counter
    current = panel_counter.get()
    panel_counter.set(current + 1)

    # Create new panel with random metrics
    new_panel = ui.accordion_panel(
        f"Custom Report {current}",
        value=f"panel_{current}",
        icon=None,
    )

    with new_panel:
        f"Metric A: {current * 100}"
        f"Metric B: {current * 10}%"
        f"Metric C: {current * 1000}"

    # Insert the new panel after the last panel
    ui.insert_accordion_panel("acc", new_panel)
