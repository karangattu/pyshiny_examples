from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, render, ui, reactive

# Generate synthetic spending data
def generate_spending_data(num_records=1000):
    np.random.seed(42)
    
    # Define categories and their typical ranges
    categories = {
        'Groceries': (30, 200),
        'Dining': (10, 100),
        'Entertainment': (20, 150),
        'Shopping': (20, 300),
        'Transportation': (10, 80),
        'Utilities': (50, 200),
        'Healthcare': (20, 500),
        'Housing': (500, 2000)
    }
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, periods=num_records)
    
    data = []
    for _ in range(num_records):
        category = np.random.choice(list(categories.keys()))
        min_amount, max_amount = categories[category]
        amount = round(np.random.uniform(min_amount, max_amount), 2)
        date = dates[_]
        data.append({
            'date': date,
            'category': category,
            'amount': amount
        })
    
    return pd.DataFrame(data)

# Generate the data
spending_df = generate_spending_data()

# UI Definition
app_ui = ui.page_fluid(
    ui.panel_title("Personal Spending Analysis Dashboard"),
    
    # Date Range Input
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_date_range(
                "date_range",
                "Select Date Range",
                start=spending_df['date'].min(),
                end=spending_df['date'].max()
            ),
            ui.input_selectize(
                "selected_categories",
                "Select Categories",
                choices=list(spending_df['category'].unique()),
                selected=list(spending_df['category'].unique()),
                multiple=True
            ),
            ui.input_numeric(
                "budget_threshold",
                "Monthly Budget Threshold ($)",
                value=3000,
                min=1000,
                max=10000
            ),
        ),
        
        # Main Content
        ui.layout_column_wrap(
            ui.value_box(
                "Total Spending",
                ui.output_text("total_spending"),
                theme="primary"
            ),
            ui.value_box(
                "Monthly Average",
                ui.output_text("monthly_avg"),
                theme="info"
            ),
            ui.value_box(
                "Top Category",
                ui.output_text("top_category"),
                theme="warning"
            ),
            width=1/3
        ),
        
        ui.layout_column_wrap(
            ui.card(
                ui.card_header("Spending Trends"),
                ui.output_plot("spending_trend")
            ),
            ui.card(
                ui.card_header("Category Breakdown"),
                ui.output_plot("category_pie")
            ),
            width=1/2
        ),
        
        ui.card(
            ui.card_header("Spending Insights and Recommendations"),
            ui.output_text("recommendations")
        )
    )
)

def server(input, output, session):
    
    @reactive.calc
    def filtered_data():
        start_date = pd.to_datetime(input.date_range()[0])
        end_date = pd.to_datetime(input.date_range()[1])
        mask = (
            (spending_df['date'] >= start_date) & 
            (spending_df['date'] <= end_date) &
            (spending_df['category'].isin(input.selected_categories()))
        )
        return spending_df[mask]
    
    @render.text
    def total_spending():
        total = filtered_data()['amount'].sum()
        return f"${total:,.2f}"
    
    @render.text
    def monthly_avg():
        monthly = filtered_data().groupby(filtered_data()['date'].dt.to_period('M'))['amount'].sum()
        avg = monthly.mean()
        return f"${avg:,.2f}"
    
    @render.text
    def top_category():
        by_category = filtered_data().groupby('category')['amount'].sum()
        top_cat = by_category.idxmax()
        return f"{top_cat}\n(${by_category[top_cat]:,.2f})"
    
    @render.plot
    def spending_trend():
        df = filtered_data()
        monthly = df.groupby(df['date'].dt.to_period('M'))['amount'].sum().reset_index()
        monthly['date'] = monthly['date'].astype(str)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(monthly['date'], monthly['amount'], marker='o')
        ax.set_xlabel('Month')
        ax.set_ylabel('Total Spending ($)')
        ax.set_title('Monthly Spending Trend')
        plt.xticks(rotation=45)
        plt.tight_layout()
        return fig
    
    @render.plot
    def category_pie():
        by_category = filtered_data().groupby('category')['amount'].sum()
        
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(by_category, labels=by_category.index, autopct='%1.1f%%')
        ax.set_title('Spending by Category')
        plt.tight_layout()
        return fig
    
    @render.text
    def recommendations():
        df = filtered_data()
        monthly = df.groupby(df['date'].dt.to_period('M'))['amount'].sum()
        monthly_avg = monthly.mean()
        by_category = df.groupby('category')['amount'].sum()
        top_categories = by_category.nlargest(3)
        
        recommendations = []
        
        # Budget threshold check
        if monthly_avg > input.budget_threshold():
            recommendations.append(
                f"⚠️ Your monthly spending (${monthly_avg:,.2f}) exceeds your budget threshold "
                f"(${input.budget_threshold():,.2f}). Consider reducing expenses."
            )
        
        # Category-specific recommendations
        recommendations.append("\nTop spending categories and recommendations:")
        for cat, amount in top_categories.items():
            if cat == "Dining":
                recommendations.append(
                    f"🍽️ {cat} (${amount:,.2f}): Consider meal prepping or reducing takeout frequency."
                )
            elif cat == "Entertainment":
                recommendations.append(
                    f"🎬 {cat} (${amount:,.2f}): Look for free or discounted entertainment options."
                )
            elif cat == "Shopping":
                recommendations.append(
                    f"🛍️ {cat} (${amount:,.2f}): Try implementing a 24-hour rule before non-essential purchases."
                )
            else:
                recommendations.append(f"📊 {cat} (${amount:,.2f})")
        
        return "\n".join(recommendations)

app = App(app_ui, server)