from shiny import reactive
from shiny.express import input, render, ui

# Sample data for demonstration
data = {
    "panel1": "Content for Panel 1",
    "panel2": "Content for Panel 2",
    "panel3": "Content for Panel 3",
    "panel4": "Content for Panel 4",
}

ui.page_opts(title="Navigation Update Demo", fillable=True)

# Controls for updating navigation
with ui.sidebar():
    ui.h4("Navigation Controls")
    ui.input_select(
        "nav_selection", "Select Panel", choices=list(data.keys()), selected="panel1"
    )
    ui.input_action_button("update_nav", "Update Navigation")
    ui.hr()
    ui.markdown(
        """
    ### About this demo
    This app demonstrates all parameters of `update_navs`:
    - id: The ID of the nav container to update
    - selected: Which panel to show
    - session: The current session (handled automatically)
    """
    )

# Main content with different types of navigation layouts
with ui.navset_card_tab(id="main_nav"):
    with ui.nav_panel("Panel 1", value="panel1"):
        ui.h3("Panel 1")
        ui.markdown(data["panel1"])

    with ui.nav_panel("Panel 2", value="panel2"):
        ui.h3("Panel 2")
        ui.markdown(data["panel2"])

    with ui.nav_panel("Panel 3", value="panel3"):
        ui.h3("Panel 3")
        ui.markdown(data["panel3"])

    with ui.nav_panel("Panel 4", value="panel4"):
        ui.h3("Panel 4")
        ui.markdown(data["panel4"])


# Display current navigation state
@render.text
def current_nav():
    return f"Current navigation state: {input.main_nav()}"


# Handle navigation updates
@reactive.effect
@reactive.event(input.update_nav)
def _():
    ui.update_navs(id="main_nav", selected=input.nav_selection())
    ui.notification_show(f"Navigation updated to {input.nav_selection()}", duration=2)
