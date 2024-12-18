from shiny import reactive
from shiny.express import input, ui, render

# Synthetic user data for demonstration
users = {"admin": "SecurePass123!", "user1": "UserPass456@", "user2": "SafeWord789#"}

ui.page_opts(title="Password Input Showcase", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        # Demonstrating various parameters of input_password
        ui.input_password("basic_password", "Basic Password Input")

        ui.input_password(
            "custom_width_password", "Password with Custom Width", width="300px"
        )

        ui.input_password(
            "placeholder_password",
            "Password with Placeholder",
            placeholder="Enter your password",
        )

        ui.input_password(
            "preset_value_password",
            "Password with Preset Value",
            value="InitialPassword",
        )

        ui.input_action_button("validate", "Validate Credentials")

    with ui.card():
        ui.card_header("Password Validation Results")

        @render.text
        def validation_result():
            # Validate password
            if input.basic_password():
                if input.basic_password() in users.values():
                    return "✅ Password Matches a User Account"
                else:
                    return "❌ Invalid Password"
            return "Enter a password to validate"

        @render.text
        def password_details():
            details = [
                f"Basic Password: {input.basic_password()}",
                f"Custom Width Password: {input.custom_width_password()}",
                f"Placeholder Password: {input.placeholder_password()}",
                f"Preset Value Password: {input.preset_value_password()}",
            ]
            return "\n".join(details)


# Optional: Add Font Awesome for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)


# Reactive effect to demonstrate password validation
@reactive.effect
@reactive.event(input.validate)
def _():
    # You could add more complex validation logic here
    ui.notification_show("Credentials Checked!", duration=3, type="message")
