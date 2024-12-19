from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render

# Generate sample data
np.random.seed(123)
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
data = pd.DataFrame(
    {
        "date": dates,
        "value": np.random.normal(100, 10, len(dates)),
        "category": np.random.choice(["A", "B", "C"], len(dates)),
    }
)

# UI components
ui.page_opts(title="Date Range Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_date_range(
            "date_range",
            "Select Date Range",
            start=datetime(2023, 1, 1),
            end=datetime(2023, 12, 31),
            format="yyyy-mm-dd",
        )

        ui.input_selectize(
            "category",
            "Select Category",
            choices=["All"] + list(data["category"].unique()),
            selected="All",
        )

    @render.data_frame
    def filtered_data():
        # Get the date range input values and convert to datetime
        start_date = pd.to_datetime(
            datetime.combine(input.date_range()[0], datetime.min.time())
        )
        end_date = pd.to_datetime(
            datetime.combine(input.date_range()[1], datetime.min.time())
        )

        # Filter data based on date range
        df = data[(data["date"] >= start_date) & (data["date"] <= end_date)]

        # Apply category filter if not "All"
        if input.category() != "All":
            df = df[df["category"] == input.category()]

        return df

    @render.plot
    def time_series_plot():
        # Get filtered data
        df = filtered_data()

        # Create the plot
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()

        if input.category() == "All":
            # Plot each category with different color
            for cat in data["category"].unique():
                cat_data = df[df["category"] == cat]
                ax.plot(cat_data["date"], cat_data["value"], label=cat)
            ax.legend()
        else:
            # Plot single category
            ax.plot(df["date"], df["value"])

        ax.set_title("Time Series Plot")
        ax.set_xlabel("Date")
        ax.set_ylabel("Value")

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)
        plt.tight_layout()

        return fig
