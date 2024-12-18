1. Uses express mode syntax for cleaner code
2. Shows proper button state handling (disabled while task running)
3. Includes cancel functionality
4. Demonstrates error handling
5. Shows task status and results
6. Uses async/await for non-blocking operation

The app allows users to:

1. Select number of simulations to run
2. Start simulations with a task button that disables while running
3. Cancel running simulations
4. See current status and results
5. Experience occasional random failures to demonstrate error handling

Key technical details:

1. Uses `@reactive.extended_task` for long-running async computation
2. Binds task to button with `@ui.bind_task_button`
3. Uses `reactive.event` to handle button clicks
4. Shows task status with `compute.running()` and `compute.complete()`
5. Gets results with `compute.result()`

The app creates synthetic data by simulating work with random delays, rather than loading external files.

To run this app, just save it as `app.py` and run with:

```bash
shiny run app.py
```

Required packages:
- shiny
- asyncio (standard library)
- random (standard library)
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkTEQAJnAZETnBQoc4oAczgB9UugqsAFFIUADZwALxyYAAqUKwA1sgAQmYU5MgAInAwpJFEdJzBwVAARqFhUQwmcACUThAA7pwU7MguRbikZp6snDbFUAz+1YgKyGPIjc2tnFg9fQNDIxDjK9NYxl0QJvAMnMT+kRC5yJEActvFtsikdGz8JkVS5KzHAIwADJ9EMNxhH+-fKAaP6fT61ZarMYuDYUTwUWJxTzFFLkA5gSpHQgnMAAJRMywAyvdHpxnsdiEVdJ4ImBihQIABabT8Aa4SLgyFQmYwzwSJ4QJEoiBo4hQCDEODBY6RADCYolUqxFNirGpkTpjKsYo8DHZdRWkxaLlFDCsi1GnONAysnnY4hsg0iRJgDyg-OQOLgrAefj1EMhFshAAFLA6sFQNBRA6sbLdWPCKCYAsNo5y+LcIKQRGQBGY4FgMRBuG5zf606sxImGMtIp6oFZeKlRPi7i6SWSwKnOZWTNXkHRa-iixA3MgQDCsMLqgBfVuu-msLBLyJdgNllYh6hhiMiVfIWOiL0+0vl8acW450xULCX0JUE+nitwKvLAdgGXMdB3uBWMeXvMFkewQUEMs49G2bqkhALyduu3bPr2NadrBCibnyMj5nAdB0HAkioWI6GyOosiUP4E4YuCB6eA+Yz-veE5Thy4z4eIkgYeo2G4VGEBoWxRFwCRIETqK4qStUYwKFRNHIHR+YiQqQx1EGLjFNwNrwvEgoUKkwrItp5CeL0NIYn6vFSPxkZbj+cIIgosS4OK+5YTJn55v4EAoNwFDiQyAB8fCUEsKz8IIwjIPZ4qktGIWGKIYpWMw0bRgAxMgzrznAbDMJl9RCHE0Z0EIfABXFI5wO5KZwWM56lQlMAFvFzBDMgAA8yDvFgnyvCgyCpR1rwAKQyew8qZTc-ZQAUvbyFVFaTawmUAKIaBKvhQWiOKNSw4HzlBE1TWIACEfpplA9STSIEXEKSsyhHA6D+B1XVMWuKw9n2EBgNORDgNA8C0OicAAI4OGI8CUIuFCRliYBkJQ1AUADCgwG6X5ZsEnDFAoWwCGyEDoPFsT6o+X0ALpAA)
