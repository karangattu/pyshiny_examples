from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_slider_update_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test target slider initial state
    target_slider = controller.InputSlider(page, "target_slider")
    target_slider.expect_label("Target Slider")
    target_slider.expect_value("50")
    target_slider.expect_min("0")
    target_slider.expect_max("100")
    target_slider.expect_step("1")

    # Test control panel inputs initial states
    new_label = controller.InputText(page, "new_label")
    new_label.expect_label("New Label")
    new_label.expect_value("Updated Label")

    new_value = controller.InputNumeric(page, "new_value")
    new_value.expect_label("New Value")
    new_value.expect_value("50")

    new_min = controller.InputNumeric(page, "new_min")
    new_min.expect_label("New Min")
    new_min.expect_value("0")

    new_max = controller.InputNumeric(page, "new_max")
    new_max.expect_label("New Max")
    new_max.expect_value("100")

    new_step = controller.InputNumeric(page, "new_step")
    new_step.expect_label("New Step")
    new_step.expect_value("1")

    use_dates = controller.InputCheckbox(page, "use_dates")
    use_dates.expect_label("Use Dates Instead")
    use_dates.expect_checked(False)

    time_format = controller.InputText(page, "time_format")
    time_format.expect_label("Time Format (for dates)")
    time_format.expect_value("%Y-%m-%d")

    timezone = controller.InputText(page, "timezone")
    timezone.expect_label("Timezone (for dates)")
    timezone.expect_value("+0000")

    update_btn = controller.InputActionButton(page, "update")
    update_btn.expect_label("Update Slider")

    # Test numeric slider update
    new_label.set("New Slider Label")
    new_value.set("75")
    new_min.set("25")
    new_max.set("150")
    new_step.set("5")
    update_btn.click()

    # Verify slider updates
    target_slider.expect_label("New Slider Label")
    target_slider.expect_value("75")
    target_slider.expect_min("25")
    target_slider.expect_max("150")
    target_slider.expect_step("5")

    # Test date slider update
    use_dates.set(True)
    new_label.set("Date Slider")
    new_value.set("10")  # 10 days from now
    new_min.set("0")  # today
    new_max.set("30")  # 30 days from now
    new_step.set("1")
    time_format.set("%Y-%m-%d")
    timezone.set("+0000")
    update_btn.click()

    # Verify slider updates for date mode
    target_slider.expect_label("Date Slider")
    target_slider.expect_time_format("%Y-%m-%d")
    target_slider.expect_timezone("+0000")
