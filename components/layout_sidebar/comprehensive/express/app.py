import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
sales_data = pd.DataFrame(
    {
        "date": dates,
        "region": np.random.choice(["North", "South", "East", "West"], len(dates)),
        "sales": np.random.randint(100, 1000, len(dates)),
        "product_category": np.random.choice(
            ["Electronics", "Clothing", "Furniture", "Groceries"], len(dates)
        ),
    }
)

# Page options
ui.page_opts(title="Layout Sidebar Showcase", fillable=True)

# Sidebar with various configuration options
with ui.layout_sidebar(
    fillable=True,  # Allow main content to be fillable
    fill=True,  # Allow sidebar layout to fill available space
    bg="light",  # Background color
    fg=None,  # Foreground color
    border=True,  # Show border
    border_radius=True,  # Round the borders
    border_color="secondary",  # Border color
    gap="1rem",  # Gap between elements
    padding="1rem",  # Padding within the sidebar
    height="100%",  # Full height
):
    # Sidebar content
    with ui.sidebar(
        id="sidebar_demo",  # ID for reactive tracking
        title="Sidebar Configuration",  # Optional sidebar title
        position="left",  # Sidebar position
        open={
            "desktop": "open",
            "mobile": "closed",
        },  # Open state for desktop and mobile
        width=250,  # Sidebar width
    ):
        # Region filter
        ui.input_checkbox_group(
            "selected_regions",
            "Select Regions",
            choices=sales_data["region"].unique().tolist(),
            selected=sales_data["region"].unique().tolist(),
        )

        # Product category filter
        ui.input_selectize(
            "selected_categories",
            "Select Product Categories",
            choices=sales_data["product_category"].unique().tolist(),
            multiple=True,
            selected=sales_data["product_category"].unique().tolist(),
        )

        # Date range selector
        ui.input_date_range(
            "date_range",
            "Select Date Range",
            start=sales_data["date"].min(),
            end=sales_data["date"].max(),
            min=sales_data["date"].min(),
            max=sales_data["date"].max(),
        )

        # Aggregation method
        ui.input_radio_buttons(
            "aggregation", "Aggregation Method", choices=["Sum", "Mean", "Median"]
        )

    # Main content area
    @render.plot
    def sales_plot():
        # Filter data based on sidebar inputs
        filtered_df = sales_data[
            (sales_data["region"].isin(input.selected_regions()))
            & (sales_data["product_category"].isin(input.selected_categories()))
            & (sales_data["date"].between(input.date_range()[0], input.date_range()[1]))
        ]

        # Aggregate data
        if input.aggregation() == "Sum":
            grouped_data = filtered_df.groupby("product_category")["sales"].sum()
        elif input.aggregation() == "Mean":
            grouped_data = filtered_df.groupby("product_category")["sales"].mean()
        else:
            grouped_data = filtered_df.groupby("product_category")["sales"].median()

        # Plot
        plt.figure(figsize=(10, 6))
        grouped_data.plot(kind="bar")
        plt.title(f"Sales by Product Category ({input.aggregation()} Aggregation)")
        plt.xlabel("Product Category")
        plt.ylabel("Sales")
        plt.tight_layout()
        return plt.gcf()

    # Data table
    @render.data_frame
    def sales_table():
        # Filter data based on sidebar inputs
        filtered_df = sales_data[
            (sales_data["region"].isin(input.selected_regions()))
            & (sales_data["product_category"].isin(input.selected_categories()))
            & (sales_data["date"].between(input.date_range()[0], input.date_range()[1]))
        ]
        return filtered_df


# Optional: Add a footer or additional information
ui.markdown("### Sales Dashboard Demonstrating Layout Sidebar Configuration")
