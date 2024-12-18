This app demonstrates several key features:

1. Uses `update_action_button()` to dynamically:
   - Change the button's disabled state
   - Change the button's label

2. Follows Shiny for Python express mode syntax
   - Uses `@reactive.effect`
   - Uses `@reactive.event`
   - Inline UI definition

3. Creates a simple interactive experience:
   - Main button tracks click count
   - Sidebar buttons allow modifying main button's state and label

4. Uses a `reactive.value()` to track click count

5. Follows the function reference documentation guidelines:
   - Imports from `shiny` and `shiny.express`
   - Uses express mode UI definition
   - Uses reactive effects correctly

The app showcases how `update_action_button()` can be used to dynamically modify a button's properties during runtime, providing an interactive user experience.

Key points from the function reference documentation I've incorporated:
- Used `@reactive.event()` with `ignore_none=False` implicitly
- Used `ui.update_action_button()` with optional parameters like `label` and `disabled`
- Created reactive effects that respond to button clicks
- Used express mode UI definition
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DZMgDEyAIK37t0dXuP+gsIKCq4AwmJQVMhQPhJSssjSUAA2JnDIFKQZDBIA1hns6RAmMABGDsikdMjEyZzEuawKtfW5APpkJpTIALyxkjJwWEmpcAAUAAwAlMEQrgAKUADm6VIUyelQdsj2rMQMnOhS5AqWOMtwbaRHrGNrGz1yYACq6LaR6W4D5MgAQmaZCDIAAicBgpCeMwgIWQAGVOPZSlBHAB3TgUdjIUoA8hNCBojHIM6sBFwJEMMZTRAKJxOVwASQg6M4KWi3yB2IogJptLOxjMbTinHIbU5gLGTxgUG4opx0MIyCeoTqDWQAFk4ABCJ5EWpQXRtR5gUoUCAAWm0-GRuEhPKcdpcfzlekyyHBtk4dF4GPSUu4WLlDr5EFMFEF7NlXPIErAHtYUFKG0j3IVTwAKqQlksNk6o0DYRQPragbzOFh+WGhSKxdGnsR2FsVm1kgm4MlkydU2BQg2ICtc4DkAAZVvJYswtXSoFkSjUETI8QZLJx9At3jEEwMGwiViFqgKAmYs7EZG2SnUktOY+ntqFKB+GP-PPIRlUHLs4u0xWXx3AzisVcoHXTdtxqFV8k6SgHQAARsPwsCoDQKAdexqhaBo2hXNdzwdL8xAoTcgToJ4n0HBs9HKagwNaOBvBAdD2kgigsBWChKQAXwyfg4CaMBZlcAAlcQBgSOA6DoOBJCXPgIH2ME52o1UmOQFFCiBP0OTlPg9AY2iFFg4T4iGMSJMkfSIhE4zZEoMYKywDSOwgKFUOQNocJ-BiOlILpmNYOA2M8piWP8ylkAAamQABGKEYSEoVRPEySRFdTIsxzGsgV3IsIAM+LjMSsycosoz1Gsti7LjBMkwy5yxNc9yv1cDM0vScoKBROAqOoKraOibZKsTXqsqoPEv3-TD-x67w+jshyMtCgBSZAACZej6SKgzLEw3g+cNjggRyYzmwMFQGjZbB6CBSCMVgJvjQbbBiuZkDiyzkBMpLpPrRtWq0ltyjHIrDMGdQCuQoG8tKudbJDMwsG+vtLn+ttHNq6o3KpB0wlwWpVnYJgTCWTEPUS0DkeSUbaXJvQ+mAJVwPVLUdUVMB5h0PQAAkHCZrsAHFSG1LtgSyWFmH81QlkFgBdB0Ny3Odm1HNpuHsDRehk0N7KnQ6pmQJaNggMZqahL8zm294qD24UDvmyVtYy5nyZ6angDl7dFYB5W7E0KWpjAdiiHAaB4FoMAxAAR0sMR4EoVgEKQhUwBnKgaBQPiIClChV2uupSgUYoBBtEMtnePFcK-Wl-aloA)
