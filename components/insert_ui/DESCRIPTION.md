This app demonstrates:

1. All possible values for the `where` parameter:
   - `"beforeBegin"`: Insert before the target element
   - `"afterBegin"`: Insert as first child of target element
   - `"beforeEnd"`: Insert as last child of target element
   - `"afterEnd"`: Insert after the target element

2. The `immediate` parameter:
   - `True`: Insert UI immediately
   - `False`: Wait for all outputs to update (default)

3. The `multiple` parameter:
   - `True`: Insert relative to all matched elements
   - `False`: Insert only relative to first matched element (default)

4. The `selector` parameter using a CSS selector (`#demo_container`)

Key Features:

1. Uses a single container div with ID for targeting insertions
2. Each click adds four new elements demonstrating different insertion positions
3. Uses different Bootstrap alert classes to visually distinguish insertion positions
4. Maintains a counter to create unique IDs for inserted elements
5. Demonstrates both immediate and delayed insertions
6. Shows both multiple and single target insertions

The app is minimal and focuses specifically on `insert_ui` functionality. Each inserted element is clearly labeled with its insertion position and count number.

To run this app, simply save it as a .py file and run it with `shiny run app.py`.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkTEQAJnAZETnBQoDEyAApQA5nGRSKAG3kIBxwvOAB9UnQKVgAKP0CAXjkwblZbCnCHZAAROBhSFIBKJwhXAEE2bk9A5AAjMwpyX1JfBk5PbwZkAFUAST4IdOFOclYFEOMzcIkpcnCGiiaIWJSoKysUohTyjd6BgFFA+EpxwmRifyhdcOSwOooIeseAWm1+KAZeGDqXgGZiqUKhdyBQoNxbMgrDIWsh2HB-OhkAB3TgUdj7QbDOZPQSsNGjIbIBSo9HIELQ6SxThWO42ArhMiUcEQWxbC5XG53dD-epCGzdJgmaxwTZgIqIBTIaXEsAAYX8nGIAGtfPD6o1mlA6qRZLD1lZMQj8tQYoMoZw6HRbKbkHiCWMUkDkHLSMKqN0msgYFBlT5hZwAI4mHx9HJ6OhCLEZUXIY0nGIKMjuyGJUTiSQyOBYaRQfwh2IABhKEAUAAExLMs+orXBJOXK5nZOpZJRqRBTBQsAaSzY6MhwrEJVKZcnKMg02OPVhvBQhyPpQvkK46nBI2IAEJwTzcZAvaPCeproQ+dE+JlgiEMJeTIYZLKcVZPGUvikyJ8vz8yugpI4m8cgFOAC+KCruucBbjupaEEuX7Spc1ysLcayBIeeYZG87Q+l83oUC8ABMWywXBNKJD+9zHmICzbtw4SAW6lBAU6z5fkUBDEdK6SBJIQh3M49KkIyoIsmyMEsZ+yLwmIdxgSekHcMxL4li+S6uFAdAevJTz7mkGTIFAIhnmwYKHmkNKnuqF4id0N6cFgunCA+H5wW+VIcZ+5F-gmyD0e6IH6Rpthaey7kvghXIoXp6HCC8rAmMQxBwLouEEUR4lwXwtLkepHrUVBdHAYpcFse5XF1k0DB8QJQnMleaUZZJNp3DlQU0dBS7KTKqlHuBBzWHuB4iAZao+NQhpmTYI0grVrLXuJt7Yk57muc5GXSp5xy2r5jGgZRcB9WK7HpXB4VIc1qFDRdLzIp8EDVClhHnKFMqkeRslUWNBUMRQTFgO5JXHZxxo8ZVKT8fkglWXVT2AyiUlwDJe0HUV0qdYu4lqYFDAHQNDlDVjU1Q7Ntn2XejkOKtn4rc962-ptAHASgLXY9Y9VrfBnJnZFaFXdwkYPWz7OvWsWPhJ920-Sjn4AxlZUg1VEM1ZexNiQ18PNVjyN-eJaPEuJU62Fg6RzlOyAANTIAAjEUYBAQAukAA)
