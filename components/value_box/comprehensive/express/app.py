import random
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from shiny import reactive
from shiny.express import input, ui, render


# Synthetic data generation
def generate_kpi_data():
    return {
        "revenue": round(random.uniform(500000, 2000000), 2),
        "customers": random.randint(1000, 50000),
        "growth_rate": round(random.uniform(-10, 30), 2),
        "satisfaction": round(random.uniform(60, 95), 2),
    }


# Icons using Font Awesome
revenue_icon = ui.HTML('<i class="fa-solid fa-chart-line" style="color: #007bff;"></i>')
customers_icon = ui.HTML('<i class="fa-solid fa-users" style="color: #28a745;"></i>')
growth_icon = ui.HTML(
    '<i class="fa-solid fa-arrow-trend-up" style="color: #dc3545;"></i>'
)
satisfaction_icon = ui.HTML('<i class="fa-solid fa-smile" style="color: #ffc107;"></i>')

# Add Font Awesome CSS
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.0/css/all.min.css">'
    )
)

# Page setup
ui.page_opts(title="Value Box Showcase", fillable=True)

# Sidebar for configuration
with ui.sidebar():
    ui.input_select(
        "showcase_layout",
        "Showcase Layout",
        choices=["left center", "top right", "bottom"],
        selected="left center",  # Add a default selected value
    )
    ui.input_select(
        "theme",
        "Theme",
        choices=[
            "primary",
            "secondary",
            "success",
            "danger",
            "warning",
            "info",
            "light",
            "dark",
            "bg-gradient-blue-purple",
            "bg-green",
            "text-red",
        ],
        selected="primary",  # Add a default selected value
    )
    ui.input_switch("full_screen", "Full Screen", value=False)

# Reactive value for KPI data
kpi_data = reactive.value(generate_kpi_data())


# Update KPI data periodically
@reactive.effect
def _():
    reactive.invalidate_later(5)  # Update every 5 seconds
    kpi_data.set(generate_kpi_data())


# Plots for showcasing
def create_trend_plot(data, color="blue"):
    plt.figure(figsize=(5, 3))
    x = np.linspace(0, 10, 50)
    y = data + np.random.normal(0, 0.5, 50)
    plt.plot(x, y, color=color)
    plt.title("Trend")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.tight_layout()
    return plt.gcf()


# Value Boxes Layout
with ui.layout_columns():
    # Revenue Value Box
    with ui.value_box(
        showcase=revenue_icon,
        showcase_layout="left center",  # Use a static value instead of input
        theme="primary",  # Use a static value instead of input
        full_screen=False,  # Use a static value instead of input
    ):
        "Total Revenue"
        f"${kpi_data().get('revenue'):,.2f}"
        "Last 30 Days"

    # Customer Value Box with Plot Showcase
    with ui.value_box(
        showcase=lambda: create_trend_plot(kpi_data().get("customers"), color="green"),
        showcase_layout="left center",  # Use a static value instead of input
        theme="success",  # Use a static value instead of input
        full_screen=False,  # Use a static value instead of input
    ):
        "Total Customers"
        f"{kpi_data().get('customers'):,}"
        "Active Users"

    # Growth Rate Value Box
    with ui.value_box(
        showcase=growth_icon,
        showcase_layout="left center",  # Use a static value instead of input
        theme="danger",  # Use a static value instead of input
        full_screen=False,  # Use a static value instead of input
    ):
        "Growth Rate"
        f"{kpi_data().get('growth_rate')}%"
        "Compared to Last Quarter"

    # Satisfaction Value Box
    with ui.value_box(
        showcase=satisfaction_icon,
        showcase_layout="left center",  # Use a static value instead of input
        theme="warning",  # Use a static value instead of input
        full_screen=False,  # Use a static value instead of input
    ):
        "Customer Satisfaction"
        f"{kpi_data().get('satisfaction')}%"
        "Net Promoter Score"


# Reactive updates for value boxes
@reactive.effect
def update_value_boxes():
    # This effect will update the value boxes when sidebar inputs change
    layout = input.showcase_layout()
    theme = input.theme()
    full_screen = input.full_screen()

    # Note: In current Shiny for Python, dynamically updating value box properties
    # is not directly supported. The effect here is more for demonstration.
