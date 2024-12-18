from shiny import reactive
from shiny.express import input, ui, render

# Define some sample data for the chat
SAMPLE_RESPONSES = {
    "greeting": "Hello! How can I assist you today?",
    "weather": "I'm not able to check real-time weather, but I can tell you it's always sunny in the digital world!",
    "help": "I can help you with basic questions. Try asking about weather or just say hello!",
    "default": "I'm not sure how to respond to that. Try asking something else!",
}

ui.page_opts(title="Simple Chat Demo", fillable=True)

# Create a welcome message
welcome = ui.markdown(
    """
    # Simple Chat Demo
    Welcome to this basic chat demo! Try these example interactions:
    * Say "hello" or "hi"
    * Ask about the weather
    * Ask for help
    """
)

# Create chat instance with welcome message
chat = ui.Chat(id="demo_chat", messages=[welcome])

# Display the chat UI
chat.ui()


@chat.on_user_submit
async def handle_chat():
    # Get user's message
    user_msg = chat.user_input().lower()

    # Determine response based on user input
    if any(word in user_msg for word in ["hello", "hi", "hey"]):
        response = SAMPLE_RESPONSES["greeting"]
    elif "weather" in user_msg:
        response = SAMPLE_RESPONSES["weather"]
    elif "help" in user_msg:
        response = SAMPLE_RESPONSES["help"]
    else:
        response = SAMPLE_RESPONSES["default"]

    # Add slight delay to simulate processing
    await chat.append_message(response)
