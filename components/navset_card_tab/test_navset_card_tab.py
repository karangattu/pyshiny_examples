from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_navset_card_tab_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test the navset card tab
    tabset = controller.NavsetCardTab(page, "tabset")

    # Test initial state
    tabset.expect_value("tab2")  # Should be initially selected
    tabset.expect_nav_titles(["Tab 1", "Tab 2", "Tab 3"])
    tabset.expect_nav_values(["tab1", "tab2", "tab3"])

    # Test tab navigation
    tabset.set("tab1")
    tabset.expect_value("tab1")

    tabset.set("tab3")
    tabset.expect_value("tab3")

    # Test the slider
    slider = controller.InputSlider(page, "n")

    # Test initial state
    slider.expect_value("20")  # Default value
    slider.expect_min("0")  # Min value
    slider.expect_max("100")  # Max value

    # Test setting new value
    slider.set("50")
    slider.expect_value("50")

    # Test another value
    slider.set("75")
    slider.expect_value("75")
