import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shiny import reactive
from shiny.express import input, ui, render

# Create sample data
np.random.seed(123)
data = pd.DataFrame(
    {
        "date": pd.date_range(start="2024-01-01", periods=100, freq="D"),
        "sales": np.random.randint(100, 1000, 100),
        "category": np.random.choice(["A", "B", "C"], 100),
    }
)

# Set page options
ui.page_opts(title="Sales Dashboard", fillable=True)

# Create sidebar with controls
with ui.sidebar():
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

# Main content
with ui.layout_columns(fill=True):
    with ui.card():
        ui.card_header("Sales Over Time")

        @render.plot
        def sales_plot():
            filtered_data = filter_data()
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(filtered_data["date"], filtered_data["sales"])
            ax.set_title("Daily Sales")
            ax.set_xlabel("Date")
            ax.set_ylabel("Sales")
            plt.xticks(rotation=45)
            plt.tight_layout()
            return fig

    with ui.card():
        ui.card_header("Sales Summary")

        @render.data_frame
        def summary_table():
            filtered_data = filter_data()
            summary = pd.DataFrame(
                {
                    "Metric": ["Total Sales", "Average Daily Sales", "Number of Days"],
                    "Value": [
                        f"${filtered_data['sales'].sum():,.0f}",
                        f"${filtered_data['sales'].mean():,.0f}",
                        len(filtered_data),
                    ],
                }
            )
            return summary


@reactive.calc
def filter_data():
    # Convert input.date_range() to datetime
    date_range = input.date_range()
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

    # Filter by date
    mask = (data["date"] >= start_date) & (data["date"] <= end_date)
    filtered = data[mask].copy()

    # Filter by category if not "All"
    if input.category() != "All":
        filtered = filtered[filtered["category"] == input.category()]

    return filtered
