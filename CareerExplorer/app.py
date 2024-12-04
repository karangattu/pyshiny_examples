import random
from datetime import datetime
from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

# Sample data for career paths
careers = {
    "Software Engineer": {
        "skills": ["Python", "Java", "SQL", "Git", "Agile"],
        "education": ["Bachelor's in Computer Science", "Master's in Computer Science"],
        "experience": ["Internship", "Entry-level", "Mid-level", "Senior"],
        "salary_growth": [60000, 80000, 100000, 120000],
    },
    "Data Analyst": {
        "skills": ["SQL", "Excel", "Tableau", "Python", "R"],
        "education": ["Bachelor's in Statistics", "Bachelor's in Economics"],
        "experience": ["Internship", "Entry-level", "Mid-level", "Senior"],
        "salary_growth": [50000, 65000, 80000, 95000],
    },
    "Marketing Manager": {
        "skills": ["Marketing Strategy", "Social Media", "SEO", "Analytics", "Communication"],
        "education": ["Bachelor's in Marketing", "MBA"],
        "experience": ["Internship", "Entry-level", "Mid-level", "Senior"],
        "salary_growth": [45000, 60000, 75000, 90000],
    },
}

app_ui = ui.page_fluid(
    ui.panel_title("Career Path Explorer"),
    ui.row(
        ui.column(4, 
            ui.input_select("career", "Select a Career", list(careers.keys()), selected="Software Engineer"),
            ui.input_select("experience", "Select Experience Level", ["Internship", "Entry-level", "Mid-level", "Senior"], selected="Entry-level"),
        ),
        ui.column(8,
            ui.output_text("skills"),
            ui.output_text("education"),
            ui.output_text("salary"),
            ui.output_plot("salary_plot"),
        ),
    ),
)

def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def selected_career() -> dict:
        return careers[input.career()]

    @render.text
    def skills():
        return "Required Skills:\n- " + "\n- ".join(selected_career()["skills"])

    @render.text
    def education():
        return "Required Education:\n- " + "\n- ".join(selected_career()["education"])

    @render.text
    def salary():
        experience_level = input.experience()
        index = selected_career()["experience"].index(experience_level)
        salary = selected_career()["salary_growth"][index]
        return f"Typical Salary: ${salary:,.0f}"

    @render.plot
    def salary_plot():
        career = selected_career()
        experience_levels = career["experience"]
        salaries = career["salary_growth"]

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(experience_levels, salaries)
        ax.set_xlabel("Experience Level")
        ax.set_ylabel("Salary ($)")
        ax.set_title(f"Salary Growth for {input.career()}")
        return fig

app = App(app_ui, server)