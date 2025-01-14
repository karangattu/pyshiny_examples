from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_modal_dialog(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test the show button
    show_btn = controller.InputActionButton(page, "show")
    show_btn.expect_label("Show modal dialog")

    # Test the output text
    txt_output = controller.OutputText(page, "txt")
    txt_output.expect_value("The main app remains interactive while modal is shown")

    # Click show button to open modal
    show_btn.click()

    # Test the modal input text
    modal_input = controller.InputText(page, "modal_input")
    modal_input.expect_label("Enter some text:")
    modal_input.expect_value("")

    # Test setting a value in the modal input
    test_text = "Test input text"
    modal_input.set(test_text)
    modal_input.expect_value(test_text)
