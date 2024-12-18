import datetime
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import App, reactive, render, ui

# Synthetic Data Generation
def generate_menu_items():
    """Generate synthetic menu items with categories and pricing."""
    categories = ['Appetizer', 'Main Course', 'Dessert', 'Beverage']
    menu_items = [
        {"id": f"item_{i}", 
         "name": f"{category} {random.choice(['Classic', 'Special', 'Deluxe'])} {random.choice(['Dish', 'Plate', 'Selection'])}",
         "category": category, 
         "price": round(random.uniform(5.99, 45.99), 2),
         "cost_price": round(random.uniform(2.00, 20.00), 2),
         "description": f"A delightful {category.lower()} with unique flavors"
        } for i, category in enumerate(categories * 5)
    ]
    return pd.DataFrame(menu_items)

def generate_inventory():
    """Generate synthetic inventory data."""
    menu_df = generate_menu_items()
    inventory = []
    for _, item in menu_df.iterrows():
        inventory.append({
            "item_id": item['id'],
            "item_name": item['name'],
            "current_stock": random.randint(10, 200),
            "unit": random.choice(['kg', 'lbs', 'pieces', 'liters']),
            "reorder_level": random.randint(20, 50),
            "last_restocked": pd.Timestamp.now() - pd.Timedelta(days=random.randint(1, 30))
        })
    return pd.DataFrame(inventory)

def generate_sales_data():
    """Generate synthetic sales data."""
    menu_df = generate_menu_items()
    sales = []
    date_range = pd.date_range(end=datetime.date.today(), periods=90)
    
    for date in date_range:
        daily_sales = menu_df.sample(n=random.randint(5, 15))
        for _, item in daily_sales.iterrows():
            quantity = random.randint(1, 10)
            sales.append({
                "date": date,
                "item_id": item['id'],
                "item_name": item['name'],
                "quantity_sold": quantity,
                "total_revenue": round(item['price'] * quantity, 2)
            })
    
    return pd.DataFrame(sales)

def generate_customer_feedback():
    """Generate synthetic customer feedback."""
    feedback_types = ['Food Quality', 'Service', 'Ambiance', 'Value for Money']
    ratings = [1, 2, 3, 4, 5]
    
    feedback = []
    for _ in range(100):
        feedback.append({
            "date": pd.Timestamp.now() - pd.Timedelta(days=random.randint(1, 90)),
            "category": random.choice(feedback_types),
            "rating": random.choice(ratings),
            "comment": f"A {random.choice(['great', 'good', 'average', 'poor'])} experience"
        })
    
    return pd.DataFrame(feedback)

# Shiny App
app_ui = ui.page_navbar(
    ui.nav_panel(
        "Menu Management",
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_selectize("category_filter", "Filter by Category", 
                                   choices=["All"] + list(generate_menu_items()['category'].unique())),
                ui.input_action_button("add_menu_item", "Add Menu Item", class_="btn-success")
            ),
            ui.output_data_frame("menu_table")
        )
    ),
    ui.nav_panel(
        "Inventory Tracking",
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_slider("stock_level", "Stock Level", min=0, max=200, value=50)
            ),
            ui.output_data_frame("inventory_table"),
            ui.output_plot("inventory_plot")
        )
    ),
    ui.nav_panel(
        "Sales Dashboard",
        ui.layout_columns(
            ui.card(
                ui.card_header("Daily Sales"),
                ui.output_plot("daily_sales_plot")
            ),
            ui.card(
                ui.card_header("Top Selling Items"),
                ui.output_data_frame("top_selling_items")
            )
        )
    ),
    ui.nav_panel(
        "Customer Feedback",
        ui.layout_columns(
            ui.card(
                ui.card_header("Feedback Ratings"),
                ui.output_plot("feedback_ratings_plot")
            ),
            ui.card(
                ui.card_header("Feedback Details"),
                ui.output_data_frame("feedback_table")
            )
        )
    ),
    title="Restaurant Management Dashboard"
)

def server(input, output, session):
    # Menu Management
    @render.data_frame
    def menu_table():
        df = generate_menu_items()
        if input.category_filter() != "All":
            df = df[df['category'] == input.category_filter()]
        return render.DataGrid(df)

    # Inventory Tracking
    @render.data_frame
    def inventory_table():
        df = generate_inventory()
        df = df[df['current_stock'] <= input.stock_level()]
        return render.DataGrid(df)

    @render.plot
    def inventory_plot():
        df = generate_inventory()
        plt.figure(figsize=(10, 6))
        df.plot(kind='bar', x='item_name', y='current_stock', ax=plt.gca())
        plt.title("Current Inventory Levels")
        plt.xlabel("Menu Items")
        plt.ylabel("Stock Quantity")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        return plt.gcf()

    # Sales Dashboard
    @render.plot
    def daily_sales_plot():
        df = generate_sales_data()
        daily_sales = df.groupby('date')['total_revenue'].sum().reset_index()
        
        plt.figure(figsize=(12, 6))
        plt.plot(daily_sales['date'], daily_sales['total_revenue'])
        plt.title("Daily Sales Revenue")
        plt.xlabel("Date")
        plt.ylabel("Total Revenue ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        return plt.gcf()

    @render.data_frame
    def top_selling_items():
        df = generate_sales_data()
        top_items = df.groupby('item_name')['quantity_sold'].sum().nlargest(5).reset_index()
        return render.DataGrid(top_items)

    # Customer Feedback
    @render.plot
    def feedback_ratings_plot():
        df = generate_customer_feedback()
        avg_ratings = df.groupby('category')['rating'].mean()
        
        plt.figure(figsize=(10, 6))
        avg_ratings.plot(kind='bar')
        plt.title("Average Feedback Ratings")
        plt.xlabel("Feedback Category")
        plt.ylabel("Average Rating")
        plt.tight_layout()
        return plt.gcf()

    @render.data_frame
    def feedback_table():
        df = generate_customer_feedback()
        return render.DataGrid(df)

app = App(app_ui, server)