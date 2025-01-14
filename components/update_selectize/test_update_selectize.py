from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_update_selectize_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test selectize input
    state_select = controller.InputSelectize(page, "state")
    state_output = controller.OutputText(page, "current_selection")

    # Test initial state
    state_select.expect_label("Choose a state:")
    state_select.expect_multiple(True)
    state_select.expect_selected(["NY"])
    state_output.expect_value("Current selection: ('NY',)")

    # Test update label button
    update_label_btn = controller.InputActionButton(page, "update_label")
    update_label_btn.expect_label("Update Label")
    update_label_btn.click()
    state_select.expect_label("Updated State Selection Label:")

    # Test update choices button
    update_choices_btn = controller.InputActionButton(page, "update_choices")
    update_choices_btn.expect_label("Update Choices")
    update_choices_btn.click()
    state_select.expect_choices(["CO", "MT", "WY"])
    state_select.expect_selected(["CO"])
    state_output.expect_value("Current selection: ('CO',)")

    # Test update selected button
    update_selected_btn = controller.InputActionButton(page, "update_selected")
    update_selected_btn.expect_label("Update Selected")
    update_selected_btn.click()
    state_select.expect_selected(["NY", "CA"])
    state_output.expect_value("Current selection: ('NY', 'CA')")

    # Test update options button
    update_options_btn = controller.InputActionButton(page, "update_options")
    update_options_btn.expect_label("Update Options")
    update_options_btn.click()

    # Test reset button
    reset_btn = controller.InputActionButton(page, "reset")
    reset_btn.expect_label("Reset")
    reset_btn.click()
    state_select.expect_label("Choose a state:")
    state_select.expect_choices(["NY", "NJ", "CT", "WA", "OR", "CA"])
    state_select.expect_selected(["NY"])
    state_output.expect_value("Current selection: ('NY',)")

    # Test setting new values
    state_select.set(["NY", "CA"])
    state_output.expect_value("Current selection: ('NY', 'CA')")
