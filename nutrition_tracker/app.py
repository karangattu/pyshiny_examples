import random
import pandas as pd
from datetime import datetime
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

# Sample data for nutrition tracking
nutrition_data = pd.DataFrame({
    "date": pd.date_range(start=datetime.now().date(), periods=30, freq="D"),
    "calories": [random.randint(1500, 2500) for _ in range(30)],
    "protein": [random.randint(50, 150) for _ in range(30)],
    "carbs": [random.randint(150, 350) for _ in range(30)],
    "fat": [random.randint(50, 100) for _ in range(30)]
})

app_ui = ui.page_fluid(
    ui.panel_title("Nutrition Tracker"),
    ui.layout_column_wrap(
        ui.input_date_range("date_range", "Select date range", start=nutrition_data["date"].min(), end=nutrition_data["date"].max()),
        ui.output_table("nutrition_table"),
        ui.output_plot("nutrition_plot"),
        width=1/2
    )
)

def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def filtered_data():
        start_date, end_date = input.date_range()
        req(start_date is not None and end_date is not None)
        return nutrition_data[(nutrition_data["date"] >= start_date) & (nutrition_data["date"] <= end_date)]

    @render.table
    def nutrition_table():
        return filtered_data()

    @render.plot
    def nutrition_plot():
        data = filtered_data()
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(data["date"], data["calories"], label="Calories")
        ax.plot(data["date"], data["protein"], label="Protein")
        ax.plot(data["date"], data["carbs"], label="Carbs")
        ax.plot(data["date"], data["fat"], label="Fat")
        ax.legend()
        ax.set_xlabel("Date")
        ax.set_ylabel("Amount")
        ax.set_title("Nutrition Tracker")
        return fig

app = App(app_ui, server)