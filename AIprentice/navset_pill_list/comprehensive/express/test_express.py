from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_navset_pill_list_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test navset pill list
    navset = controller.NavsetPillList(page, "selected_navset_pill_list")
    navset.expect_well(True)
    navset.expect_widths([3, 9])
    navset.expect_nav_titles(["Panel A", "Panel B", "Panel C", "More Options"])
    navset.expect_value("Panel A")  # Default selected panel

    # Test text input in Panel A
    text_input = controller.InputText(page, "text_input")
    text_input.expect_label("Enter some text")
    text_input.expect_value("Sample text")
    text_input.set("New test text")

    # Switch to Panel B and test region select
    navset.set("Panel B")
    navset.expect_value("Panel B")

    region_select = controller.InputSelect(page, "region")
    region_select.expect_label("Select Region")
    region_select.expect_choices(["East Coast", "West Coast", "Midwest"])
    region_select.set("East Coast")

    # Switch to Panel C and test numeric and slider inputs
    navset.set("Panel C")
    navset.expect_value("Panel C")

    number_input = controller.InputNumeric(page, "number")
    number_input.expect_label("Enter a number")
    number_input.expect_value("5")
    number_input.set("10")

    slider_input = controller.InputSlider(page, "slider")
    slider_input.expect_label("Adjust slider")
    slider_input.expect_min("0")
    slider_input.expect_max("100")
    slider_input.expect_value("50")
    slider_input.set("75")
