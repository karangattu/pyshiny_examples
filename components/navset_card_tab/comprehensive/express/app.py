import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render

# Generate some sample data
np.random.seed(123)
data = pd.DataFrame(
    {
        "x": np.random.normal(0, 1, 100),
        "y": np.random.normal(0, 1, 100),
        "category": np.random.choice(["A", "B", "C"], 100),
    }
)

# Page options for better appearance
ui.page_opts(title="Navset Card Tab Demo", fillable=True)

# Create a navset_card_tab with all available parameters
with ui.navset_card_tab(
    id="tabset1",  # Optional ID for tracking selected tab
    selected="tab1",  # Default selected tab
    header="Card Header",  # Optional header content
    footer="Card Footer",  # Optional footer content
):
    # First tab panel
    with ui.nav_panel("Basic Plot", value="tab1"):
        ui.input_slider("points", "Number of points", 10, 100, 50)

        @render.plot
        def scatter():
            n = input.points()
            return data.iloc[:n].plot.scatter("x", "y")

    # Second tab panel with sidebar
    with ui.nav_panel("Data Table", value="tab2"):
        with ui.layout_sidebar():
            with ui.sidebar():
                ui.input_select(
                    "cat_filter",
                    "Filter Category",
                    choices=["All"] + list(data["category"].unique()),
                )

            @render.data_frame
            def table():
                df = data.copy()
                if input.cat_filter() != "All":
                    df = df[df["category"] == input.cat_filter()]
                return df

    # Third tab panel
    with ui.nav_panel("Statistics", value="tab3"):

        @render.ui
        def stats():
            stats_html = [
                ui.h3("Dataset Statistics"),
                ui.tags.ul(
                    [
                        ui.tags.li(f"Mean X: {data['x'].mean():.2f}"),
                        ui.tags.li(f"Mean Y: {data['y'].mean():.2f}"),
                        ui.tags.li(f"Correlation: {data['x'].corr(data['y']):.2f}"),
                    ]
                ),
            ]
            return ui.TagList(*stats_html)


# Display the currently selected tab value
@render.text
def selected_tab():
    return f"Currently selected tab: {input.tabset1()}"
