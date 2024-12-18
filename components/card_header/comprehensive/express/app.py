from shiny import reactive
from shiny.express import input, ui, render
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Synthetic data generation
np.random.seed(42)
data = pd.DataFrame(
    {
        "Category": ["A", "B", "C", "D", "E"],
        "Value": np.random.randint(10, 100, 5),
        "Percentage": np.random.uniform(0, 100, 5),
    }
)

# Add Font Awesome CSS
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

ui.page_opts(title="Card Header Showcase", fillable=True)

# Demonstrate various card header configurations
with ui.layout_columns():
    # Basic card header
    with ui.card():
        ui.card_header("Basic Card Header")
        "This is a simple card with a basic header."

    # Card header with HTML content
    with ui.card():
        ui.card_header(ui.tags.span("HTML ", ui.tags.strong("Styled"), " Header"))
        "This header uses HTML formatting."

    # Card header with icon (corrected version)
    with ui.card():
        ui.card_header(
            "Header with Icon ",
            ui.tags.i(class_="fa-solid fa-chart-simple me-2"),
            container=ui.tags.div,
        )
        with ui.tags.div(class_="d-flex align-items-center"):
            
            "This header includes an icon."

# More advanced card header demonstrations
with ui.layout_columns():
    # Card header with container and custom attributes
    with ui.card():
        ui.card_header(
            "Custom Attributes Header",
            container=ui.tags.div,
            class_="bg-primary text-white",
        )
        "This header has custom CSS classes."

    # Card header with multiple elements
    with ui.card():
        ui.card_header(
            ui.tags.div(
                "Complex Header",
                ui.input_action_button("refresh", "Refresh", class_="btn-sm ms-2"),
            )
        )
        "This header contains a nested action button."

# Interactive card header with dynamic content
with ui.layout_columns():
    with ui.card():

        @render.ui
        def dynamic_header():
            colors = ["text-primary", "text-success", "text-danger", "text-warning"]
            return ui.card_header(
                f"Dynamic Header - {random.choice(['Red', 'Blue', 'Green'])}",
                class_=random.choice(colors),
            )

        ui.input_action_button("change_header", "Change Header")

        @reactive.effect
        @reactive.event(input.change_header)
        def _():
            # This will trigger the dynamic header to re-render
            pass

        "This header changes color randomly when the button is clicked."

    # Card header with plot
    with ui.card():
        ui.card_header("Data Visualization")

        @render.plot
        def category_plot():
            plt.figure(figsize=(8, 4))
            plt.bar(data["Category"], data["Value"])
            plt.title("Category Values")
            plt.xlabel("Category")
            plt.ylabel("Value")
            return plt.gcf()


# Tooltip demonstration with card header
with ui.layout_columns():
    with ui.card():
        with ui.tooltip(placement="right"):
            ui.card_header("Header with Tooltip")
            "This is additional tooltip information about the header."

        "Hover over the header to see more information."
