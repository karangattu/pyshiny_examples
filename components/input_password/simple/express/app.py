from shiny import reactive
from shiny.express import input, ui, render

# Synthetic user database (in a real app, this would be more secure!)
USER_DB = {"alice": "password123", "bob": "securepass", "charlie": "qwerty"}

ui.page_opts(title="Password Input Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_text("username", "Username")
        ui.input_password("password", "Password")
        ui.input_action_button("login", "Login")

    @render.ui
    def login_result():
        # Validate login credentials
        if not input.username() or not input.password():
            return ui.p("Please enter both username and password")

        # Check credentials
        if (
            input.username() in USER_DB
            and input.password() == USER_DB[input.username()]
        ):
            return ui.div(
                ui.p(f"Welcome, {input.username()}!", class_="text-success"),
                ui.p("You have successfully logged in!"),
            )
        else:
            return ui.div(ui.p("Invalid username or password", class_="text-danger"))

    # Optional: Show current input values for demonstration
    @render.text
    def show_inputs():
        return (
            f"Current Username: {input.username()}\n"
            f"Password Entered: {'*' * len(input.password()) if input.password() else 'None'}"
        )
