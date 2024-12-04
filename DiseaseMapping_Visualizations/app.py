import datetime
import random
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from shiny import App, reactive, render, ui
from shinywidgets import output_widget, render_widget

# Synthetic Data Generation
def generate_outbreak_data():
    """Generate synthetic disease outbreak data for multiple regions."""
    regions = [
        "California", "Texas", "New York", "Florida", "Illinois", 
        "Pennsylvania", "Ohio", "Georgia", "North Carolina", "Michigan"
    ]
    
    diseases = ["COVID-19", "Influenza", "RSV", "Measles"]
    
    data = []
    base_date = datetime.date(2023, 1, 1)
    
    for disease in diseases:
        for region in regions:
            for month in range(1, 13):
                # Simulate varying outbreak intensity
                base_cases = random.randint(50, 500)
                vaccination_rate = round(random.uniform(0.3, 0.9), 2)
                
                data.append({
                    "Disease": disease,
                    "Region": region,
                    "Date": base_date.replace(month=month),
                    "Cases": base_cases,
                    "Vaccination_Rate": vaccination_rate,
                    "Hospitalization_Rate": round(random.uniform(0.01, 0.15), 3)
                })
    
    return pd.DataFrame(data)

# Generate dataset
outbreak_df = generate_outbreak_data()

# Shiny App UI
app_ui = ui.page_fluid(
    ui.panel_title("Disease Outbreak Visualization Dashboard"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_selectize(
                "disease_select", 
                "Select Disease", 
                choices=outbreak_df["Disease"].unique().tolist(),
                selected="COVID-19"
            ),
            ui.input_select(
                "map_metric", 
                "Map Metric", 
                choices=[
                    "Cases", 
                    "Vaccination_Rate", 
                    "Hospitalization_Rate"
                ]
            ),
            ui.input_date_range(
                "date_range", 
                "Date Range", 
                start=outbreak_df["Date"].min(), 
                end=outbreak_df["Date"].max()
            )
        ),
        ui.layout_columns(
            ui.card(
                ui.card_header("Geographic Distribution"),
                output_widget("outbreak_map")
            ),
            ui.card(
                ui.card_header("Time Series Analysis"),
                output_widget("time_series_plot")
            )
        )
    )
)

def server(input, output, session):
    @reactive.calc
    def filtered_data():
        df = outbreak_df.copy()
        
        # Filter by disease
        df = df[df["Disease"] == input.disease_select()]
        
        # Filter by date range
        df = df[
            (df["Date"] >= pd.to_datetime(input.date_range()[0])) & 
            (df["Date"] <= pd.to_datetime(input.date_range()[1]))
        ]
        
        return df

    @render_widget
    def outbreak_map():
        df = filtered_data()
        
        # Aggregate data by region
        map_data = df.groupby("Region")[input.map_metric()].mean().reset_index()
        
        fig = px.choropleth(
            map_data, 
            locations="Region", 
            locationmode="USA-states", 
            color=input.map_metric(),
            scope="usa",
            color_continuous_scale="Viridis",
            title=f"{input.disease_select()} {input.map_metric()} Distribution"
        )
        
        fig.update_layout(height=500)
        return fig

    @render_widget
    def time_series_plot():
        df = filtered_data()
        
        # Time series aggregation
        time_series_data = df.groupby(["Date", "Disease"])[input.map_metric()].mean().reset_index()
        
        fig = px.line(
            time_series_data, 
            x="Date", 
            y=input.map_metric(), 
            color="Disease",
            title=f"{input.map_metric()} Over Time"
        )
        
        fig.update_layout(height=500)
        return fig

app = App(app_ui, server)