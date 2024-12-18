from shiny import reactive
from shiny.express import input, ui, render
from datetime import datetime
import random
import pandas as pd

# Set page options
ui.page_opts(title="Tooltip Showcase", fillable=True)

# Add Font Awesome CSS
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.0/css/all.min.css">'
    )
)


# Create some synthetic data
def generate_product_data():
    products = [
        "Laptop",
        "Smartphone",
        "Tablet",
        "Smartwatch",
        "Wireless Earbuds",
        "External SSD",
        "Gaming Console",
    ]
    return pd.DataFrame(
        {
            "Product": products,
            "Price": [round(random.uniform(500, 2000), 2) for _ in products],
            "Stock": [random.randint(10, 100) for _ in products],
            "Rating": [round(random.uniform(3.5, 5.0), 1) for _ in products],
        }
    )


# Sidebar with various tooltip configuration options
with ui.sidebar():
    ui.input_select(
        "placement",
        "Tooltip Placement",
        ["auto", "top", "right", "bottom", "left"],
        selected="auto",
    )

    ui.input_checkbox("show_icon", "Show Icon", value=True)

    ui.input_text("custom_title", "Custom Tooltip Title", placeholder="Optional title")

    ui.input_selectize(
        "options",
        "Tooltip Options",
        {"delay": "Delay", "trigger": "Trigger", "custom": "Custom option"},
        multiple=True,
    )

# Main content area with tooltips
with ui.layout_columns():
    # Tooltip with basic configuration
    with ui.card():
        ui.card_header("Basic Tooltip")

        # Modify tooltip to use a more explicit configuration
        with ui.tooltip(id="basic_tooltip"):

            @render.ui
            def info_button():
                return ui.input_action_button(
                    "info_btn",
                    "Hover for Info" if input.show_icon() else "Info Button",
                    icon=(
                        ui.tags.i(class_="fa-solid fa-info-circle")
                        if input.show_icon()
                        else None
                    ),
                )

            # Dynamic tooltip content
            ui.markdown(
                f"**Tooltip Information**\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )

    # Tooltip with data grid
    with ui.card():
        ui.card_header("Data Grid with Tooltips")

        # Generate initial product data
        product_data = generate_product_data()

        @render.data_frame
        def product_grid():
            return render.DataGrid(product_data, selection_mode="row")

        # Tooltip for selected row details
        with ui.tooltip(id="row_tooltip"):

            @render.ui
            def selected_product_info():
                # Get selected row indices
                selected = input.product_grid_selected_rows()

                if not selected:
                    return "Select a row to see details"

                # Get the selected product details
                product = product_data.iloc[selected[0]]

                return ui.markdown(
                    f"""
                **Product Details**
                - Name: {product['Product']}
                - Price: ${product['Price']:.2f}
                - Stock: {product['Stock']}
                - Rating: {product['Rating']}
                """
                )


# Render a text output to show current tooltip configuration
@render.text
def tooltip_config():
    return f"""
    Current Tooltip Configuration:
    - Placement: {input.placement()}
    - Show Icon: {input.show_icon()}
    - Custom Title: {input.custom_title() or 'Default'}
    - Additional Options: {input.options() or 'None'}
    """


# Optional: Add some custom CSS for styling
ui.include_css(
    """
    .tooltip {{ 
        max-width: 250px; 
        font-size: 0.9rem; 
    }}
"""
)
