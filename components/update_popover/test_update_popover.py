from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_popover_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Initialize controllers
    popover = controller.Popover(page, "demo_popover")
    main_btn = controller.InputActionButton(page, "main_btn")
    update_content_btn = controller.InputActionButton(page, "update_content")
    update_title_btn = controller.InputActionButton(page, "update_title")
    show_popover_btn = controller.InputActionButton(page, "show_popover")
    hide_popover_btn = controller.InputActionButton(page, "hide_popover")

    # Test initial button labels
    main_btn.expect_label("Click me (I have a popover)!")
    update_content_btn.expect_label("Update content")
    update_title_btn.expect_label("Update title & content")
    show_popover_btn.expect_label("Show popover")
    hide_popover_btn.expect_label("Hide popover")

    # Test initial popover content
    popover.expect_body("Initial popover content")

    # Test showing and hiding popover
    show_popover_btn.click()
    popover.expect_active(True)

    hide_popover_btn.click()
    popover.expect_active(False)

    # Test content update
    show_popover_btn.click()  # Show popover first
    update_content_btn.click()
    popover.expect_body("Content updated 1 times!")

    # Test title and content update
    update_title_btn.click()
    popover.expect_body("Content with title update #1")

    # Test main button click
    main_btn.click()
