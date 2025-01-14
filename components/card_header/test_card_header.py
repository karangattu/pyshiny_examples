from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_card_headers(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test demo_card
    demo_card = controller.Card(page, "demo_card")
    demo_card.expect_header("Basic Header")
    demo_card.expect_height("500px")

    # Test custom_card
    custom_card = controller.Card(page, "custom_card")
    custom_card.expect_header("Custom Container Header")
    custom_card.expect_height("100px")

    # Test complex_card
    complex_card = controller.Card(page, "complex_card")
    complex_card.expect_header("Complex Header with Multiple Elements")
    complex_card.expect_height("100px")

    # Test icon_card
    icon_card = controller.Card(page, "icon_card")
    icon_card.expect_header("Header with Icon")
    icon_card.expect_height("100px")
