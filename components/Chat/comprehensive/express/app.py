from datetime import datetime
import random
import asyncio

from shiny import reactive
from shiny.express import input, ui
from shiny.express.ui import HTML


# Simulated AI model for chat responses
class SimpleAIModel:
    async def generate_response(self, messages, stream=False):
        await asyncio.sleep(0.5)  # Simulate processing time

        # Simple response generation based on last user message
        last_message = messages[-1]["content"] if messages else "No message"

        if stream:
            # Simulate streaming response
            words = f"I received: {last_message}. Let me elaborate...".split()
            for word in words:
                await asyncio.sleep(0.1)
                yield word + " "
        else:
            # Non-streaming response
            return f"I received: {last_message}. Here's a detailed response."


# Initialize the AI model
ai_model = SimpleAIModel()

# Set page options
ui.page_opts(title="Comprehensive Chat Component Demo", fillable=True)

# Add Font Awesome for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.0/css/all.min.css">'
    )
)

# Create a welcome message
welcome_message = ui.markdown(
    """
    # Welcome to the Chat Component Demo! 
    
    This app demonstrates various features of the Shiny Chat component:
    - Different message transformations
    - Streaming and non-streaming responses
    - Error handling
    - Token limits
    """
)

# Create chat with comprehensive configuration
chat = ui.Chat(
    id="demo_chat",
    messages=[welcome_message],  # Initial messages
    on_error="sanitize",  # Error handling strategy
)

# Display the chat UI
chat.ui(
    placeholder="Type your message here...", width="min(680px, 100%)", height="500px"
)

# Add some UI controls to demonstrate chat features
with ui.layout_columns():
    ui.input_select("response_type", "Response Type", choices=["Stream", "Non-Stream"])
    ui.input_numeric("token_limit", "Token Limit", value=100, min=10, max=500)


# Transform user input to add context
@chat.transform_user_input
def process_user_input(user_input):
    # Optional: Add some preprocessing to user input
    if not user_input:
        return None

    # Optionally modify or validate input
    processed_input = f"User says at {datetime.now()}: {user_input}"
    return processed_input


# Transform assistant response for display
@chat.transform_assistant_response
def format_assistant_response(response):
    # Optional: Add markdown formatting or HTML
    if not response:
        return None

    # Add some styling to responses
    return HTML(f"<div style='color: blue;'>{response}</div>")


# Handle user message submission
@chat.on_user_submit
async def handle_chat_submission():
    # Get current chat messages
    messages = chat.messages(
        token_limits=(100, 50),  # Limit tokens for request and response
        transform_user="last",  # Only transform the last user message
    )

    try:
        # Determine streaming based on UI selection
        stream = input.response_type() == "Stream"

        if stream:
            # Stream the response
            await chat.append_message_stream(
                ai_model.generate_response(messages, stream=True)
            )
        else:
            # Non-streaming response
            response = await ai_model.generate_response(messages)
            await chat.append_message(response)

    except Exception as e:
        # Handle any errors during response generation
        await chat.append_message(f"Error occurred: {str(e)}")


# Optional: Add a button to clear chat messages
ui.input_action_button("clear_chat", "Clear Chat")


@reactive.effect
@reactive.event(input.clear_chat)
def clear_chat():
    chat.clear_messages()
    # Re-add welcome message
    chat.append_message(welcome_message)
