from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np

# Sample data
sales_data = pd.DataFrame(
    {
        "date": pd.date_range(start="2024-01-01", periods=100),
        "sales": np.random.normal(1000, 100, 100),
        "region": np.random.choice(["North", "South", "East", "West"], 100),
    }
)

# Page configuration
ui.page_opts(title="Hidden Navigation Demo", fillable=True)

# Controls for navigation
with ui.sidebar():
    ui.input_radio_buttons(
        "view_selector",
        "Select View",
        choices={
            "panel1": "Sales Overview",
            "panel2": "Regional Analysis",
            "panel3": "Detailed Data",
        },
        selected="panel1",
    )

# Main content using navset_hidden with all possible parameters
with ui.navset_hidden(
    id="main_content",  # Required for reactive updates
    selected="panel1",  # Initial panel to show
    header=ui.h3("Dynamic Content Area"),  # Header above all panels
    footer=ui.div(  # Footer below all panels
        ui.p("Data last updated: 2024-01-31", class_="text-muted"), class_="mt-3"
    ),
):
    # Panel 1: Sales Overview
    with ui.nav_panel(None, value="panel1"):
        with ui.card():
            ui.card_header("Sales Overview")

            @render.plot
            def sales_plot():
                import matplotlib.pyplot as plt

                fig, ax = plt.subplots(figsize=(10, 6))
                ax.plot(sales_data["date"], sales_data["sales"])
                ax.set_title("Daily Sales Trend")
                return fig

    # Panel 2: Regional Analysis
    with ui.nav_panel(None, value="panel2"):
        with ui.card():
            ui.card_header("Regional Analysis")

            @render.plot
            def region_plot():
                import matplotlib.pyplot as plt

                fig, ax = plt.subplots(figsize=(10, 6))
                sales_by_region = sales_data.groupby("region")["sales"].mean()
                sales_by_region.plot(kind="bar", ax=ax)
                ax.set_title("Average Sales by Region")
                return fig

    # Panel 3: Detailed Data
    with ui.nav_panel(None, value="panel3"):
        with ui.card():
            ui.card_header("Detailed Sales Data")

            @render.data_frame
            def sales_table():
                return render.DataGrid(sales_data, filters=True, height=400)


# Reactive effect to update the navigation based on radio button selection
@reactive.effect
def _():
    ui.update_navs("main_content", selected=input.view_selector())
