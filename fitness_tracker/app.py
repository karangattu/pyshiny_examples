import datetime
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta

from shiny import App, reactive, render, ui

# Synthetic Data Generation
def generate_fitness_data():
    """Generate synthetic fitness tracking data."""
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date.today()
    
    # Workout Types
    workout_types = [
        "Weight Training", 
        "Cardio", 
        "Yoga", 
        "Running", 
        "Swimming", 
        "Cycling"
    ]
    
    # Goals
    goals = {
        "Weight Training": {"target_minutes": 180, "target_intensity": "High"},
        "Cardio": {"target_minutes": 150, "target_intensity": "Moderate"},
        "Yoga": {"target_minutes": 120, "target_intensity": "Low"},
        "Running": {"target_minutes": 120, "target_intensity": "High"},
        "Swimming": {"target_minutes": 90, "target_intensity": "Moderate"},
        "Cycling": {"target_minutes": 120, "target_intensity": "High"}
    }
    
    # Generate workout log
    workout_log = []
    current_date = start_date
    while current_date <= end_date:
        if random.random() < 0.7:  # 70% chance of workout on a day
            workout = random.choice(workout_types)
            duration = max(30, min(180, int(np.random.normal(goals[workout]["target_minutes"], 30))))
            intensity = random.choice(["Low", "Moderate", "High"])
            
            workout_log.append({
                "date": current_date,
                "workout_type": workout,
                "duration": duration,
                "intensity": intensity
            })
        
        current_date += timedelta(days=1)
    
    return pd.DataFrame(workout_log), goals

# Generate fitness data
fitness_df, fitness_goals = generate_fitness_data()

# Shiny App
app_ui = ui.page_fluid(
    ui.panel_title("Personal Fitness Goal Tracker"),
    
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select(
                "workout_type", 
                "Select Workout Type", 
                list(fitness_goals.keys())
            ),
            ui.input_date_range(
                "date_range", 
                "Select Date Range", 
                start=fitness_df['date'].min(), 
                end=fitness_df['date'].max()
            ),
        ),
        
        ui.layout_columns(
            ui.card(
                ui.card_header("Workout Duration"),
                ui.output_plot("duration_plot")
            ),
            ui.card(
                ui.card_header("Workout Intensity"),
                ui.output_plot("intensity_plot")
            ),
            col_widths=[6, 6]
        ),
        
        ui.layout_columns(
            ui.value_box(
                "Total Workouts",
                ui.output_text("total_workouts"),
                showcase=ui.tags.i(class_="fa-solid fa-dumbbell", style="font-size: 2rem;"),
                theme="bg-gradient-blue-purple"
            ),
            ui.value_box(
                "Average Duration",
                ui.output_text("avg_duration"),
                showcase=ui.tags.i(class_="fa-solid fa-clock", style="font-size: 2rem;"),
                theme="bg-gradient-green-teal"
            ),
            col_widths=[6, 6]
        )
    )
)

def server(input, output, session):
    @reactive.calc
    def filtered_data():
        start_date = datetime.combine(input.date_range()[0], datetime.min.time())
        end_date = datetime.combine(input.date_range()[1], datetime.max.time())
        
        filtered_df = fitness_df[
            (fitness_df['date'] >= start_date) & 
            (fitness_df['date'] <= end_date) & 
            (fitness_df['workout_type'] == input.workout_type())
        ]
        
        return filtered_df

    @render.plot
    def duration_plot():
        df = filtered_data()
        
        plt.figure(figsize=(10, 4))
        plt.plot(df['date'], df['duration'], marker='o')
        plt.title(f"{input.workout_type()} - Duration Over Time")
        plt.xlabel("Date")
        plt.ylabel("Duration (minutes)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        return plt.gcf()

    @render.plot
    def intensity_plot():
        df = filtered_data()
        
        intensity_map = {"Low": 1, "Moderate": 2, "High": 3}
        df['intensity_numeric'] = df['intensity'].map(intensity_map)
        
        plt.figure(figsize=(10, 4))
        plt.bar(df['date'], df['intensity_numeric'], 
                tick_label=[d.strftime('%Y-%m-%d') for d in df['date']])
        plt.title(f"{input.workout_type()} - Intensity")
        plt.xlabel("Date")
        plt.ylabel("Intensity")
        plt.yticks([1, 2, 3], ["Low", "Moderate", "High"])
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        return plt.gcf()

    @render.text
    def total_workouts():
        df = filtered_data()
        return str(len(df))

    @render.text
    def avg_duration():
        df = filtered_data()
        return f"{df['duration'].mean():.1f} minutes" if not df.empty else "N/A"

app = App(app_ui, server)