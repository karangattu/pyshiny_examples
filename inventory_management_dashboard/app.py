from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, ui, render, reactive

# Generate sample data
def generate_inventory_data():
    # Generate dates for the last 30 days
    dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
    
    products = [
        'IPA Beer', 'Stout Beer', 'Lager Beer',
        'Red Wine', 'White Wine', 'Rosé Wine'
    ]
    
    inventory_types = ['Raw Materials', 'Work in Progress', 'Finished Goods']
    
    data = []
    for date in dates:
        for product in products:
            for inv_type in inventory_types:
                # Add some randomness to inventory levels
                base_level = np.random.randint(100, 1000)
                if inv_type == 'Raw Materials':
                    base_level *= 1.5
                elif inv_type == 'Work in Progress':
                    base_level *= 0.7
                
                # Add some trend and seasonality
                trend = (date - dates[0]).days * 2
                seasonality = np.sin(date.day * np.pi/15) * 50
                
                inventory_level = max(0, base_level + trend + seasonality)
                
                data.append({
                    'Date': date,
                    'Product': product,
                    'Inventory Type': inv_type,
                    'Inventory Level': round(inventory_level, 2)
                })
    
    return pd.DataFrame(data)

app_ui = ui.page_fluid(
    ui.panel_title("Brewery & Winery Inventory Management Dashboard"),
    
    ui.layout_sidebar(
        ui.sidebar(
            ui.h4("Filters"),
            ui.input_date_range(
                "date_range",
                "Date Range",
                start=datetime.now() - timedelta(days=30),
                end=datetime.now()
            ),
            ui.input_selectize(
                "product_select",
                "Select Products",
                choices=[
                    'IPA Beer', 'Stout Beer', 'Lager Beer',
                    'Red Wine', 'White Wine', 'Rosé Wine'
                ],
                multiple=True,
                selected=['IPA Beer', 'Red Wine']
            ),
            ui.input_checkbox_group(
                "inventory_type",
                "Inventory Types",
                choices=['Raw Materials', 'Work in Progress', 'Finished Goods'],
                selected=['Raw Materials', 'Work in Progress', 'Finished Goods']
            ),
            width=3
        ),
        
        ui.layout_column_wrap(
            ui.value_box(
                "Total Inventory Items",
                ui.output_text("total_items"),
                theme="primary"
            ),
            ui.value_box(
                "Raw Materials Value",
                ui.output_text("raw_materials_value"),
                theme="info"
            ),
            ui.value_box(
                "Finished Goods Value",
                ui.output_text("finished_goods_value"),
                theme="success"
            ),
            width=1/3
        ),
        
        ui.card(
            ui.card_header("Inventory Levels Over Time"),
            ui.output_plot("inventory_plot"),
            full_screen=True
        ),
        
        ui.layout_column_wrap(
            ui.card(
                ui.card_header("Inventory Distribution by Type"),
                ui.output_plot("inventory_dist_plot"),
            ),
            ui.card(
                ui.card_header("Current Inventory Levels"),
                ui.output_data_frame("inventory_table"),
            ),
            width=1/2
        )
    )
)

def server(input, output, session):
    # Initialize data
    df = reactive.Value(generate_inventory_data())
    
    @reactive.calc
    def filtered_inventory():
        inventory_df = df.get()
        
        # Apply date filter
        start_date = datetime.combine(input.date_range()[0], datetime.min.time())
        end_date = datetime.combine(input.date_range()[1], datetime.max.time())
        mask = (inventory_df['Date'] >= start_date) & (inventory_df['Date'] <= end_date)
        inventory_df = inventory_df[mask]
        
        # Apply product filter
        if input.product_select():
            inventory_df = inventory_df[inventory_df['Product'].isin(input.product_select())]
            
        # Apply inventory type filter
        if input.inventory_type():
            inventory_df = inventory_df[inventory_df['Inventory Type'].isin(input.inventory_type())]
            
        return inventory_df

    @render.text
    def total_items():
        df = filtered_inventory()
        return f"{len(df['Product'].unique()):,}"

    @render.text
    def raw_materials_value():
        df = filtered_inventory()
        raw_mat = df[df['Inventory Type'] == 'Raw Materials']['Inventory Level'].sum()
        return f"${raw_mat:,.2f}"

    @render.text
    def finished_goods_value():
        df = filtered_inventory()
        finished = df[df['Inventory Type'] == 'Finished Goods']['Inventory Level'].sum()
        return f"${finished:,.2f}"

    @render.plot
    def inventory_plot():
        df = filtered_inventory()
        fig, ax = plt.subplots(figsize=(12, 6))
        for product in df["Product"].unique():
            product_df = df[df["Product"] == product]
            for inventory_type in product_df["Inventory Type"].unique():
                type_df = product_df[product_df["Inventory Type"] == inventory_type]
                ax.plot(type_df["Date"], type_df["Inventory Level"], 
                       label=f"{product} - {inventory_type}")
        
        ax.set_xlabel("Date")
        ax.set_ylabel("Inventory Level")
        ax.set_title("Inventory Levels Over Time")
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        return fig

    @render.plot
    def inventory_dist_plot():
        df = filtered_inventory()
        fig, ax = plt.subplots(figsize=(10, 6))
        
        inventory_types = df['Inventory Type'].unique()
        x = np.arange(len(df['Product'].unique()))
        width = 0.25
        
        for i, inv_type in enumerate(inventory_types):
            data = df[df['Inventory Type'] == inv_type].groupby('Product')['Inventory Level'].mean()
            ax.bar(x + i*width, data, width, label=inv_type)
        
        ax.set_ylabel('Average Inventory Level')
        ax.set_title('Inventory Distribution by Type')
        ax.set_xticks(x + width)
        ax.set_xticklabels(df['Product'].unique(), rotation=45)
        ax.legend()
        plt.tight_layout()
        return fig

    @render.data_frame
    def inventory_table():
        df = filtered_inventory()
        current_levels = df.groupby(['Product', 'Inventory Type'])['Inventory Level'].last().reset_index()
        return render.DataGrid(current_levels, height='400px')

app = App(app_ui, server)