import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Generate sample data
num_diseases = 5
num_treatments = 3
num_patients = 1000

diseases = [f"Disease {i}" for i in range(1, num_diseases + 1)]
treatments = [f"Treatment {i}" for i in range(1, num_treatments + 1)]

disease_prevalence = [random.uniform(0.1, 0.5) for _ in range(num_diseases)]
treatment_efficacy = [[random.uniform(0.6, 0.9) for _ in range(num_treatments)] for _ in range(num_diseases)]
adverse_events = [[random.uniform(0.05, 0.2) for _ in range(num_treatments)] for _ in range(num_diseases)]

patient_data = pd.DataFrame({
    "patient_id": range(1, num_patients + 1),
    "disease": np.random.choice(diseases, num_patients),
    "treatment": np.random.choice(treatments, num_patients),
    "outcome": np.random.binomial(1, [treatment_efficacy[diseases.index(disease)][treatments.index(treatment)] for disease, treatment in zip(patient_data["disease"], patient_data["treatment"])]),
    "adverse_event": np.random.binomial(1, [adverse_events[diseases.index(disease)][treatments.index(treatment)] for disease, treatment in zip(patient_data["disease"], patient_data["treatment"])]),
})

app_ui = ui.page_fluid(
    ui.panel_title("Disease Prevalence, Treatment Efficacy, and Adverse Events"),
    ui.layout_column_wrap(
        ui.value_box(
            "Disease Prevalence",
            ", ".join([f"{d}: {p:.2f}" for d, p in zip(diseases, disease_prevalence)]),
            showcase=ui.tags.i(class_="fa-solid fa-chart-line", style="font-size: 2rem;"),
            theme="bg-gradient-orange-red",
            full_screen=True,
        ),
        ui.value_box(
            "Treatment Efficacy",
            ", ".join([f"{t}: {e:.2f}" for t, e in zip(treatments, [np.mean([treatment_efficacy[i][j] for i in range(num_diseases)]) for j in range(num_treatments)])]),
            showcase=ui.tags.i(class_="fa-solid fa-flask", style="font-size: 2rem;"),
            theme="bg-gradient-green-teal",
            full_screen=True,
        ),
        ui.value_box(
            "Adverse Events",
            ", ".join([f"{t}: {a:.2f}" for t, a in zip(treatments, [np.mean([adverse_events[i][j] for i in range(num_diseases)]) for j in range(num_treatments)])]),
            showcase=ui.tags.i(class_="fa-solid fa-skull-crossbones", style="font-size: 2rem;"),
            theme="bg-gradient-red-pink",
            full_screen=True,
        ),
        width=1 / 3,
    ),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Disease Prevalence"),
            ui.output_plot("disease_prevalence_plot"),
        ),
        ui.card(
            ui.card_header("Treatment Efficacy"),
            ui.output_plot("treatment_efficacy_plot"),
        ),
        ui.card(
            ui.card_header("Adverse Events"),
            ui.output_plot("adverse_events_plot"),
        ),
        width=2 / 3,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.plot
    def disease_prevalence_plot():
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(diseases, disease_prevalence)
        ax.set_title("Disease Prevalence")
        ax.set_xlabel("Disease")
        ax.set_ylabel("Prevalence")
        return fig

    @render.plot
    def treatment_efficacy_plot():
        fig, ax = plt.subplots(figsize=(8, 6))
        x = np.arange(len(treatments))
        width = 0.2
        for i, disease in enumerate(diseases):
            ax.bar(x + i * width, [treatment_efficacy[i][j] for j in range(num_treatments)], width, label=disease)
        ax.set_title("Treatment Efficacy")
        ax.set_xlabel("Treatment")
        ax.set_ylabel("Efficacy")
        ax.set_xticks(x + (num_diseases - 1) * width / 2)
        ax.set_xticklabels(treatments)
        ax.legend()
        return fig

    @render.plot
    def adverse_events_plot():
        fig, ax = plt.subplots(figsize=(8, 6))
        x = np.arange(len(treatments))
        width = 0.2
        for i, disease in enumerate(diseases):
            ax.bar(x + i * width, [adverse_events[i][j] for j in range(num_treatments)], width, label=disease)
        ax.set_title("Adverse Events")
        ax.set_xlabel("Treatment")
        ax.set_ylabel("Adverse Event Rate")
        ax.set_xticks(x + (num_diseases - 1) * width / 2)
        ax.set_xticklabels(treatments)
        ax.legend()
        return fig


app = App(app_ui, server)