This app demonstrates:

1. All core parameters of `navset_pill`:
   - `id`: For tracking selected tab
   - `selected`: Setting default selected tab
   - `header`: Adding header content
   - `footer`: Adding footer content

2. Different types of nav panels:
   - Basic panels with static content
   - Panels with reactive content
   - Panels with interactive elements
   - Nested panels using nav_menu

3. Features:
   - Interactive data filtering
   - Dynamic content updates
   - Multiple layout options
   - Integration with other Shiny components

4. The app uses synthetic data created on the fly instead of external files.

To run this app:

1. Save it as `app.py`
2. Make sure you have the required packages:
```bash
pip install shiny pandas numpy
```
3. Run with:
```bash
shiny run app.py
```

The app will create a multi-tab interface using pills navigation, with each tab demonstrating different functionality and ways to present data. It includes:
- A data overview tab
- A summary statistics tab
- An interactive filtering tab
- A dropdown menu with additional tabs

The navigation state is tracked and displayed at the bottom of the page, showing which tab is currently selected.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBf0HDk6KHah6vb204OuECYCvD4Q6AoKAMTIALJQANZwyCbobMzJrLDoADbJtlAUUApZAnkA+gVFyAC8vlgAIoVQAGIMsHAAFCAKyH3IAOTEhXAA5kK4AyjAAwCCA0QDAEILgwDCqwMNAwC6yABUyACsBL39A9JQOSZwU8jhWO12zFgQQjBXnQCMAAw-RL8iAAmH4ASlOEH6gzIJkodweT1sL0R3Ao3wBf2BYIUAF9QZEIDEAApQUbJUjoKTkVgKSw4UlwcoUiisTpSCh5GpyMAAOSg0lYcBERM4ORyyAacBgpG5RDoopyUAARpyACoMG74iDRZBrMQjZBQe78wUUcroBXIADunAo7ENYrcpF0nBVyXc7XgVAYNIgNrtKU4rxNQvNCs6Zz6nFsXLAFrFlSlMsIUNTfRiAHlKZxyFdkABJBrIOhCZAUdrEBLcUZsOB5SRwWxl5WR2v1qgx7lFJVfWVpqExSV0KAmHIiQXtxvNpWt9jiewMWN86ScUaFHOQkVivSS6V95AxAAS84cyDIlGoFFbJdI3tjLVIt9P56olG5-RiD6fDDP5FfV4gUFEFbGJVWVZAvhQJYvE4YgJWaCVOFYXIoFwVt-XtOloGkc0PDrCMwCaaoM1kBgVzgK0+0ua44FjbtezAIDWyhOl2AAZgIgBlbI8ng4jSPIyjGOY-oRL6AABGwFywKooHKRgOjE5B7DoFRSCtSpmk6JjIX7KExAoEwGEhUpckZWSCQHZAwKVZAgRQTjgg+BheE4oopFYKRiF9KEMMDYMcPcCB8O5RyYGc1z3JpFNqJuOjlSBbkdL01iONCpyoBc5A3PXTzYOirU9KUyTqGk2T5M9eRdLTFS1I01gMpc7TgOqvTRCFIyTJ48zmhkuBWGIBhXS6LUQOs8C2JQfMLwrKRZGQABRPJ4EoHz+j8rD+Vw4KcgI6bvQkOb5Biq44q7ZU2KSlq9I2oNFVwUgzHKVhozgJVMuapTfNtTCgxe+x3oYT7Wra-o6WMJ6JzgSQIxB0HU25YYqHGFzZS++HQrraGRDWEYUbQwh0dB4h2FIWD+pqHIkLRUyKlkmYkbGCZdiwWFOAARxubTCvhqEed5vpwfCSGqYXWGBf7blYsZeUxwcNG4Yl7kWlFb1kAANVO46IQltMYG4GpUU6WmeqKGZpZZ-WIG5nXdahD4NENyhje6zSzYuLXLagDQbaJtrpZqYAjZNt2oHNz2diwK2bb4Z2Q-pj2aK9n3QVBHY-b5v2-ZKuwHBk5oKsUxXU1q2XvUbUPgbt2xVLqePmmADP+xdspTbDoY8eZvYajqCGKCwRn8e55AADIm7TFuzND8Ok72AA+Xvhf76X5NVhxtOAH4dlBUfx9TSe6YbxObl2ZAAB5F9MZetdXuWgdBYAvm3vf0+LvSDM65S6Esj9xtsgAWFAAB1H6cRqAmALFQGAa0+i3QCuUFaJgCKxCEMkLMVIIAFWuv2OB2FtohTAAtDQ5YjTTRLFRLW8UlT-yun7OkzkEhIitNbbkrCwB+yiJw5AsxbC2FtBuPMZD3jrnIH7VUXA9DdmUkmTBJCqCSLnCkQUyBSCqTwYg4spZRhMFSNWdqioOzTlYFgLO7CzH8wRsXXBW0goENmEqR6V4To0SoUcWhb8wZBgYUwlhZjWEePTFw+xjjrISIlEmMRYT7DSjqsMQUCjkiXCGo9PQHoOjem8HYM8GBlSin4f1FRaiQxmnjOKbg2VVC8BLD+IkuA7TkBMQE5AbCkoEkHEhFCvA7TJGIEZGwHJeBQwbE2bsCgc7SSoMQhQtUhkdnKN2Ku-QP7GWLNyNYfTLw5EGVjYZ04UAgD7jgBUiZpTaRxNyMAOIiDgGgPAWgYAxCc04GIFaLIsAUGISmMAL5Lz3IUB8CguRbxUxnBAIIIQFBBQKL6P2lydhAA)
