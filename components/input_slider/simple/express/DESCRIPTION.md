1. Creates a slider input that allows selecting between 10 and 100 points, with default value of 50
2. Shows a histogram plot that updates when the slider value changes
3. Displays the current slider value as text

Technical details:
- Uses express mode which simplifies the app structure
- Generates random data on the fly using numpy 
- Uses reactive rendering to automatically update outputs when slider changes
- Follows best practices for Shiny for Python development

To run this app, save it as `app.py` and run:
```
shiny run app.py
```

The app will show a slider control, histogram plot, and text display. Moving the slider will cause both the plot and text to update automatically.

Package dependencies:
- shiny
- numpy
- matplotlib

This example demonstrates core Shiny concepts like:
- Input widgets (slider)
- Reactive rendering
- Plot output
- Text output
- Express mode syntax
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBf0HDkEEwN5Q9EdAoUAxMgAynAi6FAA5nDIUhQANvLunDhRcAD6pOgUrAAUcYkAvHJgwc6JIfGc9gzIACJwMKQlAJT+EEEAwmJQVMhQbFU1fL5mCpZYxmbprEMOuSXuMOmC3DklRCUAch4ARg7IpHTIq5SsG8gw3IUAjAAMRDBQGrd3D8jSUPEmcIUArHc2hBAshuuI+gN0PFSCIKOxeqI4KxBHY9BRSLF2DFZtUHAoAAI2Go4aEUBT2Y5cVjoyIMWC5FqIBTIFnIIIAcWoDl6MTpdmUtl6A123jgtkOEEGuNqn2+SVZbmwfNszCwrDgYtyNwATABmIEKwUUAaFRVYZWqiBCJ7xXLvG5EKYULBLFakNZ5FoG1nM1ldHp9Kk0ukwX0suicSJEZ7IU1Q52sEy7KEwz1h-oaLBB3JGqBEXbcViFbXvewQVicCi4QoAFQYP29LOearC6QKcFydBKAAlONTSLTYIdjiAnS6PG6PQyAL7IABKUH5LAACu6zq10831RR0hp4lB9raSgA1L4-DeS1lb1u4feHhZgBrlyu4VrIdNiCgmBiSiORdpBME7CkAA7piMTEN+NgiDiwyyueECEtQxJUBoZJ2HAxywQ46TwR2jIfmE36-iUACapAmGwcCJJIYrIKOozOq6pw5DOJxrusYBgNORDgNA8C0GAYgAI6WGI8BnFgFBoYQJDkFQNAoGAChPBQKYJJwuwKEseAKBEdjeO0CrGay3EALpAA)
