from datetime import datetime, timedelta
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from shiny import App, ui, render, reactive

# Generate synthetic data
def generate_medication_data():
    medications = {
        "Medication A": {"dosage": "10mg", "frequency": "Daily", "time": "Morning"},
        "Medication B": {"dosage": "20mg", "frequency": "Twice daily", "time": "Morning/Night"},
        "Medication C": {"dosage": "5mg", "frequency": "Weekly", "time": "Monday"},
    }
    return medications

def generate_appointment_data():
    today = datetime.now()
    appointments = pd.DataFrame({
        "date": pd.date_range(today, today + timedelta(days=30), freq='3D'),
        "type": ["Check-up", "Blood Test", "Consultation", "Follow-up", "Review", 
                 "Physical Therapy", "Vaccination", "Screening", "Check-up", "Blood Test"],
        "doctor": ["Dr. Smith", "Dr. Johnson", "Dr. Williams", "Dr. Brown", "Dr. Davis",
                  "Dr. Miller", "Dr. Wilson", "Dr. Moore", "Dr. Taylor", "Dr. Anderson"],
        "status": ["Scheduled"] * 10
    })
    return appointments

def generate_health_metrics():
    dates = pd.date_range(datetime.now() - timedelta(days=30), datetime.now(), freq='D')
    return pd.DataFrame({
        'date': dates,
        'blood_pressure': np.random.normal(120, 5, len(dates)),
        'heart_rate': np.random.normal(75, 3, len(dates)),
        'sleep_hours': np.random.normal(7, 1, len(dates))
    })

# Quiz data
health_quiz = [
    {
        "question": "What is a normal resting heart rate?",
        "options": ["40-50 bpm", "60-100 bpm", "120-140 bpm", "150-170 bpm"],
        "correct": "60-100 bpm"
    },
    {
        "question": "Which of these is a symptom of dehydration?",
        "options": ["Dry mouth", "Watery eyes", "Runny nose", "Oily skin"],
        "correct": "Dry mouth"
    },
    {
        "question": "How many hours of sleep are recommended for adults?",
        "options": ["4-5 hours", "6-8 hours", "7-9 hours", "10-12 hours"],
        "correct": "7-9 hours"
    }
]

# UI Definition
app_ui = ui.page_navbar(
    ui.head_content(
        ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">')
    ),
    title="Patient Health Portal",
    id="navbar_id",
    nav_panel_list=[
        ui.nav_panel("Dashboard",
            ui.layout_sidebar(
                ui.sidebar(
                    ui.h3("Patient Profile"),
                    ui.input_text("name", "Name", "John Doe"),
                    ui.input_numeric("age", "Age", 45),
                    ui.input_select("condition", "Primary Condition", 
                                  ["Hypertension", "Diabetes", "Arthritis"]),
                    width=250
                ),
                ui.card(
                    ui.card_header("Health Metrics"),
                    ui.output_plot("health_metrics_plot")
                ),
                ui.layout_column_wrap(
                    ui.value_box(
                        "Medication Adherence",
                        "85%",
                        theme="success",
                        showcase=ui.tags.i(class_="fa-solid fa-pills", style="font-size: 2rem;")
                    ),
                    ui.value_box(
                        "Next Appointment",
                        ui.output_text("next_appointment"),
                        theme="info",
                        showcase=ui.tags.i(class_="fa-solid fa-calendar", style="font-size: 2rem;")
                    ),
                    width=1/2
                )
            )
        ),
        ui.nav_panel("Medications",
            ui.card(
                ui.card_header("My Medications"),
                ui.output_table("medication_schedule")
            ),
            ui.input_checkbox("med_taken", "Mark today's medications as taken")
        ),
        ui.nav_panel("Health Education",
            ui.card(
                ui.card_header("Health Quiz"),
                ui.input_select("quiz_question", "Select Question:", 
                              [f"Question {i+1}" for i in range(len(health_quiz))]),
                ui.output_text("question_text"),
                ui.output_radio_buttons("quiz_options"),
                ui.input_action_button("check_answer", "Check Answer"),
                ui.output_text("quiz_feedback")
            )
        ),
        ui.nav_panel("Appointments",
            ui.card(
                ui.card_header("Upcoming Appointments"),
                ui.output_table("appointments")
            )
        )
    ]
)

def server(input, output, session):
    # Initialize data
    medications = generate_medication_data()
    appointments = generate_appointment_data()
    health_metrics = generate_health_metrics()
    
    # Health Metrics Plot
    @render.plot
    def health_metrics_plot():
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
        
        health_metrics.plot(x='date', y='blood_pressure', ax=ax1, color='red')
        ax1.set_title('Blood Pressure')
        
        health_metrics.plot(x='date', y='heart_rate', ax=ax2, color='blue')
        ax2.set_title('Heart Rate')
        
        health_metrics.plot(x='date', y='sleep_hours', ax=ax3, color='green')
        ax3.set_title('Sleep Hours')
        
        plt.tight_layout()
        return fig

    # Medication Schedule
    @render.table
    def medication_schedule():
        med_df = pd.DataFrame.from_dict(medications, orient='index')
        med_df.index.name = 'Medication'
        med_df.reset_index(inplace=True)
        return med_df

    # Next Appointment
    @render.text
    def next_appointment():
        next_apt = appointments.iloc[0]
        return f"{next_apt['type']} with {next_apt['doctor']}\non {next_apt['date'].strftime('%Y-%m-%d')}"

    # Appointments Table
    @render.table
    def appointments():
        return appointments

    # Quiz Logic
    @render.text
    def question_text():
        q_idx = int(input.quiz_question().split()[-1]) - 1
        return health_quiz[q_idx]["question"]

    @render.radio_buttons
    def quiz_options():
        q_idx = int(input.quiz_question().split()[-1]) - 1
        return {"choices": health_quiz[q_idx]["options"]}

    @reactive.Value
    def quiz_result():
        return {"correct": 0, "total": 0}

    @render.text
    @reactive.event(input.check_answer)
    def quiz_feedback():
        q_idx = int(input.quiz_question().split()[-1]) - 1
        if input.quiz_options() == health_quiz[q_idx]["correct"]:
            quiz_result()["correct"] += 1
            return "✅ Correct! Well done!"
        return "❌ Incorrect. Try again!"

app = App(app_ui, server)