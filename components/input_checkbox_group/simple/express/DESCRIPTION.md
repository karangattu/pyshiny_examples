This app demonstrates several key features:

1. Synthetic Data Generation:
   - Creates a DataFrame with fruit information
   - Includes columns for name, price, stock, and origin
   - Uses NumPy for random data generation

2. Checkbox Group Usage:
   - `input_checkbox_group` allows multiple fruit selections
   - All fruits are selected by default
   - Users can dynamically select/deselect fruits

3. Reactive Outputs:
   - `fruit_prices` table updates based on selected fruits
   - `summary_stats` text output changes dynamically with selections

4. Layout:
   - Uses `ui.sidebar()` for input controls
   - Uses `ui.layout_columns()` for organizing outputs
   - Employs `@render.data_frame` and `@render.text` for reactive rendering

Key Shiny for Python concepts demonstrated:
- Express mode syntax
- Reactive inputs and outputs
- Dynamic data filtering
- Synthetic data generation

When you run this app, you'll see:
- A sidebar with checkboxes for fruit selection
- A table showing details of selected fruits
- A summary text box with statistics about selected fruits

Users can interact by checking/unchecking fruits, and the outputs will update in real-time.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5dKCAEygGdk+7LgB0IDJq2QQAro1wD+EdKNEAzZqRjJeACzoR54lm2ZwoxCnQBucIqYCOajVt37cWOAA90p3vyOS+ujSFETSdHbUXHDMKhAAxMgA4tQxUFTauJQ6cJbEyDwUUKJKWMycXJpYvHBwXAAUACwATACUTuEUvAD6hVDIALxCWAAi6VAAYuXw9SCiyAvIAOTQ8EsowEsAgpgANnBLREsAQpxnh8sAwjnMzLgXS2NUDwCiu9HMAEYxdw8TdABzB5JcroA4AXQI80WSx8dGIBxQpXK3Cq0jEqhYMHqAEYiDiAAxEADsrTKpHRDTaUIgi2WvAopGIAGt1lJsCjKjAyhV9BRcUTkITBaSaXSlixAfo2ZsAKoAZS2DwAsl54aQHtc6PsHvKONKjsdygAvbUPACSRV29yOU04CKW4NEAF92hBRIkAApQAFwZCkdCWcj8CrISwUfaicI4H1wboBrr1cP7AbCMBTTrIZVQZjM3LIMa6T6kHMiMBuj3IeV0aKfHPIADudAoOmQxByLOLnmQAI00mUECbLeQ0d4NbgdeY9VaiGhC2jQRC3XbcE7pE83V7FPQ9TndOQaZq+wsdW66k6vDTRD3dLT8rgx7YGebl8IB9p+4W7dI8LgvAG54vr04ybKsEJYIyux0Ay05ip+2gPquVBcABzAXsBRSgbA4GQdB-KtAsiRbLsuzIIBXQIY+dTIJ88jRKoUDSLsFB7hWCRZlA+htuQVCUAIpj9EOrYUA2pD+iEwRdKIQkjnQWC7FAuAUhQy6kLssgQLw06zh+hHIM+bCeswv78AAKlAnyRrpyAAAKmNwMRYH0Z7THAe70WRaHNt0cIIlpM43osiT-MxMRhjkBTjOo2E0Xw1HkJRSHUeRl7WXSpgUNIzC0ilGFQMAuV9Fhazglg0H6PUi4UNUiEnlwLkXtOrROu61mJPKsgwDm8jykUlgMvCqV0nZUSOVQngsdZHm8J13XdAy6T+Tp8HIIkKRsEeSVcJ5F6BQsm11YMyBVTVVH1Sl057e+K2JJcmiSX6M0wF1dxXao2pUKY9V9EdhUgX9mErNhjplWOED1AdyHNVdV0ZVlOVpojYBXfeZ36V5FEdc93XLfBAC0yCmaQVroxeKAgPs4OQ3UrTOldBNbDY5S+sgRm-igAAkIDvaFX15ZsvngfAnDaVgzSqHTaWLATRMk71TLMuTPOfaeRVLAyCsg0906SytSNpmAzpEOAYG0GADjhKY8CULwEETW+YBkJQ1AUGbohdRQ6C7MTUGfCUsh4KIHDcHwcQrXShvgkAA)
