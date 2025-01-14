from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_navset_pill_list_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test the navset pill list
    navset = controller.NavsetPillList(page, "selected_pill_list")
    navset.expect_well(True)  # Test that well parameter is True
    navset.expect_widths([3, 9])  # Test the widths parameter
    navset.expect_value("Panel A")  # Test initial selected value
    navset.expect_nav_values(["Panel A", "Panel B", "Panel C", "Panel D"])
    navset.expect_nav_titles(["Panel A", "Panel B", "More Options"])

    # Test input text in Panel A (initially visible)
    text_a = controller.InputText(page, "text_a")
    text_a.expect_label("Enter text for Panel A")
    text_a.expect_value("")
    text_a.set("Test input")

    # Switch to Panel B and test slider
    navset.set("Panel B")
    navset.expect_value("Panel B")

    slider_b = controller.InputSlider(page, "slider_b")
    slider_b.expect_label("Slider for Panel B")
    slider_b.expect_min("0")
    slider_b.expect_max("100")
    slider_b.expect_value("50")
    slider_b.set("75")

    # Switch to Panel C and test numeric input
    navset.set("Panel C")
    navset.expect_value("Panel C")

    num_c = controller.InputNumeric(page, "num_c")
    num_c.expect_label("Number input for Panel C")
    num_c.expect_value("0")
    num_c.set("42")

    # Switch to Panel D and test checkbox
    navset.set("Panel D")
    navset.expect_value("Panel D")

    check_d = controller.InputCheckbox(page, "check_d")
    check_d.expect_label("Checkbox for Panel D")
    check_d.expect_checked(False)
    check_d.set(True)
