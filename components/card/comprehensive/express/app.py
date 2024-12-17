import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
data = pd.DataFrame(
    {
        "Category": ["A", "B", "C", "D", "E"],
        "Value": np.random.randint(50, 500, 5),
        "Percentage": np.random.uniform(0.1, 0.9, 5),
    }
)

# Page setup with full width and title
ui.page_opts(title="Card Component Showcase", full_width=True)

# Add Font Awesome CSS
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# Main layout with multiple cards demonstrating different features
with ui.layout_column_wrap(width=1 / 3):
    # Card with full screen option
    with ui.card(full_screen=True):
        ui.card_header("Full Screen Card")
        ui.p("Click the expand icon in the top right to view full screen")

        @render.plot
        def full_screen_plot():
            plt.figure(figsize=(8, 6))
            sns.barplot(x="Category", y="Value", data=data)
            plt.title("Full Screen Bar Plot")
            return plt.gcf()

    # Card with custom height and background
    with ui.card(height="400px", class_="bg-light"):
        ui.card_header("Custom Height Card")

        @render.table
        def height_table():
            return data

    # Card with border and border radius
    with ui.card(class_="border-primary rounded-4"):
        ui.card_header("Styled Card with Border")

        @render.plot
        def border_plot():
            plt.figure(figsize=(8, 6))
            plt.pie(data["Value"], labels=data["Category"], autopct="%1.1f%%")
            plt.title("Pie Chart of Values")
            return plt.gcf()

    # Card with header and footer
    with ui.card():
        ui.card_header("Card with Header and Footer")

        @render.text
        def card_text():
            return f"Total Value: {data['Value'].sum()}"

        with ui.card_footer():
            ui.p("Footer content goes here")

    # Card with custom padding and gap
    with ui.card(class_="p-4"):
        ui.card_header("Card with Custom Padding")
        ui.input_slider("n", "Number of Data Points", min=1, max=5, value=3)

        @render.table
        def padded_table():
            return data.head(input.n())

    # Card demonstrating interactive elements
    with ui.card():
        ui.card_header("Interactive Card")
        ui.input_checkbox_group(
            "categories", "Select Categories", choices=list(data["Category"])
        )

        @render.plot
        def interactive_plot():
            selected = input.categories() or list(data["Category"])
            filtered_data = data[data["Category"].isin(selected)]

            plt.figure(figsize=(8, 6))
            sns.scatterplot(x="Category", y="Value", data=filtered_data)
            plt.title("Interactive Scatter Plot")
            return plt.gcf()
