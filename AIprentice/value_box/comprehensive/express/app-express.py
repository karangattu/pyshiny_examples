from shiny import reactive
from shiny.express import input, ui, render
import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility
np.random.seed(123)

# Sample data generation
sales_data = np.random.normal(1000, 200, 30)
growth_rate = 15.7

# Add page options and Font Awesome CSS
ui.page_opts(title="Value Box Demo", fillable=True)
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

# First row of value boxes
with ui.layout_column_wrap(width=1 / 3):
    # Value Box 1: Monthly Sales
    with ui.value_box(
        showcase=ui.HTML(
            '<i class="fa-solid fa-chart-line" style="font-size: 2rem;"></i>'
        ),
        showcase_layout="left center",
        theme="bg-gradient-blue-purple",
        height="200px",
        id="box1",
    ):
        "Monthly Sales"
        f"${sales_data[-1]:,.2f}"
        f"↑ {growth_rate}% vs Last Month"

    # Value Box 2: Average Sales
    with ui.value_box(
        showcase=ui.HTML(
            '<i class="fa-solid fa-chart-bar" style="font-size: 2rem;"></i>'
        ),
        showcase_layout="top right",
        theme="bg-gradient-orange-red",
        height="200px",
        id="box2",
    ):
        "Average Sales"
        f"${np.mean(sales_data):,.2f}"
        "Last 30 Days"

    # Value Box 3: Sales Trend
    with ui.value_box(
        showcase=ui.output_plot("trend_plot", height="100px"),
        showcase_layout="bottom",
        theme="bg-gradient-green-teal",
        height="300px",
        full_screen=True,
        id="box3",
    ):
        "Sales Trend"
        f"${np.sum(sales_data):,.2f}"
        "Total Sales"


@render.plot
def trend_plot():
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.plot(sales_data, color="white", linewidth=2)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    return fig


# Second row of value boxes
with ui.layout_column_wrap(width=1 / 3):
    # Value Box 4: Revenue Growth
    with ui.value_box(
        showcase=ui.HTML(
            '<i class="fa-solid fa-dollar-sign" style="font-size: 2rem;"></i>'
        ),
        theme="text-purple",
        height="200px",
        id="box4",
    ):
        "Revenue Growth"
        f"{growth_rate}%"
        "Year over Year"

    # Value Box 5: Active Users
    with ui.value_box(
        showcase=ui.HTML('<i class="fa-solid fa-users" style="font-size: 2rem;"></i>'),
        theme="bg-cyan",
        height="200px",
        id="box5",
    ):
        "Active Users"
        f"{np.random.randint(1000, 5000)}"
        "Current Month"

    # Value Box 6: Achievement Score
    with ui.value_box(
        showcase=ui.HTML('<i class="fa-solid fa-trophy" style="font-size: 2rem;"></i>'),
        theme="bg-yellow",
        height="200px",
        id="box6",
    ):
        "Achievement Score"
        f"{np.random.randint(85, 100)}%"
        "Performance Index"
