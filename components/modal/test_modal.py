from playwright.sync_api import Page, expect
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_modal_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test small modal button
    small_modal_btn = controller.InputActionButton(page, "show_small")
    small_modal_btn.expect_label("Show Small Modal")

    # Test medium modal button
    medium_modal_btn = controller.InputActionButton(page, "show_medium")
    medium_modal_btn.expect_label("Show Medium Modal")

    # Test large modal button
    large_modal_btn = controller.InputActionButton(page, "show_large")
    large_modal_btn.expect_label("Show Large Modal")

    # Test extra large modal button
    xl_modal_btn = controller.InputActionButton(page, "show_xl")
    xl_modal_btn.expect_label("Show Extra Large Modal")

    # Test custom modal button
    custom_modal_btn = controller.InputActionButton(page, "show_custom")
    custom_modal_btn.expect_label("Show Custom Modal")

    # Test button clicks
    small_modal_btn.click()
    medium_modal_btn.click()
    large_modal_btn.click()
    xl_modal_btn.click()
    custom_modal_btn.click()
