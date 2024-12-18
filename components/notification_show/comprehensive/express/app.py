from shiny import reactive
from shiny.express import input, ui, render
import random
import pandas as pd
from datetime import datetime, timedelta


# Synthetic data generation
def generate_sample_data(num_rows=50):
    """Generate a sample DataFrame with random data."""
    return pd.DataFrame(
        {
            "id": range(1, num_rows + 1),
            "name": [f"Item {i}" for i in range(1, num_rows + 1)],
            "value": [random.uniform(10, 100) for _ in range(num_rows)],
            "category": random.choices(["A", "B", "C"], k=num_rows),
            "date": [
                datetime.now() - timedelta(days=random.randint(0, 30))
                for _ in range(num_rows)
            ],
        }
    )


# Create sample dataset
df = generate_sample_data()

# Page setup
ui.page_opts(title="Notification Showcase", fillable=True)

# Sidebar with input controls
with ui.sidebar():
    ui.input_select(
        "notification_type",
        "Notification Type",
        ["default", "message", "warning", "error"],
    )

    ui.input_slider(
        "duration", "Notification Duration (seconds)", min=1, max=10, value=5
    )

    ui.input_checkbox("close_button", "Show Close Button", value=True)

    ui.input_text(
        "notification_id",
        "Notification ID (optional)",
        placeholder="Leave blank for random ID",
    )

    ui.input_checkbox("with_action", "Include Action", value=False)

# Main content area
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Notification Demonstration")

        ui.input_action_button("show_notification", "Show Notification")

        @render.text
        def notification_details():
            return f"""
            Type: {input.notification_type()}
            Duration: {input.duration()} seconds
            Close Button: {input.close_button()}
            Custom ID: {input.notification_id() or 'Auto-generated'}
            Action: {input.with_action()}
            """


# Notification logic
@reactive.effect
@reactive.event(input.show_notification)
def _():
    # Prepare notification parameters
    notification_params = {
        "ui": f"Notification for {random.choice(df['category'])} category",
        "duration": input.duration(),
        "type": input.notification_type(),
        "close_button": input.close_button(),
    }

    # Optional ID
    if input.notification_id():
        notification_params["id"] = input.notification_id()

    # Optional action
    if input.with_action():
        notification_params["action"] = ui.a(
            "View Details", href="#", onclick="alert('Action triggered!')"
        )

    # Show notification
    ui.notification_show(**notification_params)
