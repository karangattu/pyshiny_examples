from shiny import reactive
from shiny.express import input, render, ui

# Page options
ui.page_opts(title="Nav Update Demo", fillable=True)

# Create a sidebar with controls
with ui.sidebar():
    ui.h4("Navigation Controls")
    ui.input_radio_buttons(
        "controller",
        "Select Page",
        choices=["Data", "Plot", "Summary"],
        selected="Data",
    )
    ui.input_action_button("go_next", "Go to Next Tab")

# Create some sample data
import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(123)
data = pd.DataFrame(
    {
        "category": ["A", "B", "C", "D"] * 25,
        "value": np.random.normal(100, 15, 100),
        "group": np.random.choice(["Group 1", "Group 2", "Group 3"], 100),
    }
)

# Create navigation panels
with ui.navset_tab(id="tabset"):
    with ui.nav_panel("Data"):

        @render.data_frame
        def show_data():
            return data

    with ui.nav_panel("Plot"):

        @render.plot
        def show_plot():
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots()
            data.boxplot(column="value", by="group", ax=ax)
            ax.set_title("Value Distribution by Group")
            return fig

    with ui.nav_panel("Summary"):

        @render.data_frame
        def show_summary():
            return (
                data.groupby("group").agg({"value": ["mean", "std", "count"]}).round(2)
            )


# Update navigation based on radio button selection
@reactive.effect
@reactive.event(input.controller)
def _():
    ui.update_navs("tabset", selected=input.controller())


# Handle "Next" button clicks
@reactive.effect
@reactive.event(input.go_next)
def _():
    current = input.controller()
    pages = ["Data", "Plot", "Summary"]
    current_idx = pages.index(current)
    next_idx = (current_idx + 1) % len(pages)
    next_page = pages[next_idx]

    # Update both the radio buttons and the navigation
    ui.update_radio_buttons("controller", selected=next_page)
    ui.update_navs("tabset", selected=next_page)
