from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_navset_card_pill(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Get the navset controller
    navset = controller.NavsetCardPill(page, "selected_card_pill")

    # Test initial state and structure
    navset.expect_nav_titles(["A", "B", "C", "More Options"])
    navset.expect_nav_values(["A", "B", "C"])  # Menu items aren't included in values
    navset.expect_value("A")  # First panel should be selected by default

    # Test navigation to different panels
    navset.set("B")
    navset.expect_value("B")

    navset.set("C")
    navset.expect_value("C")

    # Test panel content visibility
    # Get panel controllers for each panel
    panel_a = navset.nav_panel("A")
    panel_b = navset.nav_panel("B")
    panel_c = navset.nav_panel("C")

    # Test panel A
    navset.set("A")
    panel_a.expect_active(True)
    panel_b.expect_active(False)
    panel_c.expect_active(False)

    # Test panel B
    navset.set("B")
    panel_a.expect_active(False)
    panel_b.expect_active(True)
    panel_c.expect_active(False)

    # Test panel C
    navset.set("C")
    panel_a.expect_active(False)
    panel_b.expect_active(False)
    panel_c.expect_active(True)

    # Test the selection tracker output
    selected_text = controller.OutputText(page, "selected_panel")

    navset.set("A")
    selected_text.expect_value("Currently selected panel: A")

    navset.set("B")
    selected_text.expect_value("Currently selected panel: B")

    navset.set("C")
    selected_text.expect_value("Currently selected panel: C")
