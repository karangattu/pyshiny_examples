import random
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

# Sample data for fitness goals and progress
goals = {
    "Weight Loss": {
        "goal": 80,
        "current": 90,
        "unit": "kg",
        "start_date": datetime(2023, 1, 1),
        "end_date": datetime(2023, 6, 30),
    },
    "Steps per Day": {
        "goal": 10000,
        "current": 7500,
        "unit": "steps",
        "start_date": datetime(2023, 1, 1),
        "end_date": datetime(2023, 12, 31),
    },
    "Workout Minutes per Week": {
        "goal": 300,
        "current": 240,
        "unit": "minutes",
        "start_date": datetime(2023, 1, 1),
        "end_date": datetime(2023, 12, 31),
    },
}

app_ui = ui.page_fluid(
    ui.panel_title("Fitness Tracker"),
    ui.layout_column_wrap(
        ui.value_box(
            "Weight Loss",
            f"{goals['Weight Loss']['current']} {goals['Weight Loss']['unit']}",
            f"Goal: {goals['Weight Loss']['goal']} {goals['Weight Loss']['unit']}",
            showcase=ui.tags.i(class_="fa-solid fa-weight-scale", style="font-size: 2rem;"),
            theme="bg-gradient-orange-red",
            full_screen=True,
        ),
        ui.value_box(
            "Steps per Day",
            f"{goals['Steps per Day']['current']} {goals['Steps per Day']['unit']}",
            f"Goal: {goals['Steps per Day']['goal']} {goals['Steps per Day']['unit']}",
            showcase=ui.tags.i(class_="fa-solid fa-shoe-prints", style="font-size: 2rem;"),
            theme="bg-gradient-green-teal",
            full_screen=True,
        ),
        ui.value_box(
            "Workout Minutes",
            f"{goals['Workout Minutes per Week']['current']} {goals['Workout Minutes per Week']['unit']}",
            f"Goal: {goals['Workout Minutes per Week']['goal']} {goals['Workout Minutes per Week']['unit']}",
            showcase=ui.tags.i(class_="fa-solid fa-dumbbell", style="font-size: 2rem;"),
            theme="bg-gradient-purple-pink",
            full_screen=True,
        ),
        width=1 / 3,
    ),
    ui.hr(),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Weight Loss Progress"),
            ui.output_plot("weight_plot"),
        ),
        ui.card(
            ui.card_header("Steps per Day Progress"),
            ui.output_plot("steps_plot"),
        ),
        ui.card(
            ui.card_header("Workout Minutes Progress"),
            ui.output_plot("workout_plot"),
        ),
        width=1 / 2,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.plot
    def weight_plot():
        fig, ax = plt.subplots(figsize=(8, 6))
        x = np.linspace(
            (goals["Weight Loss"]["start_date"] - datetime(1970, 1, 1)).total_seconds() / 86400,
            (goals["Weight Loss"]["end_date"] - datetime(1970, 1, 1)).total_seconds() / 86400,
            100,
        )
        y = goals["Weight Loss"]["goal"] + (goals["Weight Loss"]["current"] - goals["Weight Loss"]["goal"]) * np.exp(
            -0.01 * x
        )
        ax.plot(x, y)
        ax.scatter(
            (datetime.now() - datetime(1970, 1, 1)).total_seconds() / 86400,
            goals["Weight Loss"]["current"],
            color="red",
            label="Current Weight",
        )
        ax.set_xlabel("Days")
        ax.set_ylabel("Weight (kg)")
        ax.set_title("Weight Loss Progress")
        ax.legend()
        return fig

    @render.plot
    def steps_plot():
        fig, ax = plt.subplots(figsize=(8, 6))
        x = np.linspace(
            (goals["Steps per Day"]["start_date"] - datetime(1970, 1, 1)).total_seconds() / 86400,
            (goals["Steps per Day"]["end_date"] - datetime(1970, 1, 1)).total_seconds() / 86400,
            100,
        )
        y = goals["Steps per Day"]["goal"] + (goals["Steps per Day"]["current"] - goals["Steps per Day"]["goal"]) * np.exp(
            0.01 * x
        )
        ax.plot(x, y)
        ax.scatter(
            (datetime.now() - datetime(1970, 1, 1)).total_seconds() / 86400,
            goals["Steps per Day"]["current"],
            color="red",
            label="Current Steps",
        )
        ax.set_xlabel("Days")
        ax.set_ylabel("Steps")
        ax.set_title("Steps per Day Progress")
        ax.legend()
        return fig

    @render.plot
    def workout_plot():
        fig, ax = plt.subplots(figsize=(8, 6))
        x = np.linspace(
            (goals["Workout Minutes per Week"]["start_date"] - datetime(1970, 1, 1)).total_seconds() / 86400,
            (goals["Workout Minutes per Week"]["end_date"] - datetime(1970, 1, 1)).total_seconds() / 86400,
            100,
        )
        y = goals["Workout Minutes per Week"]["goal"] + (goals["Workout Minutes per Week"]["current"] - goals["Workout Minutes per Week"]["goal"]) * np.exp(
            0.005 * x
        )
        ax.plot(x, y)
        ax.scatter(
            (datetime.now() - datetime(1970, 1, 1)).total_seconds() / 86400,
            goals["Workout Minutes per Week"]["current"],
            color="red",
            label="Current Workout Minutes",
        )
        ax.set_xlabel("Days")
        ax.set_ylabel("Minutes")
        ax.set_title("Workout Minutes Progress")
        ax.legend()
        return fig

app = App(app_ui, server)