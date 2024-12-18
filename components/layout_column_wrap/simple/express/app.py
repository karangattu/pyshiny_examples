import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(123)
sales_data = pd.DataFrame(
    {
        "product": ["Widgets", "Gadgets", "Tools", "Supplies"],
        "revenue": np.random.randint(1000, 10000, 4),
        "units": np.random.randint(100, 1000, 4),
        "profit_margin": np.random.uniform(0.1, 0.4, 4).round(2),
    }
)

# App title and description
ui.page_opts(title="Sales Dashboard", fillable=True)

# Layout using layout_column_wrap
with ui.layout_column_wrap(width=1 / 2):

    # Card 1: Data Table
    with ui.card():
        ui.card_header("Sales Data")

        @render.data_frame
        def sales_table():
            return render.DataGrid(sales_data)

    # Card 2: Product Filter
    with ui.card():
        ui.card_header("Filter Products")
        ui.input_selectize(
            "products",
            "Select Products",
            choices=sales_data["product"].tolist(),
            multiple=True,
        )

    # Card 3: Summary Stats
    with ui.card():
        ui.card_header("Summary Statistics")

        @render.data_frame
        def summary_stats():
            df = sales_data
            if input.products():
                df = df[df["product"].isin(input.products())]

            stats = pd.DataFrame(
                {
                    "Metric": ["Total Revenue", "Total Units", "Avg Profit Margin"],
                    "Value": [
                        f"${df['revenue'].sum():,.0f}",
                        f"{df['units'].sum():,.0f}",
                        f"{df['profit_margin'].mean():.1%}",
                    ],
                }
            )
            return stats

    # Card 4: Info Card
    with ui.card():
        ui.card_header("About")
        "This dashboard demonstrates the use of layout_column_wrap in Shiny for Python."
        "The layout automatically adjusts based on screen size."
        "Try selecting different products to see the summary stats update."
