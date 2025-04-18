from datetime import date, datetime
from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="Slider Parameters Demo", full_width=True)

with ui.layout_column_wrap(width="400px"):
    # Numeric Slider - basic parameters
    with ui.card():
        ui.card_header("Basic Numeric Slider")
        ui.input_slider("slider1", "Min, max, value", min=0, max=100, value=50)

        @render.text
        def value1():
            return f"Value: {input.slider1()}"

    # Numeric Slider with step
    with ui.card():
        ui.card_header("Step Parameter")
        ui.input_slider("slider2", "Step size = 10", min=0, max=100, value=50, step=10)

        @render.text
        def value2():
            return f"Value: {input.slider2()}"

    # Range Slider
    with ui.card():
        ui.card_header("Range Slider")
        ui.input_slider("slider3", "Select a range", min=0, max=100, value=(30, 70))

        @render.text
        def value3():
            return f"Range: {input.slider3()}"

    # Date Slider
    with ui.card():
        ui.card_header("Date Slider")
        ui.input_slider(
            "slider4",
            "Select a date",
            min=date(2023, 1, 1),
            max=date(2023, 12, 31),
            value=date(2023, 6, 15),
        )

        @render.text
        def value4():
            return f"Date: {input.slider4()}"

    # Animated Slider
    with ui.card():
        ui.card_header("Animated Slider")
        ui.input_slider(
            "slider5", "With animation", min=0, max=100, value=50, animate=True
        )

        @render.text
        def value5():
            return f"Value: {input.slider5()}"

    # Slider with custom formatting
    with ui.card():
        ui.card_header("Custom Formatting")
        ui.input_slider(
            "slider6",
            "With prefix and suffix",
            min=0,
            max=100,
            value=50,
            pre="$",
            post="%",
            sep=",",
        )

        @render.text
        def value6():
            return f"Value: {input.slider6()}"

    # Slider with ticks
    with ui.card():
        ui.card_header("Ticks Display")
        ui.input_slider(
            "slider7", "With tick marks", min=0, max=100, value=50, ticks=True
        )

        @render.text
        def value7():
            return f"Value: {input.slider7()}"

    # Date Range Slider with drag_range
    with ui.card():
        ui.card_header("Date Range")
        ui.input_slider(
            "slider9",
            "Draggable range",
            min=date(2023, 1, 1),
            max=date(2023, 12, 31),
            value=(date(2023, 3, 1), date(2023, 9, 30)),
            drag_range=True,
        )

        @render.text
        def value9():
            return f"Range: {input.slider9()}"

    # Datetime slider
    with ui.card():
        ui.card_header("Datetime Slider")
        ui.input_slider(
            "slider10",
            "With time format",
            min=datetime(2023, 1, 1, 0, 0),
            max=datetime(2023, 12, 31, 23, 59),
            value=datetime(2023, 6, 15, 12, 30),
            time_format="%Y-%m-%d %H:%M",
            timezone="+0000",
        )

        @render.text
        def value10():
            return f"Datetime: {input.slider10()}"
