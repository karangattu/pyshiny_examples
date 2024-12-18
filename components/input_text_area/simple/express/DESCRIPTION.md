This app demonstrates several key features:

1. Uses `input_text_area` with various parameters:
   - `id`: "user_text"
   - `label`: "Enter your text:"
   - `placeholder`: Provides a hint to the user
   - `value`: Initial empty string
   - `height`: Sets a specific height for the text area

2. Provides sample texts via a `input_select` for users to quickly populate the text area

3. Performs basic text analysis:
   - Word count
   - Character count
   - Simple sentiment analysis

4. Uses `reactive.effect` to update the text area when a sample text is selected

5. Follows Shiny Express mode conventions:
   - Imports from `shiny.express`
   - Uses `@render` decorators
   - Uses `input_*` and `render.*` functions

6. Uses synthetic data (dictionary of sample texts) instead of external files

The app provides an interactive way for users to analyze text, with the flexibility to either type their own text or choose from sample texts.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMq5K7OFOLJbUBRQyHRCyFQaIlDQADa4rJysCqyw6DFwAPoRFHoAvMggCsjFyHJgAEpw0pxwAO7IAIxlKGUAKt7I2qS2JpLItVB6sFAAXtwA5gCEyACSyDGksrbIVQ68CRDj6SHiFCZiyNHLtaQmMcv2dNycVHGicGQw8HZ8IhSkyKQU3gysWGUEIolMqVap1ZAAJmapTAABFEhhBNwpJsVloHDUIMQ4FhkO04MgAI4mKAxG68AZ6CBffrsQKzNHoB5UZahBjhDraTjY-6EIHFEFVGr1ADM0LKADk4GYGKT7mDari3MwCeNSN1DqwmZJWERWCrkAAjKDLQbanK4gDCp3OyBMrAJ+vg+i6smeFoBCgAvk4IJYcFBxplSOgcgAKKQUdK5NqaEQAQVi8USyFhcBgpDKAEpfbUbuw7ZwsDEoLhThQMgl7MaGGGs4h+f184WsFW4DW6w2ICUey3jGYsnGMlAxFAw43e8CwPaHIPIgDSt3J72ygBRSgOZBl-bhOMNwiL5e9tISODsUjnBwxsCtXBMz7s9CDKhb07s7LIH44rC8ogT5fSKSJhwNenpLkexTeJw4zsBQ14QgADAh6AaGU-7FDm4ErlhPb+v2FYOukkjjjhy5lCkAjpHOFALuhK5gAA8uyxDnqQDqHGwqTbNk+5-qRk5kqwFBhhRaSZNkfwANZwPEdaYUemGNnm3wtsQI62J2dH+mpDC2Bk3gmg4443nGyCJqSyZJGA8lkfxyAAAI2PYDBYNkdGXP0Qh6WQJiUJpdk9q4ADiPi7pEIRMCwcD5puM7svhD6cZRBJuQFJQfvk+FYHF1F1ololURJWBBsJWUFeJcZ1n+YDZnRPZ1SUrgAEKDNyYVREmCRJGlxQnLpeTta2aQ3HWDXFGIewMN2dBlAA6l5yDWr5FAoCA6QQGGfW2KwWY+jVdl0Y51DOa5cbuXAdDICxI4ZD5fn1mNyDBaFH5KFFMXsnFfAQKYIhhOV7WPRl32-dlDoMLlWb5VxFWRH8JVhmVMOQ9VtU9YeEHFK4lp0rKkibndIhhpoxAxCYtgTLSNxwFqp42Zj12-Mg+TrRGcZYGIJ7YsZMKo9Z9MQRN+zTWUOMjhIVDsktlDIMTGik+TlO09iO2rYzrB7XRh1OQ4p3znZHkOpQ-DUMJD3o89bymW9KwfXa4Mg2Y0PJYD6PA1lOXZHl-3I0VCNI8lKMwmjmMChb7j8GJbCmybMvRBZXVGoMcDLOQyDSbgW3daHnRsTcMiZFnzPIMAZTDGMmy0WACxLFX4yjjRB5lCcdgOHQZxVyTcAxOtjcALqPRAcDjIEBcZEX+Sl2AFMpJgpDIhMVfGrYVeCEIVeSwwnCGukVd9UJZQD+jQNDgstSbvk2TFqQ5+1gLR6PYICRSLIt2nDL+SsCYMBhg0IRhFtb6udn5jyLpwS6gDuDtQyGfBw99lxDxHi-TIhNi5fx-n-NknldJAMQaPV+YCIELSgdkGBN84GPUeuA4B+dX6oIAHzIDwcgt+y0uw5x7ELKaMI3Ax3dCgAACnnZBpRyYAA4RQr3JnABCAAWNC6Nu7UOYWPBhNCWGE3YRw8aPhhY8L4abFAUokEF1EbYCRUj7ANHkPtHO3cHRaO0Vw7sZReHG34cgKUMo5RyHEZI3xViEIKMbEdCWBd1B0DoMyRsHkMj+SPK4Wa3huzBABh+FMhFmQpyIIIUwJYXzfBSqZEc4g6LUIDmJSGjiIL+hMOgAIVBqLDlHMZT2Z0DyATJiBcq1F4Y+ERj9MwrZfaVSzHzLMWYwBeiIOAaA8BaBgDEMSTgYh3R-AoJEA8YAyAbhoCgfaMBAhpC+GSQ0Cg-QCFwAoJ8dhBi+hzlMvuQA)
