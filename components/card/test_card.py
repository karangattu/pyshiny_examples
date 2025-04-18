from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_cards(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test demo_card
    demo_card = controller.Card(page, "demo_card")
    demo_card.expect_header("Card DemoThis demonstrates all card parameters")
    demo_card.expect_height("300px")
    demo_card.expect_footer("Card Footer")
    demo_card.expect_full_screen_available(True)

    # Test dynamic_card
    dynamic_card = controller.Card(page, "dynamic_card")
    dynamic_card.expect_header("Dynamic Content Demo")
    dynamic_card.expect_height("200px")
    dynamic_card.expect_full_screen_available(True)

    # Test dynamic content in dynamic_card
    dynamic_content = controller.OutputText(page, "dynamic_content")
    dynamic_content.expect_value(
        "This card shows how to include dynamic content using render functions"
    )
