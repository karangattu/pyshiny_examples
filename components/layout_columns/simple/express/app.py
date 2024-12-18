import numpy as np
import pandas as pd
from shiny import reactive
from shiny.express import input, ui, render
from matplotlib import pyplot as plt

# Sample data generation
sales_data = pd.DataFrame(
    {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Revenue": np.random.randint(10000, 50000, 6),
        "Expenses": np.random.randint(5000, 20000, 6),
        "Customers": np.random.randint(100, 500, 6),
    }
)

ui.page_opts(title="Business Dashboard", fillable=True)

with ui.layout_columns(col_widths=[6, 6]):
    # First column
    with ui.card():
        ui.card_header("Revenue vs Expenses")

        @render.plot
        def revenue_plot():
            fig, ax = plt.subplots()
            ax.bar(
                sales_data["Month"], sales_data["Revenue"], label="Revenue", alpha=0.7
            )
            ax.bar(
                sales_data["Month"], sales_data["Expenses"], label="Expenses", alpha=0.7
            )
            ax.legend()
            ax.set_ylabel("Amount ($)")
            return fig

    # Second column
    with ui.card():
        ui.card_header("Monthly Customer Count")

        @render.plot
        def customer_plot():
            fig, ax = plt.subplots()
            ax.plot(sales_data["Month"], sales_data["Customers"], marker="o")
            ax.set_ylabel("Number of Customers")
            return fig


# Bottom row using full width
with ui.layout_columns(col_widths=[12]):
    with ui.card():
        ui.card_header("Sales Data Table")

        @render.data_frame
        def sales_table():
            return render.DataGrid(sales_data)
