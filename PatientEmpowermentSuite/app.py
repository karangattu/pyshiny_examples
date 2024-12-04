import datetime
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, reactive, render, ui

# Synthetic Patient Data Generation
def generate_patient_data():
    # Simulated patient profile
    patient = {
        "name": "Emily Johnson",
        "age": 35,
        "gender": "Female",
        "conditions": ["Hypertension", "Type 2 Diabetes"],
        "medications": [
            {"name": "Metformin", "dosage": "500mg", "frequency": "Twice daily"},
            {"name": "Lisinopril", "dosage": "10mg", "frequency": "Once daily"}
        ]
    }
    return patient

def generate_medication_adherence_data():
    # Simulated medication adherence data
    dates = pd.date_range(end=datetime.date.today(), periods=30)
    adherence = pd.DataFrame({
        'date': dates,
        'Metformin': np.random.choice([0, 1], size=30, p=[0.2, 0.8]),
        'Lisinopril': np.random.choice([0, 1], size=30, p=[0.15, 0.85])
    })
    return adherence

def generate_health_quiz_questions():
    return [
        {
            "question": "What is the recommended daily water intake?",
            "options": ["2 cups", "4 cups", "8 cups", "12 cups"],
            "correct_answer": "8 cups",
            "explanation": "8 cups (64 ounces) is generally recommended for maintaining proper hydration."
        },
        {
            "question": "How many minutes of moderate exercise are recommended per week?",
            "options": ["30 minutes", "60 minutes", "150 minutes", "240 minutes"],
            "correct_answer": "150 minutes",
            "explanation": "150 minutes of moderate exercise per week supports overall health and disease prevention."
        }
    ]

def generate_health_tips():
    return [
        "Stay hydrated by drinking water throughout the day.",
        "Get at least 7-8 hours of sleep each night.",
        "Include fruits and vegetables in every meal.",
        "Take medications at the same time daily to maintain consistency."
    ]

app_ui = ui.page_fluid(
    ui.head_content(
        ui.tags.style("""
            .health-tip { background-color: #f0f8ff; padding: 15px; border-radius: 5px; margin-bottom: 10px; }
            .quiz-card { border: 1px solid #ddd; padding: 15px; margin-bottom: 10px; }
        """)
    ),
    ui.panel_title("Patient Health Companion"),
    ui.navset_card_pill(
        ui.nav_panel("Profile", 
            ui.card(
                ui.output_text_verbatim("patient_profile"),
                ui.output_plot("medication_adherence_plot")
            )
        ),
        ui.nav_panel("Medication Management", 
            ui.card(
                ui.output_text_verbatim("medication_details"),
                ui.output_ui("medication_reminders")
            )
        ),
        ui.nav_panel("Health Education", 
            ui.card(
                ui.h4("Daily Health Tips"),
                ui.output_ui("health_tips"),
                ui.h4("Health Quiz"),
                ui.output_ui("health_quiz")
            )
        ),
        id="nav_tabs"
    )
)

def server(input, output, session):
    # Patient Profile Section
    patient_data = generate_patient_data()
    medication_adherence = generate_medication_adherence_data()

    @render.text
    def patient_profile():
        return f"""
Patient Name: {patient_data['name']}
Age: {patient_data['age']}
Gender: {patient_data['gender']}
Current Health Conditions: {', '.join(patient_data['conditions'])}
"""

    @render.plot
    def medication_adherence_plot():
        plt.figure(figsize=(10, 4))
        plt.title("Medication Adherence Tracking")
        plt.plot(medication_adherence['date'], medication_adherence['Metformin'], label='Metformin')
        plt.plot(medication_adherence['date'], medication_adherence['Lisinopril'], label='Lisinopril')
        plt.xlabel("Date")
        plt.ylabel("Adherence (1: Taken, 0: Missed)")
        plt.legend()
        return plt.gcf()

    @render.text
    def medication_details():
        details = "Medication Details:\n"
        for med in patient_data['medications']:
            details += f"{med['name']} - {med['dosage']} {med['frequency']}\n"
        return details

    @render.ui
    def medication_reminders():
        reminders = ui.TagList()
        for med in patient_data['medications']:
            reminders.append(
                ui.div(
                    {"class": "alert alert-info"},
                    f"Reminder: Take {med['name']} {med['frequency']}"
                )
            )
        return reminders

    # Health Education Section
    health_quiz_questions = generate_health_quiz_questions()
    quiz_state = reactive.Value({"current_question": 0, "score": 0})

    @render.ui
    def health_tips():
        tips = generate_health_tips()
        tip_list = ui.TagList()
        for tip in tips:
            tip_list.append(
                ui.div({"class": "health-tip"}, tip)
            )
        return tip_list

    @render.ui
    def health_quiz():
        current_question_index = quiz_state.get()["current_question"]
        
        if current_question_index < len(health_quiz_questions):
            question = health_quiz_questions[current_question_index]
            return ui.div(
                {"class": "quiz-card"},
                ui.h5(question["question"]),
                ui.input_radio_buttons(
                    "quiz_answer", 
                    "Select your answer:", 
                    question["options"]
                ),
                ui.input_action_button("submit_answer", "Submit Answer")
            )
        else:
            return ui.div(
                ui.h4("Quiz Completed!"),
                ui.p(f"Your score: {quiz_state.get()['score']} out of {len(health_quiz_questions)}")
            )

    @reactive.effect
    @reactive.event(input.submit_answer)
    def check_answer():
        current_state = quiz_state.get()
        current_question = health_quiz_questions[current_state["current_question"]]
        
        if input.quiz_answer() == current_question["correct_answer"]:
            current_state["score"] += 1
        
        current_state["current_question"] += 1
        quiz_state.set(current_state)

app = App(app_ui, server)