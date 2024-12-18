from shiny import reactive
from shiny.express import input, ui, render

# Define some mock user credentials
mock_users = {"admin": "admin123", "user1": "password123", "user2": "letmein"}

ui.page_opts(title="Password Demo", fillable=True)

with ui.card():
    ui.card_header("Login Form")

    ui.input_text("username", "Username", placeholder="Enter username")
    ui.input_password("password", "Password", placeholder="Enter password")
    ui.input_action_button("login", "Login", class_="btn-primary")


@render.ui
@reactive.event(input.login)
def result():
    if not input.username() or not input.password():
        return ui.p("Please enter both username and password", class_="text-warning")

    if (
        input.username() in mock_users
        and mock_users[input.username()] == input.password()
    ):
        return ui.p("Login successful!", class_="text-success")
    else:
        return ui.p("Invalid username or password", class_="text-danger")
