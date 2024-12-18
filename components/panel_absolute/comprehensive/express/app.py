from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np

# Make up some sample data
df = pd.DataFrame({"x": np.random.normal(0, 1, 100), "y": np.random.normal(0, 1, 100)})

ui.page_opts(title="Panel Absolute Demo", fillable=True)

# Main content
with ui.layout_columns(col_widths=[8, 4]):
    with ui.card():
        ui.card_header("Main Panel")

        # Scatter plot to demonstrate the base content
        @render.plot
        def scatter():
            return df.plot.scatter("x", "y")

        # Panel with top-left positioning
        with ui.panel_absolute(
            top="10px",
            left="10px",
            width="150px",
            height="100px",
            draggable=True,
            cursor="move",
            class_="bg-primary text-white p-2 rounded",
        ):
            "Draggable Top-Left Panel"
            ui.markdown("Drag me around!")

        # Panel with top-right positioning
        with ui.panel_absolute(
            top="10px",
            right="10px",
            width="150px",
            height="100px",
            draggable=False,
            class_="bg-success text-white p-2 rounded",
        ):
            "Fixed Top-Right Panel"

        # Panel with bottom-left positioning
        with ui.panel_absolute(
            bottom="10px",
            left="10px",
            width="150px",
            height="100px",
            draggable=True,
            cursor="default",
            class_="bg-warning p-2 rounded",
        ):
            "Bottom-Left Panel"
            ui.input_numeric("num", "Number:", 0)

        # Panel with bottom-right positioning and fixed position
        with ui.panel_absolute(
            bottom="10px",
            right="10px",
            width="150px",
            height="100px",
            fixed=True,
            class_="bg-info text-white p-2 rounded",
        ):
            "Fixed Position Panel"

            @render.text
            def fixed_text():
                return f"Value: {input.num()}"

    # Control panel
    with ui.card():
        ui.card_header("Panel Controls")
        ui.input_switch("show_panels", "Show All Panels", True)
        ui.input_select(
            "cursor_type", "Cursor Type", choices=["auto", "move", "default", "inherit"]
        )


@reactive.effect
def _():
    if input.show_panels():
        ui.update_text("panels_status", value="Panels are visible")
    else:
        ui.update_text("panels_status", value="Panels are hidden")


# Add some descriptive text
ui.markdown(
    """
### Panel Absolute Demo

This demo showcases the various parameters of `ui.panel_absolute`:

* **top, left, right, bottom**: Position the panel
* **width, height**: Set panel dimensions
* **draggable**: Allow/prevent panel dragging
* **fixed**: Fix panel position relative to viewport
* **cursor**: Change cursor appearance
"""
)
