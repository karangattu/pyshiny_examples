from playwright.sync_api import Page, expect
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_remove_accordion_panels(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Get controllers for the components
    accordion = controller.Accordion(page, "acc")
    remove_btn = controller.InputActionButton(page, "remove_panel")

    # Test initial state
    # Check if accordion allows multiple panels
    accordion.expect_multiple(True)

    # Test initial panels
    for letter in ["A", "B", "C", "D", "E"]:
        panel = accordion.accordion_panel(f"section_{letter}")
        panel.expect_label(f"Section {letter}")
        panel.expect_body(f"This is content for section {letter}")
        panel.expect_open(True)  # All panels should be open initially

    # Test remove button initial state
    remove_btn.expect_label("Remove Section A")

    # Test removing panels one by one
    for letter in ["A", "B", "C", "D"]:
        remove_btn.click()
        # Verify button label updates
        remove_btn.expect_label(f"Remove Section {chr(ord(letter) + 1)}")

    # Remove last panel
    remove_btn.click()
    # Verify final button state
    remove_btn.expect_label("All panels removed!")
