from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np

# Create sample data
np.random.seed(123)
data = pd.DataFrame(
    {
        "Category": ["A", "B", "C", "D"] * 25,
        "Value": np.random.normal(100, 15, 100),
        "Group": ["Group1", "Group2"] * 50,
    }
)

# Page options
ui.page_opts(title="Navset Tab Demo", fillable=True)

# Create a navset_tab with all possible parameters
with ui.navset_tab(
    id="tabset",  # Optional id for tracking selected tab
    selected="tab1",  # Default selected tab
    header=ui.h3("Navigation Header Example"),  # Header content above tabs
    footer=ui.div(
        "Navigation Footer Example", class_="text-muted"
    ),  # Footer content below tabs
):
    # First tab
    with ui.nav_panel("Basic Stats", value="tab1"):
        ui.h4("Basic Statistics")

        @render.data_frame
        def stats_table():
            return (
                data.groupby("Category")
                .agg({"Value": ["mean", "std", "count"]})
                .round(2)
            )

    # Second tab with a plot
    with ui.nav_panel("Visualization", value="tab2"):
        ui.h4("Data Visualization")

        with ui.layout_sidebar():
            with ui.sidebar():
                ui.input_select(
                    "group", "Select Group", choices=data["Group"].unique().tolist()
                )

            @render.plot
            def boxplot():
                filtered_data = data[data["Group"] == input.group()]
                fig, ax = plt.subplots()
                filtered_data.boxplot(column="Value", by="Category", ax=ax)
                ax.set_title(f"Values by Category for {input.group()}")
                return fig

    # Third tab with dynamic content
    with ui.nav_panel("Interactive", value="tab3"):
        ui.h4("Interactive Features")
        ui.input_slider("bins", "Number of bins", min=5, max=50, value=20)

        @render.plot
        def histogram():
            fig, ax = plt.subplots()
            data["Value"].hist(bins=input.bins(), ax=ax)
            ax.set_title("Value Distribution")
            return fig

    # Fourth tab showing current selection
    with ui.nav_panel("Selection Info", value="tab4"):
        ui.h4("Current Selection Information")

        @render.text
        def current_tab():
            return f"Currently selected tab: {input.tabset()}"


# Add a display of the currently selected tab value
@render.ui
def selected_value():
    return ui.p(f"Selected tab value: {input.tabset()}", class_="mt-3")


# Import matplotlib after the UI definitions
import matplotlib.pyplot as plt
