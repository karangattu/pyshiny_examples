import datetime
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from shiny import App, render, ui, reactive
from shiny.types import FileInfo

# Synthetic Data Generation
def generate_spending_data(num_months=12, num_categories=6):
    """Generate realistic synthetic spending data."""
    categories = [
        "Groceries", 
        "Dining Out", 
        "Entertainment", 
        "Transportation", 
        "Utilities", 
        "Shopping"
    ]
    
    months = pd.date_range(end=datetime.date.today(), periods=num_months, freq='MS')
    
    data = []
    for month in months:
        for category in categories:
            base_spend = {
                "Groceries": 500,
                "Dining Out": 300,
                "Entertainment": 200,
                "Transportation": 150,
                "Utilities": 250,
                "Shopping": 250
            }[category]
            
            # Add some randomness
            variance = base_spend * 0.3
            spend = max(0, base_spend + random.uniform(-variance, variance))
            
            data.append({
                "Month": month,
                "Category": category,
                "Amount": spend
            })
    
    return pd.DataFrame(data)

# Generate synthetic data
spending_df = generate_spending_data()

app_ui = ui.page_fluid(
    ui.panel_title("💰 Personal Spending Analyzer"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_date_range(
                "date_range", 
                "Select Date Range", 
                start=spending_df['Month'].min(), 
                end=spending_df['Month'].max()
            ),
            ui.input_checkbox_group(
                "categories", 
                "Select Categories", 
                choices=spending_df['Category'].unique().tolist(), 
                selected=spending_df['Category'].unique().tolist()
            ),
            ui.input_select(
                "visualization_type", 
                "Visualization Type", 
                choices=[
                    "Monthly Trend", 
                    "Category Breakdown", 
                    "Spending Distribution"
                ]
            )
        ),
        ui.layout_columns(
            ui.card(
                ui.card_header("Spending Analysis"),
                ui.output_plot("spending_plot")
            ),
            ui.card(
                ui.card_header("Insights & Recommendations"),
                ui.output_text_verbatim("spending_insights")
            )
        )
    )
)

def server(input, output, session):
    @reactive.calc
    def filtered_data():
        """Filter data based on user selections"""
        df = spending_df.copy()
        
        # Date range filter
        start_date, end_date = input.date_range()
        df = df[(df['Month'] >= start_date) & (df['Month'] <= end_date)]
        
        # Category filter
        df = df[df['Category'].isin(input.categories())]
        
        return df

    @render.plot
    def spending_plot():
        df = filtered_data()
        
        plt.figure(figsize=(10, 6))
        
        if input.visualization_type() == "Monthly Trend":
            df_grouped = df.groupby(['Month', 'Category'])['Amount'].sum().unstack()
            df_grouped.plot(kind='line', ax=plt.gca(), marker='o')
            plt.title("Monthly Spending Trend")
            plt.xlabel("Month")
            plt.ylabel("Amount Spent")
            plt.legend(title="Category", bbox_to_anchor=(1.05, 1), loc='upper left')
        
        elif input.visualization_type() == "Category Breakdown":
            df_grouped = df.groupby('Category')['Amount'].sum()
            df_grouped.plot(kind='pie', autopct='%1.1f%%', ax=plt.gca())
            plt.title("Spending by Category")
        
        elif input.visualization_type() == "Spending Distribution":
            sns.boxplot(x='Category', y='Amount', data=df)
            plt.title("Spending Distribution Across Categories")
            plt.xticks(rotation=45)
        
        plt.tight_layout()
        return plt.gcf()

    @render.text
    def spending_insights():
        df = filtered_data()
        
        # Calculate total spending
        total_spending = df['Amount'].sum()
        
        # Category-wise spending
        category_spending = df.groupby('Category')['Amount'].sum()
        highest_category = category_spending.idxmax()
        lowest_category = category_spending.idxmin()
        
        # Recommendations based on spending
        recommendations = {
            "Groceries": "Consider meal planning and buying in bulk to reduce costs.",
            "Dining Out": "Try cooking at home more often to save money.",
            "Entertainment": "Look for free or low-cost entertainment options.",
            "Transportation": "Consider carpooling or public transit to reduce expenses.",
            "Utilities": "Implement energy-saving practices to lower bills.",
            "Shopping": "Create a budget and avoid impulse purchases."
        }
        
        insights = f"""
Total Spending: ${total_spending:.2f}

Category Breakdown:
{category_spending}

Highest Spending Category: {highest_category}
Lowest Spending Category: {lowest_category}

💡 Recommendation for {highest_category}: 
{recommendations.get(highest_category, "No specific recommendation available.")}
"""
        return insights

app = App(app_ui, server)