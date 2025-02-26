from shiny import reactive
from shiny.express import input, ui, render

# Set page options for a clean layout
ui.page_opts(title="Chat Component Demo", fillable=True)

# Add some styling and instructions
ui.markdown(
    """
## Chat Component Demo
This is a demonstration of the Shiny Chat component. Try these interactions:
* Say "hello" 
* Ask for "help"
* Say "bye"
* Type any other message
"""
)

# Create a chat instance
chat = ui.Chat(
    id="demo_chat",
    messages=[
        {
            "role": "assistant",
            "content": "Welcome! I'm a demo chat assistant. Try saying 'hello', 'help', or 'bye'.",
        }
    ],
)

# Display the chat UI with specific styling
chat.ui(
    placeholder="Type your message here...",
    width="100%",
    height="200px",
)


# Transform user input to uppercase
@chat.transform_user_input
def transform_user(text: str) -> str:
    return text.upper()


# Add emoji prefix to assistant responses
@chat.transform_assistant_response
def transform_assistant(text: str) -> str:
    return f"🤖 {text}"


# Handle chat interactions
@chat.on_user_submit
async def handle_chat():
    user_msg = chat.user_input()

    # Generate response based on user input
    if "hello" in user_msg.lower():
        response = "Hello! How can I help you today?"
    elif "help" in user_msg.lower():
        response = "I'm here to demonstrate the Chat component. Try different messages!"
    elif "bye" in user_msg.lower():
        response = "Goodbye! Thanks for chatting with me."
    else:
        response = f"I received your message: {user_msg}"

    # Send response back to chat
    await chat.append_message({"role": "assistant", "content": response})
