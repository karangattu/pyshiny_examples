1. Using `input_checkbox_group` with:
   - A dictionary of choices that maps values to styled HTML labels
   - Pre-selected value
   - Custom styling for the labels

2. Two reactive outputs that:
   - Display the currently selected values 
   - Show a count of selected items

3. Basic error handling for when no items are selected

The app follows Shiny for Python best practices:
- Uses express mode syntax
- Properly handles reactive dependencies
- Uses pandas DataFrames for data (though not needed in this simple example)
- Follows proper naming conventions
- Uses appropriate render functions

To run this app, save it as app.py and run:
```
shiny run app.py
```

The app will show a checkbox group with three colored options. Users can select multiple colors and see their selections and count displayed reactively.

Installation requirements:
```
pip install shiny
```
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkTEQAJnAZETnBQoDEyAMqx0AGzjIrUCihkKD0gq05JTnIoBl4YDHRuAHNkaSgvEzg9ClJkLygAIzgvVgVidlIIrOQAXmQQBWQm5DkwMStWlAcsVnQoCAAKVoAlOA7CNgpcHxrWsi8hFGcAMWWABg21gG5WgEoCRubWpLFqTuRu3v6hsABxU4hWolYpmbnSBYYljYBBH42dmB9i0IM0WmAChl5LRLn1Bq0AEJQp6TaZwWZgeaLZDOTZrP6A3YKAC+TggrjccBEfSSvikFB8Cm6NLgAH1SOgKKwBvS3mAAMLsODEADWBVIGmQ91IJnQyAAInAYKQ9mTXPyxAFfOVhWKJcgTjK5cYzEzOFgTRRWTrReKNKzDbKhqCjpiPkJShMcXwIKYjFYQWDWoLSKRWL5cDKGMg6FBpEJOFRkFiGKxECjXPkil5Dk1ypViFkavmqqwDi6muGfJIxjVgK12q0ALre7RwAC0VeFIkbECJj3JCs4vXyvAoQrYxW7Y1S6UypQgAAFLDYGFgqBoKAobHRJ9WqFZre7UwNdumK3xdxBSEZfWYsCnuWfc2DRFSTAxQa0AHK5R976dxhfMQKA-UE6FaABNGUAJrKwUBAAByIhEKwAArSpBktB9jyfXZSTANV3AqAB3ZMZUoZBSF3Ls4PIz4F2XahV3XTQRG3OBdxTI8TEoU9zzBMheJEOofCwu8KBwhjT12S8fT9KSPVPZBinDZA1mA99PxjH8TBgIpo2o+iPVgg8EKEygCLAYkiHAaB4FoNo4AARwcMR4EoVh103CY3UoagKEchR4gobwby8TgCgUCA9LwBQ4X8BcX1fZprKbIA)
