from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Generate some sample data
np.random.seed(123)
data = pd.DataFrame(
    {
        "Category": ["A", "B", "C", "D"] * 25,
        "Value": np.random.normal(100, 15, 100),
        "Count": np.random.randint(1, 100, 100),
        "Date": pd.date_range(start="2023-01-01", periods=100),
    }
)

# Set page options
ui.page_opts(title="Sidebar Demo", fillable=True)

# Create a sidebar with all possible parameters
with ui.sidebar(
    id="demo_sidebar",  # Unique identifier
    title="Complete Sidebar Demo",  # Title displayed at top
    position="left",  # Position (left/right)
    open="desktop",  # Initial state
    width="300px",  # Width of sidebar
    bg="#f8f9fa",  # Background color
    fg="#212529",  # Foreground (text) color
    class_="my-custom-sidebar",  # Additional CSS classes
    max_height_mobile="80vh",  # Max height on mobile
    padding="1rem",  # Internal padding
    gap="1rem",  # Gap between elements
):
    ui.h4("Filters and Controls")

    # Add various input controls to demonstrate sidebar content
    ui.input_select(
        "category", "Select Category", choices=["All"] + list(data["Category"].unique())
    )

    ui.input_slider(
        "value_range",
        "Value Range",
        min=int(data["Value"].min()),
        max=int(data["Value"].max()),
        value=[int(data["Value"].min()), int(data["Value"].max())],
    )

    ui.input_date_range(
        "date_range", "Date Range", start=data["Date"].min(), end=data["Date"].max()
    )

    ui.input_numeric(
        "min_count", "Minimum Count", value=0, min=0, max=int(data["Count"].max())
    )

    ui.input_checkbox("show_stats", "Show Statistics", value=True)

    ui.hr()

    ui.input_action_button(
        "toggle_sidebar", "Toggle Sidebar", class_="btn-secondary w-100"
    )

# Main content area
with ui.layout_columns(col_widths=[8, 4]):
    # Left column with main plot
    with ui.card():
        ui.card_header("Data Visualization")

        @render.plot
        def main_plot():
            filtered_data = filter_data()
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.scatter(filtered_data["Value"], filtered_data["Count"])
            ax.set_xlabel("Value")
            ax.set_ylabel("Count")
            ax.set_title("Value vs Count")
            return fig

    # Right column with statistics
    with ui.card():
        ui.card_header("Statistics")

        @render.data_frame
        def stats_table():
            if not input.show_stats():
                return pd.DataFrame()

            filtered_data = filter_data()
            stats = pd.DataFrame(
                {
                    "Metric": ["Count", "Mean", "Median", "Std Dev"],
                    "Value": [
                        len(filtered_data),
                        round(filtered_data["Value"].mean(), 2),
                        round(filtered_data["Value"].median(), 2),
                        round(filtered_data["Value"].std(), 2),
                    ],
                }
            )
            return stats


# Reactive calculation for filtered data
@reactive.calc
def filter_data():
    df = data.copy()

    # Apply category filter
    if input.category() != "All":
        df = df[df["Category"] == input.category()]

    # Apply value range filter
    df = df[
        (df["Value"] >= input.value_range()[0])
        & (df["Value"] <= input.value_range()[1])
    ]

    # Apply date range filter
    start_date = pd.to_datetime(input.date_range()[0])
    end_date = pd.to_datetime(input.date_range()[1])
    df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

    # Apply minimum count filter
    df = df[df["Count"] >= input.min_count()]

    return df


# Effect for sidebar toggle button
@reactive.effect
@reactive.event(input.toggle_sidebar)
def toggle_sidebar():
    current_state = input.demo_sidebar()
    ui.update_sidebar("demo_sidebar", show=not current_state)
