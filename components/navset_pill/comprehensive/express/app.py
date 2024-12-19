from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np

# Make up some sample data
sample_data = pd.DataFrame(
    {
        "category": ["A", "B", "C", "D"] * 5,
        "value": np.random.normal(100, 10, 20),
        "count": np.random.randint(1, 100, 20),
    }
)

# Page options
ui.page_opts(title="Navset Pill Demo", fillable=True)

# Create a navset_pill with all possible parameters
with ui.navset_pill(
    id="pill_demo",  # Optional ID for tracking selected tab
    selected="tab1",  # Default selected tab
    header="Navigation Pills Demo",  # Header content
    footer="Footer content",  # Footer content
):
    # Tab 1: Basic Data Display
    with ui.nav_panel("Data Overview", value="tab1"):
        ui.h3("Sample Data Overview")

        @render.data_frame
        def show_data():
            return sample_data

    # Tab 2: Summary Statistics
    with ui.nav_panel("Summary Stats", value="tab2"):
        ui.h3("Summary Statistics")

        @render.data_frame
        def show_summary():
            return sample_data.describe()

    # Tab 3: Interactive Elements
    with ui.nav_panel("Interactive", value="tab3"):
        with ui.layout_sidebar():
            with ui.sidebar():
                ui.input_select(
                    "category",
                    "Select Category",
                    choices=list(sample_data["category"].unique()),
                )
                ui.input_slider(
                    "value_filter",
                    "Filter Value",
                    min=int(sample_data["value"].min()),
                    max=int(sample_data["value"].max()),
                    value=[
                        int(sample_data["value"].min()),
                        int(sample_data["value"].max()),
                    ],
                )

            @render.data_frame
            def filtered_data():
                df = sample_data[
                    (sample_data["category"] == input.category())
                    & (sample_data["value"] >= input.value_filter()[0])
                    & (sample_data["value"] <= input.value_filter()[1])
                ]
                return df

    # Tab 4: With Menu Items
    with ui.nav_menu("More Options"):
        with ui.nav_panel("Extra Info", value="tab4"):
            ui.markdown(
                """
            ### Additional Information
            This tab demonstrates the use of nav_menu for grouping related tabs.
            """
            )

        with ui.nav_panel("About", value="tab5"):
            ui.markdown(
                """
            ### About This Demo
            This demo showcases the various parameters and capabilities of navset_pill in Shiny for Python.
            """
            )


# Display the currently selected tab
@render.text
def selected_tab():
    return f"Currently selected tab: {input.pill_demo()}"
