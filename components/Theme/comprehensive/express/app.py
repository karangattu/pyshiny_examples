# First install required packages:
# pip install "shiny[theme]" pandas numpy matplotlib libsass

from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a custom theme with various parameters
ui.page_opts(
    title="Theme Customization Demo",
    fillable=True,
    theme=ui.Theme(
        "shiny",  # base preset
        name="custom_theme",  # custom name
    )
    .add_defaults(
        primary_color="#007bff",  # primary color
        secondary_color="#6c757d",  # secondary color
        success_color="#28a745",  # success color
        danger_color="#dc3545",  # danger color
        warning_color="#ffd700",  # warning color
        info_color="#17a2b8",  # info color
        light_color="#f8f9fa",  # light color
        dark_color="#343a40",  # dark color
        font_size_base="1rem",  # base font size
        border_radius=".25rem",  # border radius
        enable_rounded=True,  # enable rounded corners
        enable_shadows=True,  # enable shadows
        enable_gradients=True,  # enable gradients
    )
    .add_rules(
        """
        body { 
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
        }
        .card {
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        """
    ),
)

# Generate sample data
np.random.seed(123)
data = pd.DataFrame(
    {
        "Category": ["A", "B", "C", "D", "E"] * 20,
        "Value": np.random.normal(100, 15, 100),
        "Group": np.random.choice(["Group 1", "Group 2", "Group 3"], 100),
    }
)

# Layout starts here
ui.h1("Theme Customization Demo", class_="text-primary mb-4")

with ui.layout_sidebar():
    with ui.sidebar():
        ui.h3("Controls", class_="text-secondary")
        ui.input_slider("sample_size", "Sample Size", 10, 100, 50)
        ui.input_selectize(
            "group_select",
            "Select Group",
            choices=["All"] + list(data["Group"].unique()),
            selected="All",
        )
        ui.input_checkbox_group(
            "categories",
            "Select Categories",
            choices=list(data["Category"].unique()),
            selected=list(data["Category"].unique())[:3],
        )
        ui.hr()
        ui.input_dark_mode(id="dark_mode")

    with ui.layout_column_wrap(width=1 / 2):
        # Card 1 - Statistics
        with ui.card(full_screen=True, class_="mb-4"):
            ui.card_header("Summary Statistics", class_="bg-primary text-white")

            @render.data_frame
            def stats():
                filtered_data = filter_data()
                stats_df = pd.DataFrame(
                    filtered_data["Value"].agg(["mean", "std", "min", "max"])
                ).T
                return stats_df.round(2)

        # Card 2 - Plot
        with ui.card(full_screen=True, class_="mb-4"):
            ui.card_header("Distribution Plot", class_="bg-success text-white")

            @render.plot
            def dist_plot():
                filtered_data = filter_data()
                plt.figure(figsize=(10, 6))
                plt.hist(filtered_data["Value"], bins=20, alpha=0.7)
                plt.title("Value Distribution")
                plt.xlabel("Value")
                plt.ylabel("Frequency")
                return plt

    # Card 3 - Data Table
    with ui.card(full_screen=True):
        ui.card_header("Data Table", class_="bg-info text-white")

        @render.data_frame
        def table():
            return filter_data()


@reactive.calc
def filter_data():
    df = data.copy()

    # Filter by sample size
    df = df.head(input.sample_size())

    # Filter by group
    if input.group_select() != "All":
        df = df[df["Group"] == input.group_select()]

    # Filter by categories
    if input.categories():
        df = df[df["Category"].isin(input.categories())]

    return df
