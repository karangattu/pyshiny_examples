from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data
df = pd.DataFrame(
    {
        "name": ["John", "Jane", "Bob", "Alice"],
        "age": [25, 30, 35, 40],
        "score": [85, 90, 75, 95],
    }
)

ui.page_opts(title="Panel Conditional Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_radio_buttons(
            "view_type", "Select View", choices=["table", "plot", "summary"]
        )

        ui.input_slider("age_filter", "Filter by Age", min=20, max=45, value=30)

        ui.input_checkbox("show_advanced", "Show Advanced Options")

# Basic condition based on radio button selection
with ui.panel_conditional("input.view_type === 'table'"):
    ui.h3("Data Table View")

    @render.data_frame
    def show_table():
        return df[df["age"] <= input.age_filter()]


# Multiple conditions combined with AND
with ui.panel_conditional("input.view_type === 'plot' && input.age_filter > 25"):
    ui.h3("Plot View (Age > 25)")

    @render.plot
    def show_plot():
        filtered_df = df[df["age"] <= input.age_filter()]
        fig, ax = plt.subplots()
        ax.scatter(filtered_df["age"], filtered_df["score"])
        ax.set_xlabel("Age")
        ax.set_ylabel("Score")
        return fig


# Condition based on checkbox and using OR operator
with ui.panel_conditional("input.show_advanced || input.view_type === 'summary'"):
    ui.h3("Advanced Options & Summary")
    with ui.card():

        @render.data_frame
        def show_summary():
            filtered_df = df[df["age"] <= input.age_filter()]
            summary = pd.DataFrame(
                {
                    "Metric": ["Count", "Average Age", "Average Score"],
                    "Value": [
                        len(filtered_df),
                        round(filtered_df["age"].mean(), 2),
                        round(filtered_df["score"].mean(), 2),
                    ],
                }
            )
            return summary


# Complex condition with multiple operators
with ui.panel_conditional(
    "(input.view_type === 'plot' && input.age_filter > 30) || "
    "(input.view_type === 'summary' && input.show_advanced)"
):
    ui.h4("Additional Statistics")

    @render.data_frame
    def show_stats():
        filtered_df = df[df["age"] <= input.age_filter()]
        stats = pd.DataFrame(
            {
                "Statistic": ["Min Score", "Max Score", "Score StdDev"],
                "Value": [
                    filtered_df["score"].min(),
                    filtered_df["score"].max(),
                    round(filtered_df["score"].std(), 2),
                ],
            }
        )
        return stats


# Negation condition
with ui.panel_conditional("!input.show_advanced"):
    ui.markdown(
        """
        *Enable 'Show Advanced Options' to see more statistics*
    """
    )

# Numeric comparison condition
with ui.panel_conditional("input.age_filter === 30"):
    with ui.card(class_="bg-light"):
        ui.markdown("**You've selected the default age filter value!**")
