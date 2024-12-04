import random
import pandas as pd
from datetime import datetime, timedelta
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Generate sample spending data
def generate_sample_data(num_entries=100):
    categories = ["Groceries", "Dining", "Transportation", "Utilities", "Entertainment"]
    data = []
    for _ in range(num_entries):
        category = random.choice(categories)
        amount = round(random.uniform(10, 500), 2)
        date = datetime.now() - timedelta(days=random.randint(1, 90))
        data.append({"Category": category, "Amount": amount, "Date": date})
    return pd.DataFrame(data)

spending_data = generate_sample_data()

app_ui = ui.page_fluid(
    ui.panel_title("Spending Habit Analyzer"),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Spending Overview"),
            ui.output_text_verbatim("total_spending"),
            ui.output_text_verbatim("top_categories"),
            ui.output_text_verbatim("optimization_recommendations"),
            width=1 / 2,
        ),
        ui.card(
            ui.card_header("Spending Trends"),
            ui.output_plot("spending_plot"),
            width=1 / 2,
        ),
    ),
)

def server(input: Inputs, output: Outputs, session: Session):
    @render.text
    def total_spending():
        total = spending_data["Amount"].sum()
        return f"Total Spending: ${total:.2f}"

    @render.text
    def top_categories():
        top_categories = spending_data.groupby("Category")["Amount"].sum().sort_values(ascending=False).head(3).index.tolist()
        return f"Top Spending Categories: {', '.join(top_categories)}"

    @render.text
    def optimization_recommendations():
        top_categories = spending_data.groupby("Category")["Amount"].sum().sort_values(ascending=False).head(3).index.tolist()
        recommendations = []
        for category in top_categories:
            category_spending = spending_data[spending_data["Category"] == category]["Amount"].sum()
            recommendation = f"Consider optimizing your {category} spending, which accounts for ${category_spending:.2f} ({category_spending / spending_data['Amount'].sum() * 100:.2f}%) of your total spending."
            recommendations.append(recommendation)
        return "\n\n".join(recommendations)

    @render.plot
    def spending_plot():
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(12, 6))
        spending_data.groupby(pd.Grouper(key="Date", freq="M"))["Amount"].sum().plot(ax=ax)
        ax.set_xlabel("Date")
        ax.set_ylabel("Spending Amount")
        ax.set_title("Monthly Spending Trends")
        return fig

app = App(app_ui, server)