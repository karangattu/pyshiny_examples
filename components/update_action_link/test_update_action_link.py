from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_action_link_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Get controllers for the action link and update button
    action_link = controller.InputActionLink(page, "my_link")
    update_button = controller.InputActionButton(page, "update")

    # Test initial state
    action_link.expect_label("Click me to update")

    # Test update button
    update_button.expect_label("Update the action link")

    # Click the update button and verify the action link changes
    update_button.click()
    action_link.expect_label("Updated 1 times")

    # Click again to verify counter increases
    update_button.click()
    action_link.expect_label("Updated 2 times")
