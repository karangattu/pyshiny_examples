This app demonstrates:

1. All parameters of `input_checkbox_group`:
   - `id`: Unique identifier for each group
   - `label`: Display label for the group
   - `choices`: Using a dictionary with HTML-formatted choices
   - `selected`: Pre-selected values
   - `inline`: Boolean for inline display
   - `width`: Custom width specification

2. Features:
   - Three different checkbox groups showing different parameter combinations
   - Real-time display of selections
   - Summary statistics of selections across all groups
   - Card layout with full-screen capability
   - Rich HTML formatting in choices

3. Layout:
   - Uses `ui.layout_columns()` for responsive layout
   - Cards with headers for organization
   - Consistent height across cards

4. Reactive Elements:
   - Real-time updates of selections
   - Computed summary statistics
   - Formatted output display

To run this app:
1. Save it as `app.py`
2. Run `shiny run app.py` in your terminal
3. Open the provided URL in your web browser

Required packages:
- shiny
- shiny.express

This app provides a comprehensive demonstration of the `input_checkbox_group` component while following Shiny for Python best practices and express mode syntax.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMqx0AGzjJbUCihkAFpkE1ZuAHNkAAkAFQBZABlkOiE2Zl9idlJOYjg9ClI-OBhyVgoGAN8GPPZUoRgAqQhIhWzc-L0AXmQQBWRB5DkwMVsRlEssVnQoCAAKEYAlOHHCNgpcH26Rsi8hFGcAMSOABnPTgG4RgEoCAaGRgCMvE3laKZm5xbAAIVf3kQKls4DswHsDshnBdTidrmA7g9BiNImJqBMwpxprMFiMAOJoiAjIGbba7Uj7BiHc4AQRp53hiIgQ2GYFMDG870mWK+uLAAAUTByfMSNiCwRCqVCABwXWWMhQAXycEFcbjgIlmkV8pHQUnKCimWrgAH1dRRWPMpBQyWAAMLsODEADWT1IGmQBNIJnQyAAIqVSKK6JwvF4oC9QXEGG8birXHaxNVkOHcN6RAB3TgUep7EwwCCsBRZnOYrCp9MmvMFk0ZqroeZZ2w57oARgA9ABmG6IJFQ5C-KARYjIbJO13u5Co72+kv1ex0KAmLyaqBVeBUBhF5lDOdl4hr2zzOjLrwm1jEQndaNvIicWwSw+t269ncswZTA8MWwmx1QewMD8g7DsgDrjm6Hpej6tx9iyUzGGYVaOi6EEmtOPqLG+74sveYJPEOeRoUw0GELB2EphGcBeGCDqkKQrBZBSQisL2pFYeRo45HkBTdB03GsPc7HkQxPiSKs3TACMYyis8AIjAAumRgxxkSQmDAAAjYAFYFQGgUEpJR0Mg+HDmaZimBQ8w9gZLJiBQQrMnQIwAJremwVFOlQtgoCACEUFgJmEehDY3MqYAqiyrgAJIQF43BZMhE4esFfZ7p+h7Hqe56XnA1DXjGcB3g+uyHgATC+Bnpd+v7iABPwxXFEC+GBKGTlB6AwWpZZ+Uh4HukRM6YRxOHFWA3CNaaKVscNQzhk8VE0Tk9GMZSejzON8XWdNM2cZ0PF8V0gk7e5oleRJKKEgpR07RtTX5W8BkqQZmnUNpun6V1C58LF8VmRQFlWa+x12Q5qQuW5ImeasPl+Vgt2TcRIVhRFQwJuERQsE2pZjq1yWI6l2b1FVR4nmG2VXjehV8KNX62J2FVdcTNX-g4Px2ujygAOr3qWLVJZ6+MIpVWI9TjSUDRhNlDLhIxY+wEsddtM1zQtIy0cto5MVuyCNveDhbddM0HftXGHVLgxy2CAAs5zoBoIyPSj2EvXYDg6ZoH0cV9ct-QD1ldbZGqg05YCuSYJ1Q95fSwz7wVWcjqmuDSti2MgQSsPmTQMLwtPFoT+4ZTLYAZzAWe4FWh4M3BWK08zdUjG4mdrrwpBGTSYbuB5kicAaQtYX2LtvR7fZfUUgRnpD3flIDBmBSOvSw3PCtWXwRmLwRxDLzcyBUQxyDAIpXXw8gC8QBZcM-U1W+r995-w9fu++AfBlyyft9mFgseIyvnBr2fH9f0GtvR++9D4cQMmPKAXg34+AWHPbeABqFM1B1qXzgIg5BCw5YqQ4iDBgjkRhxFIOPZAEB8zzQYMgVuEcp6FjTpeeiegoHQOCixPokCvAJwHlpN2lgR5wCMpPfUEATT2ECKGS0-sOJCJ7nQ3o-QA6PD+BvAWM4MTr1MnHbev937+SXloneXg94H0NsNEYDV4qqJIigWG98DE6NsWgh+Rin7yVMeAsA3Nmz1Hauo-+-lAEYW0X-c+gSQqGOMWA8iyouoGQTEmKgac-AyE1pQKA3AojIFmFUVEGB2B6DSJQ8Q2QpyIwAOR6BkQaLqeDmRTECJEVgWBbAyCGjtYA9SoCNJwMeEYIBgqKh8mUogZSsAACtcgLCEasYJNCvIRN8GUgAcuQOAZSwo4OOoU0pM4gRd3mdwOZsimnZlKJItx5tRzhl0CaMEMAKDBHpuFLqNwwCKnkkAA)
