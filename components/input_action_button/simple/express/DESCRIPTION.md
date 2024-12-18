1. Creating action buttons with different styling using `input_action_button()`
2. Tracking button clicks using the input values
3. Using `@reactive.effect` and `@reactive.event` to respond to button clicks
4. Using `reactive.value()` to store and update data
5. Displaying reactive values using `@render.text`

The app includes:

- Two action buttons - one to increment a value and one to reset
- Display of click counts for both buttons
- A reactive value that increases by 10 when button 1 is clicked
- Reset functionality when button 2 is clicked
- Real-time display of the current value

The app follows Shiny for Python express mode conventions and best practices by:

1. Using express imports (`from shiny.express import input, ui, render`)
2. Not using external files for data
3. Properly using reactive programming patterns
4. Following correct decorator syntax
5. Using appropriate UI components

When you run this app:
- The first button will increment the value by 10 each time it's clicked
- The second button resets the value back to 100
- You'll see both the click counts and current value update in real-time
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMpwR6KAHM4yKQoAG3kISxxfOAB9UnQKVgAKQJCAXjkwAEFJTnJkACEzClyAETgYUnSASicIVwBhMSgqZAkpXIAjQvJWBXDjMyjWnIgozooiiAT09ooIAEZ0onS6oM5iAGtkeABCReRiIKhdKLSwGYgAWm1+KAZeeAuAJirezix+ikHs8lGuyenZs9CMh0gAlOCsTx7A5HVgnAGXADutwg3B8LwgLmQxU4rHQh14BzWmzIJkoPQgAAEbPYGFgqBoKAp7HR9qsNlFSZQ5glKogFMhBaJPCYGBBkHR0gVxrk5sh2EdkO04NQ2cS4LZkCAPlhzjzKgBfAL8CHpGrU6i0+maEQguxwVlEjlciiPXn88VCsQUUXiyVgaUTZCPeWK5Wqp3rDVanXnN2G43wHpgGr1RrNKDCoayZDSKBBEz+IpsIpiNjMfy2JpQZnV5ApLPZWRYPMFuAJOYABk71UxtWQ4MhIirFEziPYqrGQZDuLVGw1Cgt2bg6jodDgkkXjSbK7gskoCVjgN7LOQUXdAqFI6gWCHHe7vaxAFV0CPK3Xx5O-sg5bPIwuqW3KRmwdddN0A8Qd3UfcKEPCBTAoXVZjmSo7VPc8+UvQViFFGwRAba8sD8WDeyFZBCLvHCGDw5AAGofx7VNsVxfEoF4CgJ32XDqGHOtW0LLdLQca1GWZB0uOonion49tMM9QVvV9CVlm4yhc3zQsUBAQjiN5A10jAA0iHAaB4FoMAxAAR0sMR4HJelGWBMAyEoHjzIUGAmnxUhgk4doFDCARcAUbw7COGoyMioVDIAXSAA)
