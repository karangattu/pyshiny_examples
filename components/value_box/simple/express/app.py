from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np

# Generate some synthetic data
sales_data = pd.DataFrame(
    {
        "date": pd.date_range(start="2024-01-01", periods=30, freq="D"),
        "sales": np.random.randint(1000, 5000, 30),
        "customers": np.random.randint(100, 500, 30),
    }
)

# Page options
ui.page_opts(title="Sales Dashboard", fillable=True)

# Layout with value boxes
with ui.layout_columns(fill=False):

    # Total Sales Value Box
    with ui.value_box(
        showcase=ui.tags.i(class_="fa-solid fa-dollar-sign", style="font-size: 2rem;"),
        theme="bg-gradient-primary-secondary",
        full_screen=True,
    ):
        "Total Sales"
        f"${sales_data['sales'].sum():,.0f}"
        "Last 30 Days"

    # Average Daily Sales Value Box
    with ui.value_box(
        showcase=ui.tags.i(class_="fa-solid fa-chart-line", style="font-size: 2rem;"),
        theme="bg-gradient-info-warning",
        full_screen=True,
    ):
        "Average Daily Sales"
        f"${sales_data['sales'].mean():,.0f}"
        "Per Day"

    # Total Customers Value Box
    with ui.value_box(
        showcase=ui.tags.i(class_="fa-solid fa-users", style="font-size: 2rem;"),
        theme="bg-gradient-success-info",
        full_screen=True,
    ):
        "Total Customers"
        f"{sales_data['customers'].sum():,}"
        "Last 30 Days"

# Add Font Awesome for icons
ui.head_content(
    ui.tags.link(
        rel="stylesheet",
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css",
    )
)

# Add a simple data table below the value boxes
ui.h3("Daily Sales Data")


@render.data_frame
def sales_table():
    return sales_data.tail(5)
