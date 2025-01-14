from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_text_area_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Get the text area controller
    text_area = controller.InputTextArea(page, "text_input")

    # Test initial state
    text_area.expect_label("Enter your text:")
    text_area.expect_value(
        "This is some default text.\nIt has multiple lines.\nYou can edit it!"
    )
    text_area.expect_width("500px")
    text_area.expect_height("200px")
    text_area.expect_cols("50")
    text_area.expect_rows("8")
    text_area.expect_placeholder("Type something here...")
    text_area.expect_resize("both")
    text_area.expect_autoresize(True)
    text_area.expect_spellcheck("true")

    # Test output text controller
    output_text = controller.OutputText(page, "show_text")
    output_text.expect_value(
        "You entered:\nThis is some default text.\nIt has multiple lines.\nYou can edit it!"
    )

    # Test setting new value
    new_text = "This is new text\nWith new lines"
    text_area.set(new_text)
    output_text.expect_value(f"You entered:\n{new_text}")
