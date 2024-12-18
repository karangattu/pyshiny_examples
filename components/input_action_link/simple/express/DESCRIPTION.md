1. Creates a dictionary of sample data with content for 3 pages

2. Uses `ui.input_action_link()` to create three clickable links with IDs "link_a", "link_b", and "link_c"

3. Uses the class_="me-3" parameter to add margin to the right of each link for spacing

4. Adds a horizontal rule with `ui.hr()` for visual separation

5. Creates a reactive render.text output that:
   - Uses `@reactive.event` to respond to clicks on any of the three links
   - Returns the appropriate content from the data dictionary based on which link was clicked
   - Shows a default message if no link has been clicked yet

The app demonstrates:
- How to create clickable links with `input_action_link()`
- How to handle link clicks with `@reactive.event`
- How to conditionally display content based on which link was clicked

The app follows Shiny for Python express mode best practices and doesn't rely on any external files or data sources. All data is contained within the app itself.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkTEQAJnAZETnBQoDEyAMJioVNszhtY6AA2flZeUAqhFFDIALzIIArISchyYAAKUADmfgCCqSipACpcepx6ZJTUInRCyBnZyHmEicmp9X4AQvkpYMVlfOXkVJTINQx1WZ2pRC1JbZPu3UUlA8gVw9W17YtgCgC+ThCuOVZWyBJS5MiB3ADWemPI0NKcmV6c5AoOWMZmAPoXD4QP43CC3AAUqVBtwB0x6AHFSMgKEjtk0iMRAlBdH8Yql4ABaADMqQAlF9OD8IKYKADJECQXdIWBoX8AEZw1KI5GohZdQhrLE4vFgQkksCklIQb6-WmA8iMsHM1nETlgbkoiYNNxkw7fdgMcHkiAuZAAETKQSgvHWVWQbOxcDOVwA7lxiOxrndkC7sYLOMRbk6FAABSw2BhYKgaCihzz02TqWSUcGyrCsqBENOstlZ6lmdN3P7EY02OhrIZVI2IWZ8cvZotQau15KiOAUEwMCDISJQYDzBpNAC6tbgN3r+YohbB7Ob3dbyTEHa7PbC-fSfNSI-nSTHnAnNOnMOIc4Xi-bne7vfX2x1YG3rbHrDgNZ3C6Xl56bhugfOXrB5xsqQsg8mwcB+LalCpGAexEOA0DwLQYBiAAjg4YjwJQrBRjGApgJBFBIQoMBeEEpAUDcHIQNKAi4Ao6BQNY2KHGeZ4wUOQA)
