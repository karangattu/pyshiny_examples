This app demonstrates:

1. Basic usage of `panel_title` with both parameters:
   - `title`: The visible title in the UI
   - `window_title`: The browser tab title

2. Different ways to use the title parameter:
   - Plain text
   - HTML tags using `ui.h2()`, `ui.h3()`
   - Markdown using `ui.markdown()`
   - Dynamic titles using reactive rendering
   - Complex HTML structures with nested elements and classes

3. Various styling and layout features:
   - Bootstrap classes for styling
   - Cards and columns for organization
   - Value boxes for metrics display
   - Icons and badges for visual elements

4. Interactive elements:
   - Numeric input that affects both the displayed title and window title
   - Multiple sections with different title styles

The app creates a dashboard-like interface that shows different ways to use `panel_title` in various contexts. It includes:
- A main title section
- Two cards with different title styles (one dynamic, one static)
- A bottom section with markdown-based title
- Value boxes for metric display

To run this app, simply save it as a Python file (e.g., `app.py`) and run it using:
```bash
shiny run app.py
```

The app will demonstrate all possible ways to use the `panel_title` component in Shiny for Python's express mode, including both parameters and various ways to structure and style the title content.

Technical Details:
1. The `panel_title()` function takes two parameters:
   - `title`: Can be a string, Tag, or TagList
   - `window_title`: Must be a string

2. The app uses Bootstrap classes for styling:
   - `text-primary`, `text-success` for colors
   - `d-flex`, `align-items-center` for layout
   - `gap-2` for spacing

3. The app uses reactive rendering to update titles based on user input

4. All data is generated within the app (no external files needed)
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMpwR6KAHM4yUnQpclYFSxxfOAB9QIpWAAopCgAbOABeOTAABSgIOGTkABVOFP8AETgYUkyiOk5k5KgAI1S0woYTOABKJwhXCqqIVgoGKCpkbzzkqKTU5AB3EvZkJtIKZe9R+CoGVkQXZABGLGRZ-wBaIvZ-M9PSZFtOVnRG3m5T6+QMdAByPQBVACSBwATCdFnZSPMZiU5pdCp9bhR7o9nq8AhAPv4mkx5qwHKdmr1XAAhKCsTjEZCaWAvfyLdYrNYbKBbTwOUIQcKTfIw0rxBTIIXIcLsEECsAAWSg7zK5PYq1ZtiKsPkhGQxEauiiGTAVA0FHO2n4rNwmS6RGQrlum1g7IYXz0hV8guFENsUL5rUyco4ioYyoAPsgAILQZK4KTEUJgIWud2em2su07R1sEbcHwKHoQA4AYTEY38UGQr1IZgWSwenDodAc1BE+MknBCCgZy3CZbMUTIyRMMCG8V7UUWtnWrDSwAAbEQpwBdLr7THC1wAMU4uxExCVlcZtlw0BglNOqtdQvbIs4WG3Afii7PwqFAAEbPYGFhLA-H-Y6A8D7BKS9OA7yXR8wOFMQKBMBhMW5XJeTOAVl3AlDkDoTIQ2bWRkH+fFdhQEBjDMD88J7ctKDvABfGpkC-VC3W4D1oTONJ0LAXCOQIoiKBIhwyJMCiumosA6PAnN6OFUTLywbioi5eAGEpCUTFIsgBIoGjMgAUUoAl5KaAlSF-FTOJo6QoD7dJDgABms8SUKkl9qDfLB9Q05CwJ-EVSOGMYEnvDzUMg6DMTYvNoJsFJeBGCQAGtM2QQiIFMHiTIYfjBMor4sP8NKY16R9XA8Mg7A1HcLwACUKSUABk+ExM4HwvcIb1sECpLgqYgKQiShXCR5pB63rH1FABmCU3FwYZKncCgxhUmjNXJVgdUyNzzlYExiGIOBdHNAgpNQ8JnlyCU5BMWwAA5Rtsc7bDrEFkAAeQgZJuDVIglu1XUmigWw-BWHwNq2na9rAC1DpQr6Vt1WxzjoVINC+N6fAgc4SkqVhzh23SHR8DBzhBTJIaFCHApQhNmNVXVJumlg3DmqD8vJ0mpMc18HFczR3NQrzfKZ9qWbA4KYNosAQwaNgpqoGA9ECBwxhbcNidzPpkBJNZkRYJtgkxC8YFZWKmIa08IGaq9WsFkarx5aZEI6q8DYYI2oQgCVnA95A5Tm57ZAYaRODgeY5AUAAqAAlcRknOKR4GQbZFOjUP9qkymgN1b2Syev2A6DlXH3soUmqrTsoFwcsKDIvsBwSYdR3HScABYiGb5BG4XUCUNcPNSGrzFDlTkur3MyyolWDR4g4KFt3xNJRUOM6Luu26Lu2qB9qxeAfqB7g6GqcHO4kzJJU8RPmeGzJDgIEFRsb-Pep9GUI1DP3Invo+he73v+0xImhfNrAI9Ohj1IBPKe8wZ7pHnovK6N07rbUuhvdYlR0iZCaEDTa21doxgChfMAABxXE6x370UyAAakOAAVgAKQkNQsfcgjJSB+2QJKRh7A6EOU-sgHufdkCjUHoycIQDojj0nuwae5IoFXnYAvYmS9RrEDunQKAbELSb1QWAdB5x5isggJmc0h9SFgGdAwPwGkRJC0fJkAAnDQzh4EMLEC4HAWQ8BKDIHDkWTIYBKJEHAIeBAKAwBiAAI6WDEO4uIrkDTqjACVKgNBgkKANhQF4aw3pNAUPJPAChJi2HJAVXqvi5xAA)
