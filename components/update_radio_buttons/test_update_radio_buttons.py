from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_radio_buttons_update(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Get controllers for the components
    radio_group = controller.InputRadioButtons(page, "radio_group")
    update_btn = controller.InputActionButton(page, "update_btn")
    selection_output = controller.OutputText(page, "selection")

    # Test initial state
    radio_group.expect_label("Original Radio Buttons")
    radio_group.expect_choices(["Option A", "Option B", "Option C"])
    radio_group.expect_selected("Option A")
    radio_group.expect_inline(False)

    # Test initial selection output
    selection_output.expect_value("Current selection: Option A")

    # Test button
    update_btn.expect_label("Update Radio Buttons")

    # Test changing selection
    radio_group.set("Option B")
    selection_output.expect_value("Current selection: Option B")

    # Test updating radio buttons via button click
    update_btn.click()

    # Test updated state
    radio_group.expect_label("Updated Radio Buttons")
    radio_group.expect_choices(["New Option 1", "New Option 2", "New Option 3"])
    radio_group.expect_selected("New Option 2")
    radio_group.expect_inline(True)
    selection_output.expect_value("Current selection: New Option 2")

    # Test selection after update
    radio_group.set("New Option 3")
    selection_output.expect_value("Current selection: New Option 3")
