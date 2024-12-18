This app demonstrates:

1. Different `showcase_layout` options:
   - "left center"
   - "top right"
   - "bottom"

2. Different `theme` options:
   - Bootstrap theme ("primary")
   - Gradient theme ("bg-gradient-orange-red", "bg-gradient-blue-purple")
   - Custom theme using `value_box_theme`

3. Different types of showcases:
   - Font Awesome icons
   - Matplotlib plot

4. Other parameters:
   - `full_screen=True` for expandable boxes
   - Custom `height` settings
   - CSS classes for styling
   - Fill behavior

Technical details:

1. The app uses Font Awesome icons through a CDN link added in the head
2. Generates sample data for the trend plot
3. Uses matplotlib with customized transparent styling for the showcase plot
4. Implements responsive layout using `ui.layout_column_wrap`

To run this app:

1. Make sure you have the required packages:
```bash
pip install shiny matplotlib numpy
```

2. Save the code in a file (e.g., `app.py`) and run:
```bash
shiny run app.py
```

This example provides a comprehensive demonstration of value boxes with different configurations while maintaining clean, generated data without external dependencies.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBf0HDkMKBXQAbUhS+cAIxxcb19kKD1vCicDVwgTAV4I5Ah0BSUWWw84KXh9FxEsqly4IhL7LwooBQUAYmQAZVhvOGQiqGQAc2oHD05yBXs6Lp6GbIB9VigvOFZx9oAKAEpEBWR1tuy9AF5kYCKc-jgsCFIAd2XkAFpkcrhKqAWs3FZtjSXkOiFkDT4IUSgEG6CwAzAAGJYAXTWGymMx2KWwYzszBOQncXgWAEYwbiiAAmPHIcFLLDEBKsBLLGHrMQUEwMf4HVhEOGzGoQeoAYRMrAoyg452IEVanDIED0vO4nWQADFyCIAIJnWbMeTxThYdjiWzjcVUSgLGnISxYAASABUALIAGQWAHIADz+CAAa1E922cjAfNw8O1OW9yHYYjoXrA7AonlYiAA9LHiLYIAArVhknwmWx0LxQMRk5ixqDJqAaWP+AKsWNfShXKAq1hq2MANiwYNbCd0ha8XiwMG4ZN03oAfPalgoxxA6sgAApQbrIUjoKTkVgKU3oOdwcaLiisBZSPxwcMANWmJlaACFSL8ACJwGCkb1EOicbtQAIzbYWhjnidTrliNkyChCIL4MHyCgAAI2PYDA4D40R2HAwwUDB4wgcsqz-BszKstMszILs3QQL0VCTPhcyLBOGzIMaURYC+nQMnACyMawnAAF5HgsTYEks1EbPRGG4WwFFEGQPgMNs9pnFwVCjnRlRYBoUjEK6e7AJCAnrPRuCqepCyadptHYes9QNDktzIqwG42CIAQSK6nRMCYdiKRQWCdMKyxYKwOTjHQEhwBJQgOqcJEKaZwFKV5dA+X5FABUFIUMGF5BwJFNHGvUABK96kLIbDoNw7JRV8DBFSVfzRR5XmPKSNklWm0hnrMmHGjRjUkb5-nSJw7EfixsrTH5xnGnSDL-PRsXUpOnLIDaUC4KQZjIGcnAUOwyAtV457IAE14EfYD4SqhfRAm0nB0HQDjUCItmwDkDirhA62bSamo5stZh6qQu0wBA4xnGM6ALOttibdsWKxviKzGtlyAXhEYrba1+3XmtG1bTMdAiIKZzCn5xpvVtpo7ee4wHRoRpRZ17BCiK2ymlUnRppwCzEDmujjOGgVXA2-i2J8UBXLYf05gw-OcJ0k6EGwFB+ke3rVhQUtcSg+JiDAADc3pLAQHUbJt95K2A2j8LmuBPob6z44TW5fStFDhjjIjEHdDjW7TGx0CY3aTMQYjUF+P6lDbwZwNLkbhoSYLoBoXs0TRnMRHM4YwFc+LesacPe+s3oWr40yNBR2d57RYAACRYgQ+IggALAQACsTYAOxl0nGzegAqugyBYk3ACknxMCwXMiCdm1lwjp67a0VOY+9-J9wwUd4-TBMisTWMfVg5NblTNOd7bG-20zmos2zHNc2nysiwLnBC3zxDsLmqsuvIcu+p+ysKmrcAay1rrMA+tw7G3gOGAInQrjOSgLYTgd0rhCEBN0K4YhbCJ2PnbEU4xHZmHDMvUQa9MGd19v7Vggc4DB2-OeA25dtRrxjrieOJCk4p25unTOHcNi52PhXAA4kwM470crZG4Z3b0dcsBD3EUnb0ABRDQ7s4DwIulUBg3RdzTyivUWee0F4k3RlGAUp8RThDsNFXw293pk1apTa8R8sGmL8tsVC1BdQgSIMgXKyFboQHdrcbUljCicDEJILwVty7gNNlAmBYx4GII-OeK4pgGAtFYXTBmflcFLSdpA3w-IYAZJ9n7LwAcg4QBDrQ8ODDOjR29OCOOCdCDh3YbfMAGcs5gBzlhPh3omjwmQN+dxsispVwABwAE4wSxmeKMruYBwSiyWqIcW0pwiyDGN0bRNFdFowMTvckfJlDROsaTTU+97HU3DtglxzM5xXzaTzO+-M-qP2FlcXkz0nzy0VrzP+7F1bIE1veYBoConaggbYueVzxjRIWFA8MtR8TEBBHAJuYIfl0E6Ei4KdAwR0CxHrOhfDbkO1yfg70rtkDu0oJ7Fp5cyFlIoRUqpYd6GRzqc7SRzDmkkuPk8zhXSenh29IqSQMhWjdz8uBeZ+cwBYnxAQBuTc5UVzytMK4JQaUrUoN6MAABfIg4BoDwFoGAMQABHSwWs7ppgoCpOWYB9R3XNQodwngELlgUPERICgNx2AiByPhNFDWQiAA)
