from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_value_boxes(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test value box 1 (Monthly Sales)
    box1 = controller.ValueBox(page, "box1")
    box1.expect_title("Monthly Sales")
    box1.expect_height("200px")
    box1.expect_value("$1,209.71")  # Based on the random seed
    box1.expect_body("↑ 15.7% vs Last Month")

    # Test value box 2 (Average Sales)
    box2 = controller.ValueBox(page, "box2")
    box2.expect_title("Average Sales")
    box2.expect_height("200px")
    box2.expect_value("$1,016.67")  # Based on the random seed
    box2.expect_body("Last 30 Days")

    # Test value box 3 (Sales Trend)
    box3 = controller.ValueBox(page, "box3")
    box3.expect_title("Sales Trend")
    box3.expect_height("300px")
    box3.expect_value("$30,500.00")  # Based on the random seed
    box3.expect_body("Total Sales")
    box3.expect_full_screen_available(True)

    # Test value box 4 (Revenue Growth)
    box4 = controller.ValueBox(page, "box4")
    box4.expect_title("Revenue Growth")
    box4.expect_height("200px")
    box4.expect_value("15.7%")
    box4.expect_body("Year over Year")

    # Test value box 5 (Active Users)
    box5 = controller.ValueBox(page, "box5")
    box5.expect_title("Active Users")
    box5.expect_height("200px")
    # Not testing the exact value since it's random
    box5.expect_body("Current Month")

    # Test value box 6 (Achievement Score)
    box6 = controller.ValueBox(page, "box6")
    box6.expect_title("Achievement Score")
    box6.expect_height("200px")
    # Not testing the exact value since it's random
    box6.expect_body("Performance Index")
