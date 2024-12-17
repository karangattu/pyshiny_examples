This app demonstrates the comprehensive usage of `update_numeric()` with the following features:

1. **Label Update**: Changes the label dynamically based on the "Label Length" slider
2. **Value Update**: Randomly updates the numeric input's value
3. **Min/Max Update**: Dynamically adjusts the minimum and maximum values around the new value
4. **Step Update**: Allows changing the step size of the numeric input

### Key Demonstration Points:

- Uses `ui.update_numeric()` with all possible parameters
- Generates synthetic data
- Provides interactive controls to modify the numeric input
- Shows current input details
- Includes explanatory markdown

### Parameters Demonstrated:
- `label`: Changes the input label
- `value`: Updates the current value
- `min`: Sets a new minimum value
- `max`: Sets a new maximum value
- `step`: Modifies the increment/decrement step

### Interaction Flow:
1. The initial numeric input is set with default values
2. Users can click the "Update Numeric Input" button
3. The input will update with new label, value, min, max, and step
4. Current input details are displayed in real-time

### Recommended Improvements for Production:
- Add input validation
- Implement more complex update logic
- Add tooltips explaining each control

### Dependencies:
- shiny
- numpy
- pandas

This implementation showcases the flexibility of Shiny for Python's `update_numeric()` function in an interactive, user-friendly manner.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBf0HDRUO8ycHXEEwN5QehDoXi4i6O62gcjR6LYKCgDEyADKcOFQAOZwyKToUuSsCpY4WXAA+nkUrAAUUhQANnAAvHJgAKpxUFTIAHJ+DpzEyACSwWbIACJwMIUUDN2c5G0AlAkQyQDCYt05rLiU7OlDyFEUUArBWAseMFiscHC2NQAsAExrENycUlAN5dI-iYcs1kABWAAMChg3ABQJByChEBgUA0cIawOQoIAjBCkUlUpx7AAjKAMZAAdx+7GQZEoTAaRQgVIoNJKrCJcFJDBqK0QCmQguQyQA8gxOJluH9kL54OLhsYzAKhSVFRRyrLBsQasqhUK2qSHhq-MSHG0iLq9cg2gAhQI5fowU2OQjWiBWoWAjEtb6-f5e4EW90e5AwiDNMPowNukOh1ER1FRuBB2OsKjoZrYy2fPWWrbkeakRnIOhCZAmLpSCCZGUDeV8cYUS2qxvlCQFCDlYlmCjkHVgCtnCrEigQc3WjqVh11k5jUxNsA5-XBwXJACCtlsPyW0AatILDL0vdOMzmCx6W7odAc1BEg92bGI1DJSyZepb8-KrAanJ5ltzYANFApr-E01asuO-76mAAAywFwHuMHUJkEGulBgphs0YIpiGKIaM0ADMEI4R6AYtLi2aWs2nBYGqX4-vYf4rlabRpnA6BfpwABe8hocxAEpOmhI8ZB-FCphEJYNiJFWnhmbETGIZkZmMl6mxGaSVmzGfASACyUDcPulC3jEOwKCybI0UBuCkGY5RkBiMAQLUfJ5lMnCsOg1m0iYDA2EYjYnucnCMpaFnljRxBks8rliYKJRRQwtjlEcUCMf2my+f5oyBdMwWhYu6GKR6AACNiMVgVAaE2cUnnQDafvY+UufytV6mIFC+e6dBtL1YBFXqmV+SZABq8IoCAapYIaFSys6vIAL4DUKQ3Zbp3ATVNM3Gk6DhYGGS1tStWUmfpGibY2032jtzr7aih2xoNJ2UKk6YXfOV1GnNe3qQ9j2Cn1vXMW50yzM58yLOQuT1fePSsE+0DiqQb5CuFCXRbyrWxujSUpeI6VtJ0Q6pAjL7I6sRVFWV4iSDIcDqFecCSFTOy07I6iyJQNRTbDw6jkuHr2DDU47Vq5Rqpjy2riTz5I8g2IoETD5ASBUvICrCFYhOStULYfQmg4E7IAA1BOACEbTIAAVA2FDc5dGugchrK8gLj1q8kKSk3LbyK1OyBkWrEBwBSSZazctjMFgJhfKWDAwDUkZkUQeFJm7sYezLiNLMgBF+8TYYxHYcYaEHIflIXoJ4TUCnB6HZHIAAtMgbwQunIZ1xXqJa2GNS4rX5cN6brftx6mde7LOcvPnD7qWXofqVrU3qZxPG8mrmcAAoOHHLCsjkvNqyUvOi-KOpHWPYDbd9LoEGreqO80jtEP9yQ6zkjv3568LNJ3ychm-f2gcL6yW4L-cuYYX6PUAQXbgX8MLxk7nhKBsYYEPjwvAtg6ZwELyEq-ZA78sHsTVjpDYyART5B3H8FAG49asGYDkTQXl3DdCELwKqNUSgogYAAa0jhSCA-ZAYbESMkAAEqQCkyBjztAeAobEWBkCbB-MQHhyAADkhDHRahyvOdR0jSBsEeKcA4sATi8yZG8RRG4ABWJg0waLgiBZASFwLsH0ZEDRgl2LCTgPo48xB7G9hhDxcsU4mSA0XGABaRBwDQHgLQMAYgACOlgxDwEoKwSq1VXRgDpFQGgKB+rIm6F5UgjRODEkuH4PACgIh2ECOsf6gpokAF0gA)
