from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc
from datetime import date, datetime


def test_slider_parameters(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test basic numeric slider
    slider1 = controller.InputSlider(page, "slider1")
    slider1.expect_label("Min, max, value")
    slider1.expect_min("0")
    slider1.expect_max("100")
    slider1.expect_value("50")

    # Test slider with step
    slider2 = controller.InputSlider(page, "slider2")
    slider2.expect_label("Step size = 10")
    slider2.expect_min("0")
    slider2.expect_max("100")
    slider2.expect_value("50")
    slider2.expect_step("10")

    # Test range slider
    slider3 = controller.InputSlider(page, "slider3")
    slider3.expect_label("Select a range")
    slider3.expect_min("0")
    slider3.expect_max("100")
    slider3.expect_value("30,70")

    # Test date slider
    slider4 = controller.InputSlider(page, "slider4")
    slider4.expect_label("Select a date")
    slider4.expect_min("2023-01-01")
    slider4.expect_max("2023-12-31")
    slider4.expect_value("2023-06-15")

    # Test animated slider
    slider5 = controller.InputSlider(page, "slider5")
    slider5.expect_label("With animation")
    slider5.expect_min("0")
    slider5.expect_max("100")
    slider5.expect_value("50")

    # Test formatted slider
    slider6 = controller.InputSlider(page, "slider6")
    slider6.expect_label("With prefix and suffix")
    slider6.expect_min("0")
    slider6.expect_max("100")
    slider6.expect_value("50")
    slider6.expect_pre("$")
    slider6.expect_post("%")
    slider6.expect_sep(",")

    # Test slider with ticks
    slider7 = controller.InputSlider(page, "slider7")
    slider7.expect_label("With tick marks")
    slider7.expect_min("0")
    slider7.expect_max("100")
    slider7.expect_value("50")
    slider7.expect_ticks("true")

    # Test date range slider
    slider9 = controller.InputSlider(page, "slider9")
    slider9.expect_label("Draggable range")
    slider9.expect_min("2023-01-01")
    slider9.expect_max("2023-12-31")
    slider9.expect_value("2023-03-01,2023-09-30")
    slider9.expect_drag_range("true")

    # Test datetime slider
    slider10 = controller.InputSlider(page, "slider10")
    slider10.expect_label("With time format")
    slider10.expect_min("2023-01-01 00:00")
    slider10.expect_max("2023-12-31 23:59")
    slider10.expect_value("2023-06-15 12:30")
    slider10.expect_time_format("%Y-%m-%d %H:%M")
    slider10.expect_timezone("+0000")

    # Test output text
    current_values = controller.OutputText(page, "current_values")
    current_values.expect_value(
        "Basic Slider: 50\n"
        "Step Slider: 50\n"
        "Range Slider: [30, 70]\n"
        "Date Slider: 2023-06-15\n"
        "Animated Slider: 50\n"
        "Formatted Slider: 50\n"
        "Ticks Slider: 50\n"
        "Date Range: [datetime.date(2023, 3, 1), datetime.date(2023, 9, 30)]\n"
        "Datetime: 2023-06-15 12:30:00+00:00\n"
    )

    # Test setting new values
    slider1.set("75")
    slider2.set("80")
    slider3.set("40,60")
    slider4.set("2023-08-01")
    slider5.set("25")
    slider6.set("30")
    slider7.set("90")
    slider9.set("2023-04-01,2023-10-31")
    slider10.set("2023-07-15 15:45")

    # Verify updated output text
    current_values.expect_value(
        "Basic Slider: 75\n"
        "Step Slider: 80\n"
        "Range Slider: [40, 60]\n"
        "Date Slider: 2023-08-01\n"
        "Animated Slider: 25\n"
        "Formatted Slider: 30\n"
        "Ticks Slider: 90\n"
        "Date Range: [datetime.date(2023, 4, 1), datetime.date(2023, 10, 31)]\n"
        "Datetime: 2023-07-15 15:45:00+00:00\n"
    )
