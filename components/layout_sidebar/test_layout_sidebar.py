from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_layout_sidebar(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test sidebar component
    sidebar = controller.Sidebar(page, "demo_sidebar")
    sidebar.expect_title("Sidebar Title")
    sidebar.expect_position("left")
    sidebar.expect_width("300px")
    sidebar.expect_bg_color("#f8f9fa")
    sidebar.expect_padding("1rem")
    sidebar.expect_open(True)  # Since default is "desktop" which means open

    # Test slider input
    slider = controller.InputSlider(page, "n")
    slider.expect_label("Number of bins")
    slider.expect_min("1")
    slider.expect_max("50")
    slider.expect_value("30")  # Test initial value

    # Test checkbox group
    checkbox_group = controller.InputCheckboxGroup(page, "options")
    checkbox_group.expect_label("Choose options:")
    checkbox_group.expect_choices(["Option A", "Option B", "Option C"])
    checkbox_group.expect_selected(["Option A"])  # Test initial selection

    # Test interactions
    # Change slider value
    slider.set("25")
    slider.expect_value("25")

    # Change checkbox selections
    checkbox_group.set(["Option A", "Option B"])
    checkbox_group.expect_selected(["Option A", "Option B"])

    # Toggle sidebar
    sidebar.set(False)  # Close sidebar
    sidebar.expect_open(False)
    sidebar.set(True)  # Open sidebar
    sidebar.expect_open(True)
