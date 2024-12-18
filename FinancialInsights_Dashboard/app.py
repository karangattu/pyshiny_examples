import datetime
import random
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from shinywidgets import render_widget, output_widget
from shiny import App, reactive, render, ui

# Synthetic Data Generation
def generate_stock_data(tickers, days=365):
    """Generate synthetic stock price data."""
    dates = pd.date_range(end=datetime.date.today(), periods=days)
    data = {}
    
    for ticker in tickers:
        base_price = random.uniform(50, 500)
        volatility = random.uniform(0.01, 0.05)
        returns = np.random.normal(0, volatility, days)
        prices = base_price * (1 + returns).cumprod()
        
        ticker_data = pd.DataFrame({
            'Date': dates,
            'Close': prices,
            'Volume': np.random.randint(100000, 1000000, days),
            'Returns': returns
        })
        data[ticker] = ticker_data
    
    return data

# Predefined tickers
TICKERS = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'META']
STOCK_DATA = generate_stock_data(TICKERS)

# Portfolio Simulation
def simulate_portfolio(stock_data, initial_investment=10000):
    portfolio = {}
    total_portfolio_value = initial_investment
    allocation = {ticker: initial_investment/len(TICKERS) for ticker in TICKERS}
    
    for ticker, data in stock_data.items():
        shares = allocation[ticker] / data['Close'].iloc[0]
        portfolio[ticker] = {
            'shares': shares,
            'current_value': shares * data['Close'].iloc[-1],
            'total_return': (shares * data['Close'].iloc[-1] - allocation[ticker]) / allocation[ticker] * 100
        }
    
    return portfolio

# UI Components
app_ui = ui.page_fluid(
    ui.head_content(
        ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">')
    ),
    ui.panel_title("Stock Market Dashboard"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select(
                "selected_stock", 
                "Select Stock", 
                choices=TICKERS
            ),
            ui.input_date_range(
                "date_range", 
                "Date Range"
            ),
            ui.input_switch("show_volume", "Show Volume", value=False)
        ),
        ui.layout_columns(
            ui.card(
                ui.card_header("Stock Price"),
                output_widget("stock_chart")
            ),
            ui.card(
                ui.card_header("Portfolio Performance"),
                ui.output_data_frame("portfolio_table")
            )
        )
    ),
    ui.layout_columns(
        ui.card(
            ui.card_header("Market Heatmap"),
            output_widget("market_heatmap")
        ),
        ui.card(
            ui.card_header("Returns Distribution"),
            output_widget("returns_distribution")
        )
    )
)

def server(input, output, session):
    @render_widget
    def stock_chart():
        stock = input.selected_stock()
        df = STOCK_DATA[stock]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df['Date'], 
            y=df['Close'], 
            mode='lines', 
            name='Close Price'
        ))
        
        if input.show_volume():
            fig.add_trace(go.Bar(
                x=df['Date'], 
                y=df['Volume'], 
                name='Volume', 
                yaxis='y2'
            ))
            fig.update_layout(
                yaxis2=dict(
                    title='Volume',
                    overlaying='y',
                    side='right'
                )
            )
        
        fig.update_layout(
            title=f'{stock} Stock Price',
            xaxis_title='Date',
            yaxis_title='Price ($)'
        )
        
        return fig

    @render.data_frame
    def portfolio_table():
        portfolio = simulate_portfolio(STOCK_DATA)
        portfolio_df = pd.DataFrame.from_dict(portfolio, orient='index')
        portfolio_df.index.name = 'Ticker'
        portfolio_df['current_value'] = portfolio_df['current_value'].round(2)
        portfolio_df['total_return'] = portfolio_df['total_return'].round(2)
        return portfolio_df

    @render_widget
    def market_heatmap():
        heat_data = {
            ticker: STOCK_DATA[ticker]['Returns'].mean() * 100 
            for ticker in TICKERS
        }
        
        df = pd.DataFrame.from_dict(heat_data, orient='index', columns=['Returns'])
        df.index.name = 'Ticker'
        df.reset_index(inplace=True)
        
        fig = px.density_heatmap(
            df, 
            x='Ticker', 
            y='Returns', 
            color='Returns',
            title='Market Returns Heatmap'
        )
        return fig

    @render_widget
    def returns_distribution():
        stock = input.selected_stock()
        returns = STOCK_DATA[stock]['Returns']
        
        fig = px.histogram(
            returns, 
            title=f'{stock} Returns Distribution',
            labels={'value': 'Returns', 'count': 'Frequency'}
        )
        return fig

app = App(app_ui, server)