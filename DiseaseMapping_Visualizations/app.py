import numpy as np
import pandas as pd
import folium
from folium.plugins import HeatMap, MarkerCluster
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Generate sample data
np.random.seed(42)
countries = ["USA", "Canada", "Mexico", "Brazil", "UK", "France", "Germany", "Italy", "China", "Japan"]
lat = [38.9072, 45.4215, 23.6345, -15.7801, 51.5074, 48.8566, 52.5200, 41.9028, 39.9042, 36.2048]
lon = [-77.0369, -75.6972, -102.5528, -47.9292, -0.1278, 2.3522, 13.4050, 12.4964, 116.4074, 138.2529]
outbreak_cases = np.random.randint(100, 10000, size=len(countries))
vaccination_rate = np.random.uniform(0.3, 0.9, size=len(countries))

disease_data = pd.DataFrame({
    "country": countries,
    "latitude": lat,
    "longitude": lon,
    "outbreak_cases": outbreak_cases,
    "vaccination_rate": vaccination_rate
})

app_ui = ui.page_fluid(
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Disease Outbreak Map"),
            ui.output_ui("outbreak_map"),
            height="500px",
            width="100%",
        ),
        ui.card(
            ui.card_header("Vaccination Rate Map"),
            ui.output_ui("vaccination_map"),
            height="500px",
            width="100%",
        ),
    )
)

def server(input, output, session):
    @render.ui
    def outbreak_map():
        m = folium.Map(location=[40, -95], zoom_start=4)
        marker_cluster = MarkerCluster().add_to(m)

        for _, row in disease_data.iterrows():
            folium.Marker(
                location=[row["latitude"], row["longitude"]],
                popup=f"{row['country']}: {row['outbreak_cases']} cases",
                icon=folium.Icon(color="red", icon="medkit", prefix="fa"),
            ).add_to(marker_cluster)

        HeatMap(
            data=disease_data[["latitude", "longitude", "outbreak_cases"]].values,
            radius=20,
            blur=15,
            max_zoom=10,
        ).add_to(m)

        return ui.HTML(m._repr_html_())

    @render.ui
    def vaccination_map():
        m = folium.Map(location=[40, -95], zoom_start=4)
        marker_cluster = MarkerCluster().add_to(m)

        for _, row in disease_data.iterrows():
            folium.Marker(
                location=[row["latitude"], row["longitude"]],
                popup=f"{row['country']}: {row['vaccination_rate']*100:.2f}% vaccinated",
                icon=folium.Icon(
                    color="green" if row["vaccination_rate"] >= 0.7 else "orange",
                    icon="syringe",
                    prefix="fa",
                ),
            ).add_to(marker_cluster)

        return ui.HTML(m._repr_html_())

app = App(app_ui, server)