from datetime import datetime, timedelta
from typing import Optional, Tuple

import numpy as np
import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

# Sample data for expenses
expenses = [
    {"category": "Rent", "amount": 1000, "date": datetime(2024, 11, 1)},
    {"category": "Groceries", "amount": 500, "date": datetime(2024, 11, 10)},
    {"category": "Utilities", "amount": 200, "date": datetime(2024, 11, 10)},
    {"category": "Entertainment", "amount": 150, "date": datetime(2024, 11, 15)},
    {"category": "Transportation", "amount": 75, "date": datetime(2024, 11, 20)},
    {"category": "Rent", "amount": 1000, "date": datetime(2024, 10, 1)},
    {"category": "Groceries", "amount": 600, "date": datetime(2024, 10, 10)},
    {"category": "Utilities", "amount": 220, "date": datetime(2024, 10, 10)},
    {"category": "Entertainment", "amount": 200, "date": datetime(2024, 10, 15)},
    {"category": "Transportation", "amount": 80, "date": datetime(2024, 10, 20)},
]

# Define UI
app_ui = ui.page_fluid(
    ui.panel_title("Budgeting and Expense Tracking"),
    ui.head_content(
        ui.HTML(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'
        )
    ),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_date_range("date_range", "Date Range"),
            ui.input_select(
                "category",
                "Category",
                ["All"] + list(set(exp["category"] for exp in expenses)),
            ),
            ui.input_numeric("monthly_budget", "Monthly Budget", 2000),
        ),
        ui.layout_column_wrap(
            ui.card(
                ui.card_header("Total Expenses"),
                ui.row(
                    ui.column(
                        6,
                        ui.HTML(
                            '<i class="fa-solid fa-money-bills" style="font-size: 2rem;"></i>'
                        ),
                    ),
                    ui.column(
                        6,
                        ui.output_text("total_expenses_text"),
                    ),
                ),
                theme="bg-gradient-orange-red",
            ),
            ui.card(
                ui.card_header("Remaining Budget"),
                ui.row(
                    ui.column(
                        6,
                        ui.HTML(
                            '<i class="fa-solid fa-piggy-bank" style="font-size: 2rem;"></i>'
                        ),
                    ),
                    ui.column(
                        6,
                        ui.output_text("remaining_budget_text"),
                    ),
                ),
                theme="bg-gradient-green-teal",
            ),
            ui.card(
                ui.card_header("Expense Tracker"),
                ui.output_data_frame("expense_table"),
                height="400px",
            ),
            ui.card(
                ui.card_header("Budget Information"),
                ui.output_text_verbatim("budget_info"),
                height="200px",
            ),
        ),
    ),
)


# Define server logic
def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def filtered_expenses() -> list:
        req(input.date_range())
        start_date, end_date = input.date_range()
        category = input.category()

        filtered = [
            exp
            for exp in expenses
            if (start_date <= exp["date"].date() <= end_date)
            and (category == "All" or exp["category"] == category)
        ]
        return filtered

    @render.data_frame
    def expense_table():
        df = pd.DataFrame(
            [
                {
                    "Category": exp["category"],
                    "Amount": f"${exp['amount']:.2f}",
                    "Date": exp["date"].strftime("%Y-%m-%d"),
                }
                for exp in filtered_expenses()
            ]
        )
        return render.DataGrid(df, selection_mode="rows")

    @reactive.calc
    def total_expenses():
        return sum(exp["amount"] for exp in filtered_expenses())

    @reactive.calc
    def remaining_budget():
        monthly_budget = input.monthly_budget()
        return monthly_budget - total_expenses()

    @render.text
    def budget_info():
        monthly_budget = input.monthly_budget()
        if monthly_budget is None:
            return "Please enter a monthly budget."
        elif not input.date_range():
            return f"Monthly Budget: ${monthly_budget:.2f}\nTotal Expenses: $0.00\nRemaining Budget: ${monthly_budget:.2f}"
        else:
            return f"Monthly Budget: ${monthly_budget:.2f}\nTotal Expenses: ${total_expenses():.2f}\nRemaining Budget: ${remaining_budget():.2f}"

    @render.text
    def total_expenses_text():
        if not input.date_range():
            return "$0.00"
        else:
            return f"${total_expenses():.2f}"

    @render.text
    def remaining_budget_text():
        if not input.date_range():
            monthly_budget = input.monthly_budget() or 0
            return f"${monthly_budget:.2f}"
        else:
            return f"${remaining_budget():.2f}"


# Create Shiny app
app = App(app_ui, server)
