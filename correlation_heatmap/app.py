import numpy as np
import pandas as pd
from shiny import App, Inputs, Outputs, Session, render, ui

# Generate a random dataset
np.random.seed(42)
data = pd.DataFrame(np.random.rand(6, 4), columns=[f"Feature {i}" for i in range(6, 10)])

app_ui = ui.page_fluid(
    ui.panel_title("Correlation Heatmap"),
    ui.card_header("Correlation Heatmap"),
    ui.output_plot("correlation_heatmap"),

)

def server(input, output, session):
    @render.plot
    def correlation_heatmap():
        import matplotlib.pyplot as plt
        import seaborn as sns

        fig, ax = plt.subplots(figsize=(10, 10))
        sns.heatmap(data.corr(), annot=True, cmap="YlOrRd", ax=ax)
        ax.set_title("Correlation Heatmap")
        return fig

app = App(app_ui, server)