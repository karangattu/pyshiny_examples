This app demonstrates several key aspects of using `update_numeric()`:

1. It starts with an initial numeric input with a base value of 50
2. Three buttons allow different interactions:
   - "Double the Number" multiplies the current value by 2 (up to 100)
   - "Halve the Number" divides the current value by 2 (down to 0)
   - "Reset to Original" sets the value back to 50

The app follows the Shiny for Python express mode guidelines:
- Uses `@reactive.effect` and `@reactive.event` for button interactions
- Uses `ui.update_numeric()` to modify the input dynamically
- Follows the function reference documentation for `update_numeric()`
- Includes error prevention by using `min()` and `max()` to stay within input bounds

Key points from the function reference:
- The syntax is similar to the original input creation
- Only arguments with non-None values will be updated
- Can update value, label, min, max, and step
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzhExEACZwGAHQiNmbLjyxwAHujGtWfAUJHd0AVwpFrndeoDEyAMJioVZFGQBlHV4MdGQKdi9kZRhyVgoGLzhTa3RFBIB9CGt4Bk5iAAoASnUHHCgAczg00nQKVjypCgAbOABeVTAAVRSE5AA5LJVc5ABJCBsRABE4aPaiiBd-TmUAIygGZAB3TjDkMkomRtZ1LZ2S1iW4VYZCxHVke+RXUe3OKEbkTOyhq1s7h5KfhQMgMcvl2qtWJVPssVO0iO0AEJQSF9LIwtSEZDSN7WVoAVgADEQYNwWkTkDAoPoWgBGAkEuYPZB-e6uBG2CgxUKkCmkRScOi8MJwD4g75jX4QJkAiVAiRSchpZYc8h5dqKUjWZbNJUUeaY9oTTXakXC1EwdGzFnIGXjNLyziK5UUTkQNVgcKNWS6-XwsAACTeslC7BF-QtsLAjP+nCwgPtkkdECVKrd7WMcCByz1cOZYAASolM9zkAB5HJlbhvK3zCCuCacVjoRpQIWh3bWBgKETYxq49QAAU8idkejodDgkkHw6ko7gskoeUBWA1Wp12Ygc2UdGQaRu1vrxuaIZF0JURGorE73DKfBEGsSEAA5CIDMQ4HBFBSqdaIHANmkva4sgLQUtwS6ylgEJQmiKiFMgABUyAAExEHSDLWiUySpFQwJfGCYDQXhlqYkBrR-gBZFzNO4gjnAY4TlOEBDrRs70fO1AUBB4xYJ63oblucA7nuBS3FKDyuIGXqmu2Z4MBeEBXjkEC3tskSkI+L7IGUPIwo0pAbGBtZMhRgE4iKoGUvo3G2FByIwRG1wFMgAD0LkoUQGHifcWHdLhnyDARRFybmZEtKZVFOMxM4yOx46ThQNEOnOC5ccuGZZnqgnCfu3mPMghaQiInInsgQicJW0DvGRmGxth6QBaC7rBbBGJEGFhLUXWyANk2LZtiKxCdt2WLmTRSgqFgVD6IlE07hwBlpENXacWZfZwLlTJiBQnZSnQ7RuMNnHmuiKAgMuLWOYUAC+7RgNdRDgNA8C0GAYgAI4OGI8CUKwU0zZiYB7FQNAoGA6iUhQzakE0nDLOonx4Oo6BQEoyJRUymMPPdAC6QA)
