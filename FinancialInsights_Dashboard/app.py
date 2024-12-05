import random
import time
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from shiny import App, Inputs, Outputs, Session, reactive, render, ui
from shinywidgets import output_widget, render_widget

# Sample data for stocks, ETFs, and indices
symbols = ["AAPL", "MSFT", "AMZN", "GOOG", "FB", "TSLA", "SPY", "QQQ", "GLD", "VTI"]
prices = {symbol: random.uniform(50, 500) for symbol in symbols}
returns = {symbol: random.uniform(-0.05, 0.05) for symbol in symbols}
portfolio = {"AAPL": 100, "MSFT": 50, "VTI": 200}

# Function to generate sample data
def generate_sample_data():
    global prices, returns
    for symbol in symbols:
        prices[symbol] += random.uniform(-5, 5)
        returns[symbol] = random.uniform(-0.05, 0.05)

app_ui = ui.page_fluid(
    ui.panel_title("Stock Dashboard"),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Real-Time Stock Prices"),
            ui.input_selectize("symbols", "Select Stocks", symbols, multiple=True, selected=list(portfolio.keys())),
            output_widget("stock_prices"),
            height="400px",
        ),
        ui.card(
            ui.card_header("Portfolio Performance"),
            ui.output_text_verbatim("portfolio_value"),
            ui.output_plot("portfolio_performance"),
            height="400px",
        ),
        ui.card(
            ui.card_header("Market Trends"),
            ui.output_plot("market_heatmap"),
            ui.output_text_verbatim("market_alerts"),
            height="400px",
        ),
        width=1 / 3,
    ),
)

def server(input, output, session):
    @reactive.calc
    def portfolio_value():
        total_value = 0
        for symbol, shares in portfolio.items():
            total_value += shares * prices[symbol]
        return f"Total Portfolio Value: ${total_value:.2f}"

    @render_widget
    def stock_prices():
        df = pd.DataFrame({
            "Symbol": symbols,
            "Price": [prices[symbol] for symbol in symbols],
            "Return": [returns[symbol] for symbol in symbols]
        })
        df = df[df["Symbol"].isin(input.symbols())]
        return px.bar(df, x="Symbol", y="Price", color="Return", title="Real-Time Stock Prices")

    @render.plot
    def portfolio_performance():
        dates = pd.date_range(end=datetime.now(), periods=30, freq="-1D")
        portfolio_values = [sum(portfolio.values()) * (1 + np.random.uniform(-0.05, 0.05)) for _ in range(30)]
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(dates, portfolio_values)
        ax.set_title("Portfolio Performance")
        ax.set_xlabel("Date")
        ax.set_ylabel("Portfolio Value")
        return fig

    @render.plot
    def market_heatmap():
        df = pd.DataFrame({symbol: [returns[symbol]] for symbol in symbols})
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.heatmap(df, cmap="RdYlGn", center=0, annot=True, fmt=".2f", ax=ax)
        ax.set_title("Market Heatmap")
        return fig

    @render.text
    def market_alerts():
        alerts = []
        for symbol, return_value in returns.items():
            if return_value < -0.05:
                alerts.append(f"{symbol} has dropped more than 5%.")
            elif return_value > 0.05:
                alerts.append(f"{symbol} has increased more than 5%.")
        if alerts:
            return "\n".join(alerts)
        else:
            return "No significant market alerts."

    @reactive.effect
    def update_data():
        while True:
            generate_sample_data()
            reactive.invalidate_later(5)
            time.sleep(5)

app = App(app_ui, server)