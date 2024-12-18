import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

# Sample data for health education, medication management, and appointments
health_topics = [
    {"title": "Diabetes Management", "description": "Learn about managing your diabetes through diet, exercise, and medication."},
    {"title": "Heart Health", "description": "Discover ways to keep your heart healthy and reduce your risk of heart disease."},
    {"title": "Stress Reduction", "description": "Explore effective techniques to manage stress and improve your overall well-being."},
    {"title": "Nutrition Basics", "description": "Get an overview of a balanced diet and healthy eating habits."},
]

medications = [
    {"name": "Metformin", "description": "Used to treat type 2 diabetes", "frequency": "Twice daily"},
    {"name": "Lisinopril", "description": "Used to treat high blood pressure", "frequency": "Once daily"},
    {"name": "Atorvastatin", "description": "Used to lower cholesterol", "frequency": "Once daily"},
    {"name": "Ibuprofen", "description": "Used to reduce pain and inflammation", "frequency": "As needed"},
]

appointments = [
    {"date": datetime.now() + timedelta(days=7), "type": "Annual checkup", "provider": "Dr. Smith"},
    {"date": datetime.now() + timedelta(days=14), "type": "Diabetes follow-up", "provider": "Dr. Johnson"},
    {"date": datetime.now() + timedelta(days=30), "type": "Flu shot", "provider": "Nurse Practitioner"},
    {"date": datetime.now() + timedelta(days=45), "type": "Physical therapy", "provider": "Dr. Lee"},
]

app_ui = ui.page_fluid(
    ui.panel_title("Health Empowerment App"),
    ui.layout_column_wrap(
        ui.value_box(
            "Health Education",
            len(health_topics),
            "Explore various health topics",
            showcase=ui.tags.i(class_="fa-solid fa-book", style="font-size: 2rem;"),
            theme="bg-gradient-blue-purple",
        ),
        ui.value_box(
            "Medication Management",
            len(medications),
            "Manage your medications",
            showcase=ui.tags.i(class_="fa-solid fa-pills", style="font-size: 2rem;"),
            theme="bg-gradient-orange-red",
        ),
        ui.value_box(
            "Upcoming Appointments",
            len(appointments),
            "Stay on top of your appointments",
            showcase=ui.tags.i(class_="fa-solid fa-calendar-check", style="font-size: 2rem;"),
            theme="bg-gradient-green-teal",
        ),
        width=1 / 3,
    ),
    ui.hr(),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Health Education"),
            ui.input_select("health_topic", "Select a topic", [t["title"] for t in health_topics]),
            ui.output_text_verbatim("health_description"),
            ui.input_action_button("health_quiz", "Take Quiz"),
            ui.output_ui("health_quiz_result"),
        ),
        ui.card(
            ui.card_header("Medication Management"),
            ui.input_select("medication", "Select a medication", [m["name"] for m in medications]),
            ui.output_text_verbatim("medication_details"),
            ui.input_action_button("medication_reminder", "Set Reminder"),
            ui.output_text_verbatim("medication_reminder_status"),
        ),
        ui.card(
            ui.card_header("Upcoming Appointments"),
            ui.output_table("appointment_table"),
        ),
        width=1,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    # Health Education
    @render.text
    def health_description():
        topic = next((t for t in health_topics if t["title"] == input.health_topic()), None)
        if topic:
            return topic["description"]
        else:
            return "No topic selected"

    @reactive.effect
    @reactive.event(input.health_quiz)
    def health_quiz():
        topic = next((t for t in health_topics if t["title"] == input.health_topic()), None)
        if topic:
            score = random.randint(0, 100)
            ui.notification_show(
                f"You scored {score}% on the {topic['title']} quiz!",
                duration=5,
                type="success",
            )
            ui.update_ui("health_quiz_result", ui.p(f"Your score: {score}%"))
        else:
            ui.update_ui("health_quiz_result", ui.p("No topic selected"))

    # Medication Management
    @render.text
    def medication_details():
        medication = next((m for m in medications if m["name"] == input.medication()), None)
        if medication:
            return f"{medication['name']}: {medication['description']} (Taken {medication['frequency']})"
        else:
            return "No medication selected"

    @reactive.effect
    @reactive.event(input.medication_reminder)
    def medication_reminder():
        medication = next((m for m in medications if m["name"] == input.medication()), None)
        if medication:
            ui.notification_show(
                f"Reminder set for {medication['name']} ({medication['frequency']})",
                duration=5,
                type="success",
            )
            ui.update_ui("medication_reminder_status", ui.p("Reminder set"))
        else:
            ui.update_ui("medication_reminder_status", ui.p("No medication selected"))

    # Upcoming Appointments
    @render.table
    def appointment_table():
        return pd.DataFrame(appointments)

app = App(app_ui, server)