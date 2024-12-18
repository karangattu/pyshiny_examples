from shiny import reactive
from shiny.express import input, ui

# Synthetic data for product information
products = {
    "Laptop": {
        "price": "$999",
        "specs": "Intel Core i7, 16GB RAM, 512GB SSD",
        "rating": "4.5/5 stars",
    },
    "Smartphone": {
        "price": "$799",
        "specs": '6.1" Display, A15 Bionic Chip, 128GB Storage',
        "rating": "4.7/5 stars",
    },
    "Wireless_Earbuds": {
        "price": "$199",
        "specs": "Noise Cancellation, 8-hour Battery Life, Water Resistant",
        "rating": "4.3/5 stars",
    },
}

# Page setup
ui.page_opts(title="Product Information Popovers")

# Main layout with product cards
with ui.layout_column_wrap(width=1 / 3):
    for product, details in products.items():
        with ui.card():
            with ui.popover(placement="right", id=f"popover_{product}"):
                # Use product name with underscores for ID
                ui.input_action_button(f"btn_{product}", product.replace("_", " "))

                # Popover content with product details
                ui.h4(f"{product.replace('_', ' ')} Details")
                ui.p(f"Price: {details['price']}")
                ui.p(f"Specifications: {details['specs']}")
                ui.p(f"Customer Rating: {details['rating']}")


# Render text to show which product was last clicked
@reactive.effect
@reactive.event(input.btn_Laptop, input.btn_Smartphone, input.btn_Wireless_Earbuds)
def _():
    # Determine which button was clicked
    if input.btn_Laptop():
        clicked_product = "Laptop"
    elif input.btn_Smartphone():
        clicked_product = "Smartphone"
    elif input.btn_Wireless_Earbuds():
        clicked_product = "Wireless Earbuds"
    else:
        return  # Exit if no button was clicked

    # Show notification with the clicked product name
    ui.notification_show(f"You clicked on the {clicked_product} popover!", duration=3)
