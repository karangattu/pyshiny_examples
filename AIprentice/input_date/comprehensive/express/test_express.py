from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_date_inputs(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test basic date input
    date1 = controller.InputDate(page, "date1")
    date1.expect_label("Basic date input with default value:")
    date1.expect_value("2024-02-29")

    # Test date input with min/max range
    date2 = controller.InputDate(page, "date2")
    date2.expect_label("Date with min/max range:")
    date2.expect_value("2024-02-01")
    date2.expect_min_date("2024-01-01")
    date2.expect_max_date("2024-12-31")

    # Test date input with custom format
    date3 = controller.InputDate(page, "date3")
    date3.expect_label("Custom format (mm/dd/yy):")
    date3.expect_value("02/29/24")
    date3.expect_format("mm/dd/yy")

    # Test date input with decade view
    date4 = controller.InputDate(page, "date4")
    date4.expect_label("Start in decade view:")
    date4.expect_value("2024-02-29")
    date4.expect_startview("decade")

    # Test date input with Monday start
    date5 = controller.InputDate(page, "date5")
    date5.expect_label("Week starts on Monday:")
    date5.expect_value("2024-02-29")
    date5.expect_weekstart("1")

    # Test date input with German language
    date6 = controller.InputDate(page, "date6")
    date6.expect_label("German language:")
    date6.expect_value("2024-02-29")
    date6.expect_language("de")

    # Test date input with custom width
    date7 = controller.InputDate(page, "date7")
    date7.expect_label("Custom width:")
    date7.expect_value("2024-02-29")
    date7.expect_width("400px")

    # Test date input with autoclose disabled
    date8 = controller.InputDate(page, "date8")
    date8.expect_label("Autoclose disabled:")
    date8.expect_value("2024-02-29")
    date8.expect_autoclose("false")

    # Test date input with disabled dates
    date9 = controller.InputDate(page, "date9")
    date9.expect_label("Some dates disabled:")
    date9.expect_value("2024-02-29")
    date9.expect_datesdisabled(["2024-03-01", "2024-03-02", "2024-03-03"])

    # Test date input with disabled weekends
    date10 = controller.InputDate(page, "date10")
    date10.expect_label("Weekends disabled:")
    date10.expect_value("2024-02-29")
    date10.expect_daysofweekdisabled([0, 6])

    # Test setting new values
    date1.set("2024-03-15")
    date1.expect_value("2024-03-15")

    date2.set("2024-06-15")
    date2.expect_value("2024-06-15")
