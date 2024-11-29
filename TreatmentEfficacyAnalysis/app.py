import numpy as np
import pandas as pd
from shiny import App, Inputs, Outputs, Session, render, ui

# Generate some sample data
np.random.seed(42)
n = 100
treatment = np.random.choice(["Drug A", "Drug B", "Placebo"], size=n)
outcome = np.random.normal(loc=0.5, scale=0.2, size=n)
outcome[treatment == "Placebo"] = np.random.normal(
    loc=0.3, scale=0.2, size=(treatment == "Placebo").sum()
)
data = pd.DataFrame({"Treatment": treatment, "Outcome": outcome})

app_ui = ui.page_fluid(
    ui.panel_title("Treatment Efficacy Analysis"),
    ui.layout_column_wrap(
        ui.value_box(
            "Overall Mean Outcome",
            f"{data['Outcome'].mean():.2f}",
            showcase=ui.HTML('<i class="bi bi-bar-chart-fill"></i>'),
            theme="bg-gradient-primary",
        ),
        ui.value_box(
            "Treatment Effect",
            f"{(data[data['Treatment'] != 'Placebo']['Outcome'].mean() - data[data['Treatment'] == 'Placebo']['Outcome'].mean()):.2f}",
            showcase=ui.HTML('<i class="bi bi-graph-up"></i>'),
            theme="bg-gradient-success",
        ),
        width=1 / 2,
    ),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Treatment Comparison"),
            ui.output_plot("treatment_plot"),
            height="400px",
        ),
        ui.card(
            ui.card_header("Outcome Distribution"),
            ui.output_plot("outcome_plot"),
            height="400px",
        ),
        width=1,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.plot
    def treatment_plot():
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(8, 6))
        data.groupby("Treatment")["Outcome"].mean().plot(kind="bar", ax=ax)
        ax.set_xlabel("Treatment")
        ax.set_ylabel("Mean Outcome")
        ax.set_title("Treatment Comparison")
        return fig

    @render.plot
    def outcome_plot():
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(8, 6))
        data["Outcome"].hist(bins=20, ax=ax)
        ax.set_xlabel("Outcome")
        ax.set_ylabel("Frequency")
        ax.set_title("Outcome Distribution")
        return fig


app = App(app_ui, server)
