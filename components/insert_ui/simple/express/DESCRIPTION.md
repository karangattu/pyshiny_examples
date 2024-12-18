This app demonstrates several key aspects of `insert_ui`:

1. It uses a sidebar with two buttons:
   - "Add Person" dynamically adds a new person card
   - "Clear All" removes all dynamically added cards

2. The `@reactive.event(input.add_person)` function:
   - Generates a unique ID for each new person
   - Selects a person from synthetic data
   - Creates a card for the person
   - Uses `ui.insert_ui()` to add the card to the container

3. The `@reactive.event(input.clear_people)` function:
   - Uses `ui.remove_ui()` to remove all dynamically added cards

Key points from the function reference documentation:
- `insert_ui()` takes:
  - A UI object to insert
  - A selector to determine where to insert
  - Optional `where` parameter to specify insertion location
  - Optional `multiple` and `immediate` parameters

The app showcases how to dynamically add and remove UI elements using Shiny for Python's express mode.

## Installation and Execution
1. Ensure you have Shiny for Python installed:
```bash
pip install shiny
```

2. Save the script and run it:
```bash
python app.py
```

## Package Dependencies
- shiny
- typing (built-in)
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROcFCgMTIAwmKhU2zOG1yV2cKcWQATZygFaHg9AF5kYDkwAEEAG05ieUJkGIAhUgAjGKIY+3YoBkSUvLAAEShpTn9ctLAAUVkYgF0FKABzOAiogCYAViIAZgAGYcHkABYxqf62iGJOKW7kSOiwADk4AHdkAE0hAGs6mIBlKAhkADEGC8XWMhOwAqTO0ifM1gpyJ9PxCgo8RS8wUlhwnTgAH1SOgKKwABRSQFwcIxACSEFYcGEyAAqmjkOU4DB3mAAJTWCDbJbsZBg1g1OBZIrwsmIBTITl0zhYYxmSESKTkSFZMzfCDwmJQfz+SHobGsH6pGKxGXIAAKCqVFMuXLBfIoAsknGFooB5ElYGIQKKcrgMKBT3sNoYyAS8RiOtsDnIFCg3GxyDoQgCnlgr3i8V40v8cH8yHlDvkEDB-hk8JqqLAifQQMhZEo-og2M9lIAAk5jbJ1HQ6HBJAoK+Iq3B1LJKBmIKYKFgY3aGIqIDrY3RkJDWezdZy7ABxajY5zuKB0iCcACOJncaPKQZDFG8yGLu3lA5+U4TWogkJqqyDMRPg8hIANvZl-cHrIAvjEOVzf9PkD+IFJGQZdbggfxlAfcggyYFhSBMV1WE8fcfCSAIgn-PgIM0W9O27V9ZWgiUyWQABaZAAEZSIAUmQIEJVCbodS5Q9YHcSImNYYBuFjDR5lYiFbwhbjeM0ASuUWCheEiKTOG6HicP4rCsLsRx-iXZBiCKeNg1dVDDx2C9TwgLCj3fYVtIYeNIjBKz-Elc9WLBdhJnhJiyQILDnJ5dB4ToFUuhQEAIW-ckvKcvVfP8-IllwYKpNwMLPO8rlM2I69anPFi-3POwMSxHEDKPYzBy0nTsO+ZADILP0AwYLD9UxbFDUsRzWNY8yMvsvJIs5LFgO+BgsxsHM81qosS2VPrkG2bwxCzLI4D0uAGggn9svLSspGrZa6wbCAm0FGRWzgdsKHwswsGtcQGDtJNh2WscJ1U5AACViVIWRQMjBMxGqBDWCjbDCqoeMxuTHysDEElZEhNqBvrIaRoh-NfUm10AD5kAAKk9MBPyIcAmNoMAxA3TgYeoOEsAoDQKFSK1fWp0mFBgZxc1IQFOByCAUwEXAFHQC5AlYSkOol1BPxaIA)
