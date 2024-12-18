import datetime
import random
import numpy as np
import pandas as pd
import folium
from datetime import datetime, timedelta

from shiny import App, reactive, render, ui

# Synthetic Data Generation
def generate_traffic_data(num_points=50):
    """Generate synthetic traffic congestion and accident data."""
    locations = [
        (40.7128, -74.0060),   # New York City
        (40.7484, -73.9857),   # Manhattan
        (40.6782, -73.9442),   # Brooklyn
        (40.7282, -73.7949),   # Queens
    ]
    
    data = {
        'timestamp': [],
        'latitude': [],
        'longitude': [],
        'congestion_level': [],
        'accident_severity': [],
        'road_closure': []
    }
    
    for _ in range(num_points):
        loc = random.choice(locations)
        data['timestamp'].append(datetime.now() - timedelta(hours=random.randint(0, 24)))
        data['latitude'].append(loc[0] + random.uniform(-0.05, 0.05))
        data['longitude'].append(loc[1] + random.uniform(-0.05, 0.05))
        data['congestion_level'].append(random.randint(1, 10))
        data['accident_severity'].append(random.choice(['Low', 'Medium', 'High']))
        data['road_closure'].append(random.choice([True, False]))
    
    return pd.DataFrame(data)

# Generate initial dataset
traffic_df = generate_traffic_data()

app_ui = ui.page_fluid(
    ui.head_content(
        ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">')
    ),
    ui.panel_title("Real-Time Traffic Monitoring Dashboard"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_slider("congestion_level", "Congestion Level Threshold", 
                             min=1, max=10, value=5),
            ui.input_checkbox_group("severity", "Accident Severity", 
                                    choices=["Low", "Medium", "High"], 
                                    selected=["Low", "Medium", "High"]),
            ui.input_switch("road_closure", "Show Road Closures"),
            ui.input_action_button("refresh", "Refresh Data", 
                                   class_="btn-primary"),
        ),
        ui.layout_columns(
            ui.card(
                ui.card_header("Traffic Map"),
                ui.output_ui("traffic_map"),
                full_screen=True
            ),
            ui.card(
                ui.card_header("Traffic Statistics"),
                ui.output_data_frame("traffic_stats"),
                height="500px"
            ),
            col_widths=[8, 4]
        )
    )
)

def server(input, output, session):
    # Use a reactive value to store traffic data
    traffic_data = reactive.Value(traffic_df)

    @reactive.calc
    def filtered_traffic_data():
        df = traffic_data.get().copy()
        
        # Filter by congestion level
        df = df[df['congestion_level'] >= input.congestion_level()]
        
        # Filter by accident severity
        df = df[df['accident_severity'].isin(input.severity())]
        
        # Filter by road closure
        if input.road_closure():
            df = df[df['road_closure']]
        
        return df

    @render.ui
    def traffic_map():
        df = filtered_traffic_data()
        
        m = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
        
        # Color mapping for severity
        severity_colors = {
            'Low': 'green',
            'Medium': 'orange',
            'High': 'red'
        }
        
        # Add markers for each traffic point
        for _, row in df.iterrows():
            color = severity_colors.get(row['accident_severity'], 'blue')
            
            popup_text = f"""
            Congestion: {row['congestion_level']}/10
            Severity: {row['accident_severity']}
            Road Closure: {'Yes' if row['road_closure'] else 'No'}
            Timestamp: {row['timestamp']}
            """
            
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=row['congestion_level'] * 2,
                popup=popup_text,
                color=color,
                fill=True,
                fill_color=color
            ).add_to(m)
        
        return ui.HTML(m._repr_html_())

    @render.data_frame
    def traffic_stats():
        df = filtered_traffic_data()
        
        stats = pd.DataFrame({
            'Metric': [
                'Total Incidents', 
                'Average Congestion', 
                'Road Closures', 
                'Low Severity', 
                'Medium Severity', 
                'High Severity'
            ],
            'Value': [
                len(df),
                round(df['congestion_level'].mean(), 2) if len(df) > 0 else 0,
                df['road_closure'].sum(),
                len(df[df['accident_severity'] == 'Low']),
                len(df[df['accident_severity'] == 'Medium']),
                len(df[df['accident_severity'] == 'High'])
            ]
        })
        
        return render.DataGrid(stats)

    @reactive.effect
    @reactive.event(input.refresh)
    def _():
        # Update the reactive value with new data
        traffic_data.set(generate_traffic_data())

app = App(app_ui, server)