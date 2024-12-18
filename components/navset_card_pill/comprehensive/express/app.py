import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
sales_data = pd.DataFrame(
    {
        "Region": ["North", "South", "East", "West", "Central"] * 10,
        "Product": np.random.choice(
            ["Electronics", "Clothing", "Furniture", "Groceries"], 50
        ),
        "Sales": np.random.randint(1000, 10000, 50),
        "Profit": np.random.randint(100, 1000, 50),
    }
)

# Page options
ui.page_opts(title="NavSet Card Pill Showcase", fillable=True)

# Add Font Awesome CSS
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# NavSet Card Pill with multiple configuration options
with ui.navset_card_pill(
    id="main_navset",  # Demonstrates id parameter
    selected="Sales Overview",  # Demonstrates selected parameter
):
    # Sidebar for additional interactions
    with ui.sidebar(title="Navigation Controls"):
        ui.input_dark_mode(id="dark_mode")
        ui.input_radio_buttons(
            "chart_type", "Chart Type", choices=["Bar", "Pie", "Line"], selected="Bar"
        )
        ui.input_checkbox_group(
            "regions",
            "Select Regions",
            choices=list(sales_data["Region"].unique()),  # Convert to list
            selected=list(sales_data["Region"].unique()),  # Convert to list
        )

    # Nav Panels with various content and icons
    with ui.nav_panel(
        "Sales Overview", icon=ui.tags.i(class_="fa-solid fa-chart-simple")
    ):

        @render.plot
        def sales_chart():
            filtered_data = sales_data[sales_data["Region"].isin(input.regions())]
            plt.figure(figsize=(10, 6))

            if input.chart_type() == "Bar":
                filtered_data.groupby("Region")["Sales"].sum().plot(kind="bar")
                plt.title("Total Sales by Region")
            elif input.chart_type() == "Pie":
                filtered_data.groupby("Region")["Sales"].sum().plot(
                    kind="pie", autopct="%1.1f%%"
                )
                plt.title("Sales Distribution by Region")
            else:
                filtered_data.groupby("Region")["Sales"].sum().plot(
                    kind="line", marker="o"
                )
                plt.title("Sales Trend by Region")

            plt.tight_layout()
            return plt.gcf()

    with ui.nav_panel(
        "Profit Analysis", icon=ui.tags.i(class_="fa-solid fa-dollar-sign")
    ):

        @render.data_frame
        def profit_table():
            filtered_data = sales_data[sales_data["Region"].isin(input.regions())]
            return (
                filtered_data.groupby("Region")["Profit"]
                .agg(["sum", "mean", "max"])
                .reset_index()
            )

    with ui.nav_panel("Product Breakdown", icon=ui.tags.i(class_="fa-solid fa-box")):

        @render.plot
        def product_chart():
            filtered_data = sales_data[sales_data["Region"].isin(input.regions())]
            plt.figure(figsize=(10, 6))
            filtered_data.groupby("Product")["Sales"].sum().plot(kind="bar")
            plt.title("Total Sales by Product")
            plt.tight_layout()
            return plt.gcf()

    # Demonstrates adding a nav menu with additional options
    with ui.nav_menu("More Options", icon=ui.tags.i(class_="fa-solid fa-ellipsis")):
        with ui.nav_panel("Data Summary"):

            @render.text
            def data_summary():
                filtered_data = sales_data[sales_data["Region"].isin(input.regions())]
                return f"""
                Total Regions Selected: {len(input.regions())}
                Total Sales: ${filtered_data['Sales'].sum():,}
                Total Profit: ${filtered_data['Profit'].sum():,}
                Average Sales: ${filtered_data['Sales'].mean():,.2f}
                """

        with ui.nav_panel("About"):
            ui.markdown(
                """
            ### Sales Dashboard
            
            This interactive dashboard demonstrates the capabilities of 
            `navset_card_pill` in Shiny for Python.
            
            - Explore sales data across different regions
            - Switch between various chart types
            - Filter data dynamically
            """
            )

# Add a section to show the currently selected nav item
ui.h5("Currently Selected:")


@render.text
def selected_nav():
    return f"Selected Nav: {input.main_navset()}"
