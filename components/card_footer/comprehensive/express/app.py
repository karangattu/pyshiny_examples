import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
dates = pd.date_range(
    start=datetime.now() - timedelta(days=30), end=datetime.now(), freq="D"
)
sales_data = pd.DataFrame(
    {
        "date": dates,
        "revenue": np.random.randint(1000, 5000, len(dates)),
        "customers": np.random.randint(50, 300, len(dates)),
        "product_category": np.random.choice(
            ["Electronics", "Clothing", "Home Goods", "Books"], len(dates)
        ),
    }
)

ui.page_opts(title="Card Footer Showcase", fillable=True)

# Add head content for custom CSS
ui.head_content(
    ui.tags.style(
        """
    .card-footer {
        background-color: rgba(0, 0, 0, 0.05);
        border-top: 1px solid rgba(0, 0, 0, 0.1);
    }
    """
    )
)

with ui.layout_column_wrap(width=1 / 2):
    # Basic Card Footer
    with ui.card():
        ui.card_header("Basic Card Footer")
        ui.p("This is a simple card with a basic footer.")

        with ui.card_footer():
            "This is a basic card footer"

    # Card Footer with HTML
    with ui.card():
        ui.card_header("Card Footer with HTML")
        ui.p("This card demonstrates using HTML in the footer.")

        with ui.card_footer():
            ui.tags.span("Footer with ", ui.tags.strong("bold text"))

    # Card Footer with Multiple Elements
    with ui.card():
        ui.card_header("Card Footer with Multiple Elements")
        ui.p("This card shows multiple elements in the footer.")

        with ui.card_footer():
            ui.input_action_button("btn1", "Action Button")
            ui.tags.span("Additional text in footer")

    # Card Footer with Styling
    with ui.card():
        ui.card_header("Card Footer with Styling")
        ui.p("This card demonstrates styling the footer.")

        with ui.card_footer(class_="bg-light text-dark"):
            "Styled footer with light background"

    # Card Footer with Reactive Content
    with ui.card():
        ui.card_header("Card Footer with Reactive Content")
        ui.input_slider("days", "Select Days", min=1, max=30, value=7)

        @render.data_frame
        def filtered_sales():
            days = input.days()
            return sales_data.head(days)

        with ui.card_footer():

            @render.text
            def footer_stats():
                days = input.days()
                total_revenue = sales_data.head(days)["revenue"].sum()
                return f"Total Revenue for {days} days: ${total_revenue:,.2f}"

    # Card Footer with Plot
    with ui.card():
        ui.card_header("Card Footer with Plot")

        @render.plot
        def sales_plot():
            plt.figure(figsize=(10, 4))
            sales_data.groupby("product_category")["revenue"].sum().plot(kind="bar")
            plt.title("Revenue by Product Category")
            plt.tight_layout()

        with ui.card_footer():

            @render.text
            def category_summary():
                top_category = (
                    sales_data.groupby("product_category")["revenue"].sum().idxmax()
                )
                return f"Top Performing Category: {top_category}"
