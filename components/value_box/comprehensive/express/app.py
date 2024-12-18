from shiny import reactive
from shiny.express import input, ui, render
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta


# Sample data generation
def generate_sales_data():
    dates = [datetime.now() - timedelta(days=x) for x in range(30)]
    sales = np.random.normal(1000, 200, 30).cumsum()
    return dates, sales


# Custom showcase icons using Font Awesome
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">'
    )
)

# Page options
ui.page_opts(title="Value Box Demo", fillable=True)


# Create plot first
@render.plot
def trend_plot():
    dates, sales = generate_sales_data()

    plt.figure(figsize=(6, 2))
    plt.plot(dates, sales, color="white")
    plt.xticks([])
    plt.yticks([])

    # Set transparent background
    plt.gca().set_facecolor("none")
    plt.gcf().set_facecolor("none")

    # Remove spines
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    return plt.gcf()


# Layout with value boxes demonstrating different parameters
with ui.layout_column_wrap(width=1 / 2):

    # Basic value box with left showcase
    with ui.value_box(
        showcase=ui.tags.i(class_="fa-solid fa-dollar-sign", style="font-size: 2rem;"),
        theme="primary",
        showcase_layout="left center",
        full_screen=True,
        height="200px",
        class_="m-2",
    ):
        "Total Sales"
        "$1,234,567"
        "Up 15% from last month"

    # Value box with top right showcase
    with ui.value_box(
        showcase=ui.tags.i(class_="fa-solid fa-chart-line", style="font-size: 2rem;"),
        theme="bg-gradient-orange-red",
        showcase_layout="top right",
        full_screen=True,
        height="200px",
        class_="m-2",
    ):
        "Growth Rate"
        "23.5%"
        "Exceeding targets"

    # Value box with bottom showcase and plot
    with ui.value_box(
        showcase=trend_plot,  # Reference the plot directly
        theme="bg-gradient-blue-purple",
        showcase_layout="bottom",
        full_screen=True,
        height="300px",
        class_="m-2",
    ):
        "Sales Trend"
        "$890/day"
        "30-day rolling average"

    # Value box with custom theme
    with ui.value_box(
        showcase=ui.tags.i(class_="fa-solid fa-users", style="font-size: 2rem;"),
        theme=ui.value_box_theme(bg="#2c3e50", fg="#ecf0f1"),
        showcase_layout="left center",
        full_screen=True,
        height="200px",
        class_="m-2",
    ):
        "Active Users"
        "12,345"
        "Real-time count"
