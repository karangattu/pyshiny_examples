from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Sample data generation
def generate_data():
    np.random.seed(123)
    dates = pd.date_range(start="2024-01-01", periods=10, freq="D")
    return pd.DataFrame(
        {
            "Date": dates,
            "Value": np.random.normal(100, 10, 10),
            "Category": np.random.choice(["A", "B", "C"], 10),
        }
    )


# Page options
ui.page_opts(title="Card Examples", fillable=True)

# Basic Card with header and footer
with ui.card(full_screen=True, height="300px"):
    ui.card_header("Basic Card with Header")
    "This is a basic card with header and footer"
    ui.card_footer("Footer content")

# Card with plot and custom styling
with ui.card(
    full_screen=True, height="400px", class_="mt-3 shadow", style="border-radius: 15px;"
):
    ui.card_header("Interactive Plot Card")

    ui.input_slider("points", "Number of points", 10, 100, 50)

    @render.plot
    def plot1():
        plt.figure()
        x = np.random.normal(0, 1, input.points())
        plt.hist(x, bins=20)
        plt.title("Random Distribution")
        return plt.gcf()


# Data display card with DataGrid
with ui.card(full_screen=True, height="400px", fill=True, class_="mt-3"):
    ui.card_header("Data Display Card")

    @render.data_frame
    def data_grid():
        return render.DataGrid(
            generate_data(),
            filters=True,
            width="100%",
            height="300px",
            selection_mode="row",
        )


# Card with dynamic content
with ui.card(
    full_screen=False, height="200px", class_="mt-3", style="background-color: #f8f9fa;"
):
    ui.card_header("Dynamic Content Card")

    @render.ui
    def dynamic_content():
        reactive.invalidate_later(1)
        return ui.HTML(
            f"<h4>Current time: {pd.Timestamp.now().strftime('%H:%M:%S')}</h4>"
        )


# Card with inputs and reactive output
with ui.card(
    full_screen=True, height="300px", class_="mt-3", style="border: 2px solid #007bff;"
):
    ui.card_header("Interactive Card")

    with ui.layout_sidebar():
        with ui.sidebar():
            ui.input_text("name", "Enter your name", "User")
            ui.input_numeric("age", "Enter your age", 25)

        @render.text
        def greeting():
            return f"Hello {input.name()}, you are {input.age()} years old!"


# Card with conditional content
with ui.card(
    full_screen=True,
    height="250px",
    class_="mt-3",
    style="border-left: 5px solid #28a745;",
):
    ui.card_header("Conditional Card")
    ui.input_switch("show_extra", "Show extra content")

    @render.ui
    def conditional_content():
        if input.show_extra():
            return ui.div(
                ui.h4("Extra content visible!"),
                ui.p("This content is only visible when the switch is on."),
            )
        return ui.p("Toggle the switch to see more content")
