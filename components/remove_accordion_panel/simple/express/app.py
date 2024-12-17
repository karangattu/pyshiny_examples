from shiny import reactive
from shiny.express import input, ui

# Synthetic data for demonstration
panel_data = {
    "A": "Content for Panel A - Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "B": "Content for Panel B - Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "C": "Content for Panel C - Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.",
    "D": "Content for Panel D - Excepteur sint occaecat cupidatat non proident, sunt in culpa qui.",
    "E": "Content for Panel E - Duis aute irure dolor in reprehenderit in voluptate velit esse.",
}

# Page title and options
ui.page_opts(title="Accordion Panel Removal Demo", fillable=True)

# Create an accordion with multiple panels
with ui.accordion(id="demo_accordion", multiple=True):
    for letter, content in panel_data.items():
        with ui.accordion_panel(f"Section {letter}", value=f"sec_{letter}"):
            content

# Add a button to remove panels
ui.input_action_button("remove_panel", "Remove Last Panel")


# Reactive effect to handle panel removal
@reactive.effect
@reactive.event(input.remove_panel)
def _():
    # Get the last panel's value
    if len(panel_data) > 0:
        last_letter = list(panel_data.keys())[-1]
        ui.remove_accordion_panel("demo_accordion", f"sec_{last_letter}")

        # Remove the last item from the dictionary
        del panel_data[last_letter]

        # Update button label based on remaining panels
        if len(panel_data) == 0:
            ui.update_action_button(
                "remove_panel", label="No Panels Left", disabled=True
            )
        else:
            ui.update_action_button(
                "remove_panel", label=f"Remove Section {list(panel_data.keys())[-1]}"
            )
    else:
        ui.notification_show("No more panels to remove!", type="warning")
