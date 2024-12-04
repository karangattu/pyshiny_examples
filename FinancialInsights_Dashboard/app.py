import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, reactive, render, ui

# Generate sample data
def generate_stock_data():
    np.random.seed(42)
    stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'META']
    dates = pd.date_range(end=datetime.datetime.now(), periods=100, freq='D')
    
    data = []
    for stock in stocks:
        base_price = np.random.uniform(100, 1000)
        prices = base_price + np.random.randn(len(dates)).cumsum()
        volume = np.random.randint(100000, 1000000, size=len(dates))
        data.extend([{
            'date': date,
            'symbol': stock,
            'price': max(price, 1),
            'volume': vol,
            'change': 0  # Will be calculated later
        } for date, price, vol in zip(dates, prices, volume)])
    
    df = pd.DataFrame(data)
    df['change'] = df.groupby('symbol')['price'].pct_change() * 100
    return df

# Generate portfolio data
def generate_portfolio():
    return pd.DataFrame({
        'symbol': ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'META'],
        'shares': np.random.randint(10, 100, size=5),
        'cost_basis': np.random.uniform(100, 1000, size=5)
    })

# UI Definition
app_ui = ui.page_fluid(
    ui.panel_title("Stock Market Dashboard"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.h4("Controls"),
            ui.input_select(
                "stock_select",
                "Select Stock",
                ["AAPL", "GOOGL", "MSFT", "AMZN", "META"]
            ),
            ui.input_date_range(
                "date_range",
                "Date Range",
                start=datetime.date(2023, 1, 1),
                end=datetime.date.today()
            ),
            ui.input_numeric(
                "alert_threshold",
                "Price Alert Threshold (%)",
                value=5,
                min=1,
                max=20
            ),
            width=250
        ),
        
        ui.layout_column_wrap(
            ui.value_box(
                "Current Price",
                ui.output_text("current_price"),
                showcase=ui.tags.i(class_="fa-solid fa-dollar-sign", style="font-size: 2rem;"),
                theme="primary",
            ),
            ui.value_box(
                "Daily Change",
                ui.output_text("price_change"),
                showcase=ui.tags.i(class_="fa-solid fa-chart-line", style="font-size: 2rem;"),
                theme="info",
            ),
            ui.value_box(
                "Trading Volume",
                ui.output_text("volume"),
                showcase=ui.tags.i(class_="fa-solid fa-chart-bar", style="font-size: 2rem;"),
                theme="success",
            ),
        ),
        
        ui.card(
            ui.card_header("Price History"),
            ui.output_plot("price_plot"),
        ),
        
        ui.layout_column_wrap(
            ui.card(
                ui.card_header("Portfolio Summary"),
                ui.output_table("portfolio_table"),
            ),
            ui.card(
                ui.card_header("Market Alerts"),
                ui.output_table("alerts_table"),
            ),
        ),
    ),
)

def server(input, output, session):
    # Initialize data
    stock_data = reactive.Value(generate_stock_data())
    portfolio = reactive.Value(generate_portfolio())
    
    @reactive.calc
    def filtered_data():
        df = stock_data.get()
        symbol = input.stock_select()
        start_date = datetime.datetime.combine(input.date_range()[0], datetime.datetime.min.time())
        end_date = datetime.datetime.combine(input.date_range()[1], datetime.datetime.min.time())
        
        return df[
            (df['symbol'] == symbol) &
            (df['date'] >= start_date) &
            (df['date'] <= end_date)
        ]

    @render.text
    def current_price():
        data = filtered_data()
        if len(data) > 0:
            return f"${data.iloc[-1]['price']:.2f}"
        return "N/A"

    @render.text
    def price_change():
        data = filtered_data()
        if len(data) > 0:
            change = data.iloc[-1]['change']
            color = "green" if change >= 0 else "red"
            return ui.HTML(f"<span style='color: {color}'>{change:+.2f}%</span>")
        return "N/A"

    @render.text
    def volume():
        data = filtered_data()
        if len(data) > 0:
            return f"{data.iloc[-1]['volume']:,.0f}"
        return "N/A"

    @render.plot
    def price_plot():
        data = filtered_data()
        fig, ax = plt.subplots(figsize=(12, 6))
        
        ax.plot(data['date'], data['price'], linewidth=2)
        ax.set_title(f"{input.stock_select()} Price History")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price ($)")
        ax.grid(True)
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        return fig

    @render.table
    def portfolio_table():
        port = portfolio.get()
        data = stock_data.get()
        
        # Get latest prices
        latest_prices = data.loc[data.groupby('symbol')['date'].idxmax()]
        latest_prices = latest_prices[['symbol', 'price']]
        
        # Merge with portfolio
        result = pd.merge(port, latest_prices, on='symbol')
        result['market_value'] = result['shares'] * result['price']
        result['gain_loss'] = result['market_value'] - (result['shares'] * result['cost_basis'])
        result['gain_loss_pct'] = (result['gain_loss'] / (result['shares'] * result['cost_basis'])) * 100
        
        return result[['symbol', 'shares', 'market_value', 'gain_loss', 'gain_loss_pct']].round(2)

    @render.table
    def alerts_table():
        data = stock_data.get()
        threshold = input.alert_threshold()
        
        # Filter for significant price changes
        alerts = data[abs(data['change']) >= threshold].copy()
        alerts = alerts.sort_values('date', ascending=False).head(5)
        
        alerts['alert'] = alerts.apply(
            lambda x: f"{'🔺' if x['change'] > 0 else '🔻'} {x['symbol']}: {abs(x['change']):.1f}% change",
            axis=1
        )
        
        return alerts[['date', 'alert']]

app = App(app_ui, server)