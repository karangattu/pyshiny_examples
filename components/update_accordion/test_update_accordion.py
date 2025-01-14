from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_accordion_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Initialize controllers for components with IDs
    accordion = controller.Accordion(page, "acc")
    update_all_btn = controller.InputActionButton(page, "update_all")
    show_ac_btn = controller.InputActionButton(page, "show_ac")
    show_b_btn = controller.InputActionButton(page, "show_b")
    show_none_btn = controller.InputActionButton(page, "show_none")
    show_all_btn = controller.InputActionButton(page, "show_all")

    # Test initial accordion state
    accordion.expect_multiple(True)

    # Get panel controllers
    panel_a = accordion.accordion_panel("sec_a")
    panel_b = accordion.accordion_panel("sec_b")
    panel_c = accordion.accordion_panel("sec_c")

    # Test initial panel content
    panel_a.expect_label("Section A")
    panel_a.expect_body("Original content for Section A")

    panel_b.expect_label("Section B")
    panel_b.expect_body("Original content for Section B")

    panel_c.expect_label("Section C")
    panel_c.expect_body("Original content for Section C")

    # Test update all functionality
    update_all_btn.click()

    # Verify updated content and titles
    panel_a.expect_label("New Section A Title")
    panel_a.expect_body("Updated content for Section A")

    panel_b.expect_body("Updated content for Section B")
    panel_c.expect_body("Updated content for Section C")

    # Test show only A & C functionality
    show_ac_btn.click()
    panel_a.expect_open(True)
    panel_b.expect_open(False)
    panel_c.expect_open(True)

    # Test show only B functionality
    show_b_btn.click()
    panel_a.expect_open(False)
    panel_b.expect_open(True)
    panel_c.expect_open(False)

    # Test collapse all functionality
    show_none_btn.click()
    panel_a.expect_open(False)
    panel_b.expect_open(False)
    panel_c.expect_open(False)

    # Test expand all functionality
    show_all_btn.click()
    panel_a.expect_open(True)
    panel_b.expect_open(True)
    panel_c.expect_open(True)
