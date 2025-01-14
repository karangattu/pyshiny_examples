from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_busy_indicators(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Get references to the input buttons
    compute_btn = controller.InputActionButton(page, "compute")
    compute2_btn = controller.InputActionButton(page, "compute2")

    # Get references to the output text elements
    result_text = controller.OutputText(page, "result")
    result2_text = controller.OutputText(page, "result2")

    # Test initial state
    compute_btn.expect_label("Start Long Computation")
    compute2_btn.expect_label("Another Long Task")

    # Test first computation
    compute_btn.click()
    result_text.expect_value("First computation completed!")

    # Test second computation
    compute2_btn.click()
    result2_text.expect_value("Second computation completed!")
