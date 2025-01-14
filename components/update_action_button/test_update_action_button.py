from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_update_action_button(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test initial state of input components
    new_label = controller.InputText(page, "new_label")
    new_label.expect_label("Enter new label")
    new_label.expect_value("Updated Label")

    toggle_disabled = controller.InputCheckbox(page, "toggle_disabled")
    toggle_disabled.expect_label("Disable button")
    toggle_disabled.expect_checked(False)

    update_btn = controller.InputActionButton(page, "update_btn")
    update_btn.expect_label("Update Button")

    target_btn = controller.InputActionButton(page, "target_btn")
    target_btn.expect_label("Original Button")

    # Test button state output
    button_state = controller.OutputText(page, "button_state")
    button_state.expect_value(
        """
            Button clicks: 0
            Current label: Updated Label
            Is disabled: False
            """
    )

    # Test updating the button
    new_label.set("New Test Label")
    toggle_disabled.set(True)
    update_btn.click()

    # Verify the target button has been updated
    target_btn.expect_label("New Test Label")

    # Verify the button state output has updated
    button_state.expect_value(
        """
            Button clicks: 0
            Current label: New Test Label
            Is disabled: True
            """
    )

    # Test clicking the target button
    target_btn.click()
    button_state.expect_value(
        """
            Button clicks: 1
            Current label: New Test Label
            Is disabled: True
            """
    )

    # Test resetting the disabled state
    toggle_disabled.set(False)
    update_btn.click()
    target_btn.expect_label("New Test Label")
