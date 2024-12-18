import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render
from matplotlib import pyplot as plt

# Generate some synthetic data
np.random.seed(123)
data = pd.DataFrame(
    {
        "date": pd.date_range(start="2024-01-01", periods=100, freq="D"),
        "sales": np.random.randint(100, 1000, 100),
        "customers": np.random.randint(10, 100, 100),
        "satisfaction": np.random.uniform(3.5, 5.0, 100),
    }
)

# Set page options
ui.page_opts(title="Business Metrics Dashboard", fillable=True)

# Create navigation using navset_pill
with ui.navset_pill(id="nav"):
    with ui.nav_panel("Sales Overview"):
        with ui.layout_columns(col_widths=[6, 6]):
            with ui.card():
                ui.card_header("Daily Sales")

                @render.plot
                def sales_plot():
                    fig, ax = plt.subplots()
                    ax.plot(data["date"], data["sales"])
                    ax.set_title("Daily Sales Trend")
                    plt.xticks(rotation=45)
                    return fig

            with ui.card():
                ui.card_header("Sales Statistics")

                @render.table
                def sales_stats():
                    stats = pd.DataFrame(
                        {
                            "Metric": ["Average", "Maximum", "Minimum"],
                            "Value": [
                                f"${data['sales'].mean():.2f}",
                                f"${data['sales'].max():.2f}",
                                f"${data['sales'].min():.2f}",
                            ],
                        }
                    )
                    return stats

    with ui.nav_panel("Customer Analytics"):
        with ui.layout_columns(col_widths=[6, 6]):
            with ui.card():
                ui.card_header("Customer Count")

                @render.plot
                def customer_plot():
                    fig, ax = plt.subplots()
                    ax.bar(data["date"], data["customers"])
                    ax.set_title("Daily Customer Count")
                    plt.xticks(rotation=45)
                    return fig

            with ui.card():
                ui.card_header("Customer Satisfaction")

                @render.plot
                def satisfaction_plot():
                    fig, ax = plt.subplots()
                    ax.hist(data["satisfaction"], bins=20)
                    ax.set_title("Satisfaction Distribution")
                    return fig

    with ui.nav_panel("Raw Data"):

        @render.data_frame
        def show_data():
            return render.DataGrid(data)
