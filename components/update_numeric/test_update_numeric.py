from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_update_numeric_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test initial numeric input state
    number = controller.InputNumeric(page, "number")
    number.expect_label("Number")
    number.expect_value("5")

    # Test the control panel inputs
    new_label = controller.InputText(page, "new_label")
    new_label.expect_label("New Label")
    new_label.expect_value("Updated Number")

    new_value = controller.InputNumeric(page, "new_value")
    new_value.expect_label("New Value")
    new_value.expect_value("10")

    new_min = controller.InputNumeric(page, "new_min")
    new_min.expect_label("New Min")
    new_min.expect_value("0")

    new_max = controller.InputNumeric(page, "new_max")
    new_max.expect_label("New Max")
    new_max.expect_value("100")

    new_step = controller.InputNumeric(page, "new_step")
    new_step.expect_label("New Step")
    new_step.expect_value("5")

    update_btn = controller.InputActionButton(page, "update")
    update_btn.expect_label("Update Numeric Input")

    # Test the text output showing current value
    show_value = controller.OutputText(page, "show_value")
    show_value.expect_value("Current value: 5")

    # Test updating the numeric input
    update_btn.click()

    # Verify the numeric input was updated with new values
    number.expect_label("Updated Number")
    number.expect_value("10")
    show_value.expect_value("Current value: 10")

    # Test setting a new value
    number.set("15")
    show_value.expect_value("Current value: 15")
