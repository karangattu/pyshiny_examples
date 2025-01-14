from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_navset_tab(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Get the navset tab controller
    navset = controller.NavsetTab(page, "tabset")

    # Test initial state
    navset.expect_value("tab2")  # Should be initially selected
    navset.expect_nav_values(["tab1", "tab2", "tab3", "tab4", "tab5"])
    navset.expect_nav_titles(["Tab 1", "Tab 2", "Tab 3", "Tab 4", "Tab 5"])

    # Test navigation between tabs
    navset.set("tab1")
    navset.expect_value("tab1")

    navset.set("tab3")
    navset.expect_value("tab3")

    navset.set("tab4")
    navset.expect_value("tab4")

    navset.set("tab5")
    navset.expect_value("tab5")

    # Test output text that shows selected tab
    output_text = controller.OutputText(page, "selected_tab")

    # Test initial state
    navset.set("tab2")  # Set back to initial tab
    output_text.expect_value("Currently selected tab: tab2")

    # Test output updates when changing tabs
    navset.set("tab1")
    output_text.expect_value("Currently selected tab: tab1")

    navset.set("tab3")
    output_text.expect_value("Currently selected tab: tab3")
