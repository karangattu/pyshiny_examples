from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_text_area_update(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test initial text area
    textarea = controller.InputTextArea(page, "textarea")
    textarea.expect_label("Sample Text Area")
    textarea.expect_value("Initial text")
    textarea.expect_placeholder("Enter your text here")
    textarea.expect_height("200px")
    textarea.expect_rows("5")

    # Test control panel inputs
    new_label = controller.InputText(page, "new_label")
    new_label.expect_label("New Label")
    new_label.expect_value("Updated Label")

    new_value = controller.InputText(page, "new_value")
    new_value.expect_label("New Value")
    new_value.expect_value("Updated text content")

    new_placeholder = controller.InputText(page, "new_placeholder")
    new_placeholder.expect_label("New Placeholder")
    new_placeholder.expect_value("Updated placeholder text")

    # Test update button
    update_btn = controller.InputActionButton(page, "update")
    update_btn.expect_label("Update Text Area")

    # Test updating the text area
    update_btn.click()

    # Verify text area updates after button click
    textarea.expect_label("Updated Label")
    textarea.expect_value("Updated text content")
    textarea.expect_placeholder("Updated placeholder text")

    # Test changing values and updating again
    new_label.set("Another Label")
    new_value.set("Another text content")
    new_placeholder.set("Another placeholder")
    update_btn.click()

    # Verify new updates
    textarea.expect_label("Another Label")
    textarea.expect_value("Another text content")
    textarea.expect_placeholder("Another placeholder")
