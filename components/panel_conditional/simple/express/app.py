from shiny import reactive
from shiny.express import input, render, ui

# Page options
ui.page_opts(title="Panel Conditional Demo", fillable=True)

# Create the main layout
with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_radio_buttons(
            "viz_type",
            "Choose Visualization",
            choices=["table", "plot"],
            selected="table",
        )

        # Show controls conditionally based on visualization type
        with ui.panel_conditional("input.viz_type === 'plot'"):
            ui.input_slider("num_bins", "Number of bins", min=5, max=50, value=20)
            ui.input_selectize(
                "plot_color",
                "Plot Color",
                choices=["blue", "red", "green"],
                selected="blue",
            )

        with ui.panel_conditional("input.viz_type === 'table'"):
            ui.input_numeric("num_rows", "Number of rows", value=5, min=1, max=20)
            ui.input_checkbox("show_index", "Show row numbers", value=True)

    # Main panel content
    with ui.panel_conditional("input.viz_type === 'table'"):

        @render.data_frame
        def show_table():
            import pandas as pd
            import numpy as np

            # Generate sample data
            np.random.seed(123)
            n_rows = input.num_rows()

            df = pd.DataFrame(
                {
                    "Name": [f"Person_{i}" for i in range(n_rows)],
                    "Age": np.random.randint(20, 80, n_rows),
                    "Score": np.random.normal(75, 15, n_rows).round(2),
                }
            )

            return df.reset_index(drop=not input.show_index())

    with ui.panel_conditional("input.viz_type === 'plot'"):

        @render.plot
        def show_plot():
            import numpy as np
            import matplotlib.pyplot as plt

            # Generate sample data
            np.random.seed(123)
            data = np.random.normal(100, 15, 1000)

            # Create the plot
            fig, ax = plt.subplots()
            ax.hist(data, bins=input.num_bins(), color=input.plot_color())
            ax.set_title("Sample Distribution")
            ax.set_xlabel("Value")
            ax.set_ylabel("Frequency")

            return fig
