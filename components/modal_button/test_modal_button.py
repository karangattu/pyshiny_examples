from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_modal_button_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test the show modal button
    show_button = controller.InputActionButton(page, "show")
    show_button.expect_label("Show Modal")
    show_button.expect_class("btn-primary m-3")

    # Click the show button to open the modal
    show_button.click()

    # Test the full featured button in the modal
    full_featured_btn = controller.InputActionButton(page, "full_featured_btn")
    full_featured_btn.expect_label("Full Featured Button")
    full_featured_btn.expect_class("btn-warning")
