import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render

# Sample data generation
np.random.seed(123)
data = pd.DataFrame(
    {
        "date": pd.date_range(start="2024-01-01", periods=100),
        "value": np.random.normal(100, 15, 100),
        "category": np.random.choice(["A", "B", "C"], 100),
    }
)

ui.page_opts(title="Layout Column Wrap Demo", fillable=True)

# Example 1: Basic width parameter (fixed width)
ui.h3("1. Fixed Width Layout")
with ui.layout_column_wrap(width="300px"):
    with ui.card():
        "Fixed width of 300px"

        @render.plot
        def plot1():
            return data.plot.line(x="date", y="value")

    with ui.card():
        "Another 300px card"

        @render.table
        def table1():
            return data.head()


ui.hr()

# Example 2: Fractional width
ui.h3("2. Fractional Width Layout")
with ui.layout_column_wrap(width=1 / 3):
    with ui.card():
        "1/3 width card"

        @render.plot
        def plot2():
            return data.plot.scatter(x="value", y="value")

    with ui.card():
        "1/3 width card"

        @render.table
        def table2():
            return data.describe()

    with ui.card():
        "1/3 width card"

        @render.table
        def table3():
            return data.groupby("category").mean()


ui.hr()

# Example 3: Fixed width with heights_equal parameter
ui.h3("3. Equal Heights Layout")
with ui.layout_column_wrap(
    width="250px",
    heights_equal="all",  # Makes all cards same height
    gap="10px",  # Adding gap between cards
):
    with ui.card():
        "Equal height card 1"

        @render.text
        def text1():
            return "Short content"

    with ui.card():
        "Equal height card 2"

        @render.text
        def text2():
            return "This card has\nmore content\nbut will be\nthe same height"


ui.hr()

# Example 4: Fill and Fillable demonstration
ui.h3("4. Fill and Fillable Layout")
with ui.layout_column_wrap(
    width=1 / 2, fill=True, fillable=True, height="300px"  # Fixed height
):
    with ui.card():
        "Fillable card 1"

        @render.plot
        def plot3():
            return data.plot.box(column="value", by="category")

    with ui.card():
        "Fillable card 2"

        @render.table
        def table4():
            return data.tail(10)


ui.hr()

# Example 5: All parameters combined
ui.h3("5. Combined Parameters Layout")
with ui.layout_column_wrap(
    width="400px",
    fixed_width=True,  # Enforce exact width
    heights_equal="row",  # Equal heights within each row
    fill=True,
    fillable=True,
    height="400px",
    gap="20px",
    class_="my-custom-class",
):
    with ui.card():
        "Combined parameters card 1"

        @render.plot
        def plot4():
            return data.plot.hist(column="value", bins=20)

    with ui.card():
        "Combined parameters card 2"

        @render.table
        def table5():
            return data.groupby("category").agg({"value": ["mean", "std", "count"]})

    with ui.card():
        "Combined parameters card 3"

        @render.text
        def text3():
            return f"Total Records: {len(data)}\nCategories: {', '.join(data['category'].unique())}"
