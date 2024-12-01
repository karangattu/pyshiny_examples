import random
from datetime import datetime
from typing import List, Tuple

import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

# Sample data for restaurants and menu items
RESTAURANTS = [
    {"id": 1, "name": "The Gourmet Grill", "cuisine": "American"},
    {"id": 2, "name": "Sushi Delight", "cuisine": "Japanese"},
    {"id": 3, "name": "Bella Italiana", "cuisine": "Italian"},
    {"id": 4, "name": "Spice Emporium", "cuisine": "Indian"},
]

MENU_ITEMS = [
    {"id": 1, "name": "Grilled Steak", "price": 25.99, "restaurant_id": 1},
    {"id": 2, "name": "Veggie Burger", "price": 12.99, "restaurant_id": 1},
    {"id": 3, "name": "Sushi Platter", "price": 32.50, "restaurant_id": 2},
    {"id": 4, "name": "Miso Soup", "price": 5.99, "restaurant_id": 2},
    {"id": 5, "name": "Lasagna", "price": 18.99, "restaurant_id": 3},
    {"id": 6, "name": "Margherita Pizza", "price": 15.99, "restaurant_id": 3},
    {"id": 7, "name": "Chicken Tikka Masala", "price": 17.99, "restaurant_id": 4},
    {"id": 8, "name": "Vegetable Samosa", "price": 4.99, "restaurant_id": 4},
]

app_ui = ui.page_fluid(
    ui.panel_title("Restaurant and Menu Management"),
    ui.tags.style(
        """
/* Global Styles */

body {
  font-family: Arial, sans-serif;
  background-color: #f0f0f0;
}

/* Card Styles */

.card {
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin: 20px;
}

.card-header {
  background-color: #333;
  color: #fff;
  padding: 10px;
  border-radius: 10px 10px 0 0;
}

/* Input Styles */

input[type="text"],
input[type="number"],
select {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 5px;
}

input[type="submit"],
button {
  background-color: #4caf50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

input[type="submit"]:hover,
button:hover {
  background-color: #3e8e41;
}

/* Table Styles */

table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: left;
}

th {
  background-color: #f0f0f0;
}

/* Notification Styles */

.notification {
  position: fixed;
  top: 50px;
  right: 50px;
  background-color: #333;
  color: #fff;
  padding: 10px;
  border-radius: 5px;
  animation: fadeOut 3s;
}

@keyframes fadeOut {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

    """
    ),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Restaurants"),
            ui.input_select(
                "restaurant_select",
                "Select a restaurant",
                [r["name"] for r in RESTAURANTS],
            ),
        ),
        ui.card(
            ui.card_header("Add/Update Restaurant"),
            ui.input_text("new_restaurant_name", "Restaurant Name"),
            ui.input_text("new_restaurant_cuisine", "Cuisine"),
            ui.input_action_button("add_restaurant", "Add Restaurant"),
        ),
        ui.card(
            ui.card_header("Add/Update Menu Item"),
            ui.input_select(
                "menu_restaurant_select",
                "Select a restaurant",
                [r["name"] for r in RESTAURANTS],
            ),
            ui.input_text("new_menu_item_name", "Menu Item Name"),
            ui.input_numeric("new_menu_item_price", "Price", value=0, min=0, step=0.01),
            ui.input_action_button("add_menu_item", "Add Menu Item"),
        ),
        width=1 / 3,
    ),
    ui.output_text_verbatim("restaurant_info"),
    ui.output_data_frame("menu_items"),
)


def server(input: Inputs, output: Outputs, session: Session):
    local_restaurants: List[dict] = RESTAURANTS.copy()
    local_menu_items: List[dict] = MENU_ITEMS.copy()

    @reactive.calc
    def selected_restaurant():
        return next(
            (r for r in local_restaurants if r["name"] == input.restaurant_select()),
            None,
        )

    @render.text
    def restaurant_info():
        restaurant = selected_restaurant()
        if restaurant:
            return f"{restaurant['name']} - {restaurant['cuisine']}"
        else:
            return "No restaurant selected"

    @render.data_frame
    def selected_menu_items():
        restaurant = selected_restaurant()
        if restaurant:
            return pd.DataFrame(
                [m for m in local_menu_items if m["restaurant_id"] == restaurant["id"]]
            )
        else:
            return pd.DataFrame()

    @reactive.effect
    @reactive.event(input.add_restaurant)
    def add_new_restaurant():
        req(input.new_restaurant_name(), input.new_restaurant_cuisine())
        new_name = input.new_restaurant_name().strip()
        new_cuisine = input.new_restaurant_cuisine().strip()
        if new_name and new_cuisine:
            new_id = max([r["id"] for r in local_restaurants]) + 1
            new_restaurant = {"id": new_id, "name": new_name, "cuisine": new_cuisine}
            local_restaurants.append(new_restaurant)
            ui.update_select(
                "restaurant_select",
                choices=[r["name"] for r in local_restaurants],
                selected=new_name,
            )
            ui.update_select(
                "menu_restaurant_select",
                choices=[r["name"] for r in local_restaurants],
                selected=new_name,
            )
            ui.notification_show(f"Added new restaurant: {new_name}", type="success")
        else:
            ui.notification_show(
                "Please enter a name and cuisine for the new restaurant.", type="danger"
            )

    @reactive.effect
    @reactive.event(input.add_menu_item)
    def add_new_menu_item():
        req(
            input.menu_restaurant_select(),
            input.new_menu_item_name(),
            input.new_menu_item_price(),
        )
        restaurant_name = input.menu_restaurant_select()
        new_name = input.new_menu_item_name().strip()
        new_price = input.new_menu_item_price()
        if restaurant_name and new_name and new_price is not None:
            restaurant = next(
                (r for r in local_restaurants if r["name"] == restaurant_name), None
            )
            if restaurant:
                new_id = max([m["id"] for m in local_menu_items]) + 1
                new_menu_item = {
                    "id": new_id,
                    "name": new_name,
                    "price": new_price,
                    "restaurant_id": restaurant["id"],
                }
                local_menu_items.append(new_menu_item)
                ui.notification_show(f"Added new menu item: {new_name}", type="success")
            else:
                ui.notification_show("Please select a valid restaurant.", type="danger")
        else:
            ui.notification_show(
                "Please fill in all the menu item details.", type="danger"
            )

    @render.data_frame
    def menu_items():
        restaurant = selected_restaurant()
        if restaurant:
            return pd.DataFrame(
                [m for m in local_menu_items if m["restaurant_id"] == restaurant["id"]]
            )
        else:
            return pd.DataFrame()


app = App(app_ui, server)
