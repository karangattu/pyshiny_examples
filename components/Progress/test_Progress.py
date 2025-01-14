from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_progress_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test card1
    card1 = controller.Card(page, "card1")
    card1.expect_header("Progress Demo")
    card1.expect_height("300px")
    card1.expect_full_screen_available(True)

    # Test card2
    card2 = controller.Card(page, "card2")
    card2.expect_header("Results")
    card2.expect_height("200px")
    card2.expect_full_screen_available(True)
