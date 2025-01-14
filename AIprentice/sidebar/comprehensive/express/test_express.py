from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_dashboard_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test sidebar since it has an explicit ID
    sidebar = controller.Sidebar(page, "main_sidebar")

    # Test sidebar attributes
    sidebar.expect_title("Control Panel")
    sidebar.expect_desktop_state("open")  # Since open="desktop" in the app
    sidebar.expect_open(True)  # Sidebar should be initially open on desktop

    # Test sidebar content
    sidebar.expect_text("Filters and Controls")  # Test for h4 content

    # Close and reopen sidebar to test functionality
    sidebar.set(False)  # Close sidebar
    sidebar.expect_open(False)

    sidebar.set(True)  # Open sidebar
    sidebar.expect_open(True)
