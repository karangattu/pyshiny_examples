from shiny import reactive
from shiny.express import input, ui, render

# Synthetic data for text analysis
sample_texts = {
    "Review 1": "The product was amazing! I loved every single feature and would definitely recommend it to others.",
    "Review 2": "Disappointing experience. The quality was not what I expected for the price.",
    "Review 3": "Neutral review. Some good aspects, some bad aspects. Could use some improvements.",
}

ui.page_opts(title="Text Analysis Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_text_area(
            "user_text",
            "Enter your text:",
            placeholder="Type or paste your text here...",
            value="",
            height="200px",
        )

        ui.input_select(
            "sample_text", "Or choose a sample text:", list(sample_texts.keys())
        )

    with ui.card():
        ui.card_header("Text Analysis")

        @render.text
        def word_count():
            # Get text from either user input or sample text
            text = input.user_text() or sample_texts.get(input.sample_text(), "")

            # Basic text analysis
            words = text.split()
            return f"Word Count: {len(words)}"

        @render.text
        def char_count():
            # Get text from either user input or sample text
            text = input.user_text() or sample_texts.get(input.sample_text(), "")

            # Character count (excluding whitespace)
            chars = len(text.replace(" ", ""))
            return f"Character Count (excluding spaces): {chars}"

        @render.text
        def sentiment():
            # Get text from either user input or sample text
            text = input.user_text() or sample_texts.get(input.sample_text(), "")

            # Simple sentiment analysis based on keywords
            positive_words = ["amazing", "loved", "great", "wonderful", "excellent"]
            negative_words = ["disappointing", "bad", "poor", "terrible", "worst"]

            text_lower = text.lower()

            positive_count = sum(1 for word in positive_words if word in text_lower)
            negative_count = sum(1 for word in negative_words if word in text_lower)

            if positive_count > negative_count:
                return "Sentiment: Positive 😄"
            elif negative_count > positive_count:
                return "Sentiment: Negative 😞"
            else:
                return "Sentiment: Neutral 😐"

    @reactive.effect
    def _():
        # When a sample text is selected, populate the text area
        if input.sample_text():
            ui.update_text_area(
                "user_text", value=sample_texts.get(input.sample_text(), "")
            )
