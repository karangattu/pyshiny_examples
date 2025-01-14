from playwright.sync_api import Page, expect
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_accordion_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test main accordion
    accordion = controller.Accordion(page, "main_accordion")

    # Test initial state
    accordion.expect_multiple(True)  # Check if multiple panels can be open

    # Get individual panels
    panel_a = accordion.accordion_panel("section_a")
    panel_b = accordion.accordion_panel("section_b")
    panel_c = accordion.accordion_panel("section_c")
    panel_d = accordion.accordion_panel("section_d")

    # Test initial panel states (Section A should be open initially)
    panel_a.expect_open(True)
    panel_b.expect_open(False)
    panel_c.expect_open(False)
    panel_d.expect_open(False)

    # Test panel labels
    panel_a.expect_label("Section A")
    panel_b.expect_label("Section B")
    panel_c.expect_label("Section C")
    panel_d.expect_label("Section D")

    # Test control card
    control_card = controller.Card(page, "control_card")
    control_card.expect_header("Accordion Controls")

    # Test interactions
    # Open all panels using the button
    open_all_btn = controller.InputActionButton(page, "open_all")
    open_all_btn.click()

    # Verify all panels are open
    panel_a.expect_open(True)
    panel_b.expect_open(True)
    panel_c.expect_open(True)
    panel_d.expect_open(True)

    # Close all panels using the button
    close_all_btn = controller.InputActionButton(page, "close_all")
    close_all_btn.click()

    # Verify all panels are closed
    panel_a.expect_open(False)
    panel_b.expect_open(False)
    panel_c.expect_open(False)
    panel_d.expect_open(False)

    # Test individual panel toggling
    panel_b.set(True)  # Open panel B
    panel_b.expect_open(True)

    panel_b.set(False)  # Close panel B
    panel_b.expect_open(False)
