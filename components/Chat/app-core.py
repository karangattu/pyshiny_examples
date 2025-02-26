from shiny import App, reactive, ui

# Define the UI
app_ui = ui.page_fillable(
    ui.panel_title("Chat Component Demo"),
    # Add markdown instructions
    ui.markdown(
        """
        ## Chat Component Demo
        This is a demonstration of the Shiny Chat component. Try these interactions:
        * Say "hello" 
        * Ask for "help"
        * Say "bye"
        * Type any other message
        """
    ),
    # Add chat UI
    ui.chat_ui("demo_chat"),
    fillable_mobile=True,
)


# Define the server
def server(input, output, session):
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
            response = (
                "I'm here to demonstrate the Chat component. Try different messages!"
            )
        elif "bye" in user_msg.lower():
            response = "Goodbye! Thanks for chatting with me."
        else:
            response = f"I received your message: {user_msg}"

        # Send response back to chat
        await chat.append_message({"role": "assistant", "content": response})


# Create and return the app
app = App(app_ui, server)
