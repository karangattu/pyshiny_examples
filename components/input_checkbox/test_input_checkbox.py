from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_checkbox_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test basic checkbox
    basic_checkbox = controller.InputCheckbox(page, "basic")
    basic_checkbox.expect_label("Basic checkbox")
    basic_checkbox.expect_checked(False)  # Default value should be False

    # Test checkbox with preset value
    preset_checkbox = controller.InputCheckbox(page, "preset_value")
    preset_checkbox.expect_label("Checkbox with preset value")
    preset_checkbox.expect_checked(True)  # Should be initially True

    # Test checkbox with custom width
    custom_width_checkbox = controller.InputCheckbox(page, "custom_width")
    custom_width_checkbox.expect_label("Checkbox with custom width (300px)")
    custom_width_checkbox.expect_checked(False)  # Should be initially False
    custom_width_checkbox.expect_width("300px")

    # Test interactivity by changing values
    basic_checkbox.set(True)
    basic_checkbox.expect_checked(True)

    preset_checkbox.set(False)
    preset_checkbox.expect_checked(False)

    custom_width_checkbox.set(True)
    custom_width_checkbox.expect_checked(True)
