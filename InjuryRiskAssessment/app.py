import random

import numpy as np
import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Generate some sample data for the app
age_range = list(range(18, 81))
height_range = list(range(150, 201))
weight_range = list(range(50, 151))
activity_levels = ["Sedentary", "Light", "Moderate", "Vigorous"]

data = pd.DataFrame(
    {
        "age": [random.choice(age_range) for _ in range(100)],
        "height": [random.choice(height_range) for _ in range(100)],
        "weight": [random.choice(weight_range) for _ in range(100)],
        "activity_level": [random.choice(activity_levels) for _ in range(100)],
        "injury_risk": [random.uniform(0.1, 0.9) for _ in range(100)],
    }
)

app_ui = ui.page_fluid(
    ui.panel_title("Injury Risk Assessment"),
    ui.layout_column_wrap(
        ui.input_numeric("age", "Age", min=18, max=80, value=30),
        ui.input_numeric("height", "Height (cm)", min=150, max=200, value=170),
        ui.input_numeric("weight", "Weight (kg)", min=50, max=150, value=70),
        ui.input_select(
            "activity_level", "Activity Level", activity_levels, selected="Moderate"
        ),
        width=1 / 2,
    ),
    ui.output_text_verbatim("injury_risk"),
    ui.output_text_verbatim("risk_level"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def injury_risk():
        age = input.age()
        height = input.height()
        weight = input.weight()
        activity = input.activity_level()

        # Simplified risk calculation based on the sample data
        risk = (
            0.5
            + 0.01 * (age - 30)
            + 0.005 * (weight - 70)
            - 0.1 * activity_levels.index(activity)
        )
        return f"{risk:.2f}"

    @render.text
    def risk_level():
        risk = float(injury_risk())
        if risk < 0.3:
            return "Low Risk"
        elif risk < 0.6:
            return "Moderate Risk"
        else:
            return "High Risk"


app = App(app_ui, server)
