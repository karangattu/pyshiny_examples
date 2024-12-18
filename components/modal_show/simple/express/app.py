from shiny import reactive
from shiny.express import input, ui, render  # Added render import

# Synthetic data for demonstration
products = {
    "Laptop": {
        "price": 1200,
        "stock": 15,
        "description": "High-performance laptop for professionals",
    },
    "Smartphone": {
        "price": 800,
        "stock": 25,
        "description": "Latest model with advanced features",
    },
    "Tablet": {
        "price": 500,
        "stock": 10,
        "description": "Lightweight and portable computing device",
    },
    "Smartwatch": {
        "price": 300,
        "stock": 20,
        "description": "Fitness and health tracking smartwatch",
    },
}

# Page options
ui.page_opts(title="Product Information Modal Demo")

# Main UI layout
with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_select("product", "Select a Product", choices=list(products.keys()))
        ui.input_action_button("show_details", "Show Product Details")

    # Render product information
    @render.text
    def product_info():
        return f"Selected Product: {input.product()}"


# Modal display effect
@reactive.effect
@reactive.event(input.show_details)
def _():
    # Get the selected product details
    product = input.product()
    details = products[product]

    # Create a modal with product information
    m = ui.modal(
        ui.tags.h3(f"{product} Details"),
        ui.tags.p(f"Description: {details['description']}"),
        ui.tags.p(f"Price: ${details['price']}"),
        ui.tags.p(f"Current Stock: {details['stock']} units"),
        title="Product Information",
        footer=ui.modal_button("Close"),
        easy_close=True,
    )

    # Show the modal
    ui.modal_show(m)
