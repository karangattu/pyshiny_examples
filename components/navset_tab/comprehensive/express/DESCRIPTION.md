This app demonstrates:

1. All possible parameters of `navset_tab`:
   - `id`: For tracking selected tab
   - `selected`: Setting default selected tab
   - `header`: Content above the tabs
   - `footer`: Content below the tabs

2. Different types of content in tabs:
   - Data tables
   - Interactive plots
   - Input controls
   - Dynamic text

3. Features:
   - Reactive updates based on user input
   - Multiple visualization types
   - Interactive elements
   - Display of current tab selection

To run this app:

1. Make sure you have the required packages:
```bash
pip install shiny pandas numpy matplotlib
```

2. Save the code in a file (e.g., `app.py`)

3. Run with:
```bash
shiny run app.py
```

The app includes:
- A basic statistics tab showing summary statistics
- A visualization tab with interactive boxplots
- An interactive tab with a histogram and slider control
- A selection info tab showing the current tab selection
- Header and footer content
- Reactive elements that update based on user interaction

The app uses synthetic data generated on the fly, avoiding the need for external files. The data structure includes categories, values, and groups to demonstrate different types of visualizations and interactions.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBf0HDk6KHah6vb204OuECYCvD4Q6AoKAMTIAMJiUFRssOgANnDItolQCuFYDB62zFiscHC2ABQAjABMAMwAlApZFFDIALy+WAAi2QBiBfAVIArIY8gA5LGJcADmQrgTKMATAIITRBMAQhuTsbsT3RMAusgAVMg1AKwEo+MTAGpQqSZwS8h5BXbFEEIwz9UAAyAohVG7IKrAhq3CDjSYAcSYJnQ7xWiNIyKqB3RyJqJ3OyCugIUAF8mhBosgAApQWYZUjoKTkVgKSw4WlwAD6DIorAqUgo6XacjAADkoNJSiIACpQABGyG6cBgpBFRDonFSqXlQulDFe5Mp8XESTa0ElcAonNaCoA7pwKOxkM9Um5SLpOHL0m4oINLQ4WRB7Y7kGzzVLrfKKncxpxbMKwDapWq4amxjEAPKMzjkZ58WzIOhCZAUArEADW3FmbDg6Uk5RL8pjNbrVHjIptVRTaZiSroUBMqREpVbDZtzfY4nsDHabPYdWjYolnFmiRzsIAElOHMgAKIaFLpEXQ9PILdQafIMiUagieWkWSNuWBuFF0hUGds2wyRfi6QrtdyGQPpSHfHd90PeRCCvbVdE5BMqA0CgAFoYDMcpj1PECwIYK9yCoShkDlWtSFtJ9AwaRBmxiPpOAYVgRHHWFxmDJ0wwlTl3AgWtFy2LxOGIZAAGVWl5FNpGeV4EPlLswEo5s4TnAAWXj+MEkS1wYgSWTkhTxj0sYAAEbGnLAWigTlGFgeRmLTew6DYUTWEjL04AqeTbLTcYxAoEwGFhcysFmJF0DlXAKimGZ5gYRYGiwWlZmGAyvLGR5JLeZYJngDwDgY2wDjIExKBOZK4TJfIMTsCoakNTyYiEuBrwLG1kFY503FSd9mza9jpE4jweJFB5OFYExnk4AAvQCKWgiSXjgaS5RqY8qM8xTOCwdgVJFXpWmQYbRvGqamRm8kUuSnqNu1XAMStVg4zgOVfXc1aUrhS6Sgep6GBe0qvLZYwzE5EdGooaM1retMRWCjEIkIP7IZFBrW2QHE4ZhSHIeIdhSAEuBWHacy0RCk4sCKzgAEdXncrAKFIVIRrBs7MbhZnEYhtNjOoUy0i6jnU3sojSC0Tqmdelnxg1IcHHKTlzI6TJsmAImJjR-F2k6QGKCCkL3OOBHUw1WYiCgDQFbSbXRrlXneXcg3X01D9ZcCuVhZtioyBeGAIHaNL5t2MLfemKhosWE2NHaU22Yl02Skta0HXSCo6D9149DCuIooWQtixALWddh9ySQmaOWZ8vzYSNyI6uQaUuAYZr5Vah0nVsXBoBgAS8JvShupb0MNvNfruNSRcAEkbzLKRZHE9LFrqFbkuU8fJ4kaeMj6E0-Px48l42rXgYZ6dFzlbgdKIEVRWCYjcNIBzT4gc-kE7n3wX+COiSIOapJqQFS-0-mXM7AOBwKLZKgsuAMVIMFWAv1+YO2Ns6M2nQLYlBMNbUWfJ-52SVqnN4xxNqMwqA-Am+cSHuXDpHDQ2DUyxwjAKJOeDFSMwYJ6Mw64S4G3Lv5QsK5q5whohiYQToWocFIlWK8fkbDDlrKDdcfcQy9WHoNMAyM5FAQnkWWe81FpKUXvzZeIpYhSNvMJWRkh1zIE0X8aau9+bJSAaZRCFBwFwAcsQExlAXJwLLpaCuhYjGeMFLwEG9ZG5yhQHncIZhabyilEXEU1cYirFsAWNo35WBpCgLwO+JZJySIYNI1IITzFtifMgb+NlHEgMsM0NxLZQay0qT47yfieFsnQMnJGpSxxN0qZE-OSZLQJOgsQWCzkEwwBQgvXSFIIAxDHgEEQ-wKA2wZgqKAdAPx5IyAAVTHpkNx3AHTrkDM4Qwz9EhrM9DgXANtnR6AtmAEkRBwAdwQCgMAYgqZ0WVLeVgtMkLQTANeAiFBaBgAUCs65cpcjBDwAoLiWRAwG2eccIAA)
