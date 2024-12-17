import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
sales_data = pd.DataFrame(
    {
        "Region": ["North", "South", "East", "West"] * 3,
        "Quarter": [
            "Q1",
            "Q1",
            "Q1",
            "Q1",
            "Q2",
            "Q2",
            "Q2",
            "Q2",
            "Q3",
            "Q3",
            "Q3",
            "Q3",
        ],
        "Sales": np.random.randint(50000, 200000, 12),
        "Profit": np.random.randint(5000, 50000, 12),
    }
)

# Set page options
ui.page_opts(title="Sales Dashboard", fillable=True)

# Create a navset card tab with multiple panels
with ui.navset_card_tab(id="sales_dashboard"):
    with ui.nav_panel("Sales Overview"):
        with ui.layout_columns():

            @render.data_frame
            def sales_table():
                return sales_data

            @render.plot
            def sales_bar_chart():
                plt.figure(figsize=(10, 6))
                sales_by_region = sales_data.groupby("Region")["Sales"].sum()
                sales_by_region.plot(kind="bar")
                plt.title("Total Sales by Region")
                plt.xlabel("Region")
                plt.ylabel("Total Sales")
                plt.tight_layout()
                return plt.gcf()

    with ui.nav_panel("Profit Analysis"):
        with ui.layout_columns():

            @render.data_frame
            def profit_table():
                profit_summary = sales_data.groupby("Region")["Profit"].agg(
                    ["mean", "sum"]
                )
                return profit_summary

            @render.plot
            def profit_pie_chart():
                plt.figure(figsize=(10, 6))
                profit_by_region = sales_data.groupby("Region")["Profit"].sum()
                plt.pie(
                    profit_by_region, labels=profit_by_region.index, autopct="%1.1f%%"
                )
                plt.title("Profit Distribution by Region")
                plt.axis("equal")
                plt.tight_layout()
                return plt.gcf()

    with ui.nav_panel("Quarterly Trends"):
        with ui.layout_columns():

            @render.data_frame
            def quarterly_summary():
                quarterly_summary = sales_data.groupby("Quarter")[
                    ["Sales", "Profit"]
                ].sum()
                return quarterly_summary

            @render.plot
            def quarterly_line_chart():
                plt.figure(figsize=(10, 6))
                quarterly_data = sales_data.groupby("Quarter")[
                    ["Sales", "Profit"]
                ].sum()
                quarterly_data.plot(kind="line", marker="o")
                plt.title("Quarterly Sales and Profit Trends")
                plt.xlabel("Quarter")
                plt.ylabel("Amount")
                plt.legend(title="Metric")
                plt.tight_layout()
                return plt.gcf()
