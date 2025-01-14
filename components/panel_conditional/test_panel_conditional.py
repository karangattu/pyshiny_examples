from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_panel_conditional_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Get controllers for inputs
    checkbox = controller.InputCheckbox(page, "show")
    slider = controller.InputSlider(page, "value")
    state_text = controller.OutputText(page, "state")

    # Test initial state
    checkbox.expect_label("Show panels")
    checkbox.expect_checked(True)

    slider.expect_label("Slider value")
    slider.expect_min("0")
    slider.expect_max("100")
    slider.expect_value("75")

    # Verify initial state text
    state_text.expect_value("Current State:\nCheckbox: True\nSlider: 75")

    # Test checkbox interaction
    checkbox.set(False)
    state_text.expect_value("Current State:\nCheckbox: False\nSlider: 75")

    # Test slider interaction
    slider.set("25")
    state_text.expect_value("Current State:\nCheckbox: False\nSlider: 25")

    # Test combinations that affect the complex panel
    # First make sure checkbox is checked
    checkbox.set(True)

    # Test slider value > 75 (should show complex panel)
    slider.set("80")
    state_text.expect_value("Current State:\nCheckbox: True\nSlider: 80")

    # Test slider value < 25 (should show complex panel)
    slider.set("20")
    state_text.expect_value("Current State:\nCheckbox: True\nSlider: 20")

    # Test slider value between 25 and 75 (should hide complex panel)
    slider.set("50")
    state_text.expect_value("Current State:\nCheckbox: True\nSlider: 50")
