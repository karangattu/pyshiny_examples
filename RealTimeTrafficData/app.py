import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Generate sample data
np.random.seed(42)
num_roads = 10
num_accidents = 20
num_closures = 5

road_names = [f"Road {i+1}" for i in range(num_roads)]
road_congestion = np.random.randint(1, 6, size=num_roads)
road_accidents = np.random.choice(road_names, size=num_accidents)
road_closures = np.random.choice(road_names, size=num_closures)

traffic_data = pd.DataFrame({
    "road": road_names,
    "congestion": road_congestion,
    "accidents": road_accidents,
    "closures": road_closures
})

app_ui = ui.page_fluid(
    ui.panel_title("Traffic Visualization"),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Traffic Congestion"),
            ui.output_plot("congestion_plot"),
            height="400px",
        ),
        ui.card(
            ui.card_header("Accidents"),
            ui.output_plot("accidents_plot"),
            height="400px",
        ),
        ui.card(
            ui.card_header("Road Closures"),
            ui.output_plot("closures_plot"),
            height="400px",
        ),
        width=1/3,
    ),
)

def server(input: Inputs, output: Outputs, session: Session):
    @render.plot
    def congestion_plot():
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(traffic_data["road"], traffic_data["congestion"])
        ax.set_xlabel("Road")
        ax.set_ylabel("Congestion Level")
        ax.set_title("Traffic Congestion")
        return fig

    @render.plot
    def accidents_plot():
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(traffic_data["road"], traffic_data["road"].isin(traffic_data["accidents"]).astype(int))
        ax.set_xlabel("Road")
        ax.set_ylabel("Accidents")
        ax.set_title("Accidents")
        return fig

    @render.plot
    def closures_plot():
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(traffic_data["road"], traffic_data["road"].isin(traffic_data["closures"]).astype(int))
        ax.set_xlabel("Road")
        ax.set_ylabel("Closures")
        ax.set_title("Road Closures")
        return fig

app = App(app_ui, server)