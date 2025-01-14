from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_dark_mode_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test dark mode input
    dark_mode = controller.InputDarkMode(page, "mode")
    dark_mode.expect_mode("light")  # Default mode is light
    dark_mode.click()  # Toggle dark mode
    dark_mode.expect_mode("dark")
    dark_mode.expect_page_mode("dark")  # Check if page mode is updated

    # Test slider input
    slider = controller.InputSlider(page, "n")
    slider.expect_label("Number of bins")
    slider.expect_min("0")
    slider.expect_max("100")
    slider.expect_value("20")  # Check default value

    # Test setting new slider value
    slider.set("50")
    slider.expect_value("50")
