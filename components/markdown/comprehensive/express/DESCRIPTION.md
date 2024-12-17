python\ndef hello_world():\n    print('Hello, Markdown!')\n```\n\nInline `code` example",
        "link_text": "## Links and References\n\n[Shiny for Python](https://shiny.posit.co/py/)\n\n[Local Reference](#lists)",
        "table_text": "## Tables\n\n| Column 1 | Column 2 | Column 3 |\n|----------|----------|----------|\n| Row 1, Col 1 | Row 1, Col 2 | Row 1, Col 3 |\n| Row 2, Col 1 | Row 2, Col 2 | Row 2, Col 3 |",
        "complex_text": "# Complex Markdown\n\n## Mixed Formatting\n\n**Bold and *italic* text**\n\n> Blockquote example\n\n- List with **bold** and *italic* items\n- Another list item",
        "emoji_text": "## Emojis and Special Characters\n\n:smile: :rocket: :coffee:\n\nSpecial characters like &copy; and &trade;",
    }

# Page setup with full width and title
ui.page_opts(title="Markdown Showcase", full_width=True)

# Add Font Awesome CSS
ui.head_content(
    ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">')
)

# Sidebar for markdown selection and rendering options
with ui.sidebar():
    ui.input_select(
        "markdown_type", 
        "Select Markdown Type", 
        list(generate_markdown_examples().keys())
    )
    
    ui.input_checkbox_group(
        "render_options", 
        "Rendering Options", 
        {
            "escape": "Escape HTML",
            "inline": "Inline Rendering"
        }
    )

# Main content area with markdown rendering
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Markdown Rendering")
        
        @render.ui
        def dynamic_markdown():
            markdown_text = generate_markdown_examples()[input.markdown_type()]
            
            # Determine rendering options
            render_inline = "inline" in input.render_options()
            escape_html = "escape" in input.render_options()
            
            # Render markdown with selected options
            return ui.markdown(
                markdown_text, 
                inline=render_inline, 
                escape=escape_html
            )

    with ui.card():
        ui.card_header("Markdown Source")
        
        @render.code
        def markdown_source():
            return generate_markdown_examples()[input.markdown_type()]

# Optional: Add a footer with current timestamp
ui.markdown(f"*Last Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
```

This Shiny for Python app demonstrates the following aspects of `ui.markdown()`:

1. **Basic Markdown Rendering**: Shows various markdown types like headers, lists, code blocks, etc.
2. **Rendering Options**:
   - `inline`: Renders markdown inline or as a block
   - `escape`: Controls HTML escaping

3. **Dynamic Content**: 
   - Synthetic data generation
   - Dynamic markdown type selection
   - Real-time rendering options

4. **UI Components**:
   - Sidebar for input selection
   - Cards for displaying markdown and source code
   - Responsive layout
   - Full-screen option
   - Footer with timestamp

5. **Additional Features**:
   - Font Awesome CSS inclusion
   - Code source display
   - Emoji and special character support

Key Shiny for Python features demonstrated:
- Express mode syntax
- `@render.ui` for dynamic UI generation
- `@render.code` for source code display
- Reactive inputs and rendering
- Synthetic data generation
- Flexible layout with `ui.layout_columns()`

The app provides an interactive showcase of markdown rendering capabilities in Shiny for Python.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBf0HDRUO8ycHXtqFSnwCgoAxMgAyriU7HBSxMi+FFDIAObUDn6c5Ar2dClpDH5wAPowUAwA1rakAO4QRZqw6AA2cKwAFACUiArIvaIxJgwQyCA9feNyYABGUKycxEVUGhSTKJOhAOpwTWTwyBSkyACyZZU1w2HsNcSz8kEKACpcepx6SXMCLcilFVW1+5oKFhJgQxuNepM6EJShQqLZFoDVshJgAqFEAIVITVsyAegLRcnuEBRAElEk15rj8YSIDSAH50sIUBiccoxdhMEzJdgMkFg8GTCmsCgI5ZI9ahAAyrworBpNOCiuQAFUIEJ7GIcdLhTSALTIMlwFgARj1BqoLAATGbDSwAMzykJKgDyDA1cC1MppxqwyAAYpwGMK+BaaZbfWE4GQ7CGjTS7b6noGcZxQ4R+RMwGR7KKVrQJcgAMKkezIdFNUjEcpyolgAC+RHA0HgtDAYgAjpYxPBKKwsBRloQSOQqDQUGAFDDmqQKBSpgoICYBLgFOh3L45bThuCd-WALpAA)
