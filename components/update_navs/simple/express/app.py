from shiny import reactive
from shiny.express import input, ui, render

# Synthetic data
kpi_data = {
    "Sales": {"current": 1250000, "previous": 1000000, "change": "+25%"},
    "Customers": {"current": 5200, "previous": 4800, "change": "+8.3%"},
    "Revenue": {"current": 2500000, "previous": 2200000, "change": "+13.6%"},
}

# Page configuration
ui.page_opts(title="KPI Dashboard", fillable=True)

# Navigation setup with dynamic update
with ui.navset_card_pill(id="kpi_nav"):
    with ui.nav_panel("Sales", value="sales"):
        ui.h3("Sales KPI")
        ui.tags.p(f"Current Sales: ${kpi_data['Sales']['current']:,}")
        ui.tags.p(f"Previous Period: ${kpi_data['Sales']['previous']:,}")
        ui.tags.p(f"Change: {kpi_data['Sales']['change']}")

    with ui.nav_panel("Customers", value="customers"):
        ui.h3("Customer KPI")
        ui.tags.p(f"Current Customers: {kpi_data['Customers']['current']:,}")
        ui.tags.p(f"Previous Period: {kpi_data['Customers']['previous']:,}")
        ui.tags.p(f"Change: {kpi_data['Customers']['change']}")

    with ui.nav_panel("Revenue", value="revenue"):
        ui.h3("Revenue KPI")
        ui.tags.p(f"Current Revenue: ${kpi_data['Revenue']['current']:,}")
        ui.tags.p(f"Previous Period: ${kpi_data['Revenue']['previous']:,}")
        ui.tags.p(f"Change: {kpi_data['Revenue']['change']}")

# Sidebar for navigation control
with ui.sidebar():
    ui.input_radio_buttons(
        "kpi_selector", "Select KPI to View", ["Sales", "Customers", "Revenue"]
    )


# Reactive effect to update navigation based on radio button selection
@reactive.effect
def _():
    kpi_value = input.kpi_selector().lower()
    ui.update_navs("kpi_nav", selected=kpi_value)


# Optional: Display current selected nav for demonstration
@render.text
def nav_state():
    return f"Current selected nav: {input.kpi_nav()}"
