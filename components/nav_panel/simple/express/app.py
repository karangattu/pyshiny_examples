from shiny import reactive
from shiny.express import input, render, ui

# Synthetic data for demonstration
sales_data = {
    "North": [100, 150, 120, 200, 180],
    "South": [80, 90, 110, 130, 140],
    "East": [70, 85, 95, 105, 115],
    "West": [60, 75, 80, 90, 100],
}

regions = list(sales_data.keys())

# Page setup with navigation
ui.page_opts(title="Regional Sales Dashboard")

# Create a navbar with multiple panels
with ui.navset_card_tab(id="sales_nav"):
    # Panel for Sales Overview
    with ui.nav_panel("Overview"):
        ui.h3("Sales Overview")
        ui.markdown("Explore sales performance across different regions.")

        with ui.layout_columns():

            @render.table
            def sales_table():
                import pandas as pd

                return pd.DataFrame(sales_data)

    # Panel for Regional Breakdown
    with ui.nav_panel("Regional Details"):
        ui.h3("Regional Sales Details")

        ui.input_select("region", "Select Region", choices=regions)

        @render.plot
        def regional_plot():
            import matplotlib.pyplot as plt

            region = input.region()
            data = sales_data[region]

            plt.figure(figsize=(8, 4))
            plt.bar(range(len(data)), data)
            plt.title(f"{region} Region Sales")
            plt.xlabel("Quarter")
            plt.ylabel("Sales")
            return plt

    # Panel for Comparative Analysis
    with ui.nav_panel("Comparative Analysis"):
        ui.h3("Sales Comparison")

        @render.plot
        def comparison_plot():
            import matplotlib.pyplot as plt

            plt.figure(figsize=(10, 5))
            plt.boxplot([sales_data[region] for region in regions])
            plt.title("Sales Distribution by Region")
            plt.xlabel("Regions")
            plt.ylabel("Sales")
            plt.xticks(range(1, len(regions) + 1), regions)
            return plt

    # Panel with a dropdown menu
    with ui.nav_menu("More Information"):
        with ui.nav_panel("About"):
            ui.markdown(
                """
            ### Sales Dashboard
            
            This dashboard provides insights into regional sales performance.
            
            - **Overview**: Quick glance at sales data
            - **Regional Details**: Drill down into specific region's performance
            - **Comparative Analysis**: Compare sales across regions
            """
            )

        with ui.nav_panel("Help"):
            ui.markdown(
                """
            ### How to Use This Dashboard
            
            1. Navigate through different panels using the tabs
            2. Select a region in the "Regional Details" tab to see specific sales
            3. Use the "Comparative Analysis" to understand regional performance
            """
            )


# Optional: Display the currently selected navigation panel
@render.text
def nav_state():
    return f"Current Panel: {input.sales_nav()}"
