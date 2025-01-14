from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_dynamic_accordion(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Get controllers for components with IDs
    add_button = controller.InputActionButton(page, "add_panel")
    accordion = controller.Accordion(page, "accordion_demo")

    # Test initial state
    add_button.expect_label("Add New Panel")

    # Test initial accordion state
    initial_panel = accordion.accordion_panel("panel1")
    initial_panel.expect_label("Initial Panel")
    initial_panel.expect_open(True)  # Since open=True in initial setup

    # Test adding new panels
    # Add first new panel
    add_button.click()
    panel2 = accordion.accordion_panel("panel2")
    panel2.expect_label("Panel 2")

    # Add second new panel
    add_button.click()
    panel3 = accordion.accordion_panel("panel3")
    panel3.expect_label("Panel 3")

    # Verify all panels exist and have correct labels
    accordion.expect_panels(["Initial Panel", "Panel 2", "Panel 3"])
