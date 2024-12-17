import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
categories = ["A", "B", "C", "D", "E"]
data = pd.DataFrame(
    {
        "Category": categories,
        "Sales": np.random.randint(50, 500, len(categories)),
        "Profit": np.random.uniform(10, 100, len(categories)),
        "Growth": np.random.uniform(-0.2, 0.3, len(categories)),
    }
)

# App Title and Page Options
ui.page_opts(title="Layout Columns Showcase", fillable=True)

# Sidebar for controlling layout parameters
with ui.sidebar():
    ui.input_select(
        "col_widths_preset",
        "Column Widths Preset",
        choices={
            "Default (Auto)": "default",
            "Custom Fixed": "custom_fixed",
            "Responsive Breakpoints": "responsive",
            "Uneven Distribution": "uneven",
        },
        selected="default",
    )

    ui.input_select(
        "row_heights_preset",
        "Row Heights Preset",
        choices={
            "Default": "default",
            "Fractional Units": "fractional",
            "Mixed Heights": "mixed",
            "Auto Content": "auto_content",
        },
        selected="default",
    )

    ui.input_checkbox("fill", "Fill Container", value=True)
    ui.input_checkbox("fillable", "Fillable Elements", value=True)

    ui.input_slider("gap", "Gap Between Columns", min=0, max=2, value=0.5, step=0.25)


# Dynamically set column widths based on preset
@reactive.calc
def get_col_widths():
    preset = input.col_widths_preset()
    if preset == "default":
        return None
    elif preset == "custom_fixed":
        return [4, 8]  # First column 4 units, second 8 units
    elif preset == "responsive":
        return {"sm": [6, 6], "lg": [4, 8]}
    elif preset == "uneven":
        return [-2, 8, -2]  # Columns with padding


# Dynamically set row heights based on preset
@reactive.calc
def get_row_heights():
    preset = input.row_heights_preset()
    if preset == "default":
        return None
    elif preset == "fractional":
        return [1, 2]  # First row 1fr, second row 2fr
    elif preset == "mixed":
        return ["auto", 1]  # First row auto, second row 1fr
    elif preset == "auto_content":
        return "auto"


# Main Layout with Dynamic Configuration
with ui.layout_columns(
    col_widths=get_col_widths,
    row_heights=get_row_heights,
    fill=input.fill,
    fillable=input.fillable,
    gap=lambda: f"{input.gap()}rem",
):
    with ui.card():
        ui.card_header("Sales Data Visualization")

        @render.plot
        def sales_bar_plot():
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.bar(data["Category"], data["Sales"])
            ax.set_title("Sales by Category")
            ax.set_xlabel("Category")
            ax.set_ylabel("Sales")
            return fig

    with ui.card():
        ui.card_header("Profit Analysis")

        @render.plot
        def profit_line_plot():
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(data["Category"], data["Profit"], marker="o")
            ax.set_title("Profit Trends")
            ax.set_xlabel("Category")
            ax.set_ylabel("Profit")
            return fig

    with ui.card():
        ui.card_header("Growth Rates")

        @render.plot
        def growth_scatter_plot():
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.scatter(data["Category"], data["Growth"], color="green")
            ax.set_title("Growth Rate Distribution")
            ax.set_xlabel("Category")
            ax.set_ylabel("Growth Rate")
            return fig

    with ui.card():
        ui.card_header("Data Summary")

        @render.table
        def data_summary():
            return data.describe().reset_index()
