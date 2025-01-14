from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_layout_columns_demo(page: Page, local_app: ShinyAppProc) -> None:
    """Test the Layout Columns Demo app."""
    page.goto(local_app.url)

    # Test card1_content output
    card1_output = controller.OutputText(page, "card1_content")
    card1_output.expect_value("Dynamic content for card 1")

    # Test card2_content output
    card2_output = controller.OutputText(page, "card2_content")
    card2_output.expect_value("Dynamic content for card 2")

    # Test card3_content output
    card3_output = controller.OutputText(page, "card3_content")
    card3_output.expect_value("Dynamic content for card 3")

    # Test card4_content output
    card4_output = controller.OutputText(page, "card4_content")
    card4_output.expect_value("Dynamic content for card 4")

    # Test card5_content output
    card5_output = controller.OutputText(page, "card5_content")
    card5_output.expect_value("Dynamic content for card 5")
