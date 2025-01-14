from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_page_options_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test input slider
    slider = controller.InputSlider(page, "n")
    slider.expect_label("Number")
    slider.expect_min("0")
    slider.expect_max("100")
    slider.expect_value("20")  # Test initial value

    # Change slider value and verify output updates
    slider.set("50")
    txt1_output = controller.OutputText(page, "txt1")
    txt1_output.expect_value("You selected: 50")

    # Test numeric input
    numeric = controller.InputNumeric(page, "num")
    numeric.expect_label("Enter a number")
    numeric.expect_value("10")  # Test initial value

    # Change numeric input value and verify output updates
    numeric.set("25")
    txt2_output = controller.OutputText(page, "txt2")
    txt2_output.expect_value("You entered: 25")
