from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(123)
data = pd.DataFrame(
    {
        "date": pd.date_range(start="2024-01-01", periods=100, freq="D"),
        "value": np.random.normal(100, 15, 100),
        "category": np.random.choice(["A", "B", "C"], 100),
    }
)

# Custom sidebar content
with ui.sidebar(id="custom_sidebar"):
    ui.input_slider("n_points", "Number of points", 10, 100, 50)
    ui.input_selectize(
        "selected_category",
        "Select Category",
        choices=["All"] + list(data["category"].unique()),
    )

# Page options
ui.page_opts(title="Navset Card Underline Demo", fillable=True)

# Main content using navset_card_underline
with ui.navset_card_underline(
    id="main_nav",  # Optional id for tracking selected panel
    selected="plot",  # Initially selected panel
):
    # Add header content
    ui.h3("Interactive Data Analysis")

    # First nav panel
    with ui.nav_panel("Plot", value="plot"):

        @render.plot
        def scatter_plot():
            fig, ax = plt.subplots(figsize=(10, 6))
            df = data.head(input.n_points())
            if input.selected_category() != "All":
                df = df[df["category"] == input.selected_category()]

            ax.scatter(df["date"], df["value"], alpha=0.6)
            ax.axhline(y=input.threshold(), color="r", linestyle="--", alpha=0.5)
            ax.set_title("Time Series Scatter Plot")
            ax.set_xlabel("Date")
            ax.set_ylabel("Value")
            return fig

    # Second nav panel
    with ui.nav_panel("Table", value="table"):

        @render.data_frame
        def summary_table():
            df = data.head(input.n_points())
            if input.selected_category() != "All":
                df = df[df["category"] == input.selected_category()]
            return df

    # Third nav panel
    with ui.nav_panel("Statistics", value="stats"):

        @render.ui
        def stats_ui():
            df = data.head(input.n_points())
            if input.selected_category() != "All":
                df = df[df["category"] == input.selected_category()]

            stats = {
                "Mean": f"{df['value'].mean():.2f}",
                "Median": f"{df['value'].median():.2f}",
                "Std Dev": f"{df['value'].std():.2f}",
                "Points Above Threshold": f"{(df['value'] > input.threshold()).sum()}",
            }

            return ui.tags.div(
                ui.h4("Summary Statistics"),
                ui.tags.table(
                    [
                        ui.tags.tr(
                            ui.tags.td(
                                key, style="padding-right: 20px; font-weight: bold;"
                            ),
                            ui.tags.td(value),
                        )
                        for key, value in stats.items()
                    ],
                    class_="table table-striped",
                ),
            )


# Add threshold input outside the navset
ui.input_numeric("threshold", "Threshold", 100, min=50, max=150)

# Add footer content
ui.div(ui.p("Data last updated: 2024-01-31", class_="text-muted"), class_="p-2")


# Display current selection
@render.text
def show_selection():
    return f"Currently selected tab: {input.main_nav()}"
