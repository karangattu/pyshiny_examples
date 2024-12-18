## Technical Description
This Shiny for Python app demonstrates the comprehensive usage of `ui.notification_show()` with interactive controls:

### Features
1. Dynamic notification type selection
2. Adjustable notification duration
3. Optional close button toggle
4. Optional custom notification ID
5. Optional action link
6. Synthetic data generation
7. Real-time notification details display

### Input Controls
- **Notification Type**: Select from default, message, warning, error
- **Duration**: Slider to set notification display time (1-10 seconds)
- **Close Button**: Toggle visibility of close button
- **Notification ID**: Optional custom ID input
- **Action**: Toggle inclusion of an action link

### Notification Parameters Demonstrated
- `ui`: Notification message content
- `duration`: Display time
- `type`: Notification style/color
- `close_button`: Close button visibility
- `id`: Optional unique identifier
- `action`: Optional action component

## Installation and Execution
1. Ensure Shiny for Python is installed:
```bash
pip install shiny
```

2. Save the script and run:
```bash
shiny run app.py
```

## Package Dependencies
- shiny
- pandas
- random
- datetime

## Key Shiny for Python Concepts Demonstrated
- Express mode syntax
- Reactive effects
- Event-driven interactions
- Dynamic UI updates
- Synthetic data generation

The app provides an interactive playground to explore and understand the various parameters and behaviors of `ui.notification_show()`.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBf0HDRUO8ycHX6d7ah6AcjotgpKLP5UUvD6LiKRcNFwREn2ADYUUAoKAMTIAMq4lOyJnMTIkVDIAObUDlBS5Ar2dDV1DA1wAPqssOhp3ZUAFBAmMF1MAO6sALwArAAMAJSICsjryHJgW1sA4u2dyFW9AgPIACINUABiHTGTnBTsbh4RV1g729sQG6KJJgwfiEsJdMrdYHAhiA1r8NgByTi2OEoDoQWpDACMRFG4ymegA1MgMUsCDDYcg4dB4MjkMA6HCAJJUFggTgAXzhyDoQj4fB+qPRWOQOImpGmyEJxIAuqSfuSKdIoGkTHAacBUbZmFgTBBONyGDBMQsiBiFssuTyunyXuiRXiljKybC4cROtUhLgaRqtcR2KQynBWENgHCAIJwohwgBCEYpAGE4TLkABrGZ2sWsElO35whJqhJJLAQMVDJbIAC0yFScAyUCG-lws29MCwGu4FCGxuQAGZlmX9cgrdwbZD09MHU62UtshA8nGxIcTv04BUrqxEs1WjM2hB6lQen0Bl1htOILlkAAFKC1Nj-dAKSw4a-dUjoChBqQUAYzLYAOVIUh0GUDScOQBR+pMrrrlsRBAWkaRQAARt+AAqDAqqe575IicCIVADDIA8Tx8qYIhkJQTBpKwChEc8j6sDheEMKWqxyusj7GGYPQ1nAkhDNmGxbMWgHAY0EBdBQuDoPIhCbGxsJ-gBeqiaBPwoVJMlEAJ6zAFsLRQCYGQwZsYDwLoz7GVskz4bqaKWWADhMI4YBSk6p6-E6HEQKRPRpDhzHaSZtgAiBTSyYFikia6YkXCFMVDOu5G2Jmlnyb8MDcDMQqBTAUAaFlXaBYqypwPMblOp5nBYJxFBdL6vHJohpAaPxaWCWAxBpKQ65dIhZgUGFWltesWz5BByBxl167IFG-WDXJ8rIMVKozGhKrlfJlXVd5XFUBoHYRZASlAdFqldIiqWLZFymnWBDLnMgQyvmJSrTuFw3BAhxBwH6aT2AwP5gAAMuIsjIMh7jJhaBHNsg907PJ7mCfJXk+fVxCNc1rVXWAtFdBIYmXfKWwMhAnUmPYyChpIqlE+Sy2ldcSrQYjM55AAslAw7kVQlBHAuNGPHRVUIbgpBcWQyowBAQYrE6tHII+roMLYQx0IZaQ9MQYjUKt6FwHLH1K-hthdCUUD-fxYD-lFoU-OccAwOQrAUB0hNgEj5KBajXEE2dfUUANEBWxwYpdMJN12-ZY1isgNuR+7nsKR9AACNj-Vge0UIFLTCsdKnkMeiRc1RLGBb8YgUACPx0J8COLb86nSSgrI7RQRb57d4mSdJpZsuXGznHFqktzVWDBW7ql97eSXUR9vyTd1K6zYH5Cj23WCdUvvVzcHSz9-PGxxiYLvKPd6+kR3ttiedqtljyYZmKQ5a1LubtwEiB8Nxs1NiRfZhYDxn7cgfcB4jS+Ajc88cTp22QF1aoZQFBp3EDTWQ6g6B0F4tnCAyC-ZoLgLISgQwx6h0mOHTudtTy5y6GXeSeQLxiF8GIPO19VLBHwhCKgDA56-AjjAm+TDYB6G3NCD6WxLBbBQLXa2FCYoDhAM2TefoAz1joCGaKcB3QME9FKfeyANFaNwDBQ6E8o60DHqYsSpZZQ4x7jJFAY8+EF27hpaxh0t49QDkHSRJEAEeO6F4kBScv7I1+HkAA8m+VSSo4bnCdHqXx7cnFd1vrQxayS7ZdEETAVgukwAXRcsgbcjjZFnURKWCqdDkCRJemkI4NMmjyQSWPIBDS96sXSaUwu2TclbGAWeQp25Hx1jASZAAapwOAkwLjF04FROmDd2BiDoIDHICzFrkE6mUVMfSBjCCGGGNpVYGCcGqLUMQtgACEcI3qBSTk6PIMdpkZMJijKqLyzqkKGAAKm+R87pHCclLDAGyIg4AqQIBQGAMQABHSwYh4CUFYJnfaskOrkF5hQWg3xcoUH6ABPyiEFA4jwAoXwdgAgzm-usEFUogA)
