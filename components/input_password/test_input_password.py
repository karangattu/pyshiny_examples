from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_password_input(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test password input
    pwd = controller.InputPassword(page, "pwd")
    pwd.expect_label("Enter Password")
    pwd.expect_value("default123")
    pwd.expect_width("300px")
    pwd.expect_placeholder("Type your password here")

    # Test password length output
    pwd_length = controller.OutputText(page, "password_length")
    pwd_length.expect_value("Password length: 9 characters")

    # Test masked password output
    pwd_masked = controller.OutputText(page, "password_masked")
    pwd_masked.expect_value("Masked password: *********")

    # Test clear password button
    clear_btn = controller.InputActionButton(page, "clear_pwd")
    clear_btn.expect_label("Clear Password")
    clear_btn.click()

    # Verify password is cleared
    pwd.expect_value("")
    pwd_length.expect_value("No password entered")
    pwd_masked.expect_value("")

    # Test show length button
    show_length_btn = controller.InputActionButton(page, "show_length")
    show_length_btn.expect_label("Show Length")

    # Test setting new password
    pwd.set("newpass123")
    pwd.expect_value("newpass123")
    pwd_length.expect_value("Password length: 9 characters")
    pwd_masked.expect_value("Masked password: *********")
