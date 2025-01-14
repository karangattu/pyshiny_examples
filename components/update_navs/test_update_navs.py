from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_update_navs_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Get controllers for the navset and buttons
    navset = controller.NavsetTab(page, "inTabset")
    goto1_btn = controller.InputActionButton(page, "goto1")
    goto2_btn = controller.InputActionButton(page, "goto2")
    goto3_btn = controller.InputActionButton(page, "goto3")

    # Test initial state
    navset.expect_value("panel1")  # First panel should be selected by default

    # Test button labels
    goto1_btn.expect_label("Go to Panel 1")
    goto2_btn.expect_label("Go to Panel 2")
    goto3_btn.expect_label("Go to Panel 3")

    # Test navigation using buttons
    goto2_btn.click()
    navset.expect_value("panel2")

    goto3_btn.click()
    navset.expect_value("panel3")

    goto1_btn.click()
    navset.expect_value("panel1")

    # Test direct navigation using navset
    navset.set("panel2")
    navset.expect_value("panel2")

    navset.set("panel3")
    navset.expect_value("panel3")

    # Test nav panel titles and values
    navset.expect_nav_titles(["Panel 1", "Panel 2", "Panel 3"])
    navset.expect_nav_values(["panel1", "panel2", "panel3"])
