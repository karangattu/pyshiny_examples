### Key Features and Demonstrations:

1. **Modal Types**:
   - Basic Modal
   - Modal with Footer
   - Large Modal
   - Modal with Easy Close
   - Modal with Custom Content

2. **Parameters Demonstrated**:
   - `title`: Sets the modal's title
   - `size`: Controls modal size ('s', 'm', 'l')
   - `fade`: Toggles fade-in animation
   - `easy_close`: Allows closing by clicking outside or pressing ESC
   - `footer`: Adds custom footer content

3. **Interactive Elements**:
   - Radio button to select modal type
   - Checkbox to toggle fade effect
   - Action button to trigger modal display

4. **Data Generation**:
   - Synthetic employee dataset
   - Random employee selection for custom content modal

### Best Practices Demonstrated:
- Use of `@reactive.effect` and `@reactive.event`
- Synthetic data generation
- Dynamic modal content
- Multiple modal configuration options

### Execution Instructions:
1. Ensure Shiny for Python is installed (`pip install shiny`)
2. Copy the code into a Python file (e.g., `modal_showcase.py`)
3. Run the file with Python

This app provides a comprehensive showcase of `ui.modal_show()` functionality, allowing users to explore different modal configurations interactively.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROcF-QcNFQIAE2bWDd9A8dQ935OkeutiIQJgK8vhDoCkosXlRS8PpByHFwCXBE6Y5wADYUUAoKAMTIAMq4lOxpnMTIACJQ+cgA4tRwDI2c5AqRWB1OzFiscHCOABQALABMAJQ9sHB6ALzIwHJgAII5NfKEyOsAQqQARutE6wDC7FAM27vnYA3SnAF76wCismf7YABi-QBrb7rZodYj3H4ACWoDFw6wAugpsh5hPBKMtVutSlAcotgWAALI3AHVCAAc3x73J3BGDG4FLef24DnB+MhACUEYUIHABDlSLgRgB9OJQZArfxYBr5f4LMYgBTIJXIADkADkFiqUNB4KwCIrlSq6nAURQ0RQtchev1nDAsMR2KQdmNkTczdQKHrkLiIGMdYsZjN9RBlarsTkbrhLdbPIMbdwKGMAKwABjTKaIAEZU+miD6-QtWIHg6GVZDOGJ6o04JbgKl0lgIKQAO5jGbIAC0yCyuXyLqguFYSxtcc8CbGmbTRAAzOnA8g6EJkEK+CH-axERAAL5zCDFZAABSgZLgZTSJiiIU4OGPcCFpHQnrGUgouKW6wJpC8OTKjubxG8CE6E4HII2ON8ABUGBMOBd33UoXjgY4bmQZtOAodhkE-b9kAASUodoJCkchkAucgKCYHJWAUNCMOQSwhkQ5CGDbRADSVBjjDMIUOkcLohWOMwKHIVgxnY0MfhgL8cSFChcHQCFxNDD9pJ-CD5MUkMJKVNYtO05SwAObwaiw1TgT0-SlRUnDaMw35SFIKgGHMyyDIAGRuE9TO-FzXKswlVNQ9DMPebxeAuflhl8vzrJxIK6IuExWGElgyIIyh1iU5VN1DXdQ04yJuIdOBiABY5SA0MSwDoKBsiFOA6DoEqKHxX5atPd5Gua75pBxGCligmC4IgEoiW4UjyI9ZANjEAoIFs+jrwAhhxhmNiLIY5bHCFKp2pY2Kf2NKSIGSjpiL3MA8uVArTAoIUiK6CABKE8gqo4FshSknzGVKP9vJxdZhtGwL2WobI6XJZA3NIMkagUAABWbJBkOB1C6yQEaRqRZHUWRKDGLiKCGP9PtU3dsjoZdWPEko6k4LqxEof61I0vRkOGRxkBI9laq6ZADhekNSlyZrHvE+nV1urAvpkuSFLbcUVkOYzamwgGkCypUWBWBiZZyMSLMs9YIK4PROB8ZB2ZMvX4sw1gbFxZAyHSomzk1iSXzfZX7dVszCHd0MauyJZCawIO7waprJDbd2ru03XVKFd7WxgYbQ1yCXQ712SNIVpYlYCmzguQezHPadZ1ss7XFul1SDb8-yTfN5AbeyY7TurPRFzLhgFxMCBkfIHF0NwLA3cN-TPbgd9C7ihbS6c8eG4XBynKWBPv2eihhN9S5It2IMA+VcOQ8Konw-q9HEzjiSb-y69s+TsZU+5dPtkprPE7luA84LjyGC8mrHIFd3bVw3jieuDdjamz4BbCMADTw22TgBe2kMMKnntgAL1PCiBYTkx7+wntpKeM9-6AL9iWBuWDp7rGAXsZAJQyEYM4Ngo+SoT6hwvpHZqMciHIDvtdB+icn4vz3BZDOH8z6103t-X+PwgG22QKFVg4V94gL4WAoR35IExTAE3PQNsAIhmOKeYg+9ObHF4GYmoAJ6RczMPbbIXNe7aEWKgskSjSgXAIZQvyJCPhhVIvvZmS8G7iBUUKMxpBhgDWghkNhC52qnyllwq+vDLICI4lomSIi07KgkZLMw0jZa53bPneRgUFqJWSsoNKVAMoaz4SUHmAwYA5F4MMXEkhkAOGQLydA-JBSnkXL3NuIkKKdG6Hw-pgyRjij6XyAUwpRRDFgAMn+mYZhYBAqQYgwAUw5X0qA+Z4D9YJIYvkMkrAsB8WkDo5eNdLnXPYNOMYdAPiLKGfUNIUAQKsBQCAGZSy4DAHVJqeEW5Aa+IeRc481z0BvPWMaU05oAVAqGaC5FbpzQqghVChJ98sBPJwIisA4ZIwoAACSAs+SMUF5LYS4sQAQSFl1oXL1hVckl7ywDlkrNKOAaLaUgrLBWU8ArcVDAonQdIYwVQAFIACaHZ5UwBVY4FUMxWWZNvuyye6EvZgHeMKvCighAwEmRdPV2lqEzxgKEvyHCpGpKjtfa1Elu5r1OVvHeVUIrRIPrHd23rcnchKAAeUfI9HEKA6asAGQOJ2JgGCMxEDbb+bARaDzEYjcQyMcbcIxk4BqVM1riQYk2KQwEALnSTn+e5gcsRZqoJzBR6kFIAs-jI0prL3WOGTZapYUx3XfztW428mULIzDAFuIg4B-S0DAGIAAjpYMQ5prkUA0BQPYYBnb1J3SgMACgLUUAGY5bYpwIAhDCAoDwThvCvwbjO+EQA)
