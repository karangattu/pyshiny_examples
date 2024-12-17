from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shiny import App, render, ui, reactive
import plotly.express as px
from shinywidgets import output_widget, render_widget

# Generate sample data
def generate_menu_data():
    return pd.DataFrame({
        'item_id': range(1, 11),
        'name': ['Burger', 'Pizza', 'Pasta', 'Salad', 'Steak', 'Fish', 'Soup', 'Sandwich', 'Wings', 'Dessert'],
        'category': ['Main', 'Main', 'Main', 'Starter', 'Main', 'Main', 'Starter', 'Main', 'Starter', 'Dessert'],
        'price': [12.99, 15.99, 13.99, 8.99, 25.99, 22.99, 6.99, 11.99, 10.99, 7.99],
        'cost': [4.50, 5.20, 4.80, 2.50, 9.99, 8.50, 2.20, 4.00, 3.80, 2.50],
        'active': [True] * 10
    })

def generate_inventory_data():
    return pd.DataFrame({
        'ingredient': ['Beef', 'Cheese', 'Tomatoes', 'Lettuce', 'Bread', 'Chicken', 'Fish', 'Pasta', 'Sauce', 'Flour'],
        'quantity': np.random.randint(50, 200, 10),
        'unit': ['lbs', 'lbs', 'lbs', 'lbs', 'loaves', 'lbs', 'lbs', 'lbs', 'gallons', 'lbs'],
        'reorder_point': [50, 40, 30, 25, 30, 45, 40, 35, 20, 30]
    })

def generate_sales_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    sales = []
    for date in dates:
        daily_items = np.random.randint(50, 150)
        for _ in range(daily_items):
            sales.append({
                'date': date,
                'item_id': np.random.randint(1, 11),
                'quantity': np.random.randint(1, 5),
                'revenue': np.random.uniform(10, 100)
            })
    return pd.DataFrame(sales)

# Create the UI
app_ui = ui.page_fluid(
    ui.navset_tab(
        # Menu Management Tab
        ui.nav_panel("Menu Management",
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_text("item_name", "Item Name"),
                    ui.input_select("category", "Category", 
                                  ["Main", "Starter", "Dessert", "Beverage"]),
                    ui.input_numeric("price", "Price ($)", value=10.99),
                    ui.input_numeric("cost", "Cost ($)", value=3.99),
                    ui.input_action_button("add_item", "Add Item"),
                    width=250
                ),
                ui.card(
                    ui.card_header("Current Menu Items"),
                    ui.output_data_frame("menu_table")
                )
            )
        ),
        
        # Inventory Management Tab
        ui.nav_panel("Inventory Management",
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_numeric("restock_quantity", "Restock Quantity", value=50),
                    ui.input_action_button("restock_low", "Restock Low Items"),
                    width=250
                ),
                ui.card(
                    ui.card_header("Current Inventory"),
                    ui.output_data_frame("inventory_table")
                )
            )
        ),
        
        # Sales Analytics Tab
        ui.nav_panel("Sales Analytics",
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_date_range(
                        "date_range",
                        "Date Range",
                        start=datetime.now() - timedelta(days=30),
                        end=datetime.now()
                    ),
                    ui.input_selectize(
                        "analysis_type",
                        "Analysis Type",
                        choices=["Daily Revenue", "Top Items", "Category Performance"]
                    ),
                    width=250
                ),
                ui.layout_column_wrap(
                    ui.value_box(
                        "Total Revenue",
                        ui.output_text("total_revenue"),
                        theme="primary"
                    ),
                    ui.value_box(
                        "Total Orders",
                        ui.output_text("total_orders"),
                        theme="info"
                    ),
                    ui.value_box(
                        "Average Order Value",
                        ui.output_text("avg_order"),
                        theme="success"
                    ),
                    width=1/3
                ),
                ui.card(
                    ui.card_header("Sales Analysis"),
                    output_widget("sales_plot")
                )
            )
        )
    )
)

def server(input, output, session):
    # Initialize reactive values for data storage
    menu_data = reactive.Value(generate_menu_data())
    inventory_data = reactive.Value(generate_inventory_data())
    sales_data = reactive.Value(generate_sales_data())

    # Menu Management
    @render.data_frame
    def menu_table():
        return render.DataGrid(menu_data.get(), row_selection_mode="multiple")

    @reactive.effect
    @reactive.event(input.add_item)
    def _():
        current_menu = menu_data.get()
        new_item = pd.DataFrame({
            'item_id': [current_menu['item_id'].max() + 1],
            'name': [input.item_name()],
            'category': [input.category()],
            'price': [input.price()],
            'cost': [input.cost()],
            'active': [True]
        })
        menu_data.set(pd.concat([current_menu, new_item], ignore_index=True))

    # Inventory Management
    @render.data_frame
    def inventory_table():
        df = inventory_data.get()
        df['status'] = np.where(df['quantity'] <= df['reorder_point'], 'Low', 'OK')
        return render.DataGrid(df)

    @reactive.effect
    @reactive.event(input.restock_low)
    def _():
        df = inventory_data.get()
        df.loc[df['quantity'] <= df['reorder_point'], 'quantity'] += input.restock_quantity()
        inventory_data.set(df)

    # Sales Analytics
    @render.text
    def total_revenue():
        df = sales_data.get()
        df['date'] = pd.to_datetime(df['date'])
        mask = (df['date'] >= pd.to_datetime(input.date_range()[0])) & \
               (df['date'] <= pd.to_datetime(input.date_range()[1]))
        return f"${df[mask]['revenue'].sum():,.2f}"

    @render.text
    def total_orders():
        df = sales_data.get()
        df['date'] = pd.to_datetime(df['date'])
        mask = (df['date'] >= pd.to_datetime(input.date_range()[0])) & \
               (df['date'] <= pd.to_datetime(input.date_range()[1]))
        return f"{len(df[mask]):,}"

    @render.text
    def avg_order():
        df = sales_data.get()
        df['date'] = pd.to_datetime(df['date'])
        mask = (df['date'] >= pd.to_datetime(input.date_range()[0])) & \
               (df['date'] <= pd.to_datetime(input.date_range()[1]))
        filtered_df = df[mask]
        return f"${filtered_df['revenue'].mean():,.2f}"

    @render_widget
    def sales_plot():
        df = sales_data.get()
        df['date'] = pd.to_datetime(df['date'])
        mask = (df['date'] >= pd.to_datetime(input.date_range()[0])) & \
               (df['date'] <= pd.to_datetime(input.date_range()[1]))
        filtered_df = df[mask]

        if input.analysis_type() == "Daily Revenue":
            daily_revenue = filtered_df.groupby('date')['revenue'].sum().reset_index()
            fig = px.line(daily_revenue, x='date', y='revenue',
                         title='Daily Revenue Over Time')
            
        elif input.analysis_type() == "Top Items":
            item_sales = filtered_df.groupby('item_id')['revenue'].sum().reset_index()
            item_sales = item_sales.merge(menu_data.get()[['item_id', 'name']], on='item_id')
            fig = px.bar(item_sales.sort_values('revenue', ascending=False).head(10),
                        x='name', y='revenue', title='Top 10 Items by Revenue')
            
        else:  # Category Performance
            item_sales = filtered_df.merge(menu_data.get()[['item_id', 'category']], on='item_id')
            category_sales = item_sales.groupby('category')['revenue'].sum().reset_index()
            fig = px.pie(category_sales, values='revenue', names='category',
                        title='Revenue by Category')

        return fig

app = App(app_ui, server)