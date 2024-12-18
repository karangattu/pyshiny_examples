from shiny import reactive
from shiny.express import input, ui, render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Create synthetic datasets
def generate_dataset(name):
    np.random.seed(42)
    if name == "tips":
        return pd.DataFrame(
            {
                "total_bill": np.random.uniform(10, 50, 50),
                "tip": np.random.uniform(1, 10, 50),
                "size": np.random.randint(1, 6, 50),
            }
        )
    elif name == "flights":
        return pd.DataFrame(
            {
                "distance": np.random.uniform(100, 2000, 50),
                "air_time": np.random.uniform(60, 600, 50),
                "speed": np.random.uniform(300, 600, 50),
            }
        )
    else:
        return pd.DataFrame(
            {
                "weight": np.random.normal(70, 15, 50),
                "height": np.random.normal(170, 10, 50),
                "bmi": np.random.normal(22, 4, 50),
            }
        )


# App definition
ui.page_opts(title="NavSet Hidden Demo")

# Sidebar for dataset selection
with ui.sidebar():
    ui.input_radio_buttons("dataset", "Choose Dataset", ["tips", "flights", "exercise"])
    ui.input_radio_buttons("view", "View Type", ["summary", "table", "plot"])

# Hidden navset to manage different views
with ui.navset_hidden(id="hidden_tabs"):
    with ui.nav_panel(None, value="panel1"):

        @render.table
        def summary_table():
            df = generate_dataset(input.dataset())
            return df.describe()

    with ui.nav_panel(None, value="panel2"):

        @render.table
        def full_table():
            return generate_dataset(input.dataset())

    with ui.nav_panel(None, value="panel3"):

        @render.plot
        def dataset_plot():
            df = generate_dataset(input.dataset())

            plt.figure(figsize=(8, 6))
            plt.hist(df.iloc[:, 0], bins=20, edgecolor="black")
            plt.title(f"Histogram of {df.columns[0]} for {input.dataset()} dataset")
            plt.xlabel(df.columns[0])
            plt.ylabel("Frequency")
            return plt.gcf()


# Reactive effect to update the navset based on view selection
@reactive.effect
def _():
    selected_panel = f"panel{['summary', 'table', 'plot'].index(input.view()) + 1}"
    ui.update_navs("hidden_tabs", selected=selected_panel)
