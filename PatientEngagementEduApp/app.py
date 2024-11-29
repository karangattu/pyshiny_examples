import random
from datetime import datetime, timedelta
from typing import List

import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui


# Mock patient data
class Patient:
    def __init__(self, name: str, age: int, condition: str):
        self.name = name
        self.age = age
        self.condition = condition


patients: List[Patient] = [
    Patient("John Doe", 45, "Diabetes"),
    Patient("Jane Smith", 32, "Hypertension"),
    Patient("Michael Johnson", 58, "Asthma"),
    Patient("Emily Davis", 27, "Arthritis"),
    Patient("David Wilson", 41, "COPD"),
    Patient("Sarah Brown", 50, "Diabetes"),
    Patient("Robert Lee", 38, "Hypertension"),
    Patient("Maria Martinez", 65, "Arthritis"),
    Patient("James Taylor", 55, "Diabetes"),
    Patient("Linda Anderson", 47, "Asthma"),
    Patient("William Thomas", 60, "COPD"),
    Patient("Karen White", 29, "Hypertension"),
    Patient("Charles Harris", 52, "Arthritis"),
    Patient("Patricia Martin", 43, "Diabetes"),
    Patient("Thomas Thompson", 36, "Hypertension"),
    Patient("Jessica Garcia", 44, "Asthma"),
    Patient("Daniel Martinez", 59, "Arthritis"),
]


# Mock educational content
class EducationalContent:
    def __init__(self, title: str, description: str, url: str):
        self.title = title
        self.description = description
        self.url = url


educational_content = [
    EducationalContent(
        "Understanding Diabetes",
        "Learn about the causes, symptoms, and management of diabetes.",
        "https://example.com/diabetes-education",
    ),
    EducationalContent(
        "Controlling High Blood Pressure",
        "Discover effective ways to manage hypertension and improve your heart health.",
        "https://example.com/hypertension-education",
    ),
    EducationalContent(
        "Asthma Basics",
        "Get an overview of asthma, its triggers, and how to manage your symptoms.",
        "https://example.com/asthma-education",
    ),
    EducationalContent(
        "Arthritis Management",
        "Explore treatment options and lifestyle changes to manage arthritis pain.",
        "https://example.com/arthritis-education",
    ),
    EducationalContent(
        "COPD Awareness",
        "Learn about the causes, symptoms, and ways to manage chronic obstructive pulmonary disease.",
        "https://example.com/copd-education",
    ),
    EducationalContent(
        "Healthy Living Tips",
        "Discover simple tips for maintaining a healthy lifestyle and preventing chronic diseases.",
        "https://example.com/healthy-living-education",
    ),
    EducationalContent(
        "Nutrition and Wellness",
        "Explore the importance of nutrition and wellness in maintaining good health.",
        "https://example.com/nutrition-wellness-education",
    ),
    EducationalContent(
        "Exercise for Health",
        "Find out how regular exercise can improve your physical and mental well-being.",
        "https://example.com/exercise-education",
    ),
    EducationalContent(
        "Stress Management Techniques",
        "Learn effective strategies for managing stress and improving your mental health.",
        "https://example.com/stress-management-education",
    ),
    EducationalContent(
        "Sleep Hygiene Tips",
        "Discover the importance of good sleep hygiene and how to improve your sleep quality.",
        "https://example.com/sleep-hygiene-education",
    ),
    EducationalContent(
        "Preventive Health Screenings",
        "Understand the importance of preventive health screenings and early detection of diseases.",
        "https://example.com/preventive-screenings-education",
    ),
    EducationalContent(
        "Mental Health Awareness",
        "Learn about common mental health conditions and how to seek help when needed.",
        "https://example.com/mental-health-education",
    ),
]

app_ui = ui.page_fluid(
    ui.panel_title("Patient Engagement and Education"),
    ui.head_content(
        ui.HTML(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'
        )
    ),
    ui.layout_column_wrap(
        ui.value_box(
            "Patients",
            str(len(patients)),
            "Total Patients",
            showcase=ui.tags.i(
                class_="fa-solid fa-hospital-user", style="font-size: 2rem;"
            ),
            theme="purple",
        ),
        ui.value_box(
            "Conditions",
            len(set(patient.condition for patient in patients)),
            "Unique Conditions",
            showcase=ui.tags.i(
                class_="fa-solid fa-clipboard", style="font-size: 2rem;"
            ),
            theme="yellow",
        ),
        ui.value_box(
            "Engagement",
            f"{random.randint(50, 90)}%",
            "Patient Engagement",
            showcase=ui.tags.i(
                class_="fa-solid fa-chart-simple", style="font-size: 2rem;"
            ),
            theme="blue",
        ),
        width=1 / 3,
    ),
    ui.hr(),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Patient List"),
            ui.output_data_frame("patient_table"),
            height="400px",
        ),
        ui.card(
            ui.card_header("Educational Content"),
            ui.output_data_frame("content_table"),
            height="400px",
        ),
        width=1 / 2,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.data_frame
    def patient_table():
        return pd.DataFrame(
            [
                {
                    "Name": patient.name,
                    "Age": patient.age,
                    "Condition": patient.condition,
                }
                for patient in patients
            ]
        )

    @render.data_frame
    def content_table():
        return pd.DataFrame(
            [
                {
                    "Title": content.title,
                    "Description": content.description,
                    "URL": content.url,
                }
                for content in educational_content
            ]
        )


app = App(app_ui, server)
