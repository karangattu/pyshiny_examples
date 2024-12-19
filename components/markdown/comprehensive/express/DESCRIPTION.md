python
        def hello():
            print("Hello World!")
        ```
        """)

    # Dynamic markdown with user input
    with ui.card():
        ui.card_header("Dynamic Markdown")
        
        @render.markdown
        def dynamic_markdown():
            return input.text()

# Custom render function example
with ui.card():
    ui.card_header("Custom Render Function")
    
    @render.markdown
    def custom_markdown():
        try:
            # Create a custom render function from user input
            custom_func = eval(input.custom_func())
            return custom_func("""
            # Custom Rendered Markdown
            
            This text will be processed by the custom function.
            
            * The function is: `{}`
            * Current time: {}
            """.format(input.custom_func(), reactive.invalidate_later(1)))
        except Exception as e:
            return f"Error in custom function: {str(e)}"

# Code block example
with ui.card():
    ui.card_header("Code Blocks")
    ui.markdown("""
    
    
    ```r
    # This is R code
    print("Hello from R!")
    ```
    
    ```sql
    -- This is SQL
    SELECT * FROM table WHERE condition = TRUE;
    ```
    """)

# Table example
with ui.card():
    ui.card_header("Tables in Markdown")
    ui.markdown("""
    | Header 1 | Header 2 | Header 3 |
    |----------|----------|----------|
    | Row 1    | Data     | More     |
    | Row 2    | Info     | Details  |
    | Row 3    | Values   | Content  |
    """)

# Extended markdown features
with ui.card():
    ui.card_header("Extended Features")
    ui.markdown("""
    ## Task Lists
    
    - [x] Completed task
    - [ ] Incomplete task
    - [x] Another done task
    
    ## Definition Lists
    
    Term 1
    : Definition 1
    
    Term 2
    : Definition 2
    
    ## Footnotes
    
    Here's a sentence with a footnote[^1].
    
    [^1]: This is the footnote content.
    
    ## Blockquotes
    
    > This is a blockquote
    > It can span multiple lines
    >> And can be nested
    
    ## Horizontal Rule
    
    ---
    
    ## Subscript and Superscript
    
    H~2~O is water
    
    2^10^ is 1024
    """)

# LaTeX-style math
with ui.card():
    ui.card_header("Math Expressions")
    ui.markdown(r"""
    Inline math: $E = mc^2$
    
    Display math:
    
    $$
    \frac{d}{dx}\left( \int_{0}^{x} f(u)\,du\right)=f(x)
    $$
    
    $$
    \sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}
    $$
    """)

```

This app demonstrates:

1. Basic markdown syntax
2. Dynamic markdown with user input
3. Custom render functions
4. Code blocks with syntax highlighting
5. Tables
6. Extended markdown features like task lists and footnotes
7. LaTeX-style math expressions
8. Reactive updates
9. Layout organization with cards and columns

Key features shown:

- All markdown parameters are utilized
- Express mode syntax
- Reactive rendering
- User input integration
- Error handling for custom functions
- Various markdown formatting options
- Responsive layout with cards and columns

To run this app:

1. Save it as `app.py`
2. Install required packages:
```bash
pip install shiny
```
3. Run with:
```bash
shiny run app.py
```

The app provides an interactive demonstration of Shiny for Python's markdown capabilities, allowing users to:

- Enter custom markdown text
- Define custom render functions
- See various markdown formatting options
- Interact with reactive content
- View mathematical expressions
- Explore code highlighting

All data is generated within the app, and no external files are required.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMpwR6KAHM4yUnQpclYFSxxfOAB9QIpWAAopCgAbOABeOTAAWSgGAGtbUgB3CGQAUQ1YdFTQwmQ6TmTkqAAjVLSAFQYTOABKJwhXAGExKCpkKDZOexbc5CLOCnZkGFyC4tLiE1YKZk4ALzHOcgCg44hQiAWl5HDWabhZhnjexAVkD9vOLGMzKKoNBR4pkARRMkRMmVKA5kFsdspVvlCiVkKDwchMgAqTEACTgTVI2OQUSKQmStiiAEJMv1Sp9wr8KP9NED3p92Zk4bsYFE6CYIMR0Wz2R9MkNttzRNR7Ax6vzJOdkPEAAq4JYnMj2fp1YUizLNGAtWyTDQoDRYEyYBwvTK62kuZA5biw8hUSgTUYKa7LcLNXCkP5kZImGAXeILWxLNIARgA9AAmV661wAISg92IKzWyNKmiqqV13q+WGIuVsLzedJFxdLDAp7HEMuBYDTGcd2Y2NN17PCiPWJWbtrA3c+qfTnEzOSRG3KlQEBaresX7I6XD0nD02JapHJRNBEzsxMWUGSE6iqJZWBHouXn0xyAAMhujFQWNHr8h70+dnxX8h4x+H7RlgyAAHIhi0DhwLYv5wG+H7xiB4GGlBMGLHB-6AbeHzAE+EB5KipDuKouAALrxOwFAUOgrCILGsYcNwuA4KQ9wUCWpCxngsa0tWorDgJ9qLq4AAiuDQDAE5ZtOKJ5vO8iLkW4S1uWSbYTWZZRA2UBNpkYkSVJU79hAXbqR+AACNgyhanAfvYdDILY4mwGefY5hWH7smIFAmAwpS9h2A6MlgoIvEJ7LDBKyhWah0nGYWiw+t8KkeepymadpulgOK8IsAAStKsVGTmpl8Ri6mWYVDA2XZcAOVyzBRG5GypWV7IUAwuCVm1fGuG4UB0PivBwNIJ4mGM-hLP4DUsHyArBCZ6llTNvLysgaTICNJ7xMFK1zcQYWeXx+4bXt8o7RApjsaFvS8T1Ireb5-nfM1A6gndPWaMQcBBLO31nCc6abd191eZ4T3Fq9EDxHQkIMEwDAoCAOzPH0AC+NJgGjRDgBJCAoGAYgAI6WGI8CUKwIWAnUYBkNCNAEwoqzUckpApJwLQKBAIZ4Ao3h2OmAyg1jpFAA)
