from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_action_buttons(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test basic button
    basic_btn = controller.InputActionButton(page, "basic_btn")
    basic_btn.expect_label("Basic Button")
    basic_btn.expect_width("200px")
    basic_txt = controller.OutputText(page, "basic_clicks")
    basic_txt.expect_value("Basic button clicks: 0")
    basic_btn.click()
    basic_txt.expect_value("Basic button clicks: 1")

    # Test icon button
    icon_btn = controller.InputActionButton(page, "icon_btn")
    icon_btn.expect_label("Button with Icon")
    icon_btn.expect_width("200px")
    icon_txt = controller.OutputText(page, "icon_clicks")
    icon_txt.expect_value("Icon button clicks: 0")
    icon_btn.click()
    icon_txt.expect_value("Icon button clicks: 1")

    # Test disabled button and toggle
    disabled_btn = controller.InputActionButton(page, "disabled_btn")
    disabled_btn.expect_label("Initially Disabled")
    disabled_btn.expect_width("200px")
    disabled_txt = controller.OutputText(page, "disabled_clicks")
    disabled_txt.expect_value("Disabled button clicks: 0")

    toggle_btn = controller.InputActionButton(page, "toggle_disabled")
    toggle_btn.expect_label("Toggle Disabled State")
    toggle_btn.click()  # Enable the disabled button
    disabled_btn.click()
    disabled_txt.expect_value("Disabled button clicks: 1")

    # Test styled button
    styled_btn = controller.InputActionButton(page, "styled_btn")
    styled_btn.expect_label("Custom Styled Button")
    styled_btn.expect_width("200px")
    styled_txt = controller.OutputText(page, "styled_clicks")
    styled_txt.expect_value("Styled button clicks: 0")
    styled_btn.click()
    styled_txt.expect_value("Styled button clicks: 1")

    # Test attribute button
    attr_btn = controller.InputActionButton(page, "attr_btn")
    attr_btn.expect_label("Button with Attributes")
    attr_btn.expect_width("200px")
    attr_txt = controller.OutputText(page, "attr_clicks")
    attr_txt.expect_value("Attribute button clicks: 0")
    attr_btn.click()
    attr_txt.expect_value("Attribute button clicks: 1")

    # Test progress button
    progress_btn = controller.InputActionButton(page, "progress_btn")
    progress_btn.expect_label("Start Progress")
    progress_btn.expect_width("200px")

    # Test click statistics table
    stats_table = controller.OutputDataFrame(page, "click_stats")
    stats_table.expect_column_labels(["Button", "Clicks"])
    stats_table.expect_nrow(6)  # Should have 6 rows for 6 buttons
    stats_table.expect_ncol(2)  # Should have 2 columns (Button and Clicks)
