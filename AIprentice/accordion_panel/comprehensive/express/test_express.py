from playwright.sync_api import Page, expect
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_accordion_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test first accordion (acc1)
    accordion1 = controller.Accordion(page, "acc1")

    # Test individual panels in first accordion
    panel1 = accordion1.accordion_panel("panel1")
    panel2 = accordion1.accordion_panel("panel2")

    # Check initial states
    panel1.expect_label("Basic Panel with Icon")
    panel2.expect_label("<span style='color: blue;'>HTML Title</span>")

    # Test second accordion (acc2)
    accordion2 = controller.Accordion(page, "acc2")

    # Test panels in second accordion using the data structure from the app
    section_a = accordion2.accordion_panel("section_Section A")
    section_b = accordion2.accordion_panel("section_Section B")
    section_c = accordion2.accordion_panel("section_Section C")

    # Check content of panels
    section_a.expect_body(
        "This is the content for Section A. It demonstrates basic accordion panel usage."
    )
    section_b.expect_body(
        "This is the content for Section B with some numbers: 123, 456, 789"
    )
    section_c.expect_body(
        "This is the content for Section C with special characters: !@#$%"
    )

    # Test third accordion (acc3)
    accordion3 = controller.Accordion(page, "acc3")
    interactive_panel = accordion3.accordion_panel("interactive")
    interactive_panel.expect_label("Interactive Panel")

    # Test input elements in the interactive panel
    panel_text = controller.InputText(page, "panel_text")
    update_btn = controller.InputActionButton(page, "update_btn")

    # Test initial state of input
    panel_text.expect_label("Enter text:")
    panel_text.expect_value("Sample text")
    update_btn.expect_label("Update Panel")

    # Test interaction
    panel_text.set("New Panel Text")
    update_btn.click()

    # Test dynamic panel creation
    dynamic_panel = accordion3.accordion_panel("dynamic")
    dynamic_panel.expect_label("Dynamic Panel - New Panel Text")
