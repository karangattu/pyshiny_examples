from chatlas import ChatBedrockAnthropic
from datetime import datetime

def get_current_date() -> str:
    """Returns the current date as a formatted string."""
    now = datetime.now()
    return now.strftime("%Y-%m-%d")

chat = ChatBedrockAnthropic(
    model="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
    system_prompt="answer in 10 words or less"
)

chat.register_tool(get_current_date)

chat.chat("What is the date today?")
