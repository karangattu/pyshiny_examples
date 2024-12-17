This app demonstrates the following aspects of `update_selectize()`:

1. **Label Update**: Checkbox to toggle label modification
2. **Choices Update**: Dynamically generate and replace choices
3. **Selected Update**: Change selected items
4. **Options Update**: Modify selectize options (e.g., placeholder, max items)
5. **Server-side Toggle**: Switch between client-side and server-side loading

### Key Features:
- Uses synthetic data generation
- Demonstrates all major parameters of `update_selectize()`
- Interactive UI with checkboxes to control updates
- Shows current state of the selectize input
- Uses Shiny Express mode

### Interaction Flow:
1. The initial selectize input is populated with nested choices
2. Checkboxes allow selective updates to the input
3. The current state is displayed in real-time
4. Random data is generated for dynamic updates

### Technical Highlights:
- Uses `generate_random_string()` to create dynamic data
- Leverages `@reactive.effect` for updating the selectize input
- Demonstrates conditional updates using checkbox states
- Shows nested choice structures
- Implements server-side toggle

### Installation and Execution:
1. Ensure you have Shiny for Python installed:
```bash
pip install shiny
```

2. Save the script and run it with:
```bash
shiny run app.py
```

This implementation provides a comprehensive demonstration of the `update_selectize()` function's capabilities in a Shiny for Python application.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5ZqCAE1JgB0IDJq2QBnCszoQA5gIEAzZrzEALKbmRCWbZnCjEKdAG5wFSmKvVY4AD3S7RozY22aI6AK4Uiu7nGZEHnRyEADEyADi1P5QVGK4lCpwhsTIXLFQAlxw8sjS0RxUAPoc3LxF4pIyABQANtTSFCoAvACsAJSIAsg97MkezBDIAOTDWABWpFLVpTwwWMQqU8RwotWVUtJYUKLEdHRFHpj+xDtwRADWzfUyTe3tIdm5+RAxxa-icFxFi8ur1Z1ur1dBQBkMQEDer0+GAAGLMIIUUQwlAQoZQjE9GEYdD1FHIGEAQUweMIkMx0LAACNOLT8TCAEK06AwojkikEsCLfzMXD0sAAYSSzF5MPZvQAvgRxViwAA1OD5ChQKn1ZG0NEcqEw04i0gUfkCqB6g1k9FazlUpTEMi1YK0RnW232tnmrUw0ToKT6FT8gDKXugizFbqhEvJ4YgAnCfuSyHQUHyyFI6EM5CcHlEm3jibgRRTSOQimUojUEFw1jsDlEWCCAiCOFz+dTa0MFHqzRhsfqBjoAC84MgAKrodJxAAicBg6YksTo5FZRbotVqKo7ABUEXAHlGwsg-XRsjTmMgAO50JrIIzG+eZtyeNhkShKWrIiDny8NrNH40Arpu8IAElBEMKBajEOAe0MAd7y8ckGykB8KkguBewHaoZU5GAoCkZCoP7UxCAJUNKQAWRwoZu1Q6DB2Ah9F0w346BWURmheN48w+KhviYliAWlEiehgDxakMXE4GaTcPHOTCC3nCBWM1C1OVxfQ4CWWpsmYf0UIMTQqBgdUBOUrCoBsQCDPVFAAGZMMjKEd3JcIBXICRSFfIsWGQI4x2zURdJo+C6CwRCvB+JJiAuKlSBsDCwB82I81XKlIIYsARzHQcABkVVSsAdyhBD3DC7lIui2KYQS4peNWNKMsS5AhT+dUCt6IqkNKqKYriqq838qCvjq0cGqogxBvyoKQuKihwtQrqKvi4bijk9Mhsy5AAHlU3klrJtCmbOvKnqlr6-wTG0oiYXXUhpGkep9zO-wAFpv0Ixy93IqQc1ecCKFIVRSFPZBiAGXw2HERKBAAAV8LSsCoGwDT8XJ+uogiKmVKg-3JEEwSLMUwBDKEBVB6g2FGmj90xuB-yhJ6HoGrhUX2rBsNw1G0LgAF7N6enY2Yc6XsPGnkBAFneuQgX-G58kCZDaNkAAJT0XsTGQHJ5Go5A-u8k6IPwmCaX8rhkyGQ6YtqiAYZVwwTGseRNYMLIcl1zK8LR9DAQA5AAAVdATXRgaWZjVmQTgTZWhTyVeU9wua5BmlFzCYQAOTgIH4URKyk8EjF5BhEB2MKPNZnKDYanacNaHzsA06BwuCkSkpw7LiRNm55BM4vInlPkLyijcdhOHyaprNazEpWT2v0+QBUlTXWqNUwqEa4b15i+bsoYAxqppBl6vU5nteOM3uYd-byvZ8VZIF57i0+5PAevtKEex7siNZbdGPmzTBSE5zjkMJVIrA0lpfk9VuLxlXCA9yYCzSALANhcyll8StE0LkcWJ0f47QBOrV8g5bJukjE5YcesOaUw-CoK8N5SB3gDrAZI-g3yFWChLchBEMK5xhGzCA7tOaskws5cgXALzyTArUDQvVkDJVSrnGRtROzpROibCmBEYToNghQWsWD5G4Mgv5ZAKdyAyS4bnIR3BRHkHEZIvWNVmEUjsc0b+diNGYLdnYvR+DDHGOMhSQRjVhGWOgCuGx61yGDVzuErgzROEmTtOIaozjg4sSwEqOKddO4IgvEZUWEp2hYAuHAXAax7jERMnQDB01tFuyibg5evR9GDiMa8TC7RfGYn8S5Cxv9rGuwapHexmIBlOPTtg9MriqkSwGZ4gxzSTGALMQE7pYiQnaxundQc-kpbMCFtkaRpAoAiJkJhLZ51mhuKbqc6W49kDtDAFKUWkAGG0DALoAAjkEXQ8BKA1goIjIiXJXJkxeQIbCFBcT6jtFSAQEAPCMD5O4cOOwQgmXuQAXSAA)
