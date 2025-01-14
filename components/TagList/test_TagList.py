from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_taglist_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test Basic TagList card
    basic_card = controller.Card(page, "card1")
    basic_card.expect_header("Basic TagList")
    basic_card.expect_height("200px")
    basic_card.expect_full_screen_available(True)

    # Test HTML Elements card
    html_card = controller.Card(page, "card2")
    html_card.expect_header("TagList with HTML Elements")
    html_card.expect_height("200px")
    html_card.expect_full_screen_available(True)

    # Test Dynamic TagList card
    dynamic_card = controller.Card(page, "card3")
    dynamic_card.expect_header("Dynamic TagList")
    dynamic_card.expect_height("200px")
    dynamic_card.expect_full_screen_available(True)

    # Test Methods Demo card
    methods_card = controller.Card(page, "card4")
    methods_card.expect_header("TagList Methods Demo")
    methods_card.expect_height("200px")
    methods_card.expect_full_screen_available(True)
