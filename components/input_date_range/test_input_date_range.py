from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_date_range_input(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Initialize the date range input controller
    date_range = controller.InputDateRange(page, "date_range")

    # Test initial properties
    date_range.expect_label("Select Date Range")
    date_range.expect_value(("2023-01-01", "2023-12-31"))  # Test initial values
    date_range.expect_min_date("2020-01-01")  # Test minimum date
    date_range.expect_max_date("2025-12-31")  # Test maximum date
    date_range.expect_format("mm/dd/yyyy")  # Test date format
    date_range.expect_startview("decade")  # Test start view
    date_range.expect_weekstart("1")  # Test week start (Monday)
    date_range.expect_language("en")  # Test language setting
    date_range.expect_separator(" → ")  # Test separator
    date_range.expect_width("100%")  # Test width
    date_range.expect_autoclose("true")  # Test autoclose

    # Test setting new values
    date_range.set(("2023-06-01", "2023-06-30"))
    date_range.expect_value(("2023-06-01", "2023-06-30"))

    # Test setting only start date
    date_range.set(("2023-07-01", None))
    date_range.expect_value(("2023-07-01", None))

    # Test setting only end date
    date_range.set((None, "2023-07-31"))
    date_range.expect_value((None, "2023-07-31"))

    # Test setting dates at the boundaries
    date_range.set(("2020-01-01", "2025-12-31"))  # Min and max dates
    date_range.expect_value(("2020-01-01", "2025-12-31"))
