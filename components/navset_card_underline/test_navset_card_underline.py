from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_navset_card_underline(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test navset_card_underline
    navset = controller.NavsetCardUnderline(page, "nav_id")

    # Test initial state
    navset.expect_value("panel2")  # Initially selected panel

    # Test nav titles and values
    navset.expect_nav_titles(
        ["Panel 1", "Panel 2", "More Panels"]  # Menu title is included in nav titles
    )

    navset.expect_nav_values(
        ["panel1", "panel2", "panel3", "panel4"]  # Menu items values are included
    )

    # Test navigation between panels
    navset.set("panel1")
    navset.expect_value("panel1")

    navset.set("panel2")
    navset.expect_value("panel2")

    # Test text input in Panel 2
    text_input = controller.InputText(page, "txt")
    text_input.expect_label("Enter some text")
    text_input.expect_value("")
    text_input.set("Hello World")
    text_input.expect_value("Hello World")

    # Test slider in Panel 3
    navset.set("panel3")
    slider = controller.InputSlider(page, "n")
    slider.expect_label("N")
    slider.expect_value("20")  # Default value
    slider.set("50")
    slider.expect_value("50")

    # Test numeric input in Panel 4
    navset.set("panel4")
    numeric = controller.InputNumeric(page, "num")
    numeric.expect_label("Enter a number")
    numeric.expect_value("0")  # Default value
    numeric.set("42")
    numeric.expect_value("42")

    # Test outputs
    selected_panel_output = controller.OutputText(page, "selected_panel")
    selected_panel_output.expect_value("Currently selected panel: panel4")

    txt_output = controller.OutputText(page, "txt_out")
    txt_output.expect_value("Text input value: Hello World")

    num_output = controller.OutputText(page, "num_out")
    num_output.expect_value("Numeric input value: 42")

    slider_output = controller.OutputText(page, "slider_out")
    slider_output.expect_value("Slider value: 50")
