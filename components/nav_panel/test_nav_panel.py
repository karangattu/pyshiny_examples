from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_nav_panel_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test navset tab
    navset = controller.NavsetTab(page, "nav")

    # Test initial state
    navset.expect_nav_titles(["Basic Panel", "Panel with Value", "Panel with Icon"])
    navset.expect_nav_values(
        [
            "Basic Panel",  # When no value is specified, title is used as value
            "panel2",
            "panel3",
        ]
    )
    navset.expect_value("Basic Panel")  # First panel should be selected by default

    # Test panel selection
    navset.set("panel2")
    navset.expect_value("panel2")

    navset.set("panel3")
    navset.expect_value("panel3")

    # Test going back to first panel
    navset.set("Basic Panel")
    navset.expect_value("Basic Panel")

    # Test the output text that shows selected panel
    selected_text = controller.OutputText(page, "selected_panel")
    selected_text.expect_value("Currently selected panel value: Basic Panel")

    # Test panel selection reflects in output text
    navset.set("panel2")
    selected_text.expect_value("Currently selected panel value: panel2")

    navset.set("panel3")
    selected_text.expect_value("Currently selected panel value: panel3")
