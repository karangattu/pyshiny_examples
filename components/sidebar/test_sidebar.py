from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_sidebar_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Initialize the sidebar controller
    sidebar = controller.Sidebar(page, "demo_sidebar")

    # Test initial state and properties
    sidebar.expect_position("left")
    sidebar.expect_open(True)  # Desktop default is "open"
    sidebar.expect_width("300px")
    sidebar.expect_title("Sidebar Demo")
    sidebar.expect_bg_color("#f8f9fa")
    sidebar.expect_gap("1rem")
    sidebar.expect_padding("1rem")
    sidebar.expect_mobile_max_height("300px")

    # Test sidebar content
    sidebar.expect_text("This sidebar demonstrates all possible parameters")

    # Test sidebar state changes
    sidebar.set(False)  # Close sidebar
    sidebar.expect_open(False)

    sidebar.set(True)  # Open sidebar
    sidebar.expect_open(True)

    # Test the output text that shows sidebar state
    output_text = controller.OutputText(page, "sidebar_state")
    output_text.expect_value("Sidebar state: True")  # When sidebar is open

    sidebar.set(False)
    output_text.expect_value("Sidebar state: False")  # When sidebar is closed
