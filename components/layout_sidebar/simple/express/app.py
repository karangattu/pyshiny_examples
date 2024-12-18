import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shiny import reactive
from shiny.express import input, ui, render

# Create synthetic data
np.random.seed(123)
data = pd.DataFrame(
    {
        "date": pd.date_range(start="2023-01-01", periods=100, freq="D"),
        "sales": np.random.normal(100, 15, 100),
        "region": np.random.choice(["North", "South", "East", "West"], 100),
        "product": np.random.choice(["A", "B", "C"], 100),
    }
)

# Set page options
ui.page_opts(title="Sales Dashboard", fillable=True)

# Create layout with sidebar
with ui.layout_sidebar():
    # Sidebar contents
    with ui.sidebar():
        ui.input_selectize(
            "region",
            "Select Region",
            choices=["All"] + list(data["region"].unique()),
            selected="All",
        )
        ui.input_selectize(
            "product",
            "Select Product",
            choices=["All"] + list(data["product"].unique()),
            selected="All",
        )
        ui.input_date_range(
            "date_range",
            "Select Date Range",
            start=data["date"].min(),
            end=data["date"].max(),
        )

    # Main panel contents
    @render.data_frame
    def sales_table():
        filtered_data = filter_data()
        return filtered_data[["date", "sales", "region", "product"]].head(10)

    @render.plot
    def sales_plot():
        filtered_data = filter_data()
        fig, ax = plt.subplots()
        filtered_data.plot(x="date", y="sales", ax=ax)
        ax.set_title("Sales Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Sales")
        return fig


@reactive.calc
def filter_data():
    # Start with complete dataset
    df = data.copy()

    # Filter by date range
    start_date = input.date_range()[0]
    end_date = input.date_range()[1]
    df = df[(df["date"].dt.date >= start_date) & (df["date"].dt.date <= end_date)]

    # Filter by region if not "All"
    if input.region() != "All":
        df = df[df["region"] == input.region()]

    # Filter by product if not "All"
    if input.product() != "All":
        df = df[df["product"] == input.product()]

    return df
