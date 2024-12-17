import datetime
from datetime import date, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, ui, render, reactive

# Generate sample data functions remain the same
def generate_workout_data():
    # ... (keep existing function as is)
    pass

def generate_goals_data():
    # ... (keep existing function as is)
    pass

# Updated App UI with nav_panel instead of nav
app_ui = ui.page_fluid(
    ui.head_content(
        ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">')
    ),
    ui.panel_title("Personal Fitness Tracker"),
    
    ui.navset_tab(
        ui.nav_panel("Dashboard",
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_date_range(
                        "date_range",
                        "Date Range",
                        start=date.today() - timedelta(days=30),
                        end=date.today()
                    ),
                    ui.input_selectize(
                        "activities",
                        "Select Activities",
                        choices=['Running', 'Cycling', 'Swimming', 'Weight Training'],
                        selected=['Running', 'Cycling', 'Swimming', 'Weight Training'],
                        multiple=True
                    ),
                ),
                ui.layout_column_wrap(
                    ui.value_box(
                        "Total Workouts",
                        ui.output_text("total_workouts"),
                        showcase=ui.tags.i(class_="fa-solid fa-dumbbell", 
                                         style="font-size: 2rem;"),
                        theme="bg-primary"
                    ),
                    ui.value_box(
                        "Total Duration (hrs)",
                        ui.output_text("total_duration"),
                        showcase=ui.tags.i(class_="fa-solid fa-clock", 
                                         style="font-size: 2rem;"),
                        theme="bg-success"
                    ),
                    ui.value_box(
                        "Total Calories",
                        ui.output_text("total_calories"),
                        showcase=ui.tags.i(class_="fa-solid fa-fire", 
                                         style="font-size: 2rem;"),
                        theme="bg-warning"
                    ),
                ),
                ui.card(
                    ui.card_header("Activity Distribution"),
                    ui.output_plot("activity_dist_plot")
                ),
                ui.layout_column_wrap(
                    ui.card(
                        ui.card_header("Daily Duration Trend"),
                        ui.output_plot("duration_trend_plot")
                    ),
                    ui.card(
                        ui.card_header("Weekly Progress vs Goals"),
                        ui.output_plot("goals_progress_plot")
                    ),
                )
            )
        ),
        
        ui.nav_panel("Activity Log",
            ui.card(
                ui.card_header("Recent Activities"),
                ui.output_data_frame("activity_table")
            )
        ),
        
        ui.nav_panel("Goals",
            ui.card(
                ui.card_header("Weekly Goals"),
                ui.output_data_frame("goals_table")
            )
        )
    )
)

# Server function remains the same
def server(input, output, session):
    # ... (keep existing server code as is)
    pass

app = App(app_ui, server)