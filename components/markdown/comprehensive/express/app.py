from shiny import reactive
from shiny.express import input, ui, render
import random
import datetime

# Synthetic data generation
def generate_markdown_examples():
    return {
        "basic_text": "# Welcome to Markdown Showcase\n\nThis is a simple markdown text.",
        "formatted_text": "**Bold Text**\n\n*Italic Text*\n\n~~Strikethrough~~",
        "list_text": "## Lists\n\n### Unordered List\n- Item 1\n- Item 2\n- Item 3\n\n### Ordered List\n1. First item\n2. Second item\n3. Third item",
        "code_text": "## Code Blocks\n\n