from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_notification_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test default notification button
    default_btn = controller.InputActionButton(page, "show_default")
    default_btn.expect_label("Show Default")

    # Test message notification button
    message_btn = controller.InputActionButton(page, "show_message")
    message_btn.expect_label("Show Message")

    # Test warning notification button
    warning_btn = controller.InputActionButton(page, "show_warning")
    warning_btn.expect_label("Show Warning")

    # Test error notification button
    error_btn = controller.InputActionButton(page, "show_error")
    error_btn.expect_label("Show Error")

    # Test action notification button
    action_btn = controller.InputActionButton(page, "show_action")
    action_btn.expect_label("Show Action")

    # Test persistent notification button
    persistent_btn = controller.InputActionButton(page, "show_persistent")
    persistent_btn.expect_label("Show Persistent")

    # Test ID based notification button
    id_btn = controller.InputActionButton(page, "show_id")
    id_btn.expect_label("Show ID Based")

    # Test button interactions
    default_btn.click()
    message_btn.click()
    warning_btn.click()
    error_btn.click()
    action_btn.click()
    persistent_btn.click()
    id_btn.click()
