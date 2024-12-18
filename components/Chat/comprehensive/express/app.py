from datetime import datetime
import pandas as pd
from shiny import reactive
from shiny.express import input, ui, render

# Sample data for chat messages
initial_messages = [
    ui.markdown(
        """
        # Welcome to Chat Demo App!
        This demo shows various features of the Shiny Chat component.
        - Auto-resize
        - Token limits
        - Message transformation
        - Different response formats
        """
    )
]

# Create a chat instance with all available parameters
chat = ui.Chat(
    id="demo_chat",
    messages=initial_messages,
    on_error="auto",  # Can be 'auto', 'actual', 'sanitize', or 'unhandled'
)

ui.page_opts(title="Shiny Chat Demo", fillable=True, fillable_mobile=True)

with ui.sidebar():
    ui.input_switch("auto_resize", "Enable Auto-resize", True)
    ui.input_switch("transform_messages", "Transform Messages", True)
    ui.input_select(
        "error_handling",
        "Error Handling",
        {
            "auto": "Auto",
            "actual": "Actual",
            "sanitize": "Sanitize",
            "unhandled": "Unhandled",
        },
        selected="auto",
    )

# Display the chat UI
chat.ui(placeholder="Type your message here...", width="100%", height="auto", fill=True)


# Transform user input if enabled
@chat.transform_user_input
def transform_input(text):
    if not input.transform_messages():
        return text

    # Add timestamp to user messages
    return f"[{datetime.now().strftime('%H:%M:%S')}] {text}"


# Transform assistant responses if enabled
@chat.transform_assistant_response
def transform_response(text):
    if not input.transform_messages():
        return text

    # Add formatting to assistant responses
    return f"🤖 *Assistant*: {text}"


# Handle user submissions
@chat.on_user_submit
async def handle_submit():
    user_msg = chat.user_input()

    # Simulate different response types based on user input
    if "error" in user_msg.lower():
        # Demonstrate error handling
        raise Exception("This is a test error message")

    if "data" in user_msg.lower():
        # Return tabular data
        df = pd.DataFrame({"A": range(1, 4), "B": ["x", "y", "z"]})
        await chat.append_message(f"Here's your data:\n{df.to_string()}")
    else:
        # Echo the message back with some additional context
        response = f"You said: {user_msg}\nThis is a simple echo response."
        await chat.append_message(response)


# Update error handling mode when changed
@reactive.effect
def update_error_handling():
    chat.on_error = input.error_handling()
