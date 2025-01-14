from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_radio_buttons_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test radio buttons input
    radio_buttons = controller.InputRadioButtons(page, "radio_demo")
    selection_output = controller.OutputText(page, "selection")

    # Test initial state
    radio_buttons.expect_label("Demo Radio Group")
    radio_buttons.expect_choices(["choice1", "choice2", "choice3"])
    radio_buttons.expect_selected("choice1")  # Test default selection
    radio_buttons.expect_inline(True)
    radio_buttons.expect_width("300px")
    selection_output.expect_value("You selected: choice1")

    # Test changing selections
    radio_buttons.set("choice2")
    selection_output.expect_value("You selected: choice2")

    radio_buttons.set("choice3")
    selection_output.expect_value("You selected: choice3")

    # Test going back to first choice
    radio_buttons.set("choice1")
    selection_output.expect_value("You selected: choice1")
