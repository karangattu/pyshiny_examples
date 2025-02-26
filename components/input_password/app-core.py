from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fluid(
    # Card container
    ui.card(
        ui.card_header("Password Input Example"),
        # Create password input
        ui.input_password(
            id="pwd",
            label="Enter Password",
            value="default123",
            width="300px",
            placeholder="Type your password here",
        ),
        # Output for password length
        ui.output_text("password_length"),
        # Output for masked password
        ui.output_text("password_masked"),
        # Action buttons
        ui.input_action_button(
            id="clear_pwd", label="Clear Password", class_="btn-danger"
        ),
        ui.input_action_button(
            id="show_length", label="Show Length", class_="btn-primary"
        ),
    )
)


# Define the server
def server(input, output, session):
    # Show current input length
    @output
    @render.text
    def password_length():
        pwd = input.pwd()
        if not pwd:
            return "No password entered"
        return f"Password length: {len(pwd)} characters"

    # Show masked password
    @output
    @render.text
    def password_masked():
        pwd = input.pwd()
        if not pwd:
            return ""
        return f"Masked password: {'*' * len(pwd)}"

    # Add effect to clear password
    @reactive.effect
    @reactive.event(input.clear_pwd)
    def _():
        ui.update_password("pwd", value="")


# Create and return the app
app = App(app_ui, server)
