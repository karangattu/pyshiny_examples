from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np

# Sample data generation
df = pd.DataFrame(
    {
        "date": pd.date_range(start="2024-01-01", periods=100),
        "value": np.random.normal(100, 15, 100),
        "category": np.random.choice(["A", "B", "C"], 100),
    }
)

# Page options
ui.page_opts(title="Nav Panel Demo", fillable=True)

# Nav panel with basic title
with ui.nav_panel("Basic Panel"):
    "This is a basic nav panel with just a title"
    ui.input_slider("n1", "Number of points", 1, 100, 50)

    @render.plot
    def plot1():
        return df.head(input.n1()).plot()


# Nav panel with value parameter
with ui.nav_panel("Custom Value Panel", value="custom_panel"):
    "This panel has a custom value that can be used for programmatic selection"
    ui.input_numeric("num", "Enter a number", 10)

    @render.text
    def text1():
        return f"You entered: {input.num()}"


# Nav panel with icon
with ui.nav_panel(
    "Panel with Icon",
    icon=ui.tags.i(class_="fa-solid fa-chart-simple", style="font-size: 1rem;"),
):
    "This panel includes a Font Awesome icon"
    ui.input_select("cat", "Select Category", choices=["A", "B", "C"])

    @render.table
    def table1():
        return df[df["category"] == input.cat()]


# Nav panel with all parameters
with ui.nav_panel(
    title="Complete Panel",
    value="full_panel",
    icon=ui.tags.i(class_="fa-solid fa-shield-halved"),
):
    with ui.layout_sidebar():
        with ui.sidebar():
            ui.input_date_range(
                "dates", "Select Date Range", start="2024-01-01", end="2024-03-31"
            )
            ui.input_selectize(
                "categories",
                "Select Categories",
                choices=["A", "B", "C"],
                multiple=True,
            )

        with ui.card():
            ui.card_header("Data Analysis")

            @render.data_frame
            def filtered_data():
                start_date = pd.to_datetime(input.dates()[0])
                end_date = pd.to_datetime(input.dates()[1])
                mask = (df["date"] >= start_date) & (df["date"] <= end_date)
                if input.categories():
                    mask = mask & (df["category"].isin(input.categories()))
                return df[mask]


# Add Font Awesome to the header
ui.head_content(
    ui.tags.link(
        rel="stylesheet",
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css",
    )
)

# Navigation controls
ui.nav_spacer()
with ui.nav_menu(
    "More Options", icon=ui.tags.i(class_="fa-solid fa-ellipsis-vertical")
):
    with ui.nav_panel("About"):
        ui.markdown(
            """
        # About Nav Panels
        
        This app demonstrates the various parameters of `ui.nav_panel()`:
        
        * **title**: The display text for the panel
        * **value**: A unique identifier for the panel
        * **icon**: An optional icon to display
        """
        )

    with ui.nav_panel("Help"):
        "Need help? Contact support!"

# Add a dark mode toggle
with ui.nav_control():
    ui.input_dark_mode()
