from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_nav_menu(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test the navset
    navset = controller.NavsetCardTab(page, "selected_nav")

    # Test nav values
    navset.expect_nav_values(["panel_a", "panel_b", "panel_c", "Regular Panel"])

    # Test nav titles
    navset.expect_nav_titles(["Panel A", "Panel B", "Panel C", "Regular Panel"])

    # Test initial value
    navset.expect_value("panel_a")

    # Test selection changes
    navset.set("panel_b")
    navset.expect_value("panel_b")

    navset.set("panel_c")
    navset.expect_value("panel_c")

    # Get the output text showing current selection
    output_text = controller.OutputText(page, "current_selection")
    output_text.expect_value("Currently selected: panel_c")

    # Test switching to regular panel
    navset.set("Regular Panel")
    navset.expect_value("Regular Panel")
    output_text.expect_value("Currently selected: Regular Panel")
