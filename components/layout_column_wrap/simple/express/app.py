import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
data = pd.DataFrame(
    {
        "Category A": np.random.normal(50, 10, 100),
        "Category B": np.random.normal(60, 15, 100),
        "Category C": np.random.normal(40, 5, 100),
        "Group": np.random.choice(["X", "Y", "Z"], 100),
    }
)

# App UI and Layout
ui.page_opts(title="Layout Column Wrap Demo", fillable=True)

# Use layout_column_wrap to create a responsive grid
with ui.layout_column_wrap(width=1 / 3):
    # First column: Histogram
    with ui.card():
        ui.card_header("Histogram")

        @render.plot
        def histogram_plot():
            plt.figure(figsize=(8, 6))
            sns.histplot(data=data, x="Category A", kde=True)
            plt.title("Distribution of Category A")
            return plt.gcf()

    # Second column: Boxplot
    with ui.card():
        ui.card_header("Boxplot")

        @render.plot
        def boxplot():
            plt.figure(figsize=(8, 6))
            sns.boxplot(data=data, x="Group", y="Category B")
            plt.title("Category B by Group")
            return plt.gcf()

    # Third column: Scatter Plot
    with ui.card():
        ui.card_header("Scatter Plot")

        @render.plot
        def scatter_plot():
            plt.figure(figsize=(8, 6))
            sns.scatterplot(data=data, x="Category A", y="Category C", hue="Group")
            plt.title("Category A vs Category C")
            return plt.gcf()

    # Fourth column: Summary Statistics
    with ui.card():
        ui.card_header("Summary Statistics")

        @render.table
        def summary_stats():
            return data.groupby("Group").agg(
                {
                    "Category A": ["mean", "std"],
                    "Category B": ["mean", "std"],
                    "Category C": ["mean", "std"],
                }
            )

    # Fifth column: Pie Chart
    with ui.card():
        ui.card_header("Group Distribution")

        @render.plot
        def pie_chart():
            plt.figure(figsize=(8, 6))
            data["Group"].value_counts().plot(kind="pie", autopct="%1.1f%%")
            plt.title("Distribution of Groups")
            return plt.gcf()

    # Sixth column: Interactive Input
    with ui.card():
        ui.card_header("Interactive Control")
        ui.input_slider("sample_size", "Sample Size", min=10, max=100, value=50)

        @render.text
        def sample_info():
            sample = data.sample(n=input.sample_size())
            return f"Current sample size: {len(sample)}"
