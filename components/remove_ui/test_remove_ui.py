from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_dynamic_ui(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test action buttons
    add_btn = controller.InputActionButton(page, "add")
    remove_btn = controller.InputActionButton(page, "remove")

    # Test initial button states
    add_btn.expect_label("Add Content")
    remove_btn.expect_label("Remove Content")

    # Test adding content
    add_btn.click()

    # Test removing content
    remove_btn.click()
