from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np

# Generate some sample data
np.random.seed(123)
data = pd.DataFrame(
    {
        "Category": ["A", "B", "C", "D", "E"] * 4,
        "Value": np.random.randint(1, 100, 20),
        "Score": np.random.normal(50, 15, 20).round(2),
    }
)

# Set page options
ui.page_opts(title="Card Demo", fillable=True)

# Create a card with inputs
with ui.card(full_screen=True):
    ui.card_header("Data Filters")
    ui.input_numeric("min_value", "Minimum Value", value=0)
    ui.input_slider("score_range", "Score Range", min=0, max=100, value=[20, 80])

# Create a card to display filtered data
with ui.card(full_screen=True):
    ui.card_header("Filtered Data")

    @render.data_frame
    def filtered_table():
        df = data[
            (data["Value"] >= input.min_value())
            & (data["Score"] >= input.score_range()[0])
            & (data["Score"] <= input.score_range()[1])
        ]
        return df


# Create a card with summary statistics
with ui.card():
    ui.card_header("Summary Statistics")

    @render.data_frame
    def summary_stats():
        df = data[
            (data["Value"] >= input.min_value())
            & (data["Score"] >= input.score_range()[0])
            & (data["Score"] <= input.score_range()[1])
        ]

        summary = pd.DataFrame(
            {
                "Metric": ["Count", "Avg Value", "Avg Score"],
                "Value": [
                    len(df),
                    df["Value"].mean().round(2),
                    df["Score"].mean().round(2),
                ],
            }
        )
        return summary
