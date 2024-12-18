from shiny import reactive
from shiny.express import input, ui, render
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Synthetic data generation
np.random.seed(42)
products = [
    "Laptop",
    "Smartphone",
    "Tablet",
    "Smartwatch",
    "Wireless Earbuds",
    "Gaming Console",
    "Camera",
]
sales_data = pd.DataFrame(
    {
        "Product": products,
        "Sales": np.random.randint(100, 1000, len(products)),
        "Profit Margin": np.random.uniform(10, 50, len(products)).round(2),
    }
)

# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# Page setup
ui.page_opts(title="Popover Showcase", fillable=True)

# Sidebar with popover configuration inputs
with ui.sidebar():
    ui.input_select(
        "placement",
        "Popover Placement",
        ["auto", "top", "right", "bottom", "left"],
        selected="auto",  # Add a default value
    )

    ui.input_checkbox_group(
        "options",
        "Popover Options",
        {
            "trigger": "Click Trigger",
            "hover": "Hover Trigger",
            "focus": "Focus Trigger",
        },
    )

    ui.input_switch("custom_content", "Custom Content")

# Main content with various popover demonstrations
with ui.layout_columns():
    # Product Sales Popover
    with ui.card():
        # Determine trigger based on selected options
        @reactive.calc
        def get_trigger():
            if "trigger" in input.options():
                return "click"
            elif "hover" in input.options():
                return "hover"
            elif "focus" in input.options():
                return "focus"
            return "click"  # Default trigger

        with ui.popover(
            id="sales_popover",
            placement=input.placement,  # Use input directly
            options={"trigger": get_trigger()},
        ):
            ui.input_action_button("product_btn", "Product Sales")

            @render.ui
            def sales_content():
                if input.custom_content():
                    return ui.div(
                        ui.markdown("### 🚀 **Detailed Sales Report**"),
                        ui.tags.ul(
                            ui.tags.li("Comprehensive sales analysis"),
                            ui.tags.li("Profit margin insights"),
                            ui.tags.li("Trend visualization"),
                        ),
                    )
                else:
                    return render.table(sales_data)

    # Profit Margin Popover
    with ui.card():
        with ui.popover(
            id="profit_popover",
            placement=input.placement,  # Use input directly
            options={"trigger": get_trigger()},
        ):
            ui.input_action_button("profit_btn", "Profit Margins")

            @render.ui
            def profit_content():
                if input.custom_content():
                    return ui.div(
                        ui.markdown("### 💰 **Profit Margin Details**"),
                        ui.tags.ul(
                            ui.tags.li("Margin calculation methodology"),
                            ui.tags.li("Comparative analysis"),
                            ui.tags.li("Strategic insights"),
                        ),
                    )
                else:
                    # Create plot function
                    plt.figure(figsize=(8, 4))
                    plt.bar(sales_data["Product"], sales_data["Profit Margin"])
                    plt.title("Product Profit Margins")
                    plt.xlabel("Product")
                    plt.ylabel("Profit Margin (%)")
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    return render.plot(plt.gcf())


# Optional: Add a notification when popover is triggered
@reactive.effect
@reactive.event(input.product_btn)
def _():
    ui.notification_show("Product Sales popover triggered!", duration=2, type="message")


@reactive.effect
@reactive.event(input.profit_btn)
def _():
    ui.notification_show(
        "Profit Margins popover triggered!", duration=2, type="message"
    )
