This app demonstrates several key features:

1. Uses synthetic data generated within the script
2. Utilizes `ui.card()` with `full_screen=True` for expandable cards
3. Includes `ui.card_header()` for card titles
4. Creates multiple cards with different visualizations
5. Uses `render.plot()` and `render.table()` for dynamic content
6. Includes a sidebar with a region selection dropdown
7. Uses `ui.layout_column_wrap()` for responsive layout

Key Shiny for Python concepts demonstrated:
- Express mode syntax
- Reactive interactions
- Card-based layout
- Matplotlib rendering
- Dynamic data selection

Execution Instructions:
1. Ensure you have Shiny for Python installed (`pip install shiny`)
2. Save the script as `app.py`
3. Run the app using `shiny run app.py`

Package Dependencies:
- shiny
- pandas
- numpy
- matplotlib

The app provides an interactive dashboard showing sales and profit margin data across different regions, with the ability to select and view detailed information for a specific region.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5dKCAEygGdk+7LgB0IDJq2QQAro1wD+EdKPEs2MKBXQAbUhW10ARjlw69C9toqjRAM2akYyXgAs6EeasnM4UYhToANzg7BydXd1wsOAAPdB9efi82d3RpCiJpOiIfbjhmGwgAYmQAcWp8zThnXEoXOADiZB4KKFElLGZOLkcsXjg4LgAKABYAJgBKUV4obTheAH0WqGQAXiEsABFNKAAxLvghkFFkU+QAcgAlOABzOnJzlGBzgDk1F3Oic4BlUnSPr4AUT4FE+FwA6vNQV8AMLUChdbTnAC6BBOZx+s3mjyk2C63F6+K47goQwArAAGKkUohjalUohkiZoiBnC4ABQctjoFAWAFkoMw7hAcR0ib1pGJbCwYEMKVgAIxEeUAZkZUwgAF8NaISt8GuwoDdqqR0AFyLxRFkcEa4AtTRReEMAvo4KthGBvlj+NtXIZSIKRIRkNztNooIY5qsACrMaRwHXFZAwnxVATOOhcOCGQUhljIaT9ZjIEmVfz3CCiADuPJcBbofUz2cFQwmiHRp2tqXSC36c38Qw7bOQHr7cH8gwWPju5A9RCHbI9+v7bGuM8rwYXZ2ILlIdGI81WMzmi2WzzXFZRWAopAMvFJGrZiZKABkoLg-mwaxQ6zBpFY6B0apiEDS0IG-OtrXDD8ezIbRZAgBYqy6dAhhrLgf1WBUAHpJnbVkzj1b1k0DIcIPrLAQOYYZbH-bRe2IHxqBjOME3w4czmtKiuAWeooCzZhBzAaM9FmZAvRPZBDHkC9ZzAR8OJHAiOIAAVyAScF0axlOHLNbGcb0FjMB92MUtkdAoLBuRuaQfCGazeDoAAvN0hgADiIAA2CYFLM04LKwHNBOPeYlh2c9bkvVEDJPMLWmeCTsWRXy-ICl05iGTFJIAQUY0hEmQWSIF4c4UrMgKYnDQw4G0TKitKrcOIC3AqpqzLEv4IYABIJganTyqsLAYkaABrJ0HFac0IFWEYmUa4cfAoWzWQCm5iFsVtCjZEpOVIbk2AFIV3BI6iyNrCjuPsuiGKY6bY3jNt5q4wNeN8AShN2-bkEO4VLXk+b5rU6gNOM+a9PYLkeSMrTW1MvzLEs6zbLgey6BuRyXNWdyvJ8+bzMG9A6BRvHFJC09wvOT6oZ+9wUXnfr4eQVrtF4I9DLPK5IoeaKSY4qB0lNfxVnOABSBVFVsEWRfOXnkDKxS0p5DLKchg7BV+qSZK5kV5Y4xbloRrA1o259kE2BooDoOYuEK7XkAASQgaVmA0KaTpEcDzue6irrDG6Bju1jHp072eL496PSKs2Latv6UqHIG8mYa8IzmIdwenCslhjlnYfmscJxt9Zu0sguqB4zPyE2hnTn15hWTJuKoGARuOfq5E1nWMvBmRMBNSIcBoHgWgwB8ABHLIfHgSheGvYbgzAMhKHhEfRFd4yDEMdpZDwUQOG4PgtsZvvkSAA)