from shiny import reactive
from shiny.express import input, ui, render

# Set page title
ui.page_opts(full_width=True)

with ui.card():
    ui.card_header("Password Input Example")

    # Create password input
    ui.input_password(
        id="pwd",
        label="Enter Password",
        value="default123",
        width="300px",
        placeholder="Type your password here",
    )

    # Show current input length
    @render.text
    def password_length():
        pwd = input.pwd()
        if not pwd:
            return "No password entered"
        return f"Password length: {len(pwd)} characters"

    # Show masked password
    @render.text
    def password_masked():
        pwd = input.pwd()
        if not pwd:
            return ""
        return f"Masked password: {'*' * len(pwd)}"

    # Add some action buttons
    ui.input_action_button(id="clear_pwd", label="Clear Password", class_="btn-danger")

    ui.input_action_button(id="show_length", label="Show Length", class_="btn-primary")


# Add effect to clear password
@reactive.effect
@reactive.event(input.clear_pwd)
def _():
    ui.update_password("pwd", value="")
