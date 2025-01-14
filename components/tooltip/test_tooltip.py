from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_tooltips(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test tooltip1 (default placement)
    tooltip1 = controller.Tooltip(page, "tooltip1")
    tooltip1.expect_body("This is a basic tooltip")
    tooltip1.expect_placement("top")  # Default placement is top

    # Test tooltip2 (right placement)
    tooltip2 = controller.Tooltip(page, "tooltip2")
    tooltip2.expect_body("This tooltip appears on the right")
    tooltip2.expect_placement("right")

    # Test tooltip3 (bottom placement)
    tooltip3 = controller.Tooltip(page, "tooltip3")
    tooltip3.expect_body("This tooltip appears at the bottom")
    tooltip3.expect_placement("bottom")

    # Test tooltip4 (left placement)
    tooltip4 = controller.Tooltip(page, "tooltip4")
    tooltip4.expect_body("This tooltip appears on the left")
    tooltip4.expect_placement("left")

    # Test tooltip5 (auto placement)
    tooltip5 = controller.Tooltip(page, "tooltip5")
    tooltip5.expect_body("This tooltip has custom animation and delay")
    tooltip5.expect_placement("auto")

    # Test showing/hiding tooltips
    # Initially all tooltips should be inactive
    for tooltip in [tooltip1, tooltip2, tooltip3, tooltip4, tooltip5]:
        tooltip.expect_active(False)

    # Click toggle button and verify tooltips become active
    toggle_btn = controller.InputActionButton(page, "toggle_tooltips")
    toggle_btn.expect_label("Toggle All Tooltips")
    toggle_btn.click()

    # After clicking toggle button, tooltips should be active
    for tooltip in [tooltip1, tooltip2, tooltip3, tooltip4, tooltip5]:
        tooltip.expect_active(True)

    # Test updating tooltip content
    update_btn = controller.InputActionButton(page, "update_content")
    update_btn.expect_label("Update Tooltip Content")
    update_btn.click()

    # Verify updated content
    expected_updated_content = (
        "Updated content 1 times! <i class='fa-solid fa-sync'></i>"
    )
    for tooltip in [tooltip1, tooltip2, tooltip3, tooltip4, tooltip5]:
        tooltip.expect_body(expected_updated_content)
