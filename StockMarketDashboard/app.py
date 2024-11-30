import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from shiny import App, Inputs, Outputs, Session, reactive, render, ui


# Generate some sample stock data
def generate_stock_data(
    num_stocks=5,
    start_date=datetime.now() - timedelta(days=365),
    end_date=datetime.now(),
):
    dates = pd.date_range(start_date, end_date, freq="D")
    stocks = [f"Stock {i+1}" for i in range(num_stocks)]
    data = np.random.rand(len(dates), len(stocks)) * 100
    df = pd.DataFrame(data, index=dates, columns=stocks)
    return df


stock_data = generate_stock_data()

app_ui = ui.page_fluid(
    ui.tags.head(
        ui.tags.link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css",
        ),
        ui.tags.style(
            """
            body {
                font-family: 'Roboto', sans-serif;
                background-color: #f8f9fa;
                color: #333;
            }
            .panel-title {
                text-align: center;
                font-size: 2.5em;
                color: #0056b3;
                margin-bottom: 1em;
                font-weight: bold;
            }
            .card {
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
                padding: 20px;
                transition: box-shadow 0.3s ease;
            }
            .card:hover {
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            }
            .card-header {
                background-color: #007bff;
                color: white;
                padding: 15px;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                font-weight: 600;
                font-size: 1.2em;
                margin-bottom: 15px;
            }
            .form-control, .selectize-input {
                border-radius: 5px;
                border: 1px solid #ddd;
                padding: 10px;
                margin-bottom: 15px;
            }
            .value-box {
                text-align: center;
                margin-bottom: 20px;
            }
            .value-box .card-body {
                 padding: 20px;
            }
            .value-box-title {
                font-weight: bold;
                font-size: 1.2em;
                margin-bottom: 5px;
            }
            .value-box-value {
                font-size: 1.8em;
                margin-bottom: 5px;
            }
            .value-box-subtitle {
                font-size: 0.9em;
            }
            .value-box-icon {
                font-size: 2rem;
                margin-bottom: 10px;
                color: white;
            }
            .bg-market-cap {
                background-color: #28a745; /* Green */
            }
            .bg-top-stock {
                background-color: #007bff; /* Blue */
            }
            .bg-worst-stock {
                background-color: #dc3545; /* Red */
            }
            .shiny-date-range-input {
                display: flex;
                flex-direction: column;
            }
            .shiny-date-range-input > div {
                margin-bottom: 10px;
                border-radius: 5px;
                border: 1px solid #ddd;
                padding: 10px;
            }
            .shiny-date-range-input input {
                border: none;
                padding: 0;
            }
            """
        ),
    ),
    ui.div(
        {"class": "panel-title"},
        ui.tags.i(class_="fas fa-chart-line", style="margin-right: 10px;"),
        "Stock Market Dashboard",
    ),
    ui.layout_column_wrap(
        ui.div(
            {"class": "value-box card bg-market-cap"},
            ui.div(
                {"class": "card-body"},
                ui.tags.i(class_="fas fa-chart-bar value-box-icon"),
                ui.div({"class": "value-box-title"}, "Total Market Cap"),
                ui.div({"class": "value-box-value"}, f"${stock_data.sum().sum():.2f}"),
                ui.div({"class": "value-box-subtitle"}, "Up 5% from last month"),
            ),
        ),
        ui.div(
            {"class": "value-box card bg-top-stock"},
            ui.div(
                {"class": "card-body"},
                ui.tags.i(class_="fas fa-chart-line value-box-icon"),
                ui.div({"class": "value-box-title"}, "Top Performing Stock"),
                ui.div({"class": "value-box-value"}, f"{stock_data.max().max():.2f}"),
                ui.div({"class": "value-box-subtitle"}, "Up 15% this week"),
            ),
        ),
        ui.div(
            {"class": "value-box card bg-worst-stock"},
            ui.div(
                {"class": "card-body"},
                ui.tags.i(class_="fas fa-chart-line value-box-icon"),
                ui.div({"class": "value-box-title"}, "Worst Performing Stock"),
                ui.div({"class": "value-box-value"}, f"{stock_data.min().min():.2f}"),
                ui.div({"class": "value-box-subtitle"}, "Down 8% this week"),
            ),
        ),
    ),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Stock Prices"),
            ui.input_selectize(
                "selected_stocks",
                "Select Stocks",
                list(stock_data.columns),
                multiple=True,
                selected=list(stock_data.columns[:3]),
            ),
            ui.output_plot("stock_plot"),
        ),
        ui.card(
            ui.card_header("Stock Performance"),
            ui.input_date_range(
                "date_range",
                "Select Date Range",
                start=stock_data.index.min().strftime("%Y-%m-%d"),
                end=stock_data.index.max().strftime("%Y-%m-%d"),
            ),
            ui.output_plot("performance_plot"),
        ),
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.plot
    def stock_plot():
        fig, ax = plt.subplots(figsize=(12, 6))
        for stock in input.selected_stocks():
            ax.plot(stock_data.index, stock_data[stock], label=stock)
        ax.legend()
        ax.set_title("Stock Prices")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        return fig

    @render.plot
    def performance_plot():
        date_range = input.date_range()
        if date_range is None:
            return None

        start_date, end_date = date_range

        if start_date and end_date:
            filtered_data = stock_data.loc[
                start_date.strftime("%Y-%m-%d") : end_date.strftime("%Y-%m-%d")
            ]
            fig, ax = plt.subplots(figsize=(12, 6))
            for stock in filtered_data.columns:
                ax.plot(filtered_data.index, filtered_data[stock], label=stock)
            ax.legend()
            ax.set_title("Stock Performance")
            ax.set_xlabel("Date")
            ax.set_ylabel("Price")
            return fig
        else:
            return None


app = App(app_ui, server)
