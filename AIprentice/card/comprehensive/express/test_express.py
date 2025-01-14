from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_card_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test main card with ID "demo_card"
    demo_card = controller.Card(page, "demo_card")

    # Test card properties
    demo_card.expect_header("Interactive Card Demo")
    demo_card.expect_height("400px")
    demo_card.expect_footer(
        "*This is an interactive demonstration of Shiny card capabilities.*"
    )
    demo_card.expect_full_screen_available(True)

    # Test card's content exists
    demo_card.expect_body("")  # Empty string since we're just checking if body exists
