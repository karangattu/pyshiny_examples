import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
data = {
    "City": cities,
    "Population": np.random.randint(1_000_000, 9_000_000, len(cities)),
    "Growth Rate (%)": np.round(np.random.uniform(0.5, 3.5, len(cities)), 2),
    "Median Income": np.random.randint(50_000, 120_000, len(cities)),
}
df = pd.DataFrame(data)

# Page options
ui.page_opts(title="City Demographics Explorer", fillable=True)

# Navigation set with underline
with ui.navset_underline(id="city_nav"):
    with ui.nav_panel("Population"):

        @render.plot
        def population_plot():
            plt.figure(figsize=(10, 6))
            plt.bar(df["City"], df["Population"])
            plt.title("City Populations")
            plt.xlabel("City")
            plt.ylabel("Population")
            plt.xticks(rotation=45)
            plt.tight_layout()
            return plt.gcf()

    with ui.nav_panel("Growth Rate"):

        @render.plot
        def growth_plot():
            plt.figure(figsize=(10, 6))
            plt.bar(df["City"], df["Growth Rate (%)"], color="green")
            plt.title("City Growth Rates")
            plt.xlabel("City")
            plt.ylabel("Growth Rate (%)")
            plt.xticks(rotation=45)
            plt.tight_layout()
            return plt.gcf()

    with ui.nav_panel("Median Income"):

        @render.plot
        def income_plot():
            plt.figure(figsize=(10, 6))
            plt.bar(df["City"], df["Median Income"], color="purple")
            plt.title("City Median Incomes")
            plt.xlabel("City")
            plt.ylabel("Median Income ($)")
            plt.xticks(rotation=45)
            plt.tight_layout()
            return plt.gcf()

    with ui.nav_panel("Data Table"):

        @render.data_frame
        def city_table():
            return df
