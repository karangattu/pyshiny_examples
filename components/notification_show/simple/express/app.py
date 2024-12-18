import random
import pandas as pd
from shiny import reactive
from shiny.express import input, ui, render


# Generate synthetic product sales data
def generate_sales_data():
    products = ["Laptop", "Smartphone", "Tablet", "Smartwatch", "Headphones"]
    return pd.DataFrame(
        {
            "Product": products,
            "Sales": [random.randint(100, 1000) for _ in range(len(products))],
            "Revenue": [random.randint(5000, 50000) for _ in range(len(products))],
        }
    )


# Create the sales dataset
sales_df = generate_sales_data()

# App UI and Functionality
ui.page_opts(title="Notification Showcase")

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_select(
            "notification_type",
            "Notification Type",
            ["default", "message", "warning", "error"],
        )
        ui.input_slider(
            "duration", "Notification Duration (seconds)", min=1, max=10, value=5
        )
        ui.input_action_button("show_notification", "Show Notification")
        ui.input_action_button("random_sales", "Regenerate Sales Data")

    with ui.card():
        ui.card_header("Product Sales Data")

        @render.data_frame
        def sales_table():
            return sales_df


# Notification functionality
@reactive.effect
@reactive.event(input.show_notification)
def _():
    # Create a custom notification message based on the selected type
    message = f"This is a {input.notification_type()} type notification!"

    ui.notification_show(
        message, duration=input.duration(), type=input.notification_type()
    )


# Random data regeneration functionality
@reactive.effect
@reactive.event(input.random_sales)
def _():
    global sales_df
    sales_df = generate_sales_data()

    # Show a message when data is regenerated
    ui.notification_show("Sales data has been regenerated!", duration=3, type="message")
