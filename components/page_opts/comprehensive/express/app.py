import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from shiny import reactive
from shiny.express import input, ui, render

# Synthetic data generation
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
sales_data = pd.DataFrame(
    {
        "date": dates,
        "region": np.random.choice(["North", "South", "East", "West"], len(dates)),
        "sales": np.random.randint(100, 1000, len(dates)),
        "category": np.random.choice(
            ["Electronics", "Clothing", "Furniture", "Groceries"], len(dates)
        ),
    }
)

# Page options demonstration
ui.page_opts(
    title="Page Options Showcase",  # Page title
    window_title="Shiny Page Options Demo",  # Browser window title
    lang="en",  # Language code
    fillable=True,  # Allow content to fill the page
    full_width=False,  # Don't expand to full width
)

# Add Font Awesome for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">'
    )
)

# Sidebar for interactive elements
with ui.sidebar(id="sidebar", open="desktop"):
    ui.input_select(
        "region", "Select Region", choices=["All"] + list(sales_data["region"].unique())
    )
    ui.input_select(
        "category",
        "Select Category",
        choices=["All"] + list(sales_data["category"].unique()),
    )
    ui.input_date_range(
        "date_range",
        "Date Range",
        start=sales_data["date"].min(),
        end=sales_data["date"].max(),
    )
    ui.input_dark_mode(id="dark_mode")

# Main content with multiple sections
with ui.navset_card_pill(id="main_tabs"):
    with ui.nav_panel("Sales Overview"):
        with ui.layout_columns():
            with ui.card(full_screen=True):
                ui.card_header("Total Sales by Region")

                @render.plot
                def region_sales():
                    plt.close("all")  # Close any existing plots
                    region_filter = input.region()
                    category_filter = input.category()

                    filtered_data = sales_data.copy()
                    if region_filter != "All":
                        filtered_data = filtered_data[
                            filtered_data["region"] == region_filter
                        ]
                    if category_filter != "All":
                        filtered_data = filtered_data[
                            filtered_data["category"] == category_filter
                        ]

                    region_totals = filtered_data.groupby("region")["sales"].sum()

                    plt.figure(figsize=(8, 5))
                    region_totals.plot(kind="bar")
                    plt.title("Sales by Region")
                    plt.xlabel("Region")
                    plt.ylabel("Total Sales")
                    plt.tight_layout()
                    return plt.gcf()

            with ui.card(full_screen=True):
                ui.card_header("Sales Trend")

                @render.plot
                def sales_trend():
                    plt.close("all")  # Close any existing plots
                    start_date = input.date_range()[0]
                    end_date = input.date_range()[1]
                    region_filter = input.region()
                    category_filter = input.category()

                    filtered_data = sales_data.copy()
                    filtered_data = filtered_data[
                        (filtered_data["date"] >= start_date)
                        & (filtered_data["date"] <= end_date)
                    ]

                    if region_filter != "All":
                        filtered_data = filtered_data[
                            filtered_data["region"] == region_filter
                        ]
                    if category_filter != "All":
                        filtered_data = filtered_data[
                            filtered_data["category"] == category_filter
                        ]

                    daily_sales = filtered_data.groupby("date")["sales"].sum()

                    plt.figure(figsize=(10, 5))
                    daily_sales.plot()
                    plt.title("Daily Sales Trend")
                    plt.xlabel("Date")
                    plt.ylabel("Sales")
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    return plt.gcf()

    with ui.nav_panel("Category Analysis"):

        @render.data_frame
        def category_summary():
            start_date = input.date_range()[0]
            end_date = input.date_range()[1]
            region_filter = input.region()
            category_filter = input.category()

            filtered_data = sales_data.copy()
            filtered_data = filtered_data[
                (filtered_data["date"] >= start_date)
                & (filtered_data["date"] <= end_date)
            ]

            if region_filter != "All":
                filtered_data = filtered_data[filtered_data["region"] == region_filter]
            if category_filter != "All":
                filtered_data = filtered_data[
                    filtered_data["category"] == category_filter
                ]

            summary = (
                filtered_data.groupby("category")["sales"]
                .agg(["sum", "mean", "count"])
                .reset_index()
            )
            summary.columns = [
                "Category",
                "Total Sales",
                "Average Sales",
                "Number of Sales",
            ]
            return summary


# Optional: Add a footer
ui.markdown("© 2024 Sales Analytics Dashboard")
