from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
years = [2020, 2021, 2022, 2023]


# Create a synthetic DataFrame
def generate_city_data():
    data = []
    for city in cities:
        for year in years:
            data.append(
                {
                    "City": city,
                    "Year": year,
                    "Population": np.random.randint(500000, 9000000),
                    "GDP": np.random.randint(50000, 1000000),
                    "Crime Rate": np.random.uniform(100, 1000),
                    "Unemployment": np.random.uniform(2, 10),
                }
            )
    return pd.DataFrame(data)


df = generate_city_data()

# Set page options
ui.page_opts(title="Navset Card Underline Demo", fillable=True)

# Create the navset card underline with various configurations
with ui.navset_card_underline(
    id="main_navset",  # Adding an ID to demonstrate reactive behavior
    selected="Population",  # Initially selected tab
    header=ui.markdown("## City Metrics Exploration"),  # Optional header
):
    # Population Tab
    with ui.nav_panel("Population", value="population_panel"):

        @render.plot
        def population_plot():
            plt.figure(figsize=(10, 6))
            pop_data = df.groupby("City")["Population"].mean()
            pop_data.plot(kind="bar")
            plt.title("Average Population by City")
            plt.xlabel("City")
            plt.ylabel("Population")
            plt.xticks(rotation=45)
            plt.tight_layout()
            return plt.gcf()

        @render.data_frame
        def population_table():
            return df.groupby("City")["Population"].mean().reset_index()

    # GDP Tab
    with ui.nav_panel("GDP", value="gdp_panel"):

        @render.plot
        def gdp_plot():
            plt.figure(figsize=(10, 6))
            gdp_data = df.groupby("City")["GDP"].mean()
            gdp_data.plot(kind="bar")
            plt.title("Average GDP by City")
            plt.xlabel("City")
            plt.ylabel("GDP")
            plt.xticks(rotation=45)
            plt.tight_layout()
            return plt.gcf()

        @render.data_frame
        def gdp_table():
            return df.groupby("City")["GDP"].mean().reset_index()

    # Crime Rate Tab
    with ui.nav_panel("Crime Rate", value="crime_panel"):

        @render.plot
        def crime_plot():
            plt.figure(figsize=(10, 6))
            crime_data = df.groupby("City")["Crime Rate"].mean()
            crime_data.plot(kind="bar")
            plt.title("Average Crime Rate by City")
            plt.xlabel("City")
            plt.ylabel("Crime Rate")
            plt.xticks(rotation=45)
            plt.tight_layout()
            return plt.gcf()

        @render.data_frame
        def crime_table():
            return df.groupby("City")["Crime Rate"].mean().reset_index()

    # Unemployment Tab
    with ui.nav_panel("Unemployment", value="unemployment_panel"):

        @render.plot
        def unemployment_plot():
            plt.figure(figsize=(10, 6))
            unemployment_data = df.groupby("City")["Unemployment"].mean()
            unemployment_data.plot(kind="bar")
            plt.title("Average Unemployment Rate by City")
            plt.xlabel("City")
            plt.ylabel("Unemployment Rate (%)")
            plt.xticks(rotation=45)
            plt.tight_layout()
            return plt.gcf()

        @render.data_frame
        def unemployment_table():
            return df.groupby("City")["Unemployment"].mean().reset_index()


# Sidebar for additional interactions
with ui.sidebar():
    ui.input_select("city_filter", "Filter City", choices=["All"] + cities)

    ui.input_dark_mode(id="dark_mode")

# Display the currently selected tab
ui.h5("Selected Tab:")


@render.text
def selected_tab():
    return f"Current tab: {input.main_navset()}"


# Optional: Demonstrate reactive filtering
@reactive.calc
def filtered_data():
    if input.city_filter() == "All":
        return df
    return df[df["City"] == input.city_filter()]
