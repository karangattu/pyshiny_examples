from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
categories = ["Electronics", "Clothing", "Books", "Home & Garden", "Sports"]
sales_data = pd.DataFrame(
    {
        "Category": categories,
        "Sales": np.random.randint(50000, 500000, len(categories)),
        "Profit Margin": np.random.uniform(0.1, 0.5, len(categories)),
        "Customer Satisfaction": np.random.uniform(3.5, 5.0, len(categories)),
    }
)

# Add some description for each category
category_descriptions = {
    "Electronics": "Cutting-edge technology and gadgets for modern living.",
    "Clothing": "Trendy and comfortable fashion for all ages and styles.",
    "Books": "A vast collection of literature, from classics to contemporary reads.",
    "Home & Garden": "Everything to make your living space comfortable and beautiful.",
    "Sports": "High-quality equipment and gear for athletes and enthusiasts.",
}

# Page setup with full options
ui.page_opts(title="NavSet Pill Showcase", fillable=True)

# Create NavSet with multiple parameters
with ui.navset_pill(
    id="category_nav",  # Enables tracking of selected nav item
    selected="Electronics",  # Default selected item
    header=ui.tags.h3("Product Category Analysis"),  # Optional header
    footer=ui.tags.p("Data updated in real-time"),  # Optional footer
):
    # Create nav panels for each category
    for category in categories:
        with ui.nav_panel(category, value=category):
            with ui.layout_columns():
                # Sales Card
                with ui.card():
                    ui.card_header("Sales Performance")

                    @render.text
                    def sales_text():
                        sales = sales_data[sales_data["Category"] == category][
                            "Sales"
                        ].values[0]
                        return f"Total Sales: ${sales:,}"

                # Profit Margin Card
                with ui.card():
                    ui.card_header("Profit Margin")

                    @render.text
                    def profit_text():
                        profit = sales_data[sales_data["Category"] == category][
                            "Profit Margin"
                        ].values[0]
                        return f"Profit Margin: {profit:.2%}"

                # Customer Satisfaction Card
                with ui.card():
                    ui.card_header("Customer Satisfaction")

                    @render.text
                    def satisfaction_text():
                        satisfaction = sales_data[sales_data["Category"] == category][
                            "Customer Satisfaction"
                        ].values[0]
                        return f"Rating: {satisfaction:.2f}/5.0"

            # Category Description
            ui.markdown(f"### About {category}")
            ui.markdown(f"*{category_descriptions[category]}*")

            # Visualization
            @render.plot
            def category_plot():
                plt.figure(figsize=(8, 4))
                category_data = sales_data[sales_data["Category"] == category]
                plt.bar(
                    ["Sales", "Profit Margin", "Customer Satisfaction"],
                    [
                        category_data["Sales"].values[0] / 10000,
                        category_data["Profit Margin"].values[0] * 100,
                        category_data["Customer Satisfaction"].values[0] * 20,
                    ],
                )
                plt.title(f"{category} Performance Metrics")
                plt.ylabel("Scaled Value")
                return plt.gcf()


# Show selected nav item
ui.hr()
ui.h4("Current Selection:")


@render.text
def selected_nav():
    return f"Selected Category: {input.category_nav()}"
