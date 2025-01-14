from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(123)
data = pd.DataFrame(
    {
        "Category": ["A", "B", "C", "D"] * 25,
        "Values": np.random.normal(100, 15, 100),
        "Date": pd.date_range(start="2023-01-01", periods=100, freq="D"),
        "Status": np.random.choice(["Active", "Inactive", "Pending"], 100),
    }
)

# Page options for the app
ui.page_opts(title="Dashboard Demo", fillable=True)

# Create sidebar layout
with ui.layout_sidebar():
    with ui.sidebar(id="main_sidebar", open="desktop", title="Control Panel"):
        # Add sidebar controls
        ui.h4("Filters and Controls")

        ui.input_date_range(
            "date_range", "Select Date Range", start="2023-01-01", end="2023-04-10"
        )

        ui.input_selectize(
            "category",
            "Select Categories",
            choices=sorted(data["Category"].unique()),
            multiple=True,
            selected=["A"],
        )

        ui.input_selectize(
            "status",
            "Select Status",
            choices=sorted(data["Status"].unique()),
            multiple=True,
        )

        ui.input_slider(
            "value_range",
            "Value Range",
            min=int(data["Values"].min()),
            max=int(data["Values"].max()),
            value=[int(data["Values"].min()), int(data["Values"].max())],
        )

        ui.hr()

        ui.input_switch("show_summary", "Show Summary Statistics", value=True)

        ui.input_radio_buttons(
            "plot_type",
            "Plot Type",
            choices=["Line", "Bar", "Scatter"],
            selected="Line",
        )

        ui.input_numeric("point_size", "Point Size", value=3, min=1, max=10)

    # Main content area
    ui.h2("Data Visualization Dashboard")

    # Create layout for main content
    with ui.layout_column_wrap(width="400px"):
        # First card with filtered data table
        with ui.card():
            ui.card_header("Filtered Data")

            @render.data_frame
            def filtered_table():
                df = data.copy()

                # Apply date filter
                start_date = pd.to_datetime(input.date_range()[0])
                end_date = pd.to_datetime(input.date_range()[1])
                df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

                # Apply category filter
                if input.category():
                    df = df[df["Category"].isin(input.category())]

                # Apply status filter
                if input.status():
                    df = df[df["Status"].isin(input.status())]

                # Apply value range filter
                df = df[
                    (df["Values"] >= input.value_range()[0])
                    & (df["Values"] <= input.value_range()[1])
                ]

                return df

        # Second card with summary statistics
        with ui.card():
            ui.card_header("Summary Statistics")

            @render.data_frame
            def summary_stats():
                if not input.show_summary():
                    return pd.DataFrame()

                df = filtered_table()
                summary = pd.DataFrame(
                    {
                        "Metric": ["Count", "Mean", "Median", "Std Dev"],
                        "Value": [
                            len(df),
                            round(df["Values"].mean(), 2),
                            round(df["Values"].median(), 2),
                            round(df["Values"].std(), 2),
                        ],
                    }
                )
                return summary

        # Third card with plot
        with ui.card():
            ui.card_header("Data Visualization")

            @render.plot
            def data_plot():
                df = filtered_table()

                fig, ax = plt.subplots(figsize=(10, 6))

                if input.plot_type() == "Line":
                    df.groupby("Date")["Values"].mean().plot(ax=ax)
                elif input.plot_type() == "Bar":
                    df.groupby("Category")["Values"].mean().plot(kind="bar", ax=ax)
                else:  # Scatter plot
                    ax.scatter(df["Date"], df["Values"], s=input.point_size() * 20)

                plt.xticks(rotation=45)
                plt.tight_layout()
                return fig
