from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_navset_underline(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test navset
    navset = controller.NavsetUnderline(page, "nav_id")

    # Test initial state
    navset.expect_value("Panel A")
    navset.expect_nav_titles(["Panel A", "Panel B", "Panel C", "More Options"])
    navset.expect_nav_values(["Panel A", "panel_b", "Panel C", "More Options"])

    # Test input components
    text_a = controller.InputText(page, "text_a")
    text_a.expect_label("Enter text for Panel A")
    text_a.expect_value("Sample text")
    text_a.set("New text")

    # Switch to Panel B and test numeric input
    navset.set("panel_b")
    navset.expect_value("panel_b")

    num_b = controller.InputNumeric(page, "num_b")
    num_b.expect_label("Enter number for Panel B")
    num_b.expect_value("42")
    num_b.set("100")

    # Switch to Panel C and test slider
    navset.set("Panel C")
    navset.expect_value("Panel C")

    slider_c = controller.InputSlider(page, "slider_c")
    slider_c.expect_label("Slide in Panel C")
    slider_c.expect_value("50")
    slider_c.set("75")

    # Switch to Panel D and test checkbox
    navset.set("Panel D")
    navset.expect_value("Panel D")

    check_d = controller.InputCheckbox(page, "check_d")
    check_d.expect_label("Check this in Panel D")
    check_d.expect_checked(False)
    check_d.set(True)

    # Switch to Panel E and test radio buttons
    navset.set("Panel E")
    navset.expect_value("Panel E")

    radio_e = controller.InputRadioButtons(page, "radio_e")
    radio_e.expect_label("Choose in Panel E")
    radio_e.expect_choices(["Option 1", "Option 2", "Option 3"])
    radio_e.expect_selected(None)  # Initially no selection
    radio_e.set("Option 2")
