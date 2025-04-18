from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_cards_with_footer(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test card1
    card1 = controller.Card(page, "card1")
    card1.expect_header("Basic Card with Header")
    card1.expect_height("300px")
    card1.expect_footer("Footer content")
    card1.expect_full_screen_available(True)

    # Test card2
    card2 = controller.Card(page, "card2")
    card2.expect_header("Card with Complex Footer")
    card2.expect_height("300px")
    card2.expect_full_screen_available(True)

    # Test card3
    card3 = controller.Card(page, "card3")
    card3.expect_header("Card with Interactive Footer")
    card3.expect_height("300px")
    card3.expect_full_screen_available(True)

    # Test the button and its interaction
    btn = controller.InputActionButton(page, "btn")
    btn.expect_label("Click Me")

    # Test initial state
    output_text = controller.OutputText(page, "click_count")
    output_text.expect_value("No clicks yet")

    # Test after clicking
    btn.click()
    output_text.expect_value("Clicked 1 times")

    # Test multiple clicks
    btn.click()
    output_text.expect_value("Clicked 2 times")
