from shiny import reactive
from shiny.express import input, ui, render

# Synthetic data for demonstration
nav_data = {
    "panel1": {"title": "Sales Data", "content": "Total sales this quarter: $500,000"},
    "panel2": {
        "title": "Marketing Insights",
        "content": "Campaign reach: 1.2 million users",
    },
    "panel3": {"title": "Customer Metrics", "content": "Customer satisfaction: 92%"},
    "panel4": {"title": "Product Performance", "content": "Top product: Smart Watch X"},
    "panel5": {"title": "Financial Overview", "content": "Profit margin: 35%"},
}

# Page options
ui.page_opts(title="Navigation Update Demo", fillable=True)

# Sidebar with controls
with ui.sidebar():
    ui.input_radio_buttons(
        "nav_controller",
        "Navigation Controller",
        choices=[
            "Select Panel",
            "Reset to First",
            "Cycle Panels",
            "Disable/Enable Panels",
        ],
    )

# Navigation set with multiple panels
with ui.navset_card_pill(id="demo_navset"):
    for key, panel_info in nav_data.items():
        with ui.nav_panel(panel_info["title"], value=key):
            ui.markdown(f"## {panel_info['title']}")
            ui.p(panel_info["content"])


# Reactive effects to demonstrate update_navs functionality
@reactive.effect
@reactive.event(input.nav_controller)
def update_navigation():
    controller = input.nav_controller()

    if controller == "Select Panel":
        # Select a specific panel
        ui.update_navs("demo_navset", selected="panel3")

    elif controller == "Reset to First":
        # Reset to the first panel
        ui.update_navs("demo_navset", selected="panel1")

    elif controller == "Cycle Panels":
        # Cycle through panels (this is a simplistic demonstration)
        current_panels = list(nav_data.keys())
        current_index = current_panels.index(input.demo_navset())
        next_index = (current_index + 1) % len(current_panels)
        next_panel = current_panels[next_index]
        ui.update_navs("demo_navset", selected=next_panel)

    elif controller == "Disable/Enable Panels":
        # This demonstrates how you might dynamically manage panel visibility
        ui.update_navs("demo_navset", selected="panel1")


# Display the current selected panel for demonstration
@render.text
def show_current_panel():
    return f"Current Panel: {input.demo_navset()}"
