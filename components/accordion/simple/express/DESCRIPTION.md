This app demonstrates several key features:

1. Uses `ui.accordion()` with `multiple=True` to allow multiple panels to be open simultaneously
2. Creates accordion panels dynamically from a dictionary of course data
3. Uses `ui.markdown()` to format the content within each accordion panel
4. Includes a reactive text output that shows which courses are currently expanded
5. Uses synthetic data instead of external files
6. Follows Shiny for Python express mode conventions

Key points from the documentation used:
- `ui.accordion(id="course_accordion", multiple=True)` allows multiple panels to be open
- `ui.accordion_panel()` creates individual panels within the accordion
- `input.course_accordion()` provides the currently expanded panel values

When you run this app, you'll see:
- An accordion with three course descriptions
- The ability to expand/collapse multiple courses
- A dynamic text display showing which courses are currently expanded

The app showcases how to use accordions in a clean, interactive way, demonstrating both the UI creation and reactive capabilities of Shiny for Python.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMq5K7OFOLJbUBRQyHRC-nAw5KwUDIGc5ApkJgyscAD6AUHIALzIIArIhchyYAAKuBTs5MilTADmsTAw3HUlKPkQRV3FYPasxAyc6FIJtCUAgshkAmLeEKwycFOkyanLsoMQdTUVVZ10Jnaw1EEANnpQdshQttKXxHC2yBSk6JzErFglBAXdhSW2ZJxUYoEoARgATMgAO5wOAAa1Y31+fwBnDodHeJlOFFwbR6AElKA54LZOIF5GAUcgAL4-TpFEoAEUCwTcxE41AeyAAQqRSBRiLB0PiOn9-r04P1BsN4hB8SUADLiBidTLBfqciDcpQsaWBYjsZAmBZbHaVchEdCXAKsIg25AwCSqJanFUQFrIU6cABGsUGUq+hGpXQBQJG8rGYDBADYYXDEd9igzUb10ZjiNjcQqwONbvdHiVqXTqSUAOpwH3IJlwWSnV7wSgwziVasAK0udVIopDjMl0qGEZzPMspyeB1OpwAtNEJPD41WMOhvUKI3oTZ7yhbOg7KksmR2tqQQo04NChPCg-TxT1AbEh1GwQAGeMIpHBlPdNEYrE4vFRokqAYUlySoItPxpBRIPlCBXDcHxkGtOolleNcFEsHAoGQtJUNYAAKKQKDdbISgAYRWFIllI1l61aQgQk4ScoB9YiABUGBMOAAEonFg5BSLEClrh3YgyAYMlqhefxOFYZcoF4JJKL4RQhCdIcIGhFsjQwiQxIkiA8M4WwSLARTUjSXShH0pMYCzIY2I47jEGpUIGGWVZ0mgeAiHsIJGL0bh3MojJWSwFsInwrjnM-LpNNbHTRKsuU0mtCA4FOPCzM844ot7P4MKdBh4VsUhoQMugiypKkYvFZw6ryLK0i8uBoJvUMar+AAqTqawHWVyEQbq8l8qB-OAAByPoBkHOVxoAXVatr-g67op2QbqmXDOVBs64afFG84JrvYEIHmxalrWjb01-XFkGVOsdr2vzDsm67Mz-M68q-KqSh4mDXDzJ4NTgSQ5WeY8OFKmEuENILUguMQpmSGwiN4TRUvsWx0M4LB2AAFjwsjkZOU5eAAUS0G1Hn4ij4ecsA-oUAABGx7AYLAqA0CgFHsOgVFKtJ0ap2w0iyyLoq6IW7EeUXaalHJlNMCgsEayzxLlPC-q6dFkAgAVkClzHZY81gJfFMQKGSToSgAOWPMXrkRzMGBR0mDcp6XbCDakLatkISgpjHqbF9pxqIcasDbUhuDww2ZbFrjILAMA6TySBjloMAxAAR0sMRGwoT4KC5+jTPIKgaBQaq1OXAVvR9BQIBMAQ8QgDGoCRGClsKFO5qAA)