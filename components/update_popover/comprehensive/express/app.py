from shiny import reactive
from shiny.express import input, ui, render

# Synthetic data for demonstration
kpi_data = {
    "Sales": {
        "value": "$1.2M",
        "trend": "↑ 15%",
        "description": "Total sales for Q2 2024",
    },
    "Customers": {
        "value": "5,342",
        "trend": "↑ 22%",
        "description": "New customers acquired this quarter",
    },
    "Revenue": {
        "value": "$850K",
        "trend": "↓ 5%",
        "description": "Net revenue after expenses",
    },
}

# Add Font Awesome CSS for icons
ui.page_opts(title="Popover Update Demo")
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">'
    )
)

# Main layout with sidebar
with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_select(
            "kpi_select",
            "Select KPI",
            list(kpi_data.keys()),
            selected="Sales",  # Add a default selection
        )

        ui.input_radio_buttons(
            "popover_placement",
            "Popover Placement",
            ["auto", "top", "right", "bottom", "left"],
            selected="auto",  # Add a default selection
        )

        ui.input_checkbox_group(
            "popover_options",
            "Popover Options",
            ["Show Popover", "Custom Content", "Change Title"],
        )

    # KPI Display with Popover
    with ui.card():
        with ui.popover(
            id="kpi_popover",
            placement="auto",  # Use a fixed placement initially
            options={"trigger": "click"},
        ):
            ui.tags.span(
                ui.tags.i(class_="fa-solid fa-circle-info me-2"), f"KPI Details"
            )

            "Default popover content"

    # KPI Value Display
    @render.text
    def kpi_value():
        kpi = input.kpi_select()
        return f"{kpi}: {kpi_data[kpi]['value']} {kpi_data[kpi]['trend']}"


# Reactive effect to update popover
@reactive.effect
def _():
    kpi = input.kpi_select()
    placement = input.popover_placement()
    options = input.popover_options()

    # Update popover based on selected options
    if "Show Popover" in options:
        ui.update_popover(
            "kpi_popover",
            # Demonstrate updating content
            f"Detailed Information for {kpi}: {kpi_data[kpi]['description']}",
            # Demonstrate changing title
            title="KPI Insights" if "Change Title" in options else None,
            # Demonstrate showing/hiding
            show=True,
            # Demonstrate custom placement
            placement=placement,
        )
    else:
        # Hide popover if not selected
        ui.update_popover("kpi_popover", show=False)
