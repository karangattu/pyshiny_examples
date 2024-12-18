import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
sales_data = pd.DataFrame(
    {
        "Region": ["North", "South", "East", "West", "Central"],
        "Q1 Sales": np.random.randint(100000, 500000, 5),
        "Q2 Sales": np.random.randint(100000, 500000, 5),
        "Q3 Sales": np.random.randint(100000, 500000, 5),
        "Q4 Sales": np.random.randint(100000, 500000, 5),
    }
)

# Set page options
ui.page_opts(title="Sales Dashboard", fillable=True)

# Create a navset_bar with multiple panels
with ui.navset_bar(title="Sales Analytics Dashboard", id="sales_nav"):
    # Sales Overview Panel
    with ui.nav_panel("Sales Overview"):
        with ui.layout_columns():
            with ui.card():
                ui.card_header("Quarterly Sales by Region")

                @render.table
                def sales_table():
                    return sales_data

    # Regional Performance Panel
    with ui.nav_panel("Regional Performance"):
        with ui.layout_columns():
            ui.input_select(
                "region_select", "Select Region", choices=sales_data["Region"].tolist()
            )

            @render.plot
            def regional_sales_plot():
                region = input.region_select()
                region_data = sales_data[sales_data["Region"] == region]

                plt.figure(figsize=(8, 5))
                quarters = ["Q1", "Q2", "Q3", "Q4"]
                sales = [
                    region_data["Q1 Sales"].values[0],
                    region_data["Q2 Sales"].values[0],
                    region_data["Q3 Sales"].values[0],
                    region_data["Q4 Sales"].values[0],
                ]
                plt.bar(quarters, sales)
                plt.title(f"{region} Region Quarterly Sales")
                plt.ylabel("Sales ($)")
                return plt.gcf()

    # Quarterly Comparison Panel
    with ui.nav_panel("Quarterly Comparison"):

        @render.plot
        def quarterly_comparison_plot():
            plt.figure(figsize=(10, 6))
            quarterly_cols = ["Q1 Sales", "Q2 Sales", "Q3 Sales", "Q4 Sales"]
            sales_data[quarterly_cols].plot(kind="bar")
            plt.title("Sales Comparison Across Regions")
            plt.xlabel("Regions")
            plt.ylabel("Sales ($)")
            plt.legend(title="Quarters")
            return plt.gcf()

    # Summary Statistics Panel
    with ui.nav_panel("Summary Statistics"):

        @render.table
        def summary_stats():
            quarterly_cols = ["Q1 Sales", "Q2 Sales", "Q3 Sales", "Q4 Sales"]
            summary = sales_data[quarterly_cols].agg(["mean", "min", "max"])
            summary.index = ["Average", "Minimum", "Maximum"]
            return summary
