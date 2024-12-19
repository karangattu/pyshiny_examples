1. A counter using reactive.value() to track number of elements
2. An action button that triggers UI insertion 
3. A container div where new elements are inserted
4. A reactive effect that:
   - Increments the counter
   - Inserts a new div containing text and a button
   - Uses insert_ui() to add elements to the container

Installation and execution:
1. Requirements:
   ```
   pip install shiny
   ```

2. Run with:
   ```
   shiny run app.py
   ```

The app shows how to:
- Dynamically add UI elements in response to user actions
- Track state with reactive values
- Use insert_ui() to modify the DOM
- Structure event handling with reactive.effect
- Create nested UI elements with ui.div()

The app demonstrates a simple but complete example of dynamic UI manipulation in Shiny for Python using the express syntax mode.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMJioVZFDb90ADZwyGQmlA7IFKSRDBIA1sgQJjAARhGkdMhwQfCUelC29rYKoeEMyAC8ouKSMnBY0lABJnAAFAAMAJROEK4AgoU+teTIKWZREJHRFAycAOZzEQCqAJJ8EKwOUuQKlljGZgD6EtsQh2MUE61yaIU3RDcDtsiryACiOdQUN90QLshPELkChQbgRWwyZAAd3YDmC2TguQoeihnACAVGwW4m2EcGKSU4WAh0lanFsFRuZEooIgDh+PQAAp5arJ1HQ6HBJAomTUpKy4LJKKSIKYKFgCrZfvZMhLDgika1OogFMhVcg5gFSCkmkCwlRHJM1aURFVjQ4sIsKIrkABqZAARhVRtIevNmytxt+auQTtVrhWGy2PkScChyGJ0M4FHYkU0IigdlG4x2htVe2xW0Olmuqe9yD2xJzeeLyDoNw+iK+yBAxoAvvdfSW04SDhRjsMzhcrmWwCkKGcay7KPXCD6wG4ApxiAl4ABCH4ERtN4gBKC6Q4UsAwCgAWgAzMh0PvRkJ7OUmGEijcl2rOovc97NkFJEJN84qSCwY5CDfVTC4ZuaR0EIcBvHY165p0YC1kQ4DQPAtBgGIACOlhiEirBYBQGgUKOYAfl8iEKDAXiBKQFCTikChJAIuAKOgCa2GuPRNt60EALpAA)
