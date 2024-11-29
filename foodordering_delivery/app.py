from datetime import datetime
from typing import Dict, List, Optional, Tuple

import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, ui
from shiny.reactive import Value

# Sample menu data
menu_data: List[Dict] = [
    {"id": 1, "name": "Pizza Margherita", "category": "Pizza", "price": 12.99},
    {"id": 2, "name": "Pasta Carbonara", "category": "Pasta", "price": 10.99},
    {"id": 3, "name": "Caesar Salad", "category": "Salad", "price": 7.99},
    {"id": 4, "name": "Pepperoni Pizza", "category": "Pizza", "price": 14.99},
    {"id": 5, "name": "Spaghetti Aglio e Olio", "category": "Pasta", "price": 9.99},
    {"id": 6, "name": "Greek Salad", "category": "Salad", "price": 8.99},
    {"id": 7, "name": "Tiramisu", "category": "Dessert", "price": 6.99},
    {"id": 8, "name": "Cannoli", "category": "Dessert", "price": 5.99},
    {"id": 9, "name": "Garlic Bread", "category": "Appetizer", "price": 4.99},
    {"id": 10, "name": "Mozzarella Sticks", "category": "Appetizer", "price": 6.99},
]

# Order Statistics
order_stats: Dict[str, int | float] = {
    "num_orders": 0,
    "total_revenue": 0.0,
    "avg_order_value": 0.0,
}

# UI definition
app_ui = ui.page_fluid(
    ui.panel_title("Delicious Delights Restaurant"),
    ui.head_content(
        ui.HTML(
            """
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
            <style>
                .card-title {
                    font-size: 1.2em;
                    font-weight: bold;
                    margin-bottom: 0.5em;
                }
                .cart-item {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 0.5em;
                    border-bottom: 1px solid #eee;
                }
                .cart-item-name {
                    flex-grow: 1;
                }
                .cart-item-price {
                    width: 60px;
                    text-align: right;
                }
                .remove-item {
                    color: #dc3545;
                    cursor: pointer;
                    margin-left: 0.5em;
                }
                .order-container {
                    margin-top: 1em;
                    text-align: center;
                }
            </style>
            """
        )
    ),
    ui.layout_sidebar(
        ui.sidebar(
            ui.card(
                ui.card_header("Order Summary"),
                ui.layout_column_wrap(
                    ui.value_box(
                        "Orders",
                        ui.output_text("num_orders"),
                        theme="bg-primary text-white",
                        showcase=ui.HTML('<i class="fa fa-shopping-cart"></i>'),
                    ),
                    ui.value_box(
                        "Total Revenue",
                        ui.output_text("total_revenue"),
                        theme="bg-success text-white",
                        showcase=ui.HTML('<i class="fa fa-dollar-sign"></i>'),
                    ),
                    ui.value_box(
                        "Average Order",
                        ui.output_text("avg_order_value"),
                        theme="bg-info text-white",
                        showcase=ui.HTML('<i class="fa fa-average"></i>'),
                    ),
                    width=1,
                ),
            ),
            ui.card(
                ui.card_header("Delivery Information"),
                ui.input_text("delivery_address", "Delivery Address"),
                ui.input_date("delivery_date", "Delivery Date", value=datetime.today()),
                ui.input_action_button(
                    "place_order", "Place Order", class_="btn-success w-100"
                ),
            ),
        ),
        ui.div(
            ui.layout_column_wrap(
                ui.card(
                    ui.card_header("Menu"),
                    ui.column(
                        12,
                        ui.input_select(
                            "category_filter",
                            "Filter by Category",
                            ["All"]
                            + sorted(list(set(item["category"] for item in menu_data))),
                        ),
                    ),
                    ui.column(
                        12,
                        ui.output_ui("menu_items"),
                    ),
                ),
                ui.card(
                    ui.card_header("Cart"),
                    ui.output_ui("cart_items"),
                ),
            ),
        ),
    ),
)


# Server logic
def server(input: Inputs, output: Outputs, session: Session):
    # Reactive Values
    cart: Value[Dict[int, Tuple[str, float, int]]] = Value({})
    order_stats_reactive = Value(order_stats.copy())

    # Update Menu Items based on category
    @render.ui
    def menu_items():
        category = input.category_filter()
        filtered_menu = [
            item
            for item in menu_data
            if category == "All" or item["category"] == category
        ]
        return ui.div(
            *[
                ui.div(
                    ui.div(
                        f"{item['name']} - ${item['price']:.2f}",
                        style="font-weight: bold;",
                    ),
                    ui.div(
                        ui.input_action_button(
                            f"add_to_cart_{item['id']}",  # Unique ID
                            "Add to Cart",
                            class_="btn-primary btn-sm",
                        ),
                    ),
                    style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5em;",
                )
                for item in filtered_menu
            ]
        )

    # New improved add to cart logic
    for item in menu_data:

        @reactive.effect
        @reactive.event(input[f"add_to_cart_{item['id']}"])
        def _():
            current_cart = cart.get()
            if item["id"] in current_cart:
                name, price, quantity = current_cart[item["id"]]
                current_cart[item["id"]] = (name, price, quantity + 1)
            else:
                current_cart[item["id"]] = (item["name"], item["price"], 1)
            cart.set(current_cart)

    # Remove from cart logic
    @reactive.effect
    def _remove_from_cart():
        current_cart = cart.get()
        for item in menu_data:
            if (
                f"remove_item_{item['id']}" in input
                and input[f"remove_item_{item['id']}"]
            ):
                if item["id"] in current_cart:
                    if current_cart[item["id"]][2] > 1:
                        # Decrease quantity if more than 1
                        name, price, quantity = current_cart[item["id"]]
                        current_cart[item["id"]] = (name, price, quantity - 1)
                    else:
                        # Remove item if quantity is 1
                        del current_cart[item["id"]]
                    cart.set(current_cart)
                break  # Exit loop after handling one removal

    # Cart display
    @render.ui
    def cart_items():

        cart_ui = []
        for item_id, (name, price, quantity) in cart.get().items():
            print(cart.get().items())
            cart_ui.append(
                ui.div(
                    ui.div(f"{quantity} x {name}", class_="cart-item-name"),
                    ui.div(
                        f"${(price * quantity):.2f}",
                        class_="cart-item-price",
                    ),
                    ui.input_action_button(
                        f"remove_item_{item_id}",
                        ui.icon("trash"),
                        class_="remove-item btn-danger btn-sm",
                    ),
                    class_="cart-item",
                )
            )

        cart_ui.append(
            ui.div(
                ui.div("Total:", class_="cart-item-name"),
                ui.div(
                    f"${sum(price * quantity for _, (name, price, quantity) in cart.get().items()):.2f}",
                    class_="cart-item-price",
                ),
                class_="cart-item",
            )
        )

        return ui.div(*cart_ui)

    # Update order statistics
    @reactive.calc
    def update_order_stats():
        num_orders = sum(quantity for _, (_, _, quantity) in cart.get().items())
        total_revenue = sum(
            price * quantity for _, (_, price, quantity) in cart.get().items()
        )
        avg_order_value = total_revenue / num_orders if num_orders > 0 else 0.0
        return {
            "num_orders": num_orders,
            "total_revenue": total_revenue,
            "avg_order_value": avg_order_value,
        }

    # Place order logic
    @reactive.effect
    @reactive.event(input.place_order)
    def place_order():
        order_info = update_order_stats()  # Get current order info
        current_stats = order_stats_reactive.get()
        updated_stats = {
            "num_orders": current_stats["num_orders"] + 1,
            "total_revenue": current_stats["total_revenue"]
            + order_info["total_revenue"],
            "avg_order_value": (
                (current_stats["total_revenue"] + order_info["total_revenue"])
                / (current_stats["num_orders"] + 1)
                if current_stats["num_orders"] + 1 > 0
                else 0.0
            ),
        }

        order_stats_reactive.set(updated_stats)  # Update global stats
        cart.set({})  # Clear cart
        ui.notification_show("Order placed successfully!")

    # Display order statistics
    @render.text
    def num_orders():
        return f"{order_stats_reactive.get()['num_orders']}"

    @render.text
    def total_revenue():
        return f"${order_stats_reactive.get()['total_revenue']:.2f}"

    @render.text
    def avg_order_value():
        return f"${order_stats_reactive.get()['avg_order_value']:.2f}"


# Create the app
app = App(app_ui, server)
