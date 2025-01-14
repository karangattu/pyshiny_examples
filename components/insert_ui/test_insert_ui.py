from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_insert_ui_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test the add button
    add_button = controller.InputActionButton(page, "add")
    add_button.expect_label("Add UI Elements")

    # Click the button and test the first set of insertions
    add_button.click()

    # Note: We cannot test the dynamically inserted elements directly with controllers
    # since they don't exist at app initialization and controllers require IDs to be
    # defined in the original app code. The dynamic IDs are generated after button clicks.
