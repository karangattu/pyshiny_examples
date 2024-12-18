from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
    }
)

# Custom theme setup
my_theme = ui.Theme("shiny").add_rules(  # Changed from "default" to "shiny"
    """
        h1, h2, h3 { 
            color: #2c3e50;
            font-weight: 600;
        }
        .value-box {
            background-color: #f8f9fa;
            border-radius: 8px;
            padding: 15px;
            margin: 10px 0;
        }
    """
)

# Page options setup
ui.page_opts(
    title="Complete Page Options Demo",
    window_title="Page Opts Demo",
    lang="en",
    theme=my_theme,
    fillable=True,
    full_width=True,
)

# Add Font Awesome for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">'
    )
)

# Sidebar layout
with ui.sidebar(title="Controls"):
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
    ui.input_numeric("threshold", "Value Threshold", value=100, min=50, max=150)
    ui.hr()
    ui.input_dark_mode(id="dark_mode")  # Changed to proper dark mode input

# Main content
with ui.layout_columns(fill=True):
    # First row of cards
    with ui.card(full_screen=True):
        ui.card_header("Data Statistics")

        @render.data_frame
        def stats_table():
            df = filtered_data()
            stats = pd.DataFrame(
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
            return stats

    with ui.card(full_screen=True):
        ui.card_header("Time Series Plot")

        @render.plot
        def time_series():
            df = filtered_data()
            fig, ax = plt.subplots(figsize=(10, 6))
            for cat in df["category"].unique():
                cat_data = df[df["category"] == cat]
                ax.plot(cat_data["date"], cat_data["value"], label=cat)
            ax.axhline(y=input.threshold(), color="r", linestyle="--", alpha=0.5)
            ax.set_title("Value Over Time by Category")
            ax.legend()
            return fig


# Second row
with ui.layout_columns(fill=True):
    with ui.value_box(
        showcase=ui.HTML(
            '<i class="fa-solid fa-chart-line" style="font-size: 2rem;"></i>'
        ),
        theme="primary",
    ):
        "Average Value"

        @render.text
        def avg_value():
            return f"{filtered_data()['value'].mean():.2f}"

    with ui.value_box(
        showcase=ui.HTML('<i class="fa-solid fa-list" style="font-size: 2rem;"></i>'),
        theme="info",
    ):
        "Number of Records"

        @render.text
        def record_count():
            return f"{len(filtered_data()):,}"


# Data table at the bottom
with ui.card(full_screen=True):
    ui.card_header("Detailed Data")

    @render.data_frame
    def detail_table():
        return render.DataGrid(
            filtered_data(),
            selection_mode="rows",
            width="100%",
            height="300px",
        )


@reactive.calc
def filtered_data():
    df = data.copy()

    # Date range filter
    if input.date_range() is not None:
        start_date = datetime.combine(input.date_range()[0], datetime.min.time())
        end_date = datetime.combine(input.date_range()[1], datetime.max.time())
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    # Category filter
    if input.category() != "All":
        df = df[df["category"] == input.category()]

    # Value threshold filter
    df = df[df["value"] >= input.threshold()]

    return df
