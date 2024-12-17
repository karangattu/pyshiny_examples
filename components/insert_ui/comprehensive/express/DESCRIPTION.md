This app demonstrates the key features of `insert_ui`:

1. **Selector Options**: 
   - Users can choose between two different selectors (`#target_div` and `#button_container`)
   
2. **Insertion Location**:
   - Supports all four insertion locations: 
     - `beforeBegin`: Before the selected element
     - `afterBegin`: Inside the selected element, before its first child
     - `beforeEnd`: Inside the selected element, after its last child
     - `afterEnd`: After the selected element

3. **Multiple Insertion**:
   - Toggle between single and multiple insertions
   
4. **Immediate vs Deferred Insertion**:
   - Default is `immediate=False`, which means insertions are deferred until after all reactive processing

5. **Dynamic UI Generation**:
   - Generates random synthetic data for insertion
   - Tracks inserted elements
   - Allows removal of the last inserted element

Features demonstrated:
- `insert_ui` parameters: `selector`, `where`, `multiple`, `immediate`
- Reactive tracking of inserted elements
- Dynamic UI generation
- Error handling and state management

When you run this app, you'll be able to:
- Insert UI elements at different locations
- Choose different target selectors
- Toggle between single and multiple insertions
- Remove the last inserted element
- See a list of currently inserted elements

The app provides an interactive way to explore the capabilities of `insert_ui` in Shiny for Python.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzhExEACZwGAHQiNmbLjyxwAHujGtWfAUJHd0AVwpFrndf0HDRUJcyfnXrCg24A5urqAMTIAMq4lOxwUsTIilAUUMgB1CpJnOTqynSp6QxJcAD6hR4wxb7+EAEAFAA21AEU7AC8AKwAlIjqyH2isdYMEMgA5KNYAFak3LVlisxYxOwzxHCstVWBWFCsxJycxdaYKsS7cMgA1Gx+24qcAZwUrEQA1q2NNS2dncFKcHk0hAMlRKrB0I1iolkrUINYKk84DBWK0AIwABm6vX6YgoQxGwGx-X6ICJxPJo04ilGKCBIJK82YlVuNVqnQIZPJ-VG0HgNOQdFUYAAklQWCBOJdUQBfIUckZcinSKD1axwflMaxKObuBYwLBazh0IQwWoYogYzFEABMvwVXOlAqEfD4IzKaVh8OKiORduJAF0-mEAIKYZAAFSejWQuuQAAUoGlkAB5dBScisdQOHCJkqkNMbKQURqtIXcVgqChHTjIAAiSIzfky2UIAs49XqUAARiXwww1XbQhEqXAu1AGMgAO5PdjIMiUJj1TMQactZDZ1gjscMNk9e3rzhYKy2UpQe6kYpd2wUDO1Tn9IWTmJiOXIe99IXCiAV4RZEYAGVIM50wgV932QQkwC7AEhDgAAhOBHlA1shSgOgqAYBCkLAqCYLEABRJQcLQjDCMUIVA33P0H33bNjyrQpz0va9b3AoUK0aSQhDA-diSFcI4E4m8J3Dcc0goHjFQgoUQmSBhxKhGQcJCK8KBvCBinnZJuBUCiyWoj9aMPejNJiYhXi7Uh9DvMAYGseopAhOAcIAWXsxzoy-H8QNfZVVTgVoADEVQrAy3yMo8IBsKsJBA5i1PIGzy0rS8KGQohP2-StkAAVWFIUwrJOiopPWK-3i9SbLEGBSFkVL0rfMAACUG1kZB-12EQvMrOByLAQcIDCFyoG4OdyCoSgYzEKB1FXWds07XBSBPMhVRgb9dzJMJRPk2IEhkJ0J2S38MyKw97mkWoqVLMA5IUi7X18XASyFSyGGUBgUGtdB9DYUh6ipZAezVABuZAYG4ABaGIHnYCgvvRdEfpBySpI-MAdvEusDuNCdupO78CrJLbkDgliRi0kbgQnXGYwclRoCkNrjpA5diWzC6rsUG7VPUzTxqp3TWyel6oKED6vp+v6AcUVIxGoMGIYgaG4Fh+HkEtZHUbRoUyYSkYAGEBZ0tR+qDZAWrKtq-LVZAbztwpzNdbzeuQQSkWoZ4nCy4ReuKd34EoUxWgGK24CwG24FqYB-QGsJ8ZEPLkHwug6DgSR1AAAWmyQZHDgE04ziBs-EXPZD0WRKCukqKEi7z6rtXJkGKTb9zCABxAoijYcFo2hGb91YXuSn75AQ7pQpQSHgRIX72oAGY+DyeisDshzOCctk3aXC5UUK-daZ9V0e5nkekigPcpLCA3pqoGN9ukKcZztmI+DFUZTG4XGYGbUDeP6YEk5FKPxDhzGQd5-5ckFCKWsKAJRimAJSak-ppREAAHKwDgHAn0iDeTqhQUQAAaiqNU2CEGjEjqMFBcpwLEmutAlmft4FIkQVSKhspCC0P6CLAKr0JCvACJqJQkNVpCBQADAIcNcCCXqKQScisxLcBQO0ZGyB0BnnuDUFAGItZgHAmFPikDkDxx9onYUT81yKCiLATg8R1GFHgBhNmipir1wcBAtGAC4BAIuvKTxfQOLp2Eq0FegSuI7nZFwvoT4VABRXjEsQbI-H+LXh5OJNdV7uQ3o0JJUSzDwHuEUIKIULjGLrACKA7kgZwHYFAaQWQ1BGIMTRK+EZHavGdj1WWAdPbOK5MQIYCgqw9KDmPTpvtFD+0aIHZ4WBxJbyNOMqgkyRmzM4KwSosQt6CQrBBSiUkBkMCGVMj2QcdgnG1Aw0xTCcFIPYUTIxjCVnTN6VgCsFBaiHOOas1gccLatQuEnFOhcJLFxzkzfOqcglZ3BXnCuntq7RSwNVWqJQuxpUbgCZurc6HL2uc805ayNnvK3rGJ5JyZmsDmVsrERjOy+ApZ7b0ssQ7kp+dSj5nRgCQ1RPslxh4UV1XcdAkIIB6XDJeZQZlHDmmGVaTldA0ILgtGVe012PzwJfKZT8sZbLJWzPmbKucgztX6qpYIdAbJwJ6sJVSklWqpU-M6EvY1RzTW2u3rsm1lKDRZU5ebWs6yIRQF4A64svAnnb1tTC6gH0sBUH0KCpuHA5HenxTi-oizvWvPWZszll9FS4nxAKIUBsTWUHqLwBOrt8JmrgaMIgExpizGzWcw1nQOFkiLcMRqaDSBRspUs120iJJgDAKg5A4A8G0DAGIAAjg4aqryKCJtbGALSnsZ3qB-hQCEpBiycC7OoOEAhcDqHUUoXYfx-GoGlP6IAA)
