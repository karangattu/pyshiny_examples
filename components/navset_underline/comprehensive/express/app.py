from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np

# Sample data generation
df = pd.DataFrame(
    {
        "date": pd.date_range(start="2024-01-01", periods=100, freq="D"),
        "value": np.random.normal(100, 10, 100),
        "category": np.random.choice(["A", "B", "C"], 100),
    }
)

# Page options for better layout
ui.page_opts(title="Navset Underline Demo", fillable=True)

# Create a navset_underline with all possible parameters
with ui.navset_underline(
    id="nav_demo",  # Optional ID for tracking selected tab
    selected="tab1",  # Initially selected tab
    header=ui.h3("Navigation Demo with Underlined Tabs"),  # Header content
    footer=ui.div(  # Footer content
        ui.p("Footer content for the navset", class_="text-muted"), class_="mt-3"
    ),
):
    # First tab panel
    with ui.nav_panel("Basic Plot", value="tab1"):
        with ui.layout_sidebar():
            with ui.sidebar():
                ui.input_slider("points", "Number of Points", 10, 100, 50)
                ui.input_selectize(
                    "category",
                    "Select Category",
                    choices=["All"] + list(df["category"].unique()),
                )

            @render.plot
            def basic_plot():
                filtered_df = df.copy()
                if input.category() != "All":
                    filtered_df = df[df["category"] == input.category()]
                filtered_df = filtered_df.head(input.points())
                return filtered_df.plot.scatter(x="date", y="value")

    # Second tab panel
    with ui.nav_panel("Data Table", value="tab2"):

        @render.data_frame
        def data_table():
            filtered_df = df.copy()
            if input.category() != "All":
                filtered_df = df[df["category"] == input.category()]
            return render.DataGrid(
                filtered_df.head(input.points()), filters=True, height=400
            )

    # Third tab panel with a menu
    with ui.nav_menu("More Options", value="menu1"):
        with ui.nav_panel("Summary Stats", value="tab3"):

            @render.data_frame
            def summary_stats():
                filtered_df = df.copy()
                if input.category() != "All":
                    filtered_df = df[df["category"] == input.category()]
                stats_df = pd.DataFrame(
                    {
                        "Statistic": ["Mean", "Median", "Std Dev", "Min", "Max"],
                        "Value": [
                            filtered_df["value"].mean(),
                            filtered_df["value"].median(),
                            filtered_df["value"].std(),
                            filtered_df["value"].min(),
                            filtered_df["value"].max(),
                        ],
                    }
                )
                return stats_df

        with ui.nav_panel("About", value="tab4"):
            ui.markdown(
                """
            ### About This Demo
            
            This demo showcases the `navset_underline` component with:
            
            * Multiple navigation panels
            * Dropdown menu
            * Interactive plots and tables
            * Reactive filtering
            * Header and footer content
            """
            )

    # Add a nav_spacer for visual separation
    ui.nav_spacer()

    # Add a nav_control with custom content
    with ui.nav_control():
        ui.a(
            ui.tags.i(class_="fa-solid fa-github"),
            "Source",
            href="https://github.com/",
            target="_blank",
        )


# Display currently selected tab value
@render.text
def selected_tab():
    return f"Currently selected tab: {input.nav_demo()}"
