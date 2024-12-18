import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render

# Generate some sample data
np.random.seed(123)
data = pd.DataFrame(
    {
        "category": ["A", "B", "C", "D", "E"] * 20,
        "value": np.random.normal(100, 20, 100),
        "group": ["Group 1", "Group 2"] * 50,
    }
)

# Set page options
ui.page_opts(title="Sidebar Demo", fillable=True)

# Create sidebar with controls
with ui.sidebar():
    ui.input_select(
        "category", "Select Category", choices=["All"] + list(data["category"].unique())
    )
    ui.input_numeric("threshold", "Value Threshold", value=100, min=0, max=200)
    ui.input_checkbox_group(
        "groups",
        "Select Groups",
        choices=list(data["group"].unique()),
        selected=list(data["group"].unique()),
    )

# Main content area
ui.h2("Data Analysis Dashboard")

# Create two cards in a row
with ui.layout_columns():
    # First card with filtered data table
    with ui.card():
        ui.card_header("Filtered Data")

        @render.data_frame
        def filtered_table():
            df = data.copy()
            # Filter by category
            if input.category() != "All":
                df = df[df["category"] == input.category()]
            # Filter by threshold
            df = df[df["value"] >= input.threshold()]
            # Filter by groups
            df = df[df["group"].isin(input.groups())]
            return df

    # Second card with summary statistics
    with ui.card():
        ui.card_header("Summary Statistics")

        @render.data_frame
        def summary_stats():
            df = data.copy()
            # Apply same filters as table
            if input.category() != "All":
                df = df[df["category"] == input.category()]
            df = df[df["value"] >= input.threshold()]
            df = df[df["group"].isin(input.groups())]

            # Calculate summary statistics
            summary = pd.DataFrame(
                {
                    "Metric": ["Count", "Mean", "Median", "Std Dev"],
                    "Value": [
                        len(df),
                        round(df["value"].mean(), 2),
                        round(df["value"].median(), 2),
                        round(df["value"].std(), 2),
                    ],
                }
            )
            return summary
