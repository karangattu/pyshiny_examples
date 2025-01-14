from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_popovers(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test basic popover
    basic_popover = controller.Popover(page, "basic_popover")
    basic_popover.expect_active(False)
    basic_popover.expect_body("This is a basic popover with default parameters")
    basic_popover.set(True)
    basic_popover.expect_active(True)
    basic_popover.set(False)
    basic_popover.expect_active(False)

    # Test right popover
    right_popover = controller.Popover(page, "right_popover")
    right_popover.expect_active(False)
    right_popover.expect_body("This popover appears on the right")
    right_popover.expect_placement("right")
    right_popover.set(True)
    right_popover.expect_active(True)
    right_popover.set(False)
    right_popover.expect_active(False)

    # Test top popover
    top_popover = controller.Popover(page, "top_popover")
    top_popover.expect_active(False)
    top_popover.expect_body("This popover appears on top")
    top_popover.expect_placement("top")
    top_popover.set(True)
    top_popover.expect_active(True)
    top_popover.set(False)
    top_popover.expect_active(False)

    # Test bottom popover
    bottom_popover = controller.Popover(page, "bottom_popover")
    bottom_popover.expect_active(False)
    bottom_popover.expect_body("This popover appears at the bottom")
    bottom_popover.expect_placement("bottom")
    bottom_popover.set(True)
    bottom_popover.expect_active(True)
    bottom_popover.set(False)
    bottom_popover.expect_active(False)

    # Test custom popover
    custom_popover = controller.Popover(page, "custom_popover")
    custom_popover.expect_active(False)
    custom_popover.expect_body(
        "This popover has custom animation, delay, and trigger options"
    )
    custom_popover.expect_placement("auto")
    custom_popover.set(True)
    custom_popover.expect_active(True)
    custom_popover.set(False)
    custom_popover.expect_active(False)
