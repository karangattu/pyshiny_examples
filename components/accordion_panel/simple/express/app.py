from shiny import reactive
from shiny.express import input, render, ui

# Sample data for demonstration
sales_data = {
    "Q1": {"Revenue": "$150,000", "Units": 1200, "Growth": "+15%"},
    "Q2": {"Revenue": "$180,000", "Units": 1450, "Growth": "+20%"},
    "Q3": {"Revenue": "$210,000", "Units": 1680, "Growth": "+17%"},
    "Q4": {"Revenue": "$250,000", "Units": 2000, "Growth": "+19%"},
}

ui.page_opts(title="Sales Performance Dashboard", fillable=True)

# Create accordion with multiple panels
with ui.accordion(id="sales_accordion", open=True):
    # Q1 Panel
    with ui.accordion_panel("Q1 2024 Performance"):
        ui.markdown(
            f"""
        ### Q1 2024 Results
        * Revenue: {sales_data['Q1']['Revenue']}
        * Units Sold: {sales_data['Q1']['Units']}
        * Growth Rate: {sales_data['Q1']['Growth']}
        """
        )

    # Q2 Panel
    with ui.accordion_panel("Q2 2024 Performance"):
        ui.markdown(
            f"""
        ### Q2 2024 Results
        * Revenue: {sales_data['Q2']['Revenue']}
        * Units Sold: {sales_data['Q2']['Units']}
        * Growth Rate: {sales_data['Q2']['Growth']}
        """
        )

    # Q3 Panel
    with ui.accordion_panel("Q3 2024 Performance"):
        ui.markdown(
            f"""
        ### Q3 2024 Results
        * Revenue: {sales_data['Q3']['Revenue']}
        * Units Sold: {sales_data['Q3']['Units']}
        * Growth Rate: {sales_data['Q3']['Growth']}
        """
        )

    # Q4 Panel
    with ui.accordion_panel("Q4 2024 Performance"):
        ui.markdown(
            f"""
        ### Q4 2024 Results
        * Revenue: {sales_data['Q4']['Revenue']}
        * Units Sold: {sales_data['Q4']['Units']}
        * Growth Rate: {sales_data['Q4']['Growth']}
        """
        )


@render.ui
def selected_quarter():
    if input.sales_accordion():
        return ui.h4(f"Currently viewing: {input.sales_accordion()}")
    return ui.h4("Select a quarter to view details")
