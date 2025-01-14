from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_update_select_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test initial state of select input
    state_select = controller.InputSelect(page, "state")
    state_select.expect_label("Choose a state:")
    state_select.expect_selected(["NY"])  # Test initial selection
    state_select.expect_choices(
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

    # Test update button
    update_btn = controller.InputActionButton(page, "update")
    update_btn.expect_label("Update Select Input")

    # Test interaction flow
    update_btn.click()

    # After clicking update, verify the select input has been updated
    state_select.expect_label("Updated State Selection (Click #1)")
    state_select.expect_selected(["TX"])  # New selection after update
    state_select.expect_choices(["FL", "TX", "AZ"])  # New choices after update

    # Test changing selection
    state_select.set("FL")
    state_select.expect_selected(["FL"])

    # Test another update
    update_btn.click()
    state_select.expect_label("Updated State Selection (Click #2)")
    state_select.expect_selected(["TX"])  # Selection resets to TX after each update
