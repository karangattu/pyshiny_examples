import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render

# Sample data generation
np.random.seed(123)
sales_data = pd.DataFrame(
    {
        "date": pd.date_range(start="2023-01-01", periods=100, freq="D"),
        "revenue": np.random.normal(1000, 200, 100),
        "customers": np.random.randint(50, 150, 100),
        "region": np.random.choice(["North", "South", "East", "West"], 100),
    }
)

# Page configuration
ui.page_opts(title="Layout Columns Demo", fillable=True)

# Header
ui.h2("Layout Columns Demonstration", class_="p-3 bg-primary text-white")

# Basic columns with col_widths parameter
with ui.layout_columns(col_widths=[6, 6]):
    with ui.card():
        ui.card_header("Equal Width Columns (6/12 each)")

        @render.plot
        def revenue_plot():
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots()
            ax.plot(sales_data["date"], sales_data["revenue"])
            ax.set_title("Revenue Over Time")
            return fig

    with ui.card():
        ui.card_header("Customer Distribution")

        @render.plot
        def customer_plot():
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots()
            ax.hist(sales_data["customers"], bins=20)
            ax.set_title("Customer Distribution")
            return fig


# Responsive columns with different breakpoints
with ui.layout_columns(col_widths={"sm": [12, 12], "md": [6, 6], "lg": [4, 8]}):
    with ui.card():
        ui.card_header("Responsive Layout")
        ui.markdown(
            """
        This card changes width based on screen size:
        - Small screens: Full width (12/12)
        - Medium screens: Half width (6/12)
        - Large screens: One-third width (4/12)
        """
        )

    with ui.card():
        ui.card_header("Regional Data")

        @render.table
        def region_summary():
            return (
                sales_data.groupby("region")
                .agg({"revenue": ["mean", "sum"], "customers": ["mean", "count"]})
                .round(2)
            )


# Columns with row heights parameter
with ui.layout_columns(
    col_widths=[4, 4, 4], row_heights=["200px", "auto"], gap="1rem", class_="mt-3"
):
    # First row
    with ui.card():
        ui.card_header("Fixed Height Card")
        ui.markdown("This card has a fixed height of 200px")

    with ui.card():
        ui.card_header("Card with Stats")
        ui.markdown(
            f"""
        **Total Revenue**: ${sales_data['revenue'].sum():,.2f}  
        **Average Customers**: {sales_data['customers'].mean():.1f}
        """
        )

    with ui.card():
        ui.card_header("Regional Split")

        @render.plot
        def region_pie():
            import matplotlib.pyplot as plt

            region_counts = sales_data["region"].value_counts()
            fig, ax = plt.subplots()
            ax.pie(region_counts, labels=region_counts.index, autopct="%1.1f%%")
            return fig


# Fillable columns with height parameter
with ui.layout_columns(
    col_widths=[6, 6], fill=True, fillable=True, height="400px", class_="mt-3"
):
    with ui.card():
        ui.card_header("Fillable Card 1")
        ui.input_select(
            "region_filter",
            "Select Region",
            choices=["All"] + list(sales_data["region"].unique()),
        )

        @render.table
        def filtered_data():
            df = sales_data.copy()
            if input.region_filter() != "All":
                df = df[df["region"] == input.region_filter()]
            return df.tail(5)

    with ui.card():
        ui.card_header("Fillable Card 2")

        @render.plot
        def region_boxplot():
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots()
            sales_data.boxplot(column="revenue", by="region", ax=ax)
            ax.set_title("Revenue by Region")
            plt.xticks(rotation=45)
            return fig
