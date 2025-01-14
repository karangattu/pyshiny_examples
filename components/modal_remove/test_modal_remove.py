from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_modal_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test show modal button
    show_btn = controller.InputActionButton(page, "show")
    show_btn.expect_label("Show Modal")

    # Test remove modal button
    remove_btn = controller.InputActionButton(page, "remove")
    remove_btn.expect_label("Remove Modal")

    # Test modal interaction
    show_btn.click()

    # Test remove from modal button
    remove_modal_btn = controller.InputActionButton(page, "remove_from_modal")
    remove_modal_btn.expect_label("Remove")

    # Test removing modal using the button inside modal
    remove_modal_btn.click()

    # Show modal again
    show_btn.click()

    # Test removing modal using the button outside modal
    remove_btn.click()
