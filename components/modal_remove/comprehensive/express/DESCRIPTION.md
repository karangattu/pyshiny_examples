This app demonstrates:

1. Three different types of modals:
   - A basic modal with automatic removal
   - A complex modal with form inputs
   - A form modal with selection and text area

2. Different ways to use `modal_remove()`:
   - Automatic removal with `easy_close=True`
   - Manual removal after form submission
   - Manual removal on cancel

3. Features:
   - Modal titles
   - Form inputs within modals
   - Notification feedback
   - Button-triggered modal displays
   - Different modal closing behaviors

To run the app:
1. Save the code in a file (e.g., `app.py`)
2. Install required packages: `pip install shiny`
3. Run with: `shiny run app.py`

The app demonstrates all parameters of `modal_remove()`:
- `session=None` (default) - The session is automatically inferred
- The function is called in various contexts showing its flexibility

Note that while `modal_remove()` itself has minimal parameters, this example shows its use in different scenarios and with various modal configurations.

The app includes:
- Multiple modal types
- Different closing behaviors
- Form handling
- Notifications
- Status display
- Various button triggers
- Layout management

This provides a comprehensive demonstration of modal management in a Shiny for Python app using express mode.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMpwR6KAHM4yUnQpclYFSxxfOAB9QIpWAAopCgAbOABeOTAAWVJbKGTkACU4GFJZZAAREtJMojpOZOSoACNUtIAVBhM4AEonCFcAYTEoKmRmswoQ5CmVUgB3ZFtOOjoHahEKXHQ4PVI6ZFK85NCIec4KdmRwptxSMyiyZJMYCCj5hgx4nsQFZH-rpwsMYHhJgm8JhQphB4pkOAsos0oKxOMRashMm52AtkAAhZGo5A5Y7o4hNXRRDJgGAAWgATJk+hAAYDgRBTBQomDOOREZNyLCwPD5o9mOhUhp0ZjsYtBmKJUTcvlSeTWJTMrSGWAmSzwiDOdzeZDoYLhVE6EIYFKwFicQAxS2KkmEZBk5Fqqmaxn9IYjMZQJacVjiqC8KAjZAWhhsCijEx6eC6SKnAACNnsDCwlgU9gOrFjFHjUWWwdu31+zIB4WW0lhlZZ-0xBfjh12rGTyHOjWQGB24eQ7HWtT+Df+nFsVPzcbV4fEw-rDbdFKp6BpAGZDvTxkIM6J7nY4LZMiP-kyXMgABJQOypaNR8YE4iHJXJBRp8SSGRwdSrOCSN8jJ+sjqLIlDxPqWBmkiKLEEyuZzCK0GolERz5OWJ7PscyBpKyqHJHWo6NmA7RcHoQY9g+MGYfkMzsKMnYNAUzT+GIpSyLYPZmMwoyovkyS4POhEzBcbSZPiVHEsqhAYSy4isLgjzJKQrDpJ03QYTqVZAnhUTCvEeFngMl7XrYt6RkIrrypo1EFOclyHNeJg0axZTKhA77csBcC-v+7mAVIXmgRQ4HsmYkEyqKAgSnB3kIZF4qaChL7oQueHYbhyUyVpbIclEVAaMFmTQPA1oAKKUA4yB3CY0bFfI2oEFl-x6qFnIQC8DiooKkRlRV0bVdGPUutI+TdGkdIAKw9I1C66kCtz3JyTwvG8HxfE1DYtblhoQvyMIai+jzXsQcCvi6mSDMdp0qu66pgM0FAQDSeQQH4jgNRtc05aCn5Gntgo6awJjNDAFzWm4wOgxQN3LpkD1PUDxAnbo3qzQC00bUkolgHKUXWZJZ0zUJckKWSynpHa+QqRpGHhIDMr6S+hmuFeN6VfeUYsHhAEfgF37eWsvkeUB-NBSFHLhQinMxXmEWc0lxwpSyaU4XTmVo81QL6rpp1-oVGsNpkxDYqi9VE0JAKYrrkg9sysQ8hAgkW-8xukKbrBpMAmQAPJBA7yAAILWr74J4sHfvkMggyZAAuhtGMG1tDz5QaIwEc7GJgGQMDwJQoTSQbLKZAHtjLOCNG47ncRO87I3POkmTlVQ-X3NG2dV3og5iFgPfHgbCdCTcoaLaKzyvO8nzoOnztJwav27VCAqZPLxBXYTmeXRAJ3r0uHpw49NIqWQdjhgJH2F9l2s7Xyi-7WA8tAyDYPnTakPP0Qu93fDNLaPwp+o0JAehEsYNzAA6BgLACY1wbCTRS5M0iUxOPIBcmlNZYHpgsRmxxmbGTZgwPQ940o7VTP5L8P5BbQz8rzMhcAxYQR0qvLep0ZYDhMqkBW+QjpMPwj8Wm2lDouVkN8PhWAICkCkPUVe4JdIMwulZDQNlXRr1SEeF0WwdhUnmOGCA3AfCox5p5fmPlKHCz5iBDY4swqAzfhQFhdE2YcOSLpGxStso6UEXAYRC5whiIkbxaRekNp0ExDYqgtgUAADlYDpBABBOq3wAC+RAA5+DSLE1qWBIiJOgSydRoDEztj8H3FkhlTE0OMQYkW5iwIQRXmvOxbDoh1O4a4tB7jqhCNQayXxKx-EOxkZgzI4CWCMO3io9EeTNHaN0foqhhjyF60qWY2hFjamWmcU-WxOZYr2NMk09Zj8oatIyscKIHivFfR6ZInivJAkG2CWAx0hyLhhJQIME2J00kQVdqbRJRBK4bA9ukiW7dAXZILkJSZGo2xDQ0mAJJyBwB1VoGAMQABHSwrFAVYAoAVF0WdyBUBoCgMACgYCjHFOI5InBmgKHagIAS7ITLIn6BnVACSY5AA)
