import random
import datetime
from typing import List, Tuple

import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui
from shinywidgets import output_widget, render_widget

# Sample data for the restaurant management app
menu_items = [
    {"item": "Beef Burger", "category": "Entrees", "price": 12.99, "inventory": 50},
    {"item": "Chicken Salad", "category": "Salads", "price": 9.99, "inventory": 30},
    {"item": "Fries", "category": "Sides", "price": 3.99, "inventory": 75},
    {"item": "Chocolate Cake", "category": "Desserts", "price": 6.99, "inventory": 20},
    {"item": "Iced Tea", "category": "Drinks", "price": 2.49, "inventory": 100},
]

sales_data = [
    (datetime.date(2023, 4, 1), "Beef Burger", 15, 12.99),
    (datetime.date(2023, 4, 1), "Chicken Salad", 8, 9.99),
    (datetime.date(2023, 4, 1), "Fries", 20, 3.99),
    (datetime.date(2023, 4, 2), "Beef Burger", 18, 12.99),
    (datetime.date(2023, 4, 2), "Chocolate Cake", 6, 6.99),
    (datetime.date(2023, 4, 2), "Iced Tea", 25, 2.49),
    (datetime.date(2023, 4, 3), "Chicken Salad", 12, 9.99),
    (datetime.date(2023, 4, 3), "Fries", 18, 3.99),
    (datetime.date(2023, 4, 3), "Chocolate Cake", 4, 6.99),
]

app_ui = ui.page_fluid(
    ui.panel_title("Restaurant Management App"),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Menu Management"),
            ui.input_action_button("add_menu_item", "Add Menu Item"),
            ui.output_data_frame("menu_table"),
            ui.modal(
                ui.input_text("new_item", "New Menu Item"),
                ui.input_select("new_category", "Category", [item["category"] for item in menu_items]),
                ui.input_numeric("new_price", "Price", 0, 100, 9.99),
                ui.input_numeric("new_inventory", "Inventory", 0, 1000, 50),
                title="Add New Menu Item",
                footer=ui.modal_button("Save", class_="btn-primary"),
                id="add_menu_modal",
            ),
            width=6,
        ),
        ui.card(
            ui.card_header("Inventory Management"),
            ui.input_action_button("update_inventory", "Update Inventory"),
            ui.output_data_frame("inventory_table"),
            width=6,
        ),
        ui.card(
            ui.card_header("Sales Analytics"),
            ui.output_plot("sales_plot"),
            ui.output_text_verbatim("sales_summary"),
            width=12,
        ),
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    # Menu Management
    @render.data_frame
    def menu_table():
        return pd.DataFrame(menu_items)

    @reactive.effect
    @reactive.event(input.add_menu_item)
    def _():
        ui.modal_show(ui.modal_get("add_menu_modal"))

    @reactive.effect
    @ui.bind_task_button(button_id="add_menu_modal_save")
    async def save_new_menu_item():
        new_item = {
            "item": input.new_item(),
            "category": input.new_category(),
            "price": input.new_price(),
            "inventory": input.new_inventory(),
        }
        menu_items.append(new_item)
        ui.update_data_frame("menu_table", pd.DataFrame(menu_items))
        ui.modal_remove()

    # Inventory Management
    @render.data_frame
    def inventory_table():
        return pd.DataFrame(menu_items)[["item", "inventory"]]

    @reactive.effect
    @reactive.event(input.update_inventory)
    def _():
        for item in menu_items:
            item["inventory"] = random.randint(0, 100)
        ui.update_data_frame("inventory_table", pd.DataFrame(menu_items)[["item", "inventory"]])

    # Sales Analytics
    @render.plot
    def sales_plot():
        sales_df = pd.DataFrame(sales_data, columns=["date", "item", "quantity", "price"])
        sales_df["revenue"] = sales_df["quantity"] * sales_df["price"]

        fig, ax = plt.subplots(figsize=(12, 6))
        sales_df.groupby("date")["revenue"].sum().plot(kind="bar", ax=ax)
        ax.set_xlabel("Date")
        ax.set_ylabel("Revenue")
        ax.set_title("Daily Sales Revenue")
        return fig

    @render.text
    def sales_summary():
        sales_df = pd.DataFrame(sales_data, columns=["date", "item", "quantity", "price"])
        sales_df["revenue"] = sales_df["quantity"] * sales_df["price"]
        total_revenue = sales_df["revenue"].sum()
        top_items = (
            sales_df.groupby("item")["quantity"].sum().sort_values(ascending=False).head(3)
        )
        return f"""
        Total Revenue: ${total_revenue:.2f}
        Top 3 Selling Items:
        {top_items.to_string()}
        """

app = App(app_ui, server)