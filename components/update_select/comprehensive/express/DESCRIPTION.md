This app demonstrates:

1. All parameters of `update_select`:
   - `id`: The ID of the select input to update
   - `label`: Updating the label text
   - `choices`: Updating the available choices (including grouped options)
   - `selected`: Updating the selected value(s)

2. Different scenarios:
   - Simple list of choices
   - Grouped choices using nested dictionaries
   - Clearing all choices
   - Multiple selections
   - Resetting to default state

3. Features:
   - A sidebar with control buttons
   - Real-time display of selected values
   - Different types of choice structures
   - Multiple update scenarios

4. The app uses:
   - Express mode syntax
   - Reactive effects
   - Event handling
   - UI updates
   - Card layout
   - Sidebar layout

To run this app, simply save it as a .py file and run it with `shiny run app.py`. The app provides a comprehensive demonstration of all the functionality available in the `update_select` function.

Installation requirements:
```
pip install shiny
```

The app demonstrates how to:
1. Update the label dynamically
2. Change the choices between different formats (simple list vs grouped options)
3. Update selected values
4. Clear all choices
5. Reset to initial state

Each action is triggered by a dedicated button, making it easy to understand and test each parameter of the `update_select` function.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMqx0AGzjJbUCihkOiE-Tjo6B2oRVmJqKAZOUlYFVkCqPQBeZBAFZHzkOTAAUSg05ABhUjKKIpRciAKmwrAAOQBNOpbWuAB3ZHahAGsigjzm-KLWgCkuqb7kaYdWOFxR8YmiioAVObAqiAg4SU5iMyKN5ABfMcaCooB1OHKqmq6GicmwB4BBPYeyqoAOYUcjrO6bMAAeQASnsoWIgWDCJcmls-rQtlAvOEhBBOFALhDrrc0WAALKcWy9Z61WgfT5FcmtPaUw7PUiBcGfFoPACS-04sXIrG43MZYD5GJQRT5pF6hLAlyuChVEAUjEsFCyyGARR+mB8oxaACEoNBoMaigjzUD5IQWgBxBgYe1EJm20hFAC6TgglhwUDtAH1SOhtQAKKQUHyZIomdD+KjBlY+STIAAicBgXoddE4Xi8UAARrHtgwTHAAJR+3qcCjsZABou4UhmFNUuDFhIRquIS51htNzhYUX2bsMXv94lNAPsAAsEa25AoTC8yAACua4F4ijWZwUA8Z2xIpORg8WzKCIEuwAmk3Bg0XizurWAAKqJgK+AAyJdfYD7jyR4QKYFDBqeSQQBeV7kLe97fsGxDsKQpzPG+n4PpUKFoSkgGooeI7HuBkHnpeFDXvBX7JqmxxULYGHUb4bg7nRcAMfhB75CBYEQScZGwTeRTED4CQQYWb4VKJDDID8hbYahcR4UBnw8Se-HQeRlFFDocB0u6YAws8enIKCmZwHQUAmF4dIqRMc6TnZzRqeBLq2EkMEUSKS5cc0wk4XEwYULg6BugRkIVAFvjbCFYW+U0DI8pCooCEamJgG4-DeL+Qr6eFSVFECTAJuxezOm2oW2MgULhlBeGkklkLZuGazpcUAjBQpuFEo1+Rqjy+4DvWjYBsQCS2FO+WjeNwbsOI9iTkUWY5u4rHpnyoHnJxPKuNsc1sGtRibSINIAOTyS+TbUdwQJTURx0podPm9S09g5o9aZ5fF9z7ChyS+PW2asP2KLffkyGKc8mSavWrANY1tGSOxcZgAa2Xio1MDWVI2WZOWlb5YNvkAAI2AtWCWPl9h0Adn1QcG3AhJNYPIGcDA2CI2TEVgb2kB9dG9vlTThMgECcqzJjs9E04vU0YgUJLjQBugt6tKQfBUDAeiI-RxoiWUrDBijVAaBQAC0WO69tvUi0K3BpOacQRmzHNEDiaR9kLnzy4rw44BGdBFCxn3sRrQP1KdRCnVgABWqE3i70RViq1uNT7DBKyOKuBxlh2h4DMD1InlAp0TrhZvmRyiOIJyyMgFmRJIeghDJNcjUxyBhg4ARQQopM11IsjqBEdF92IkFD3AsiUBG3MIcmz47vu1PIMGzNNGQJiUA4yBc8dFNMU+-5eILxIBvPj4689Eq8-zkgY80i9eNDWx-SsYda8gEaYd+VUgJv28GBXFMvwZ4nslTEiJv3CecBh6N1qBAaBtdYFT2iLPfeF8kJRVYMvCyq914FAhmhIKsVd58H3kQwKwVQqnzRMSEWlDHzUN8JkbIRQUroyQPlI4vQsGQx1HqaEtVyAtGQAAajYKuWeVZgihE4OQ0Qto4ARgAIxEAAGxVl9L5c+h8r5ey+LfHWD8eSMNYJkHhfDcLwySjrZGlizHAAAAzaIGpcHcDCookNCrvNhYAioVVKlwnRI5MH6JZkUIxh0TGfDMZkB2GQbE8jsbYFGFQMSE3cV4FYKBkCuGasFO6B8Hx3woNfRqkTsx82MaDF6cTgDeiSZ8FJmQ1ZHEyeqRB49kFwNHl0geMgUHTzKXPPRedbC4JpmvT2xJGHeJYeQsCWA5nMNofcehNMVmkNYS0DhaUZaqVCWMz65SCpgCiZ9GJEwWmCJqmeRoAAmN8dyoLIHnD6DpTQPGbK8cw3xLQAklQ4gc+yRySnhJepU96NSmnXPGZkQR6S3wdA+b5JyO4clFLCU9Axr0qmlKuc0FpbT5Bor9EgweKCR7336TA9Qwz0FLJEuIBg4kvCTPwTM2cYLEIQpvvimF+V6mNPysS8gpKmhQO6ZS3pNKKWDPpWg7mukKAcumSCv22KTn5ShdU6JtTPhPzSW-AGmtgaEriTDbUsLaZsVSfqQ09pLhVjADcHIkBYAIBQGAMQABHSwYh4CUFYFgCgpsHRgDINvGg3qFAwACN4TkOJiwKH9AINYoFzT+BSJ0l6rrvRAA)
