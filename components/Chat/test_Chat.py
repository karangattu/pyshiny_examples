from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_chat_component(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Initialize chat controller
    chat = controller.Chat(page, "demo_chat")

    # Test initial state - check the welcome message
    chat.expect_latest_message(
        "🤖 Welcome! I'm a demo chat assistant. Try saying 'hello', 'help', or 'bye'."
    )

    # Test hello interaction
    chat.set_user_input("hello")
    chat.send_user_input()
    chat.expect_latest_message("🤖 Hello! How can I help you today?")

    # Test help interaction
    chat.set_user_input("help")
    chat.send_user_input()
    chat.expect_latest_message(
        "🤖 I'm here to demonstrate the Chat component. Try different messages!"
    )

    # Test bye interaction
    chat.set_user_input("bye")
    chat.send_user_input()
    chat.expect_latest_message("🤖 Goodbye! Thanks for chatting with me.")

    # Test generic message
    chat.set_user_input("test message")
    chat.send_user_input()
    chat.expect_latest_message("🤖 I received your message: TEST MESSAGE")
