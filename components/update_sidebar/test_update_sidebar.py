from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_update_sidebar(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Get controllers for the components with IDs
    sidebar = controller.Sidebar(page, "demo_sidebar")
    show_btn = controller.InputActionButton(page, "show_sidebar")
    hide_btn = controller.InputActionButton(page, "hide_sidebar")

    # Test initial state
    sidebar.expect_open(True)  # Since open="always" in initial state

    # Test button labels
    show_btn.expect_label("Show Sidebar")
    hide_btn.expect_label("Hide Sidebar")

    # Test hiding sidebar
    hide_btn.click()
    sidebar.expect_open(False)

    # Test showing sidebar
    show_btn.click()
    sidebar.expect_open(True)
