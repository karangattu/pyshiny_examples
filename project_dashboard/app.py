import datetime
import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui
from shiny.types import FileInfo

# Sample data generation
def generate_sample_data(num_projects=5, num_tasks_per_project=10, num_team_members=10):
    # Generate sample project data
    project_names = [f"Project {i+1}" for i in range(num_projects)]
    project_start_dates = [datetime.date(2023, 1, 1) + datetime.timedelta(days=random.randint(0, 30)) for _ in range(num_projects)]
    project_end_dates = [start_date + datetime.timedelta(days=random.randint(30, 120)) for start_date in project_start_dates]
    project_progress = [random.randint(0, 100) for _ in range(num_projects)]

    # Generate sample task data
    task_names = [f"Task {i+1}" for i in range(num_tasks_per_project * num_projects)]
    task_project_ids = [i // num_tasks_per_project for i in range(len(task_names))]
    task_assignees = [f"Team Member {i+1}" for i in range(num_team_members)]
    task_start_dates = [project_start_dates[project_id] + datetime.timedelta(days=random.randint(0, (project_end_dates[project_id] - project_start_dates[project_id]).days)) for project_id in task_project_ids]
    task_end_dates = [start_date + datetime.timedelta(days=random.randint(1, 30)) for start_date in task_start_dates]
    task_progress = [random.randint(0, 100) for _ in range(len(task_names))]

    # Generate sample team member data
    team_member_names = [f"Team Member {i+1}" for i in range(num_team_members)]
    team_member_roles = ["Project Manager", "Developer", "Designer", "Tester"]
    team_member_skills = ["Python", "SQL", "Agile", "UX Design", "Testing"]

    project_df = pd.DataFrame({
        "name": project_names,
        "start_date": project_start_dates,
        "end_date": project_end_dates,
        "progress": project_progress
    })

    task_df = pd.DataFrame({
        "name": task_names,
        "project_id": task_project_ids,
        "assignee": [random.choice(task_assignees) for _ in range(len(task_names))],
        "start_date": task_start_dates,
        "end_date": task_end_dates,
        "progress": task_progress
    })

    team_member_df = pd.DataFrame({
        "name": team_member_names,
        "role": [random.choice(team_member_roles) for _ in range(num_team_members)],
        "skills": [", ".join(random.sample(team_member_skills, random.randint(1, 3))) for _ in range(num_team_members)]
    })

    return project_df, task_df, team_member_df

# Generate sample data
project_df, task_df, team_member_df = generate_sample_data()

app_ui = ui.page_fluid(
    ui.panel_title("Project Management Dashboard"),
    ui.layout_column_wrap(
        ui.value_box(
            "Total Projects",
            str(len(project_df)),
            showcase=ui.tags.i(class_="fa-solid fa-chart-simple", style="font-size: 2rem;"),
            theme="bg-gradient-orange-red",
            full_screen=True,
        ),
        ui.value_box(
            "Total Tasks",
            str(len(task_df)),
            showcase=ui.tags.i(class_="fa-solid fa-clipboard-list", style="font-size: 2rem;"),
            theme="bg-gradient-green-teal",
            full_screen=True,
        ),
        ui.value_box(
            "Team Members",
            str(len(team_member_df)),
            showcase=ui.tags.i(class_="fa-solid fa-users", style="font-size: 2rem;"),
            theme="bg-gradient-purple-pink",
            full_screen=True,
        ),
        width=1 / 3,
    ),
    ui.hr(),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Project Timeline"),
            ui.output_plot("project_timeline_plot"),
            height="400px",
        ),
        ui.card(
            ui.card_header("Task Progress"),
            ui.output_plot("task_progress_plot"),
            height="400px",
        ),
        ui.card(
            ui.card_header("Team Member Skills"),
            ui.output_plot("team_skills_plot"),
            height="400px",
        ),
        width=1 / 2,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.plot
    def project_timeline_plot():
        fig, ax = plt.subplots(figsize=(12, 6))
        project_df.plot(x="start_date", y="progress", kind="scatter", ax=ax)
        for i, row in project_df.iterrows():
            ax.plot(
                [row["start_date"], row["end_date"]],
                [row["progress"], row["progress"]],
                color="blue",
            )
            ax.text(
                row["start_date"],
                row["progress"],
                row["name"],
                va="bottom",
                ha="right",
                rotation=45,
            )
        ax.set_xlabel("Date")
        ax.set_ylabel("Progress (%)")
        ax.set_title("Project Timeline")
        return fig

    @render.plot
    def task_progress_plot():
        fig, ax = plt.subplots(figsize=(12, 6))
        task_df.plot(x="start_date", y="progress", kind="scatter", ax=ax)
        for i, row in task_df.iterrows():
            ax.plot(
                [row["start_date"], row["end_date"]],
                [row["progress"], row["progress"]],
                color="green",
            )
            ax.text(
                row["start_date"],
                row["progress"],
                row["name"],
                va="bottom",
                ha="right",
                rotation=45,
            )
        ax.set_xlabel("Date")
        ax.set_ylabel("Progress (%)")
        ax.set_title("Task Progress")
        return fig

    @render.plot
    def team_skills_plot():
        fig, ax = plt.subplots(figsize=(12, 6))
        team_skills = team_member_df["skills"].str.split(", ", expand=True).fillna(0)
        team_skills.plot(kind="bar", ax=ax)
        ax.set_xlabel("Team Member")
        ax.set_ylabel("Skills")
        ax.set_title("Team Member Skills")
        return fig

app = App(app_ui, server)