This app demonstrates:

1. Theme Customization:
   - Uses a custom theme with preset "shiny"
   - Customizes colors, fonts, and various Bootstrap parameters
   - Adds custom CSS rules for cards and general styling

2. Features:
   - Responsive layout with sidebar
   - Interactive controls (slider, selectize, checkbox group, dark mode switch)
   - Multiple visualization types (table, plot, statistics)
   - Card-based layout with full-screen capability
   - Dark mode toggle

3. Data Visualization:
   - Summary statistics
   - Distribution plot
   - Interactive data table
   - Filtered data based on user inputs

To install and run this app, you need the following dependencies:

```bash
pip install shiny pandas numpy matplotlib
```

To run the app:
```bash
shiny run app.py
```

The app features:
1. A sidebar with various controls
2. Three main cards showing different views of the data
3. Dark mode toggle
4. Responsive layout
5. Custom styling with hover effects
6. Bootstrap color themes
7. Custom fonts and spacing

The theme customization demonstrates:
1. Color schemes
2. Typography
3. Spacing and borders
4. Card styling
5. Interactive elements
6. Dark mode support
7. Custom CSS rules

This example provides a comprehensive demonstration of Shiny for Python's theming capabilities while maintaining a clean and professional appearance.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQGJkAxASwCcBnC5ZiTqAG37JWcAI4BXNnAAmydFGIBrKAHM47RAB0IDdM3TdeFAUM1h2ACx65gFC3HgBdM3KgRpUdsgjiYeZDBQFOj8pBT8zABGyBGR7J7s2toAZqykMMiW1tx+pKxcIgoUzABucClpGVkQuFhwAB7oIuxezLn5hujiFESSRCLucKzabeh5XPLunsjT6NIj7Vw+frgzXhDoC2MdgcGh4VE4uCFha3L8FEk6yADChVQzyMTinOnIdg5wyADuzHbIJSgrGYpBerlYsDgVA42kkOFUcAA+qR0BR2AAKbTIbHvP78OAAXjMABV7PBbi8KOlmAAvIIgiDIAAiDlIZgIWJxyWYgigkXxBOJrHEcA5jJxH3gBLhpM+mPFOJxZmquHZivVGs1DEini+TXUUM5GugUrMz1eMERkvKhE1OIY5qpGRN5QVyAAlFgoNJpIjpHBklBxBcMUb1U02kDcIiyKFWESwHQAAxJgDskWSyTV6t0wMCrFWsbyYcV7DgZCmBZjpDjCboADZiKmAKyp+a2+2ZcvkDwFp414tu0viYjEdTsau1sx0ABMAA4oKmACzN7OKhjsEdjlr9uMlnEeCBqViTvJ16TEADMzZXa-XyEPx93g7t3yBEB4KlP8enmekqZTO9sQYN9WA-I9n2GIccR4ZJSG-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)