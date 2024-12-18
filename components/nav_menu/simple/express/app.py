from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np

# Synthetic data generation
np.random.seed(42)
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
population_data = pd.DataFrame(
    {
        "City": cities,
        "Population": np.random.randint(1_000_000, 10_000_000, len(cities)),
        "Growth_Rate": np.random.uniform(0.5, 3.5, len(cities)).round(2),
        "Median_Age": np.random.randint(25, 45, len(cities)),
    }
)

# Page setup
ui.page_opts(title="City Demographics Explorer", fillable=True)

# Navigation with nav_menu
with ui.navset_card_tab(id="city_nav"):
    with ui.nav_menu("City Details"):
        with ui.nav_panel("Population", value="population_tab"):

            @render.data_frame
            def population_table():
                return population_data[["City", "Population"]]

        with ui.nav_panel("Growth Rates", value="growth_tab"):

            @render.data_frame
            def growth_table():
                return population_data[["City", "Growth_Rate"]]

        with ui.nav_panel("Age Demographics", value="age_tab"):

            @render.data_frame
            def age_table():
                return population_data[["City", "Median_Age"]]

    with ui.nav_menu("Visualizations"):
        with ui.nav_panel("Bar Chart", value="bar_chart"):

            @render.plot
            def plot_population():
                import matplotlib.pyplot as plt

                plt.figure(figsize=(10, 6))
                plt.bar(population_data["City"], population_data["Population"])
                plt.title("City Populations")
                plt.xlabel("City")
                plt.ylabel("Population")
                plt.xticks(rotation=45)
                return plt.gcf()

        with ui.nav_panel("Pie Chart", value="pie_chart"):

            @render.plot
            def plot_growth():
                import matplotlib.pyplot as plt

                plt.figure(figsize=(10, 6))
                plt.pie(
                    population_data["Growth_Rate"],
                    labels=population_data["City"],
                    autopct="%1.1f%%",
                )
                plt.title("City Growth Rates")
                return plt.gcf()


# Optional: Show selected navigation
ui.h4("Selected Navigation:")


@render.text
def nav_state():
    return f"Current Navigation: {input.city_nav()}"
