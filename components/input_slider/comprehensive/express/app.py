from datetime import date, datetime, timedelta
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Slider Demo", fillable=True)

with ui.layout_columns():
    # Basic numeric slider
    with ui.card():
        ui.card_header("Basic Numeric Slider")
        ui.input_slider(
            "numeric_slider", "Basic Slider (min, max, value)", min=0, max=100, value=50
        )

        @render.text
        def numeric_value():
            return f"Selected value: {input.numeric_slider()}"

    # Slider with step
    with ui.card():
        ui.card_header("Slider with Step")
        ui.input_slider("step_slider", "Step Slider", min=0, max=10, value=5, step=0.5)

        @render.text
        def step_value():
            return f"Selected value: {input.step_slider()}"

    # Range slider
    with ui.card():
        ui.card_header("Range Slider")
        ui.input_slider(
            "range_slider", "Range Selection", min=0, max=100, value=(30, 70)
        )

        @render.text
        def range_value():
            return f"Selected range: {input.range_slider()}"


# Second row
with ui.layout_columns():
    # Date slider
    with ui.card():
        ui.card_header("Date Slider")
        ui.input_slider(
            "date_slider",
            "Select Date",
            min=date(2023, 1, 1),
            max=date(2023, 12, 31),
            value=date(2023, 6, 15),
        )

        @render.text
        def date_value():
            return f"Selected date: {input.date_slider()}"

    # Animated slider
    with ui.card():
        ui.card_header("Animated Slider")
        ui.input_slider(
            "animated_slider", "Animated Slider", min=0, max=100, value=50, animate=True
        )

        @render.text
        def animated_value():
            return f"Selected value: {input.animated_slider()}"

    # Slider with ticks
    with ui.card():
        ui.card_header("Slider with Ticks")
        ui.input_slider(
            "ticks_slider", "Ticks Slider", min=0, max=10, value=5, step=1, ticks=True
        )

        @render.text
        def ticks_value():
            return f"Selected value: {input.ticks_slider()}"


# Third row
with ui.layout_columns():
    # Slider with custom formatting
    with ui.card():
        ui.card_header("Slider with Custom Formatting")
        ui.input_slider(
            "format_slider",
            "Price Slider",
            min=0,
            max=1000,
            value=500,
            pre="$",
            sep=",",
        )

        @render.text
        def format_value():
            return f"Selected price: ${input.format_slider():,}"

    # Date Range slider
    with ui.card():
        ui.card_header("Date Range Slider")
        ui.input_slider(
            "date_range_slider",
            "Select Date Range",
            min=date(2023, 1, 1),
            max=date(2023, 12, 31),
            value=(date(2023, 3, 1), date(2023, 9, 30)),
        )

        @render.text
        def date_range_value():
            return f"Selected date range: {input.date_range_slider()}"

    # Drag Range slider
    with ui.card():
        ui.card_header("Drag Range Slider")
        ui.input_slider(
            "drag_range_slider",
            "Drag Range Slider",
            min=0,
            max=100,
            value=(20, 80),
            drag_range=True,
        )

        @render.text
        def drag_range_value():
            return f"Selected range: {input.drag_range_slider()}"


# Create a plot that responds to a slider
with ui.card():
    ui.card_header("Interactive Plot with Slider")
    ui.input_slider(
        "plot_slider", "Number of points", min=10, max=1000, value=100, step=10
    )

    @render.plot
    def histogram():
        n_points = input.plot_slider()
        data = np.random.normal(0, 1, n_points)
        fig, ax = plt.subplots()
        ax.hist(data, bins=30)
        ax.set_title(f"Histogram of {n_points} random points")
        return fig
