import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from shiny import App, reactive, render, ui

# Synthetic Data Generation
def generate_inventory_data():
    """Generate realistic synthetic inventory data for breweries and wineries."""
    np.random.seed(42)
    
    # Define product types
    products = ['Craft Beer', 'Wine', 'Spirits', 'Malt', 'Hops', 'Grape Concentrate']
    inventory_types = ['Raw Materials', 'Work-in-Progress', 'Finished Goods']
    
    # Date range
    date_range = pd.date_range(start='2023-01-01', end='2024-01-01', freq='D')
    
    # Generate comprehensive inventory data
    data = []
    for product in products:
        for inventory_type in inventory_types:
            base_level = np.random.randint(500, 2000)
            volatility = np.random.uniform(0.05, 0.2)
            
            inventory_levels = [
                base_level + 
                np.random.normal(0, base_level * volatility) * 
                (1 + 0.1 * np.sin(i/10))  # Add some cyclical variation
                for i in range(len(date_range))
            ]
            
            for date, level in zip(date_range, inventory_levels):
                data.append({
                    'Date': date,
                    'Product': product,
                    'Inventory Type': inventory_type,
                    'Inventory Level': max(0, level),  # Ensure non-negative
                })
    
    return pd.DataFrame(data)

# Generate the inventory dataset
inventory_df = generate_inventory_data()

# Shiny App UI
app_ui = ui.page_fluid(
    ui.head_content(
        ui.tags.style("""
            .card-header { background-color: #f8f9fa; }
            .inventory-card { margin-bottom: 15px; }
        """)
    ),
    ui.panel_title("Brewery & Winery Inventory Dashboard"),
    
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_checkbox_group(
                "selected_products", 
                "Select Products", 
                choices=inventory_df['Product'].unique().tolist(),
                selected=inventory_df['Product'].unique().tolist()
            ),
            ui.input_checkbox_group(
                "selected_inventory_types", 
                "Inventory Types", 
                choices=inventory_df['Inventory Type'].unique().tolist(),
                selected=inventory_df['Inventory Type'].unique().tolist()
            ),
            ui.input_date_range(
                "date_range", 
                "Date Range", 
                start=inventory_df['Date'].min().date(), 
                end=inventory_df['Date'].max().date()
            ),
            ui.input_switch("show_trend", "Show Trend Line", value=False)
        ),
        ui.layout_columns(
            ui.card(
                ui.card_header("Inventory Levels Over Time"),
                ui.output_plot("inventory_plot"),
                class_="inventory-card"
            ),
            ui.card(
                ui.card_header("Inventory Distribution"),
                ui.output_plot("inventory_distribution"),
                class_="inventory-card"
            ),
            ui.card(
                ui.card_header("Inventory Summary"),
                ui.output_table("inventory_summary"),
                class_="inventory-card"
            )
        )
    )
)

def server(input, output, session):
    @reactive.calc
    def filtered_inventory():
        # Filter DataFrame based on user inputs
        df = inventory_df.copy()
        
        # Filter by products
        if input.selected_products():
            df = df[df['Product'].isin(input.selected_products())]
        
        # Filter by inventory types
        if input.selected_inventory_types():
            df = df[df['Inventory Type'].isin(input.selected_inventory_types())]
        
        # Filter by date range
        start_date = datetime.datetime.combine(input.date_range()[0], datetime.min.time())
        end_date = datetime.datetime.combine(input.date_range()[1], datetime.datetime.max.time())
        df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
        
        return df

    @render.plot
    def inventory_plot():
        df = filtered_inventory()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        for product in df["Product"].unique():
            for inventory_type in df["Inventory Type"].unique():
                type_df = df[(df["Product"] == product) & (df["Inventory Type"] == inventory_type)]
                ax.plot(type_df["Date"], type_df["Inventory Level"], 
                        label=f"{product} - {inventory_type}")
                
                # Optional trend line
                if input.show_trend():
                    z = np.polyfit(range(len(type_df)), type_df["Inventory Level"], 1)
                    p = np.poly1d(z)
                    ax.plot(type_df["Date"], p(range(len(type_df))), 
                            linestyle='--', alpha=0.5)
        
        ax.set_xlabel("Date")
        ax.set_ylabel("Inventory Level")
        ax.set_title("Inventory Levels Over Time")
        plt.xticks(rotation=45)
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.tight_layout()
        return fig

    @render.plot
    def inventory_distribution():
        df = filtered_inventory()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        df.boxplot(column='Inventory Level', by='Product', ax=ax)
        
        ax.set_title("Inventory Level Distribution by Product")
        ax.set_xlabel("Product")
        ax.set_ylabel("Inventory Level")
        plt.xticks(rotation=45)
        plt.tight_layout()
        return fig

    @render.table
    def inventory_summary():
        df = filtered_inventory()
        summary = df.groupby(['Product', 'Inventory Type'])['Inventory Level'].agg([
            ('Avg Inventory', 'mean'), 
            ('Min Inventory', 'min'), 
            ('Max Inventory', 'max')
        ]).round(2)
        
        return summary

app = App(app_ui, server)