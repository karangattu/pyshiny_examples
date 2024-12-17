import pandas as pd
import numpy as np

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
data = {
    "City": cities,
    "Population": np.random.randint(1_000_000, 9_000_000, len(cities)),
    "Area (sq mi)": np.random.uniform(300, 800, len(cities)).round(2),
    "Median Income": np.random.randint(50_000, 100_000, len(cities)),
}
df = pd.DataFrame(data)

# Set page options
ui.page_opts(title="City Statistics Explorer", fillable=True)

# Create navset_pill_list with different views of the data
with ui.navset_pill_list(id="city_view"):
    with ui.nav_panel("Population View"):

        @render.data_frame
        def population_table():
            return df.sort_values("Population", ascending=False)

    with ui.nav_panel("Area View"):

        @render.data_frame
        def area_table():
            return df.sort_values("Area (sq mi)", ascending=False)

    with ui.nav_panel("Income View"):

        @render.data_frame
        def income_table():
            return df.sort_values("Median Income", ascending=False)


# Optional: Add a section to show which view is currently selected
ui.h4("Current View:")


@render.text
def selected_view():
    return f"Selected: {input.city_view()}"
