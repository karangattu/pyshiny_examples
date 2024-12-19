This app demonstrates several key features:

1. Uses `panel_absolute` to create two floating panels:
   - A draggable controls panel in the top-right corner
   - An info message panel in the bottom-left corner

2. The controls panel contains:
   - A slider to control how many rows of data to display
   - A switch to toggle date column visibility

3. The main content area shows a data table that responds to the controls

4. The panels stay in their fixed positions relative to the viewport

To run this app, simply save it as a .py file and run it with `shiny run app.py`.

Key technical points:
- Uses express mode syntax for cleaner code
- Properly handles reactive updates
- Uses `draggable=True` to allow user interaction with the control panel
- Demonstrates positioning with `top`, `right`, `bottom`, `left` attributes
- Shows how to nest cards within absolute panels

The app is self-contained and doesn't require any external files since it generates its own sample data.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBf0HDk6KHah6vb204OuECYCvD4Q6AoKAMTIALJQANZwyCbobMzJrLDoADbJtlAUUAoFRcgAvL5YACKFUABiDLBwABQgCsidyADkpXDdKOi2WH0A+k0QAOatrEXC5d0ATAAMiwAsALTLAIxb291E6A6cpLas5dvLAJQEHV3d0lA5Jv0o4VgTtsxYEEIwTy1LssiJcQdcFABfK6RCAxAAKUGmyFI6Ck5FYCksOERcFGKIorBaUgoeXKcjACIgcByyAAggAjVikZ5UZDVOAwUjkoh0Tg5HJQemkgAqDBe0Ig0TiUG4yDIlGoFAUAHdOBR2ClOFhiFAGLYWldEHdOlidXrRuxxPYGC1yfFZQBhchUSh0sTFMASrrIY3IAACNmtWCKQvkEG99joyFKUFGIbyBqN4e9XVsUcqMe1KNwBt93s4Ud+RnCZiwHFIytGfUJhrzKc6aYq0boIyY6BavUK-SIUA0nHO2y99dEcAoJgY4bTWEtUH1xlLEHGFZrEql9RypEK3Embg81OQqvVcudTByGIgh41WPcVJyo0FTJZrV9DE4k3YFDJYBW6A03N9FAol+P5-oQvqqrY6rAcsyy-v+yYNk0kyTIKIpimGtYIQeapXlqZr6phw6atquq2BaVoOLaYBOpQp4Yp6dYmlq84UKMrA5Jw1q2lhRHkouTDKvRtw8cO5IAHLBPSDjIlGABKy7wUR3owNwFzCUpXT-BoFzAoxKaPM8cDlAArHpQ71liLFsYexDsFR5aVtW3I+mAADK7AVmyXZCcgorijCMS0rYtjIFAyB0BuW5THwiikMg9KkBooUiOqyQJRQgEwCqOHETe1L3oyzJmM+WF5HQn7kiBildOlmXQXBYFYRBUHkgAzDBDUKIRXSXsR+GJnp5JyCYtgABytX4I06tsbJIcgqXHrRzJ6HlNK6qQJh2PNlpsMQYjUAAhENIlMVg9I2uZKbksKO2rXoqr8mwRS8LyGhwCFYgClIsjzXFC3SJwcDKi4FBYOSYAQkQ4DQPAtBgGIACOlhiPAlCsMGGgUIQJDOoqcMKP8FC5KQJKcPSChBCECg3gU556d6EMALpAA)
