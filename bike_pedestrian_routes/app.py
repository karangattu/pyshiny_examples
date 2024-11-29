import random
from datetime import datetime
from typing import Tuple

import folium
import pandas as pd
from folium.plugins import MarkerCluster
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

# Sample data for bike and pedestrian routes
routes_data = pd.DataFrame(
    {
        "name": ["Route A", "Route B", "Route C", "Route D", "Route E"],
        "type": ["Bike", "Bike", "Pedestrian", "Pedestrian", "Bike"],
        "distance": [5.2, 8.1, 3.7, 2.9, 6.5],
        "duration": [45, 60, 30, 25, 50],
        "start_lat": [40.730610, 40.741820, 40.750930, 40.728540, 40.735790],
        "start_lon": [-73.997282, -73.989120, -73.983450, -73.992180, -73.991230],
        "end_lat": [40.734520, 40.747930, 40.754810, 40.732450, 40.740680],
        "end_lon": [-73.992180, -73.984560, -73.978920, -73.998310, -73.986540],
    }
)

app_ui = ui.page_fluid(
    ui.panel_title("Bike and Pedestrian Route Planner"),
    ui.layout_column_wrap(
        ui.input_select(
            "route_type", "Route Type", ["All", "Bike", "Pedestrian"], selected="All"
        ),
        ui.input_slider(
            "max_distance", "Maximum Distance (km)", min=0, max=20, value=10, step=0.5
        ),
        ui.input_slider(
            "max_duration", "Maximum Duration (min)", min=0, max=120, value=60, step=5
        ),
        width=1 / 3,
    ),
    ui.output_ui("route_map"),
    ui.output_table("route_table"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def filtered_routes():
        df = routes_data.copy()
        if input.route_type() != "All":
            df = df[df["type"] == input.route_type()]
        df = df[df["distance"] <= input.max_distance()]
        df = df[df["duration"] <= input.max_duration()]
        return df

    @render.ui
    def route_map():
        m = folium.Map(location=[40.730610, -73.997282], zoom_start=13)
        marker_cluster = MarkerCluster().add_to(m)

        for _, row in filtered_routes().iterrows():
            folium.Marker(
                location=[row["start_lat"], row["start_lon"]],
                popup=f"{row['name']} ({row['type']}), {row['distance']}km, {row['duration']}min",
                icon=folium.Icon(color="red" if row["type"] == "Bike" else "green"),
            ).add_to(marker_cluster)

        return ui.HTML(m._repr_html_())

    @render.table
    def route_table():
        return filtered_routes()[["name", "type", "distance", "duration"]]


app = App(app_ui, server)
