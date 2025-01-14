from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_accordion_update(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Get controllers for the components with IDs
    accordion = controller.Accordion(page, "acc1")
    update_btn = controller.InputActionButton(page, "update_btn")

    # Test initial state of accordion
    accordion.expect_panels(["Original Title"])
    panel = accordion.accordion_panel("panel1")
    panel.expect_open(True)
    panel.expect_label("Original Title")
    panel.expect_body("This is the original content")

    # Test update button
    update_btn.expect_label("Update Panel Content")

    # Click update button and verify changes
    update_btn.click()

    # Verify the panel updates after clicking
    panel = accordion.accordion_panel("panel1")
    panel.expect_open(True)
    panel.expect_label("Updated Title")
