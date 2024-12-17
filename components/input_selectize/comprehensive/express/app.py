import random
import string
from typing import Dict, List, Union

import pandas as pd
from shiny import reactive
from shiny.express import input, render, ui


# Generate synthetic data
def generate_companies() -> Dict[str, Dict[str, str]]:
    """Generate a nested dictionary of companies grouped by industry."""
    industries = {
        "Technology": {
            "AAPL": "Apple Inc.",
            "MSFT": "Microsoft Corporation",
            "GOOGL": "Alphabet Inc.",
            "AMZN": "Amazon.com Inc.",
        },
        "Finance": {
            "JPM": "JPMorgan Chase & Co.",
            "BAC": "Bank of America",
            "GS": "Goldman Sachs",
            "MS": "Morgan Stanley",
        },
        "Healthcare": {
            "JNJ": "Johnson & Johnson",
            "PFE": "Pfizer Inc.",
            "UNH": "UnitedHealth Group",
            "MRK": "Merck & Co.",
        },
    }
    return industries


# Generate random stock performance data
def generate_stock_performance(companies: Dict[str, Dict[str, str]]) -> pd.DataFrame:
    """Generate synthetic stock performance data."""
    data = []
    for industry, company_dict in companies.items():
        for ticker, name in company_dict.items():
            data.append(
                {
                    "Ticker": ticker,
                    "Company": name,
                    "Industry": industry,
                    "Price": round(random.uniform(50, 500), 2),
                    "Performance": round(random.uniform(-20, 30), 2),
                }
            )
    return pd.DataFrame(data)


# Create page options and title
ui.page_opts(title="Selectize Input Showcase", fillable=True)

# Generate data
companies = generate_companies()
stock_df = generate_stock_performance(companies)

# Sidebar with various selectize inputs
with ui.sidebar():
    # Basic selectize input with simple list
    ui.input_selectize(
        "basic_select",
        "Basic Selectize",
        choices=list(companies.keys()),
        multiple=False,
    )

    # Selectize with dictionary (optgroup)
    ui.input_selectize(
        "company_select", "Select Companies", choices=companies, multiple=True
    )

    # Selectize with custom options
    ui.input_selectize(
        "advanced_select",
        "Advanced Selectize",
        choices=companies,
        multiple=True,
        options={
            "placeholder": "Select companies...",
            "maxItems": 3,
            "create": True,  # Allow creating new items
        },
    )

    # Selectize with remove button
    ui.input_selectize(
        "remove_select",
        "Selectize with Remove Button",
        choices=stock_df["Ticker"].tolist(),
        multiple=True,
        remove_button=True,
    )

# Main content area
with ui.layout_columns():
    # Display selected industries
    @render.text
    def show_industries():
        return f"Selected Industries: {input.basic_select()}"

    # Display selected companies
    @render.text
    def show_companies():
        selected = input.company_select() or []
        companies_list = [
            company
            for industry in selected
            for company in companies.get(industry, {}).values()
        ]
        return f"Selected Companies: {', '.join(companies_list)}"

    # Show stock performance for selected tickers
    @render.data_frame
    def stock_performance():
        selected = input.remove_select() or []
        if not selected:
            return stock_df
        return stock_df[stock_df["Ticker"].isin(selected)]

    # Show advanced selectize details
    @render.text
    def advanced_select_details():
        selected = input.advanced_select() or []
        return f"Advanced Selection: {', '.join(selected)}"
