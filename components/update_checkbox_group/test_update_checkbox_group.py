from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_checkbox_group_updates(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Get controllers for all components with IDs
    checkbox_group = controller.InputCheckboxGroup(page, "checkbox_group")
    new_label = controller.InputText(page, "new_label")
    inline_toggle = controller.InputCheckbox(page, "inline_toggle")
    new_choices = controller.InputSelectize(page, "new_choices")
    new_selected = controller.InputSelectize(page, "new_selected")
    update_btn = controller.InputActionButton(page, "update")
    current_value = controller.OutputText(page, "current_value")

    # Test initial states
    checkbox_group.expect_label("Checkbox Group (will be updated)")
    checkbox_group.expect_choices(["Item A", "Item B", "Item C", "Item D"])
    checkbox_group.expect_selected(["Item A"])
    checkbox_group.expect_inline(False)

    new_label.expect_value("Updated Label")
    inline_toggle.expect_checked(False)

    new_choices.expect_choices(["Item A", "Item B", "Item C", "Item D"])
    new_choices.expect_selected(["Item A", "Item B"])
    new_choices.expect_multiple(True)

    new_selected.expect_choices(["Item A", "Item B", "Item C", "Item D"])
    new_selected.expect_selected(["Item A"])
    new_selected.expect_multiple(True)

    current_value.expect_value("Current selection: ('Item A',)")

    # Test updating checkbox group
    # Change label
    new_label.set("New Custom Label")

    # Toggle inline display
    inline_toggle.set(True)

    # Change choices
    new_choices.set(["Item B", "Item C"])

    # Change selected values
    new_selected.set(["Item B", "Item C"])

    # Click update button
    update_btn.click()

    # Verify updates
    checkbox_group.expect_label("New Custom Label")
    checkbox_group.expect_choices(["Item B", "Item C"])
    checkbox_group.expect_selected(["Item B", "Item C"])
    checkbox_group.expect_inline(True)

    current_value.expect_value("Current selection: ('Item B', 'Item C')")
