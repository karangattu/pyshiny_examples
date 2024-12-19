from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np

# Sample data
df = pd.DataFrame(
    {
        "date": pd.date_range(start="2024-01-01", periods=100),
        "value": np.random.normal(100, 10, 100),
        "category": np.random.choice(["A", "B", "C"], 100),
    }
)

# Page options
ui.page_opts(title="Navset Card Pill Demo", fillable=True)

# Create a navset_card_pill with all possible parameters
with ui.navset_card_pill(
    id="nav_pills",  # Optional ID for tracking selected tab
    selected="tab1",  # Default selected tab
    header="Navigation Pills Demo",  # Header content
    footer="Footer content",  # Footer content
    placement="above",  # Placement of nav items relative to content
):
    # First tab
    with ui.nav_panel("Basic Data", value="tab1"):
        with ui.layout_columns(col_widths=[6, 6]):
            # Data table
            @render.data_frame
            def basic_table():
                return df.head(10)

            # Basic stats
            @render.table
            def stats():
                return pd.DataFrame(
                    {
                        "Statistic": ["Mean", "Std Dev", "Count"],
                        "Value": [
                            round(df["value"].mean(), 2),
                            round(df["value"].std(), 2),
                            len(df),
                        ],
                    }
                )

    # Second tab with sidebar
    with ui.nav_panel("Interactive", value="tab2"):
        with ui.layout_sidebar():
            with ui.sidebar():
                ui.input_slider("n_rows", "Number of rows", 5, 50, 10)
                ui.input_selectize(
                    "category",
                    "Select Category",
                    choices=["All"] + list(df["category"].unique()),
                    selected="All",
                )

            @render.data_frame
            def filtered_data():
                filtered_df = df.copy()
                if input.category() != "All":
                    filtered_df = filtered_df[
                        filtered_df["category"] == input.category()
                    ]
                return filtered_df.head(input.n_rows())

    # Third tab with visualization
    with ui.nav_panel("Visualization", value="tab3"):
        with ui.layout_columns(col_widths=[8, 4]):

            @render.plot
            def time_series():
                import matplotlib.pyplot as plt

                fig, ax = plt.subplots(figsize=(10, 6))
                for cat in df["category"].unique():
                    cat_data = df[df["category"] == cat]
                    ax.plot(cat_data["date"], cat_data["value"], label=cat)
                ax.set_title("Time Series by Category")
                ax.legend()
                return fig

            @render.table
            def summary_by_category():
                return df.groupby("category")["value"].agg(["mean", "count"]).round(2)


# Track selected tab
@render.text
def selected_tab():
    return f"Currently selected tab: {input.nav_pills()}"
