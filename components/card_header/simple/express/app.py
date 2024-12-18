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
        "Sales": np.random.randint(50000, 200000, 5),
        "Growth": np.random.uniform(0.05, 0.25, 5),
    }
)

ui.page_opts(title="Sales Dashboard")

with ui.layout_columns():
    # First Card with a simple header
    with ui.card():
        ui.card_header("Total Sales by Region")

        @render.table
        def sales_table():
            return sales_data

    # Second Card with a more complex header
    with ui.card():
        ui.card_header(
            ui.tags.div(
                "Sales Growth", ui.tags.span("Year-over-Year", class_="text-muted ms-2")
            )
        )

        @render.plot
        def growth_plot():
            plt.figure(figsize=(8, 4))
            plt.bar(sales_data["Region"], sales_data["Growth"] * 100)
            plt.title("Sales Growth Percentage")
            plt.ylabel("Growth (%)")
            plt.xlabel("Region")
            return plt.gcf()

    # Third Card with an icon in the header
    with ui.card():
        ui.card_header(
            ui.tags.div(
                "Performance Metrics", ui.tags.i(class_="fa-solid fa-chart-line ms-2")
            )
        )

        @render.table
        def performance_metrics():
            metrics_df = sales_data.copy()
            metrics_df["Performance"] = np.where(
                metrics_df["Growth"] > 0.15, "Excellent", "Needs Improvement"
            )
            return metrics_df[["Region", "Sales", "Growth", "Performance"]]
