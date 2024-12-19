This app demonstrates:

1. All parameters of `update_tooltip`:
   - `id`: Used to identify the tooltip ("tooltip_demo")
   - `*args`: Passing multiple UI elements as new content
   - `show`: Boolean to control tooltip visibility
   - `session`: (optional, uses default)

2. Features:
   - A tooltip attached to an info icon
   - Buttons to show/hide the tooltip
   - Button to update tooltip content with counter
   - Dynamic content updates with HTML formatting
   - Font Awesome icons
   - Notifications for user feedback
   - Display of tooltip visibility state

3. UI organization:
   - Uses `layout_columns` for a clean layout
   - Cards to group related controls
   - Bootstrap styling classes
   - Font Awesome icons

4. Reactive elements:
   - Event handlers for buttons
   - Reactive display of tooltip state
   - Counter for content updates

To run this app:

1. Required packages:
```
pip install shiny
```

2. Save the code to a file (e.g., `app.py`)
3. Run with:
```
shiny run app.py
```

The app provides a complete demonstration of tooltip functionality with:
- Show/hide controls
- Dynamic content updates
- State monitoring
- Visual feedback through notifications
- Rich formatting of tooltip content
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAApQA5nGSl0U8j0oO2QAMXIRAEEAdzhWZh8AYQBlZIVLHC84AH0-ClYACikKABs4AF45MAAVUlISqXRkABE4GFIqojpOEpKoACMy8uqGEzgASnTOLHZxW2yySmoKAoVkdeQMgAlqgFkAGQKAcgAeEu4Aa1E4EsqwVgpcMo44OAoq5HYxOjv2Cgp0KxEAB6YHEWwQABWrCwxBKpBMtjofTEsOYwKgkKgGmB536rGBdAiAFooLF4vBgQA2LAAFiwACYwboMb0sDBuLDdFUAHxHSYQAUuZCJMRQKjIKDIPq4BEiaKcCjsZBkEomGAQVgKBVKzbTGVyhb1dWagrjRBrDauUKcBgPFXGjXIHXKxYUJglLUQDbOxXKjLEKAMWxmi3en0bANB+azKD2BirGp1BqcJqJCIerVgAURyPTYxmbISAIQbL9MwUciJ-oUUscUjRTrIKrJdgN5CV+qNJtwqC6bJ3eDEhlVHO5vVYAsUIuSTjkMsVqtVGulrj2JtVLacewd5Pdwgqvr9wdwYejy25jJTmclhf-JdgFfZEzoWzi+QHqoAVVf793XdTB0lkoHsj1YAcqiHEdswvCMrwgUxpwgdUHE4YhEzIEwlkcT8wB-N8JUw7Cm2kKA1QqABGIVw3WVxkjgRZbAdNUnRdf8Uyaex2lgtio2DUNYJ9PiYzmBxE1qACmlabiYJoiNBKtEUxQlKVOw431dWCPhFgU9ZeOmNTGgKbc7kM1Nsi4joD3QPpiDaZY7gYThPD+Ucw3HODplYdBglWOSPKEgyvBhTgCl7Y8qjoKBiXic4mKi4liFtOFT24IkmweJ4KkiklWE4AAvOAUAZMQYAAblHAhdICzKhiqYgTDtIQUEEbgqAYCqwGqn0xwC5swAASQgRVODI9jGiAqgQK6iBhXTLD2uQIkGEm5ZNl-KgvTdZYjQWhxkHKa5ixkOAsFI8iCiopwIAAATFWdZHUOg6AY95bvuqRHrgWRKGMhCzCwJ962iAV7DoFQG2yMz0AEuSMhfAicmhxNoYstorKIYHhlGCZYIyCBSCkbpA1vYHxL3QDgdmg9HnQbKwHgXQsnPWb3vEB7TrgZ7XoUO72c+zmfpWKdAdrbI11xuwuc+bckYpmHzTx6YEffKH5ZR+W0ZkzG22icpQjI1hJcCrACaJtDxTnOtdfJySZdsexqaIWn6eiINhogTwWd5j6Tqel7JB9-m-e+5Y-sQ0XSxVqhQel6O5cko1gJWRW5IgOBoiTqaREO4BqoydhaQKOhvw2uAmPTZPkGcEARaI9qzQAX0q-Pphhqpqi4PROCCZBbFwaAOWIcbAJdC1syq-y8ywChgqwEwSj8vr1gyWfPBhc5E12BfGjKZAbnsygs3GSfl4nNeN9Czc9n2JahBgcUpE9lup8vIL16wTfV7n0LwvAu4EqxW3EtaKxBZjEAuJVfqyABqLGPtVXqyAAC6sFYKuHwn+aGGllTp2iKtSgkoQjAz4G9E28c1aSQ1onSyTYABUuCs7LB1g2bGYxEH40JpwYmlt5xkxLmASu2d1qIyYpWautd-oUDRHtBM4xm401wHTE8TNvDewgK4ZoPcbJQF4A1BgNgRBYIeO+IOUsGAz00G9MGI90DZGMRQEwhRU4+jEA4hg3p+ESXUtIHunB+g9EVLorS-QfBgIYhccuyAfFShFqjSyoZkASIjnE9GTcqhgEbkQcAg8EAoDAGIAAjpYUqywYQUA0BQA8YBto0DyQoB+AJ4SlD8QoZCAhcAKB8nYPs10z4ZKQUAA)
