from shiny import reactive
from shiny.express import input, ui

# Synthetic data for demonstration
products = {
    "Laptop": {
        "price": 1200,
        "stock": 50,
        "description": "High-performance laptop for professionals",
    },
    "Smartphone": {
        "price": 800,
        "stock": 75,
        "description": "Latest model with advanced features",
    },
    "Tablet": {
        "price": 500,
        "stock": 30,
        "description": "Lightweight and portable computing device",
    },
}

ui.page_opts(title="Product Information Modal")

# Action button to trigger modal
ui.input_action_button("show_modal", "View Product Details")


# Reactive effect to show modal when button is clicked
@reactive.effect
@reactive.event(input.show_modal)
def _():
    # Create a modal with product information
    m = ui.modal(
        ui.p(f"Product: Laptop"),
        ui.p(f"Price: ${products['Laptop']['price']}"),
        ui.p(f"Stock: {products['Laptop']['stock']} units"),
        ui.p(f"Description: {products['Laptop']['description']}"),
        title="Product Details",
        footer=ui.modal_button("Close"),
        easy_close=True,
    )
    ui.modal_show(m)
