import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from shiny import App, Inputs, Outputs, Session, render, ui

# Generate some sample medical research data
np.random.seed(42)
num_patients = 100
age = np.random.normal(50, 10, num_patients)
blood_pressure = np.random.normal(120, 20, num_patients)
cholesterol = np.random.normal(200, 40, num_patients)
diabetes_status = np.random.choice([0, 1], num_patients, p=[0.8, 0.2])
data = pd.DataFrame(
    {
        "Age": age,
        "Blood Pressure": blood_pressure,
        "Cholesterol": cholesterol,
        "Diabetes": diabetes_status,
    }
)

app_ui = ui.page_fluid(
    ui.panel_title("Medical Research Data Visualization"),
    ui.layout_column_wrap(
        ui.value_box(
            "Average Age",
            f"{data['Age'].mean():.2f}",
            "years",
            showcase=ui.HTML('<i class="fas fa-user-md"></i>'),
            theme="bg-gradient-blue-purple",
            full_screen=True,
        ),
        ui.value_box(
            "Average Blood Pressure",
            f"{data['Blood Pressure'].mean():.2f}",
            "mmHg",
            showcase=ui.HTML('<i class="fas fa-heartbeat"></i>'),
            theme="bg-gradient-orange-red",
            full_screen=True,
        ),
        ui.value_box(
            "Average Cholesterol",
            f"{data['Cholesterol'].mean():.2f}",
            "mg/dL",
            showcase=ui.HTML('<i class="fas fa-flask"></i>'),
            theme="bg-gradient-green-teal",
            full_screen=True,
        ),
        ui.value_box(
            "Diabetes Prevalence",
            f"{data['Diabetes'].mean():.2%}",
            "",
            showcase=ui.HTML('<i class="fas fa-syringe"></i>'),
            theme="bg-gradient-pink-purple",
            full_screen=True,
        ),
        width=1 / 2,
    ),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Age Distribution"),
            ui.output_plot("age_hist"),
        ),
        ui.card(
            ui.card_header("Blood Pressure Distribution"),
            ui.output_plot("bp_hist"),
        ),
        ui.card(
            ui.card_header("Cholesterol Distribution"),
            ui.output_plot("chol_hist"),
        ),
        width=1,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.plot
    def age_hist():
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(data["Age"], bins=20)
        ax.set_xlabel("Age (years)")
        ax.set_ylabel("Count")
        ax.set_title("Age Distribution")
        return fig

    @render.plot
    def bp_hist():
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(data["Blood Pressure"], bins=20)
        ax.set_xlabel("Blood Pressure (mmHg)")
        ax.set_ylabel("Count")
        ax.set_title("Blood Pressure Distribution")
        return fig

    @render.plot
    def chol_hist():
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(data["Cholesterol"], bins=20)
        ax.set_xlabel("Cholesterol (mg/dL)")
        ax.set_ylabel("Count")
        ax.set_title("Cholesterol Distribution")
        return fig


app = App(app_ui, server)
