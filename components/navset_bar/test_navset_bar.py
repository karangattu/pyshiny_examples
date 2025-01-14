from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_navset_bar_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test navset bar
    navset = controller.NavsetBar(page, "nav_id")
    navset.expect_value("tab1")  # Check initial selected value
    navset.expect_nav_values(["tab1", "tab2", "menu1", "menu2", "tab3"])
    navset.expect_nav_titles(["Tab 1", "Tab 2", "Menu Item 1", "Menu Item 2", "Tab 3"])

    # Test text input in Tab 1
    txt1 = controller.InputText(page, "txt1")
    txt1.expect_label("Enter text:")
    txt1.expect_value("Sample text")
    txt1.set("New text")
    txt1.expect_value("New text")

    # Switch to Tab 2 and test numeric input
    navset.set("tab2")
    navset.expect_value("tab2")

    num1 = controller.InputNumeric(page, "num1")
    num1.expect_label("Enter number:")
    num1.expect_value("5")
    num1.set("10")
    num1.expect_value("10")

    # Switch to Menu Item 1 and test slider
    navset.set("menu1")
    navset.expect_value("menu1")

    slider1 = controller.InputSlider(page, "slider1")
    slider1.expect_label("Select value:")
    slider1.expect_min("0")
    slider1.expect_max("100")
    slider1.expect_value("50")
    slider1.set("75")
    slider1.expect_value("75")

    # Switch to Menu Item 2 and test checkbox
    navset.set("menu2")
    navset.expect_value("menu2")

    chk1 = controller.InputCheckbox(page, "chk1")
    chk1.expect_label("Check this")
    chk1.expect_checked(True)
    chk1.set(False)
    chk1.expect_checked(False)

    # Switch to Tab 3 and test date input
    navset.set("tab3")
    navset.expect_value("tab3")

    date1 = controller.InputDate(page, "date1")
    date1.expect_label("Select date:")
    # Set a specific date and verify
    date1.set("2024-01-01")
    date1.expect_value("2024-01-01")

    # Test the selected tab output
    selected_output = controller.OutputText(page, "selected_tab")
    selected_output.expect_value("Currently selected: tab3")
