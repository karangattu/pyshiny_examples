from datetime import datetime
import numpy as np
import pandas as pd
from shiny import reactive
from shiny.express import input, ui, render


# Sample data generation
def generate_data():
    np.random.seed(123)
    dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
    return pd.DataFrame(
        {
            "date": dates,
            "value": np.random.randn(len(dates)).cumsum(),
            "category": np.random.choice(["A", "B", "C"], len(dates)),
        }
    )


# Add Font Awesome for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">'
    )
)

# Page options
ui.page_opts(title="Navset Bar Demo", fillable=True)

# Create a sidebar component
with ui.sidebar(open="desktop"):
    ui.input_date_range(
        "date_range", "Select Date Range", start="2024-01-01", end="2024-12-31"
    )
    ui.input_selectize(
        "category", "Select Category", choices=["All", "A", "B", "C"], selected="All"
    )

# Main navigation bar with all possible parameters
with ui.navset_bar(
    title="Advanced Dashboard",  # Title parameter
    id="main_nav",  # ID parameter
    selected="overview",  # Selected parameter
    position="static-top",  # Position parameter
    header=ui.h4("Header Content", class_="mt-2"),  # Header parameter
    footer=ui.p("Footer Content", class_="text-muted"),  # Footer parameter
    bg="light",  # Background parameter
    inverse=False,  # Inverse parameter
    underline=True,  # Underline parameter
    collapsible=True,  # Collapsible parameter
    fluid=True,  # Fluid parameter
):
    # Regular nav panel
    with ui.nav_panel("Overview", value="overview"):
        with ui.card():
            ui.card_header("Data Overview")

            @render.plot
            def overview_plot():
                df = generate_data()
                fig, ax = plt.subplots()
                ax.plot(df["date"], df["value"])
                ax.set_title("Time Series Overview")
                return fig

    # Nav panel with icon
    with ui.nav_panel(
        ui.HTML('<i class="fa-solid fa-chart-line"></i> Analytics'), value="analytics"
    ):
        with ui.layout_column_wrap():
            with ui.card():
                ui.card_header("Analytics Card 1")

                @render.data_frame
                def analytics_table():
                    df = generate_data()
                    return df.head(10)

            with ui.card():
                ui.card_header("Analytics Card 2")

                @render.text
                def stats_summary():
                    df = generate_data()
                    return f"Total Records: {len(df)}"

    # Nav menu with dropdown items
    with ui.nav_menu("More Options", align="right"):
        with ui.nav_panel("Settings", value="settings"):
            ui.input_switch("dark_mode", "Dark Mode")
            ui.input_slider(
                "refresh_rate", "Refresh Rate (seconds)", min=1, max=60, value=5
            )

        with ui.nav_panel("Help", value="help"):
            ui.markdown(
                """
            ### Help Section
            This is a demo application showing all possible parameters of navset_bar:
            - Title
            - ID
            - Selected
            - Position
            - Header
            - Footer
            - Background
            - Inverse
            - Underline
            - Collapsible
            - Fluid
            """
            )

    # Nav control for custom content
    with ui.nav_control():
        ui.a(
            ui.HTML('<i class="fa-solid fa-github"></i> GitHub'),
            href="https://github.com",
            target="_blank",
            class_="btn btn-light",
        )


# Add reactive behavior
@reactive.effect
def _():
    print(f"Current nav selection: {input.main_nav()}")
