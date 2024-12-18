from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample data
np.random.seed(123)
data = pd.DataFrame(
    {
        "Category": ["A", "B", "C", "D", "E"] * 20,
        "Value": np.random.normal(100, 15, 100),
        "Group": np.random.choice(["Group 1", "Group 2", "Group 3"], 100),
    }
)

# Create a custom theme
custom_theme = (
    ui.Theme(preset="sketchy")
    .add_rules(
        """
        .card { 
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
    """
    )
    .add_defaults(primary_color="#6a4c93", secondary_color="#1a936f")
)

# Set page options with custom theme
ui.page_opts(title="Theme Demo App", theme=custom_theme, fillable=True)

# Create the layout
with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_selectize(
            "group",
            "Select Group",
            choices=["All"] + list(data["Group"].unique()),
            selected="All",
        )

        ui.input_slider("bins", "Number of bins", min=5, max=50, value=20)

    with ui.card():
        ui.card_header("Data Distribution")

        @render.plot
        def histogram():
            filtered_data = data
            if input.group() != "All":
                filtered_data = data[data["Group"] == input.group()]

            fig, ax = plt.subplots()
            ax.hist(
                filtered_data["Value"],
                bins=input.bins(),
                color="#6a4c93",  # Using primary color directly
                alpha=0.7,
            )
            ax.set_title("Value Distribution")
            ax.set_xlabel("Value")
            ax.set_ylabel("Frequency")
            return fig

    with ui.card():
        ui.card_header("Summary Statistics")

        @render.data_frame
        def summary_stats():
            filtered_data = data
            if input.group() != "All":
                filtered_data = data[data["Group"] == input.group()]

            stats = pd.DataFrame(
                {
                    "Metric": ["Mean", "Median", "Std Dev", "Count"],
                    "Value": [
                        round(filtered_data["Value"].mean(), 2),
                        round(filtered_data["Value"].median(), 2),
                        round(filtered_data["Value"].std(), 2),
                        len(filtered_data),
                    ],
                }
            )
            return stats
