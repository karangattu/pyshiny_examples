import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now())
sales_data = pd.DataFrame(
    {
        "date": dates,
        "sales": np.random.randint(100, 1000, size=len(dates)),
        "category": np.random.choice(
            ["Electronics", "Clothing", "Books", "Furniture"], size=len(dates)
        ),
    }
)

# Shiny App
ui.page_opts(title="Sales Dashboard")

with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Daily Sales Overview")

        @render.plot
        def sales_plot():
            category = input.category()
            filtered_data = sales_data[sales_data["category"] == category]

            import matplotlib.pyplot as plt

            plt.figure(figsize=(10, 6))
            plt.plot(filtered_data["date"], filtered_data["sales"])
            plt.title(f"Sales Trend for {category}")
            plt.xlabel("Date")
            plt.ylabel("Sales")
            plt.xticks(rotation=45)
            return plt.gcf()

        with ui.card_footer():
            ui.input_select(
                "category",
                "Select Category",
                choices=sales_data["category"].unique().tolist(),
            )
            "Footer with category selection"

    with ui.card(full_screen=True):
        ui.card_header("Sales Summary")

        @render.table
        def sales_summary():
            category = input.category()
            filtered_data = sales_data[sales_data["category"] == category]
            summary = (
                filtered_data.groupby("category")["sales"]
                .agg(["sum", "mean", "max"])
                .reset_index()
            )
            return summary

        with ui.card_footer():
            ui.tags.small(
                "Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
