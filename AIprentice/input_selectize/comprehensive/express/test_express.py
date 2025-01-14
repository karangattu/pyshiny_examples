from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_selectize_inputs(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test first selectize (single selection)
    select1 = controller.InputSelectize(page, "select1")
    value1 = controller.OutputText(page, "value1")
    select1.expect_label("Choose a state:")
    select1.expect_multiple(False)
    select1.expect_choices(
        [
            "NY",
            "NJ",
            "CT",  # East Coast
            "WA",
            "OR",
            "CA",  # West Coast
            "MN",
            "WI",
            "IA",  # Midwest
        ]
    )
    select1.set("NY")
    value1.expect_value("Selected: 'NY'")

    # Test second selectize (multiple selection)
    select2 = controller.InputSelectize(page, "select2")
    value2 = controller.OutputText(page, "value2")
    select2.expect_label("Choose multiple states:")
    select2.expect_multiple(True)
    select2.expect_choices(
        [
            "NY",
            "NJ",
            "CT",  # East Coast
            "WA",
            "OR",
            "CA",  # West Coast
            "MN",
            "WI",
            "IA",  # Midwest
        ]
    )
    select2.set(["NY", "CA"])
    value2.expect_value("Selected: ('NY', 'CA')")

    # Test third selectize (with custom options)
    select3 = controller.InputSelectize(page, "select3")
    value3 = controller.OutputText(page, "value3")
    select3.expect_label("With placeholder:")
    select3.expect_multiple(True)
    select3.expect_choices(
        [
            "NY",
            "NJ",
            "CT",  # East Coast
            "WA",
            "OR",
            "CA",  # West Coast
            "MN",
            "WI",
            "IA",  # Midwest
        ]
    )
    select3.set(["WA", "OR"])
    value3.expect_value("Selected: ('WA', 'OR')")

    # Test fourth selectize (dynamic updates)
    select4 = controller.InputSelectize(page, "select4")
    value4 = controller.OutputText(page, "value4")
    update_btn = controller.InputActionButton(page, "update_btn")
    select4.expect_label("Dynamically updated choices:")
    select4.expect_multiple(True)
    select4.expect_choices([])  # Initially empty

    # Test update button functionality
    update_btn.click()
    select4.expect_choices(["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"])
    select4.expect_selected(["Option 1"])  # Default selection after update
    value4.expect_value("Selected: ('Option 1',)")

    # Test fifth selectize (server-side)
    select5 = controller.InputSelectize(page, "select5")
    value5 = controller.OutputText(page, "value5")
    select5.expect_label("Server-side search:")
    select5.expect_multiple(True)

    # Test sixth selectize (custom width)
    select6 = controller.InputSelectize(page, "select6")
    value6 = controller.OutputText(page, "value6")
    select6.expect_label("Fixed width selectize:")
    select6.expect_multiple(False)
    select6.expect_width("200px")
    select6.set("CA")
    value6.expect_value("Selected: 'CA'")
