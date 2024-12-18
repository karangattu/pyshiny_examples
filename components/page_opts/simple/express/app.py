from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create synthetic data with consistent array lengths
np.random.seed(42)

# Ensure all arrays have the same length (25 elements)
regions = ["North", "South", "East", "West", "Central"] * 5
products = ["Electronics", "Clothing", "Furniture", "Groceries", "Appliances"] * 5
sales = np.random.randint(1000, 10000, 25)
profits = np.random.uniform(0.1, 0.5, 25)

sales_data = pd.DataFrame(
    {"Region": regions, "Product": products, "Sales": sales, "Profit": profits}
)

# Set page options with a title, window title, and language
ui.page_opts(
    title="Sales Dashboard",  # Page title shown in the app
    window_title="Company Sales Analytics",  # Browser window title
    lang="en",  # Language set to English
    fillable=True,  # Make the page fillable
)

# Sidebar for user interactions
with ui.sidebar():
    ui.input_select(
        "region", "Select Region", choices=sales_data["Region"].unique().tolist()
    )
    ui.input_select(
        "product", "Select Product", choices=sales_data["Product"].unique().tolist()
    )

# Main content layout
with ui.layout_columns():

    @render.plot
    def sales_plot():
        # Filter data based on user selection
        filtered_data = sales_data[
            (sales_data["Region"] == input.region())
            & (sales_data["Product"] == input.product())
        ]

        plt.figure(figsize=(8, 4))
        plt.bar(filtered_data["Region"], filtered_data["Sales"])
        plt.title(f"Sales for {input.product()} in {input.region()}")
        plt.xlabel("Region")
        plt.ylabel("Sales Amount")
        return plt.gcf()

    @render.table
    def sales_table():
        filtered_data = sales_data[
            (sales_data["Region"] == input.region())
            & (sales_data["Product"] == input.product())
        ]
        return filtered_data[["Region", "Product", "Sales", "Profit"]]
