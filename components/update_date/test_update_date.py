from datetime import date, timedelta
from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_date_update_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Get controllers for the input date and buttons
    date_input = controller.InputDate(page, "demo_date")
    update_label_btn = controller.InputActionButton(page, "update_label")
    update_value_btn = controller.InputActionButton(page, "update_value")
    update_min_btn = controller.InputActionButton(page, "update_min")
    update_max_btn = controller.InputActionButton(page, "update_max")
    current_value_txt = controller.OutputText(page, "current_value")

    # Test initial state
    date_input.expect_label("Select a date")
    date_input.expect_value("2024-01-01")
    current_value_txt.expect_value("Current date: 2024-01-01")

    # Test update label button
    update_label_btn.expect_label("Update Label")
    update_label_btn.click()
    today_str = date.today().strftime("%Y-%m-%d")
    date_input.expect_label(f"Updated Label ({today_str})")

    # Test update value button
    update_value_btn.expect_label("Update Value")
    update_value_btn.click()
    tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    date_input.expect_value(tomorrow)
    current_value_txt.expect_value(f"Current date: {tomorrow}")

    # Test update min date button
    update_min_btn.expect_label("Update Min Date")
    update_min_btn.click()
    today = date.today().strftime("%Y-%m-%d")
    date_input.expect_min_date(today)

    # Test update max date button
    update_max_btn.expect_label("Update Max Date")
    update_max_btn.click()
    max_date = (date.today() + timedelta(days=30)).strftime("%Y-%m-%d")
    date_input.expect_max_date(max_date)

    # Test setting a new date value directly
    new_date = "2024-02-15"
    date_input.set(new_date)
    date_input.expect_value(new_date)
    current_value_txt.expect_value(f"Current date: {new_date}")
