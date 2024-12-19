from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np

# Generate some sample data
np.random.seed(123)
sales_data = pd.DataFrame(
    {
        "Product": ["Widget A", "Widget B", "Widget C", "Widget D"],
        "Revenue": np.random.randint(1000, 10000, 4),
        "Units": np.random.randint(50, 500, 4),
    }
)

# Page title
ui.page_opts(title="Card Header Demo", fillable=True)

# Create a card with header and content
with ui.card():
    ui.card_header(
        "Sales Dashboard",
        ui.h4("Q4 2023", class_="text-muted"),
        class_="d-flex justify-content-between align-items-center",
    )

    @render.data_frame
    def sales_table():
        return sales_data


# Create another card with header and interactive content
with ui.card():
    ui.card_header(
        "Product Analysis",
        ui.input_select("product", "", choices=sales_data["Product"].tolist()),
        class_="d-flex justify-content-between align-items-center",
    )

    @render.text
    def product_stats():
        if input.product():
            selected = sales_data[sales_data["Product"] == input.product()]
            return f"Revenue: ${selected['Revenue'].iloc[0]:,} | Units Sold: {selected['Units'].iloc[0]:,}"
        return "Select a product to see details"
