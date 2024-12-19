from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np


# Sample data generation
def generate_sales_data():
    np.random.seed(123)
    dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
    sales = np.random.randint(100, 1000, size=len(dates))
    products = np.random.choice(["Laptop", "Phone", "Tablet", "Watch"], size=len(dates))

    return pd.DataFrame({"date": dates, "sales": sales, "product": products})


sales_data = generate_sales_data()

# Page title and options
ui.page_opts(title="Sales Dashboard with Accordions", fillable=True)

# Create accordion sections
with ui.accordion(id="sales_accordion", open=True):

    with ui.accordion_panel("Overview", value="panel1"):
        ui.h4("Sales Summary")

        @render.data_frame
        def summary_stats():
            summary = (
                sales_data.groupby("product")["sales"]
                .agg(["mean", "min", "max"])
                .round(2)
            )
            summary.columns = ["Average Sales", "Minimum Sales", "Maximum Sales"]
            return summary

    with ui.accordion_panel("Product Details", value="panel2"):
        ui.input_selectize(
            "product_select",
            "Select Product",
            choices=list(sales_data["product"].unique()),
            multiple=False,
        )

        @render.table
        def product_details():
            filtered = sales_data[sales_data["product"] == input.product_select()]
            return filtered.head(10)

    with ui.accordion_panel("Data Filters", value="panel3"):
        with ui.layout_column_wrap(
            width=1 / 3
        ):  # This divides space into 3 equal columns
            ui.input_numeric("min_sales", "Minimum Sales", value=100)
            ui.input_numeric("max_sales", "Maximum Sales", value=1000)
            ui.input_action_button("apply_filter", "Apply Filter", class_="btn-primary")

        @render.table
        @reactive.event(input.apply_filter)
        def filtered_data():
            filtered = sales_data[
                (sales_data["sales"] >= input.min_sales())
                & (sales_data["sales"] <= input.max_sales())
            ]
            return filtered.head(10)


# Show which panel is currently selected
@render.text
def current_panel():
    return f"Currently selected panel: {input.sales_accordion()}"
