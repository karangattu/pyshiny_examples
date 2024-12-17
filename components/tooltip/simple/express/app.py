from shiny import reactive
from shiny.express import input, ui

# Synthetic dataset for demonstration
products = {
    "Laptop": {
        "price": "$999",
        "description": "High-performance laptop with latest processor",
    },
    "Smartphone": {
        "price": "$599",
        "description": "Advanced smartphone with multiple camera lenses",
    },
    "Tablet": {
        "price": "$399",
        "description": "Lightweight tablet for productivity and entertainment",
    },
}

# Page title and setup
ui.page_opts(title="Product Showcase with Tooltips")

# Main layout
with ui.layout_column_wrap(width=1 / 3):
    for product, details in products.items():
        with ui.card():
            # Card with tooltip
            with ui.tooltip(placement="right"):
                ui.tags.h3(product)
                f"Price: {details['price']}"
                f"Description: {details['description']}"

            # Visible card content
            ui.tags.h3(product)
            ui.tags.p(f"Price: {details['price']}")
            ui.input_action_button(f"btn_{product}", "Learn More")


# Reactive effect to show notification when "Learn More" is clicked
@reactive.effect
def _():
    for product in products.keys():

        @reactive.event(getattr(input, f"btn_{product}"))
        def show_product_details():
            ui.notification_show(
                f"You clicked Learn More for {product}!", duration=3, type="message"
            )
