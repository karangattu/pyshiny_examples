from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_date_range_update(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test initial date range input
    date_range = controller.InputDateRange(page, "date_range")
    date_range.expect_label("Select Date Range")
    date_range.expect_value(("2023-01-01", "2023-12-31"))
    date_range.expect_min_date("2023-01-01")
    date_range.expect_max_date("2023-12-31")

    # Test new label input
    new_label = controller.InputText(page, "new_label")
    new_label.expect_label("New Label")
    new_label.expect_value("Updated Date Range")

    # Test new start date input
    new_start = controller.InputDate(page, "new_start")
    new_start.expect_label("New Start Date")
    new_start.expect_value("2023-06-01")

    # Test new end date input
    new_end = controller.InputDate(page, "new_end")
    new_end.expect_label("New End Date")
    new_end.expect_value("2023-06-30")

    # Test new min date input
    new_min = controller.InputDate(page, "new_min")
    new_min.expect_label("New Min Date")
    new_min.expect_value("2023-01-01")

    # Test new max date input
    new_max = controller.InputDate(page, "new_max")
    new_max.expect_label("New Max Date")
    new_max.expect_value("2023-12-31")

    # Test update button
    update_btn = controller.InputActionButton(page, "update")
    update_btn.expect_label("Update Date Range")

    # Test the output text
    current_range = controller.OutputText(page, "current_range")
    current_range.expect_value("Current selection: 2023-01-01 to 2023-12-31")

    # Test updating the date range
    new_label.set("New Custom Range")
    new_start.set("2023-06-15")
    new_end.set("2023-06-20")
    new_min.set("2023-06-01")
    new_max.set("2023-06-30")
    update_btn.click()

    # Verify the updates took effect
    date_range.expect_label("New Custom Range")
    date_range.expect_value(("2023-06-15", "2023-06-20"))
    date_range.expect_min_date("2023-06-01")
    date_range.expect_max_date("2023-06-30")
    current_range.expect_value("Current selection: 2023-06-15 to 2023-06-20")
