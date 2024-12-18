import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
sales_data = pd.DataFrame(
    {
        "Region": ["North", "South", "East", "West"],
        "Q1 Sales": np.random.randint(100, 500, 4),
        "Q2 Sales": np.random.randint(100, 500, 4),
        "Q3 Sales": np.random.randint(100, 500, 4),
        "Q4 Sales": np.random.randint(100, 500, 4),
    }
)

# Set page options
ui.page_opts(title="Sales Dashboard", fillable=True)

# Create navigation set with pills
with ui.navset_pill(id="sales_nav"):
    with ui.nav_panel("Sales Overview"):
        ui.h3("Quarterly Sales Overview")

        @render.table
        def sales_table():
            return sales_data

    with ui.nav_panel("Sales by Region"):
        ui.input_radio_buttons(
            "region", "Select Region", choices=sales_data["Region"].tolist()
        )

        @render.plot
        def region_plot():
            region = input.region()
            region_data = sales_data[sales_data["Region"] == region]

            plt.figure(figsize=(8, 5))
            plt.bar(["Q1", "Q2", "Q3", "Q4"], region_data.iloc[0, 1:5], color="skyblue")
            plt.title(f"{region} Region Quarterly Sales")
            plt.ylabel("Sales Amount")
            plt.xlabel("Quarter")
            return plt.gcf()

    with ui.nav_panel("Total Sales Trend"):

        @render.plot
        def total_sales_plot():
            quarterly_totals = sales_data.iloc[:, 1:5].sum()

            plt.figure(figsize=(8, 5))
            plt.plot(
                ["Q1", "Q2", "Q3", "Q4"],
                quarterly_totals,
                marker="o",
                linestyle="-",
                color="green",
            )
            plt.title("Total Sales Across All Regions")
            plt.ylabel("Total Sales")
            plt.xlabel("Quarter")
            return plt.gcf()
