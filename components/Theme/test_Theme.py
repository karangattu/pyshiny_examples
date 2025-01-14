from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_theme_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test input text
    name_input = controller.InputText(page, "name")
    name_input.expect_label("Enter your name")
    name_input.expect_value("User")  # Test default value
    name_input.set("Test User")
    name_input.expect_value("Test User")

    # Test slider
    size_slider = controller.InputSlider(page, "size")
    size_slider.expect_label("Text size")
    size_slider.expect_min("12")  # Convert number to string for testing
    size_slider.expect_max("32")
    size_slider.expect_value("16")  # Test default value
    size_slider.set("20")
    size_slider.expect_value("20")

    # Test select input
    color_select = controller.InputSelect(page, "color")
    color_select.expect_label("Select color theme")
    color_select.expect_choices(["primary", "success", "warning", "danger"])
    color_select.expect_selected(["primary"])  # Test default value
    color_select.set("success")
    color_select.expect_selected(["success"])
