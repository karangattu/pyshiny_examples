import random

import pandas as pd
import plotly.express as px
from shiny import App, Inputs, Outputs, Session, reactive, render, ui
from shinywidgets import output_widget, render_widget

# Generate sample data
food_items = [
    "Apples",
    "Bananas",
    "Bread",
    "Chicken",
    "Eggs",
    "Milk",
    "Rice",
    "Spinach",
]
food_waste_data = pd.DataFrame(
    {
        "Item": food_items,
        "Waste (lbs)": [random.randint(1, 10) for _ in range(len(food_items))],
        "Recovered (lbs)": [random.randint(1, 5) for _ in range(len(food_items))],
    }
)

# Calculate trends
total_waste = food_waste_data["Waste (lbs)"].sum()
total_recovered = food_waste_data["Recovered (lbs)"].sum()
recovery_rate = (total_recovered / total_waste) * 100

app_ui = ui.page_fluid(
    ui.panel_title("Food Waste Reduction and Recovery"),
    ui.head_content(
        ui.HTML(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'
        )
    ),
    ui.layout_column_wrap(
        ui.value_box(
            "Total Waste",
            f"{total_waste:.2f} lbs",
            theme="bg-gradient-orange-red",
            showcase=ui.HTML('<i class="fa-solid fa-trash-can"></i>'),
            full_screen=True,
        ),
        ui.value_box(
            "Total Recovered",
            f"{total_recovered:.2f} lbs",
            theme="bg-gradient-green-teal",
            showcase=ui.HTML('<i class="fa-solid fa-recycle"></i>'),
            full_screen=True,
        ),
        ui.value_box(
            "Recovery Rate",
            f"{recovery_rate:.2f}%",
            theme="bg-gradient-blue-purple",
            showcase=ui.HTML('<i class="fa-solid fa-chart-line"></i>'),
            full_screen=True,
        ),
        ui.card(
            ui.card_header("Food Waste and Recovery"),
            ui.output_data_frame("food_waste_table"),
            height="400px",
        ),
        ui.card(
            ui.card_header("Waste and Recovery Trends"),
            output_widget("waste_trends_plot"),
            height="400px",
        ),
        ui.card(
            ui.card_header("Top 3 Wasted Items"),
            ui.output_data_frame("top_wasted_items"),
            height="200px",
        ),
        ui.card(
            ui.card_header("Top 3 Recovered Items"),
            ui.output_data_frame("top_recovered_items"),
            height="200px",
        ),
        width=1 / 2,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.data_frame
    def food_waste_table():
        return food_waste_data

    @render_widget
    def waste_trends_plot():
        fig = px.bar(
            food_waste_data,
            x="Item",
            y=["Waste (lbs)", "Recovered (lbs)"],
            barmode="group",
        )
        return fig

    @render.data_frame
    def top_wasted_items():
        top_wasted = food_waste_data.nlargest(3, "Waste (lbs)")
        return top_wasted[["Item", "Waste (lbs)"]]

    @render.data_frame
    def top_recovered_items():
        top_recovered = food_waste_data.nlargest(3, "Recovered (lbs)")
        return top_recovered[["Item", "Recovered (lbs)"]]


app = App(app_ui, server)
