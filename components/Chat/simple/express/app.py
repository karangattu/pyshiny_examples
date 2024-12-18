from shiny import reactive
from shiny.express import ui

# Set up page options
ui.page_opts(title="Simple AI Chat Demo", fillable=True)

# Add custom CSS directly using ui.tags.style instead of ui.include_css
ui.tags.style(
    """
    .chat-container {
        max-width: 600px;
        margin: 0 auto;
    }
"""
)

# Create a chat instance with an initial welcome message
chat = ui.Chat(
    id="demo_chat",
    messages=[
        "Hello! I'm a simple AI assistant. Ask me about programming, weather, or just chat!"
    ],
)

# Display the chat UI
chat.ui()


# Define a simple response generation function
@chat.on_user_submit
async def _():
    # Get the user's most recent message
    user_message = chat.user_input().lower()

    # Simple predefined responses
    responses = {
        "python": "Python is an awesome programming language! It's known for its readability and versatility.",
        "weather": "The weather looks great today! Sunny with a chance of coding. 🌞💻",
        "hello": "Hi there! How can I help you today?",
        "help": "I can chat about programming, weather, or anything else. Just ask!",
    }

    # Match user message to predefined responses
    response = "I'm not sure how to respond to that. Try asking about Python, weather, or just say hello!"
    for key, value in responses.items():
        if key in user_message:
            response = value
            break

    # Append the response to the chat
    await chat.append_message(response)
