from datetime import datetime
import numpy as np
import pandas as pd
from shiny import reactive
from shiny.express import input, ui, render

# Generate some sample data
np.random.seed(123)
dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
data = pd.DataFrame(
    {
        "date": dates,
        "value": np.random.normal(100, 15, len(dates)),
        "category": np.random.choice(["A", "B", "C"], len(dates)),
        "metric": np.random.uniform(0, 1, len(dates)),
    }
)

# Set page options with a fillable layout
ui.page_opts(
    title="Layout Sidebar Demo",
    fillable=True,
)

# Main layout with sidebar
with ui.layout_sidebar(
    # fillable parameter to allow content to fill available space
    fillable=True,
    # fill parameter to allow the sidebar layout to grow/shrink
    fill=True,
    # bg parameter for background color
    bg="#f8f9fa",
    # fg parameter for foreground (text) color
    fg="#212529",
    # border parameter to show border
    border=True,
    # border_radius parameter for rounded corners
    border_radius=True,
    # border_color parameter for border color
    border_color="#dee2e6",
    # gap parameter for spacing between elements
    gap="1rem",
    # padding parameter for internal spacing
    padding=["1rem", "1.5rem"],
    # height parameter for layout height
    height="100%",
):
    # Sidebar content
    with ui.sidebar(
        title="Control Panel", bg="#e9ecef", position="left", open="desktop"
    ):
        ui.h4("Filters")
        ui.input_date_range(
            "date_range",
            "Select Date Range",
            start=data["date"].min(),
            end=data["date"].max(),
        )

        ui.input_selectize(
            "category",
            "Select Category",
            choices=["All"] + list(data["category"].unique()),
            selected="All",
        )

        ui.input_slider("metric_range", "Metric Range", min=0, max=1, value=[0, 1])

        ui.hr()
        ui.input_switch("show_stats", "Show Statistics", value=True)

    # Main content area
    ui.h2("Data Analysis Dashboard")

    # Create card for statistics
    with ui.card():
        ui.card_header("Summary Statistics")

        @render.data_frame
        def stats():
            df = filtered_data()
            stats_df = pd.DataFrame(
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
            return stats_df

    # Create card for visualization
    with ui.card():
        ui.card_header("Time Series Plot")

        @render.plot
        def plot():
            df = filtered_data()
            fig, ax = plt.subplots(figsize=(10, 6))
            for cat in df["category"].unique():
                cat_data = df[df["category"] == cat]
                ax.scatter(cat_data["date"], cat_data["value"], label=cat, alpha=0.6)
            ax.set_xlabel("Date")
            ax.set_ylabel("Value")
            ax.legend()
            ax.grid(True, alpha=0.3)
            return fig


@reactive.calc
def filtered_data():
    df = data.copy()

    # Date range filter
    if input.date_range() is not None:
        start_date, end_date = input.date_range()
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    # Category filter
    if input.category() != "All":
        df = df[df["category"] == input.category()]

    # Metric range filter
    min_metric, max_metric = input.metric_range()
    df = df[(df["metric"] >= min_metric) & (df["metric"] <= max_metric)]

    return df
