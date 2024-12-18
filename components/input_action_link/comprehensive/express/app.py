from shiny import reactive
from shiny.express import input, ui, render
import random
import pandas as pd
from datetime import datetime, timedelta


# Generate synthetic data
def generate_transactions():
    """Create a synthetic dataset of financial transactions."""
    num_transactions = 50
    transaction_types = ["Deposit", "Withdrawal", "Transfer", "Payment"]
    accounts = ["Checking", "Savings", "Credit Card", "Investment"]

    data = {
        "Date": [
            datetime.now() - timedelta(days=random.randint(1, 30))
            for _ in range(num_transactions)
        ],
        "Type": [random.choice(transaction_types) for _ in range(num_transactions)],
        "Account": [random.choice(accounts) for _ in range(num_transactions)],
        "Amount": [round(random.uniform(10, 1000), 2) for _ in range(num_transactions)],
    }

    return pd.DataFrame(data)


# Global variable to store transactions
transactions_df = generate_transactions()

# Page setup with full width and title
ui.page_opts(title="Input Action Link Showcase", full_width=True)

# Sidebar with various action links
with ui.sidebar():
    # Basic action link
    ui.input_action_link("basic_link", "Basic Action Link")

    # Action link with icon
    ui.input_action_link(
        "icon_link",
        "Link with Icon",
        icon=ui.tags.i(class_="fa-solid fa-chart-simple", style="font-size: 1rem;"),
    )

    # Action link with custom attributes
    ui.input_action_link(
        "custom_link",
        "Custom Styled Link",
        class_="text-primary",
        style="font-weight: bold;",
    )

    # Action link with multiple clicks tracking
    ui.input_action_link(
        "multi_click_link", "Multi-Click Tracker", class_="text-success"
    )

# Main content area
with ui.layout_columns():
    # Card to show basic link interactions
    with ui.card():
        ui.card_header("Basic Link Interactions")

        @render.text
        def basic_link_output():
            return f"Basic Link Clicked: {input.basic_link()} times"

    # Card to show icon link interactions
    with ui.card():
        ui.card_header("Icon Link Interactions")

        @render.text
        def icon_link_output():
            return f"Icon Link Clicked: {input.icon_link()} times"

    # Card to show custom link interactions
    with ui.card():
        ui.card_header("Custom Link Interactions")

        @render.text
        def custom_link_output():
            return f"Custom Link Clicked: {input.custom_link()} times"

    # Card to show multi-click tracking
    with ui.card():
        ui.card_header("Multi-Click Tracking")

        @render.text
        def multi_click_output():
            clicks = input.multi_click_link()
            return f"Multi-Click Link Pressed: {clicks} times"


# Reactive effects for different link interactions
@reactive.effect
@reactive.event(input.basic_link)
def _():
    ui.notification_show(
        f"Basic Link Clicked {input.basic_link()} times!", duration=2, type="message"
    )


@reactive.effect
@reactive.event(input.icon_link)
def _():
    ui.notification_show(
        f"Icon Link Clicked {input.icon_link()} times!", duration=2, type="success"
    )


@reactive.effect
@reactive.event(input.custom_link)
def _():
    ui.notification_show(
        f"Custom Link Clicked {input.custom_link()} times!", duration=2, type="warning"
    )


@reactive.effect
@reactive.event(input.multi_click_link)
def _():
    ui.notification_show(
        f"Multi-Click Link Pressed {input.multi_click_link()} times!",
        duration=2,
        type="message",
    )
