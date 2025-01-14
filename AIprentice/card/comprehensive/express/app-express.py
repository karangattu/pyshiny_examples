from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Add Font Awesome CSS in the head section
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">'
    )
)

# Page options
ui.page_opts(title="Card Demo", fillable=True)

# Main card container
with ui.card(
    id="demo_card",
    full_screen=True,
    height="400px",
    fill=True,
    class_="my-custom-class",
):
    # Card header with icon
    ui.card_header(
        "Interactive Card Demo",
        ui.tags.i(class_="fa-solid fa-chart-line", style="font-size: 2rem;"),
        class_="d-flex justify-content-between align-items-center",
    )

    # Layout with two columns
    with ui.layout_column_wrap(width=1 / 2):
        # Left column - Controls
        with ui.card():
            ui.card_header("Controls")
            ui.input_slider("points", "Number of points", min=5, max=50, value=20)
            ui.input_select(
                "chart_type",
                "Chart Type",
                choices=["Line", "Scatter", "Bar"],
                selected="Line",
            )
            ui.input_checkbox("show_grid", "Show Grid", value=True)

        # Right column - Plot
        with ui.card():
            ui.card_header("Visualization")

            @render.plot
            def plot():
                # Create data based on user input
                data = pd.DataFrame(
                    {
                        "x": range(input.points()),
                        "y": np.random.normal(0, 1, input.points()),
                    }
                )

                # Create the plot
                fig, ax = plt.subplots(figsize=(8, 6))

                # Plot based on selected chart type
                if input.chart_type() == "Line":
                    ax.plot(data["x"], data["y"], "-o")
                elif input.chart_type() == "Scatter":
                    ax.scatter(data["x"], data["y"], alpha=0.6)
                else:  # Bar
                    ax.bar(data["x"], data["y"])

                # Add grid if selected
                if input.show_grid():
                    ax.grid(True, linestyle="--", alpha=0.7)

                ax.set_title("Dynamic Chart")
                ax.set_xlabel("X Axis")
                ax.set_ylabel("Y Axis")

                plt.tight_layout()
                return fig

    # Data table section
    @render.data_frame
    def table():
        return pd.DataFrame(
            {
                "Date": pd.date_range(start="2024-01-01", periods=input.points()),
                "Value": np.random.normal(0, 1, input.points()),
            }
        ).round(3)

    # Card footer with markdown
    ui.card_footer(
        ui.markdown(
            "*This is an interactive demonstration of Shiny card capabilities.*"
        ),
        class_="text-muted",
    )
