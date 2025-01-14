from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_update_checkbox_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test initial state of components
    new_label = controller.InputText(page, "new_label")
    new_label.expect_label("Enter new label for checkbox")
    new_label.expect_value("Updated checkbox label")

    new_value = controller.InputCheckbox(page, "new_value")
    new_value.expect_label("Set checkbox value to")
    new_value.expect_checked(True)

    update_btn = controller.InputActionButton(page, "update_btn")
    update_btn.expect_label("Update Checkbox")

    my_checkbox = controller.InputCheckbox(page, "my_checkbox")
    my_checkbox.expect_label("Initial checkbox label")
    my_checkbox.expect_checked(False)

    current_state = controller.OutputText(page, "current_state")
    current_state.expect_value("Current checkbox state: False")

    # Test updating the checkbox
    new_label.set("New Test Label")
    new_value.set(True)
    update_btn.click()

    # Verify the updates took effect
    my_checkbox.expect_label("New Test Label")
    my_checkbox.expect_checked(True)
    current_state.expect_value("Current checkbox state: True")

    # Test another update with different values
    new_label.set("Another Label")
    new_value.set(False)
    update_btn.click()

    # Verify the new updates
    my_checkbox.expect_label("Another Label")
    my_checkbox.expect_checked(False)
    current_state.expect_value("Current checkbox state: False")
