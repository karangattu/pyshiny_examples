import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Synthetic data generation
np.random.seed(42)
sales_data = pd.DataFrame(
    {
        "Region": ["North", "South", "East", "West", "Central"],
        "Sales": np.random.randint(500000, 2000000, 5),
        "Growth": np.random.uniform(0.05, 0.25, 5),
    }
)

# Icons (using Font Awesome)
ui.page_opts(title="Sales Dashboard")
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# Layout with value boxes
with ui.layout_columns():
    with ui.value_box(
        showcase=ui.tags.i(class_="fa-solid fa-chart-line", style="font-size: 2rem;"),
        theme="bg-gradient-blue-purple",
    ):
        "Total Sales"
        f"${sales_data['Sales'].sum():,}"
        "Across All Regions"

    with ui.value_box(
        showcase=ui.tags.i(
            class_="fa-solid fa-arrow-trend-up", style="font-size: 2rem;"
        ),
        theme="bg-green",
    ):
        "Average Growth Rate"
        f"{sales_data['Growth'].mean():.2%}"
        "Year-over-Year"

    with ui.value_box(
        showcase=ui.tags.i(class_="fa-solid fa-globe", style="font-size: 2rem;"),
        theme="bg-orange",
    ):
        "Top Performing Region"
        sales_data.loc[sales_data["Sales"].idxmax(), "Region"]
        f"${sales_data['Sales'].max():,} in Sales"


# Add a plot to complement the value boxes
@render.plot
def sales_plot():
    plt.figure(figsize=(10, 6))
    plt.bar(sales_data["Region"], sales_data["Sales"])
    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf()


# Optional: Add some interactivity
with ui.sidebar():
    ui.input_slider("year", "Select Year", min=2020, max=2024, value=2023)
