This app demonstrates all the parameters of `update_action_button`:
1. `id`: The target button ID ("target_btn")
2. `label`: Updated through the text input
3. `icon`: Toggled between a star and heart icon based on click count
4. `disabled`: Controlled through a switch input

Features of the app:
1. A sidebar with controls to modify the button
2. A main area showing the target button and its click count
3. Visual feedback through notifications when updates are applied
4. Font Awesome icons for visual enhancement
5. Bootstrap styling for better appearance

The app uses:
- `ui.layout_sidebar()` for layout
- `ui.card()` for content organization
- Reactive programming with `@reactive.effect` and `@reactive.event`
- Font Awesome icons through CDN
- Bootstrap classes for styling

Installation and execution:
1. Install required packages:
```bash
pip install shiny
```

2. Save the code in a file (e.g., `app.py`)
3. Run with:
```bash
shiny run app.py
```

Package dependencies:
- shiny

The app demonstrates all parameters of `update_action_button` in an interactive way, allowing users to:
- Change the button's label
- Enable/disable the button
- See the button's click count
- Watch icons change based on interactions
- Receive visual feedback through notifications
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQss4oAczgB9UugqsAFFIUADZwALxyYACCkpzkyABCZhTxAKrotlBUyAAicDCkkUR0nMHBUABGoWEAKgwmcACUThAAxMgAwmJZcMhQyOW4pGbIAO6cFOx9bJz2FVCOEOOTyC6DwxSerLNw8wz+jYgKyCdjE1Mu23MLB0cQpw+rnFjsACz+kR3kFEzByAAKUAgcGCkWa90eJxcxjMnioGgoH0gcFGnnKFRBRWQkQAcijEsl4gAZSqYwjIaRQYINCJgDrBTjEADWyHgAEIwcdIU8sDDNqxlsR2EjbJxWJVQp4KoSIFjIjkxRLekkKClZeTKdTwgAxKmsJpcyHQiCmTYSKTkKUypEmDI9KUUdVESLpTLZFVq5AAZTgqu4blYWOI5V0nlpFUdAFptPwFrhORCjc92PtwdyeTAFkzbKRRhAkZFC4nHq1SwCFrBfQ49HkChBWD8erY7unI8gAFTt9EgzsoDrsIEeZDS1XxeEUQ2PNudxnkXvIKK2WwAejEBVkfDIsuLD2n7dF4qqcFs84AotAj8uD0rhzLJw9C2AE5P2gBZKDcZBbqiUPrdSfLBczzEAsti3PepwuCBDC2J47DiPY+zyvkpALv+YBptyEEnO0NQLB4Igjp6kxZGcZTDr0tpuse2E8nynjmnEEBWqO+a0Q+YAUPhvoOk67GnJEADyDCcG43BUgSrFFPxJyzhAYQuFxAa8v4wZQKGtJ0FAkasKQDK2MgWk6VxjgYQQMlfiGrBhpEEYQDpJjEMQcC6EW6bgrR7QKqw6CDH+4iGUIlmMiyZAmJQtEAAI2IhWDjrR9h0MFzKeGFlDgTu3JiBQJgMPcdCRB68QDnoGLUMlTLHsgIB8nF3GbHZBwAL7IFI8CBk+27tKedB0HAkitahA52KEqx2lQgYQNF4ixLI6i9f1E5Td0s1wOosjpbVVH2nZ4KJcgngZQ87Suj0rXwberFnCswKjGwvpSBAAaTi421UAxsSWkR5AfJlJyRCZBG8dJf0DKSwRhLVt1ouDBxEMgJ3jb03Z-EoLDjnwJpmLRclhDi5C9JwSW1YDPGNY0yAAKTIAATMgYRhMgAAMyAgvqPJKawKlqRpkRGbp+mGdp8ELBOZk4cgNSkG4bijXJCWKketiQ1jFBYNeR4sWqBwS6d2Qa6EBkNj0k6Yf9xbtF67C5sgECkFIJQgRa24PC4dsO4yWRMVs1ujL96aFTK91+k9ehvceHKELRFC4Og4SRO14oeCD6a2LlXvkGEADMpstO0i4Gdq3wLqMLnML0dBBXJk0uCLsHftQiIvc8nNYAyEBMv7WUgrSDa4KEHBwL6KfcimcB0LS7CqugrCIMuy7ELYEAAFZc8Gwy2HQ5RiFgZAwMuUDL1AGjLgyFSsMuleUJGUCl7p8DLgAbFgTMvwvugH2UWAwNwu+uZ1DxwSNDAE1Ig4BoDwFoGAMQABHSwa5G5cwoAickYAG40BQJ1TMFBfL2zPgoCAJgBDxhNECTIk0LIgIALpAA)
