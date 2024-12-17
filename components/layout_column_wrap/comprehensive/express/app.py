import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
data = {
    "Category A": np.random.normal(50, 10, 100),
    "Category B": np.random.normal(60, 15, 100),
    "Category C": np.random.normal(40, 5, 100),
    "Category D": np.random.normal(70, 20, 100),
}
df = pd.DataFrame(data)

# App Title and Description
ui.page_opts(title="layout_column_wrap() Parameters Showcase", fillable=True)

# Sidebar for controlling layout parameters
with ui.sidebar():
    ui.input_slider("width", "Column Width", min=0.1, max=1, value=1 / 3, step=0.1)
    ui.input_checkbox("fixed_width", "Fixed Width", value=False)
    ui.input_select(
        "heights_equal", "Heights Equal", choices=["all", "row"], selected="all"
    )
    ui.input_checkbox("fill", "Fill Container", value=True)
    ui.input_checkbox("fillable", "Fillable", value=True)
    ui.input_slider("gap", "Gap", min=0, max=2, value=0.5, step=0.1)

# Reactive value to store layout configuration
layout_config = reactive.value(
    {
        "width": 1 / 3,
        "fixed_width": False,
        "heights_equal": "all",
        "fill": True,
        "fillable": True,
        "gap": 0.5,
    }
)


# Update layout configuration when inputs change
@reactive.effect
def _update_layout_config():
    layout_config.set(
        {
            "width": input.width(),
            "fixed_width": input.fixed_width(),
            "heights_equal": input.heights_equal(),
            "fill": input.fill(),
            "fillable": input.fillable(),
            "gap": input.gap(),
        }
    )


# Main Layout Demonstration
@render.ui
def dynamic_layout():
    config = layout_config.get()
    with ui.layout_column_wrap(
        width=config["width"],
        fixed_width=config["fixed_width"],
        heights_equal=config["heights_equal"],
        fill=config["fill"],
        fillable=config["fillable"],
        gap=f"{config['gap']}rem",
    ):
        # Card 1: Line Plot
        with ui.card(full_screen=True):
            ui.card_header("Line Plot")

            @render.plot
            def line_plot():
                plt.figure(figsize=(8, 6))
                for col in df.columns:
                    plt.plot(df[col], label=col)
                plt.title("Line Plot of Categories")
                plt.legend()
                return plt.gcf()

        # Card 2: Bar Plot
        with ui.card(full_screen=True):
            ui.card_header("Bar Plot")

            @render.plot
            def bar_plot():
                plt.figure(figsize=(8, 6))
                df.mean().plot(kind="bar")
                plt.title("Mean of Categories")
                plt.ylabel("Mean Value")
                return plt.gcf()

        # Card 3: Box Plot
        with ui.card(full_screen=True):
            ui.card_header("Box Plot")

            @render.plot
            def box_plot():
                plt.figure(figsize=(8, 6))
                df.boxplot()
                plt.title("Box Plot of Categories")
                plt.ylabel("Values")
                return plt.gcf()

        # Card 4: Scatter Plot
        with ui.card(full_screen=True):
            ui.card_header("Scatter Plot")

            @render.plot
            def scatter_plot():
                plt.figure(figsize=(8, 6))
                plt.scatter(df["Category A"], df["Category B"])
                plt.title("Scatter: Category A vs Category B")
                plt.xlabel("Category A")
                plt.ylabel("Category B")
                return plt.gcf()


# Descriptive Statistics Card
with ui.card():
    ui.card_header("Descriptive Statistics")

    @render.table
    def stats_table():
        return df.describe().T


# Layout Parameters Display
with ui.card():
    ui.card_header("Current Layout Parameters")

    @render.text
    def layout_params():
        config = layout_config.get()
        return f"""
        Column Width: {config['width']}
        Fixed Width: {config['fixed_width']}
        Heights Equal: {config['heights_equal']}
        Fill: {config['fill']}
        Fillable: {config['fillable']}
        Gap: {config['gap']} rem
        """
