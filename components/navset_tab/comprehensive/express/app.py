from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
sales_data = pd.DataFrame(
    {
        "Region": ["North", "South", "East", "West", "Central"] * 4,
        "Year": [
            2020,
            2020,
            2020,
            2020,
            2020,
            2021,
            2021,
            2021,
            2021,
            2021,
            2022,
            2022,
            2022,
            2022,
            2022,
            2023,
            2023,
            2023,
            2023,
            2023,
        ],
        "Sales": np.random.randint(100, 1000, 20),
        "Profit": np.random.randint(10, 200, 20),
    }
)

# Set page options
ui.page_opts(title="NavSet Tab Demonstration", fillable=True)

# Create a navset_tab with various parameters
with ui.navset_tab(
    id="main_navset",  # Provides an input value to track selected tab
    selected="Sales Overview",  # Set default selected tab
    header=ui.tags.h3("Business Performance Dashboard"),  # Optional header
    footer=ui.tags.p("Data is simulated for demonstration purposes"),  # Optional footer
):
    # First Nav Panel
    with ui.nav_panel("Sales Overview"):
        with ui.layout_columns():

            @render.plot
            def sales_plot():
                plt.figure(figsize=(10, 6))
                sales_by_region = sales_data.groupby("Region")["Sales"].sum()
                sales_by_region.plot(kind="bar")
                plt.title("Total Sales by Region")
                plt.xlabel("Region")
                plt.ylabel("Total Sales")
                plt.tight_layout()
                return plt.gcf()

            @render.table
            def sales_table():
                return (
                    sales_data.groupby("Region")["Sales"].agg(["sum", "mean"]).round(2)
                )

    # Second Nav Panel
    with ui.nav_panel("Profit Analysis"):
        with ui.layout_columns():

            @render.plot
            def profit_plot():
                plt.figure(figsize=(10, 6))
                profit_by_year = sales_data.groupby("Year")["Profit"].sum()
                profit_by_year.plot(kind="line", marker="o")
                plt.title("Profit Trend Over Years")
                plt.xlabel("Year")
                plt.ylabel("Total Profit")
                plt.tight_layout()
                return plt.gcf()

            @render.table
            def profit_table():
                return (
                    sales_data.groupby("Year")["Profit"].agg(["sum", "mean"]).round(2)
                )

    # Third Nav Panel with a menu
    with ui.nav_menu("More Insights"):
        with ui.nav_panel("Regional Breakdown"):

            @render.data_frame
            def regional_details():
                return (
                    sales_data.groupby(["Region", "Year"])
                    .agg({"Sales": "sum", "Profit": "sum"})
                    .reset_index()
                )

        with ui.nav_panel("Yearly Comparison"):

            @render.data_frame
            def yearly_details():
                return sales_data.groupby("Year").agg(
                    {"Sales": ["sum", "mean"], "Profit": ["sum", "mean"]}
                )


# Add a section to show the currently selected tab
ui.h4("Current Selected Tab:")


@render.text
def selected_tab():
    return f"Selected Tab: {input.main_navset()}"
