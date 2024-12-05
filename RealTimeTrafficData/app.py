from datetime import datetime, timedelta
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, reactive, render, ui

# Generate synthetic data
def generate_traffic_data(n_locations=10):
    locations = [f"Location {i+1}" for i in range(n_locations)]
    current_time = datetime.now()
    times = [current_time - timedelta(minutes=i) for i in range(60)]
    
    data = []
    for t in times:
        for loc in locations:
            data.append({
                'timestamp': t,
                'location': loc,
                'congestion_level': random.randint(0, 100),
                'accidents': random.randint(0, 3),
                'road_closure': random.choice([True, False]),
            })
    
    return pd.DataFrame(data)

# UI
app_ui = ui.page_fluid(
    ui.panel_title("Traffic Monitoring Dashboard"),
    
    ui.layout_sidebar(
        ui.sidebar(
            ui.h4("Controls"),
            ui.input_select(
                "location",
                "Select Location",
                choices=["All"] + [f"Location {i+1}" for i in range(10)]
            ),
            ui.input_checkbox_group(
                "metrics",
                "Select Metrics",
                choices=["Congestion", "Accidents", "Road Closures"],
                selected=["Congestion"]
            ),
            ui.input_slider(
                "time_window",
                "Time Window (minutes)",
                min=5,
                max=60,
                value=30,
                step=5
            ),
            ui.input_action_button(
                "refresh",
                "Refresh Data",
                class_="btn-primary"
            )
        ),
        
        ui.layout_column_wrap(
            ui.value_box(
                "Average Congestion",
                ui.output_text("avg_congestion"),
                showcase=ui.tags.i(class_="fa-solid fa-car", style="font-size: 2rem;"),
                theme="warning"
            ),
            ui.value_box(
                "Total Accidents",
                ui.output_text("total_accidents"),
                showcase=ui.tags.i(class_="fa-solid fa-car-burst", style="font-size: 2rem;"),
                theme="danger"
            ),
            ui.value_box(
                "Active Road Closures",
                ui.output_text("road_closures"),
                showcase=ui.tags.i(class_="fa-solid fa-road-barrier", style="font-size: 2rem;"),
                theme="info"
            ),
        ),
        
        ui.card(
            ui.card_header("Traffic Trends"),
            ui.output_plot("trend_plot")
        ),
        
        ui.card(
            ui.card_header("Current Status"),
            ui.output_table("status_table")
        )
    ),
)

def server(input, output, session):
    # Reactive data source
    @reactive.calc
    def traffic_data():
        input.refresh()  # Add dependency on refresh button
        return generate_traffic_data()

    @reactive.calc
    def filtered_data():
        df = traffic_data()
        window = timedelta(minutes=input.time_window())
        df = df[df['timestamp'] >= datetime.now() - window]
        
        if input.location() != "All":
            df = df[df['location'] == input.location()]
            
        return df

    # Value box outputs
    @render.text
    def avg_congestion():
        df = filtered_data()
        return f"{df['congestion_level'].mean():.1f}%"

    @render.text
    def total_accidents():
        df = filtered_data()
        return str(df['accidents'].sum())

    @render.text
    def road_closures():
        df = filtered_data()
        return str(df['road_closure'].sum())

    # Trend plot
    @render.plot
    def trend_plot():
        df = filtered_data()
        metrics = input.metrics()
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if "Congestion" in metrics:
            congestion_data = df.groupby('timestamp')['congestion_level'].mean()
            ax.plot(congestion_data.index, congestion_data.values, 
                   label='Congestion Level (%)', color='orange')
        
        if "Accidents" in metrics:
            accidents_data = df.groupby('timestamp')['accidents'].sum()
            ax2 = ax.twinx()
            ax2.plot(accidents_data.index, accidents_data.values, 
                    label='Accidents', color='red', linestyle='--')
            ax2.set_ylabel('Number of Accidents')
        
        if "Road Closures" in metrics:
            closures_data = df.groupby('timestamp')['road_closure'].sum()
            if "Accidents" not in metrics:
                ax2 = ax.twinx()
            ax2.plot(closures_data.index, closures_data.values, 
                    label='Road Closures', color='blue', linestyle=':')
        
        ax.set_xlabel('Time')
        ax.set_ylabel('Congestion Level (%)')
        
        # Combine legends if necessary
        lines1, labels1 = ax.get_legend_handles_labels()
        if any(m in metrics for m in ["Accidents", "Road Closures"]):
            lines2, labels2 = ax2.get_legend_handles_labels()
            ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
        else:
            ax.legend(loc='upper left')
            
        plt.title('Traffic Metrics Over Time')
        return fig

    # Status table
    @render.table
    def status_table():
        df = filtered_data()
        latest = df.groupby('location').last().reset_index()
        
        # Format the data for display
        display_df = latest[['location', 'congestion_level', 'accidents', 'road_closure']]
        display_df.columns = ['Location', 'Congestion Level (%)', 'Active Accidents', 'Road Closure']
        return display_df

app = App(app_ui, server)