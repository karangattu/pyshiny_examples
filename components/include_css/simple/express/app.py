from pathlib import Path
from shiny import reactive
from shiny.express import input, ui, render

# Create a custom CSS string to demonstrate include_css
custom_css = """
body {
    background-color: #f0f0f0;
}

.custom-card {
    border: 2px solid #4a4a4a;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    margin-bottom: 15px;
}

.highlight {
    color: #007bff;
    font-weight: bold;
}

.data-table {
    background-color: #ffffff;
    border-collapse: collapse;
    width: 100%;
}

.data-table th {
    background-color: #4a4a4a;
    color: white;
    padding: 10px;
}

.data-table td {
    border: 1px solid #ddd;
    padding: 8px;
}

.data-table tr:nth-child(even) {
    background-color: #f2f2f2;
}
"""

# Instead of trying to read from a file, write the CSS to a file
css_file = Path(__file__).resolve().parent / "custom_styles.css"
css_file.write_text(custom_css)

# Include the custom CSS
ui.include_css(css_file, method="link")

# Create a synthetic dataset
import pandas as pd
import numpy as np

# Generate random product sales data
np.random.seed(42)
products = ["Laptop", "Smartphone", "Tablet", "Smartwatch", "Headphones"]
sales_data = pd.DataFrame(
    {
        "Product": products,
        "Sales": np.random.randint(100, 1000, size=len(products)),
        "Revenue": np.random.uniform(50000, 500000, size=len(products)).round(2),
    }
)

# App UI and logic
ui.page_opts(title="CSS Styling Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_select("product_select", "Select Product", choices=products)

    # Main content area
    with ui.card(class_="custom-card"):

        @render.table
        def product_table():
            # Filter the table based on selected product
            filtered_df = sales_data[sales_data["Product"] == input.product_select()]
            return filtered_df

        @render.ui
        def product_summary():
            selected_product = input.product_select()
            product_info = sales_data[sales_data["Product"] == selected_product].iloc[0]

            return ui.tags.div(
                ui.tags.h3(
                    f"Product Details for {selected_product}", class_="highlight"
                ),
                ui.tags.p(f"Total Sales: {product_info['Sales']}"),
                ui.tags.p(f"Total Revenue: ${product_info['Revenue']:,.2f}"),
            )
