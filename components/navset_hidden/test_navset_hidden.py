from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_navset_hidden_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test radio buttons controller
    radio_buttons = controller.InputRadioButtons(page, "controller")
    radio_buttons.expect_label("Select Panel")
    radio_buttons.expect_choices(["panel1", "panel2", "panel3"])
    radio_buttons.expect_selected("panel1")  # Test initial selection

    # Test navset_hidden
    navset = controller.NavsetHidden(page, "hidden_nav")
    navset.expect_nav_values(["panel1", "panel2", "panel3"])
    navset.expect_value("panel1")  # Test initial panel

    # Test switching panels using radio buttons and verify navset updates
    radio_buttons.set("panel2")
    navset.expect_value("panel2")

    radio_buttons.set("panel3")
    navset.expect_value("panel3")

    # Switch back to first panel
    radio_buttons.set("panel1")
    navset.expect_value("panel1")
