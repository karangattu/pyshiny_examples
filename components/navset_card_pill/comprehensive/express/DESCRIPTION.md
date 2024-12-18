This app demonstrates:

1. All parameters of `navset_card_pill`:
   - `id`: For tracking selected tab
   - `selected`: Default selected tab
   - `header`: Header content
   - `footer`: Footer content
   - `placement`: Navigation items placement

2. Features:
   - Multiple nav panels with different values
   - Mix of different layouts (columns, sidebar)
   - Interactive elements (slider, selectize)
   - Data visualization
   - Reactive elements

3. Technical implementation details:
   - Uses express mode syntax
   - Generates sample data within the app
   - Uses pandas DataFrames for data handling
   - Implements matplotlib for visualization
   - Shows reactive behavior with input controls

To run this app, you'll need the following dependencies:
```
pip install shiny pandas numpy matplotlib
```

The app provides three main tabs:
1. Basic Data: Shows raw data and basic statistics
2. Interactive: Allows filtering and row selection
3. Visualization: Displays time series plot and category summaries

Each tab demonstrates different layouts and functionality while maintaining a consistent navigation structure through the card pill interface.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBf0HDk6KHah6vb204OuECYCvD4Q6AoKAMTIAMqw6AA2cMi2UBRQCrZ0yAC8vlgAIulQAGIMsHAAFCAKyPXIAORpVI0o6LZYLXAA+hUQAObVrBnCuY0ATAAMEwAsALRTAIyLS41E6A6cpLasuUtTUwCUBHUNjdJQiSZwbcjhWP22zFgQQjBXVQdTRAe-hyczvVGsR0nABkJcHcHk8XsR2KROMRqsBGgBBdZNABCmMaAGFGgBdf7HBQAXyOkQgMQAClAhshSOgpORWApLDh6b0mRRWFUpBRkrk5GAAHJQaSsOAiPFQBi2ZA0ziJRLIQpwGCkEVEOjKxJQABGQoAKgwbpSINFkHixGDkFB7hKpRQeqD5T10HrkAB3TgUdj2lVuUi6ThGlLuCrwKgMNkQX3+5Ac6CS6WuuW2D16qpAvi2YWQCVZlVswgNcvlmIAeWZ22gqoAkoVkHQhMgKBViABrbgDNhwZKSOAKjIG3NSwdUfMi0dLbUVisxdV0KAmRIiCdwIcjw259jiewMAvi6ScAbpOuKvV6dWa+fIGIACQPDmQZEo1AoudbpBjBdKpC-q+75UJQ94xABQEMG+5CgV+EDlkkEgap+BaGqQsgiguDS0vqyLwJQjI5CmfBUDAehiPqUiyO2pAwR+YEQEciC5hBnCxiIo65gmAbJkW7gQAOOZgFiXhImqJTzpc1xwAWs4isxubljxSacFg+q4KQZiuqQ1wwBAfJkIkPS+rY-p7MAABsRCWYSikIdhlYSRk7aGskSnYQAAjYh5dCUPSMJUHkLvYOQGmJxA9KOyRVPZjmOWIFAmAwCHZFg+5QLYXykg58XIMFi7IKJrDiSM6Rxnl9TedQvnRfIuXxaFbAZLysUsQ1lWiNKyUIR0RQlOUlQ1AVnWNLELWcCMSJ3KiACy4gQLi40Kuq0i4niWmUESpwdZ15wAGpXDcM0jXt9RMCYdhVNkqLScdhJYPAHixUQEyArtZ3lhdV03RcR23A9IxZScyBvTtn3xckEDXXQFoQ+WhKnQuFJUk5sRbuQO4Gj6foBiV9jhY4DUqXx0geh4Qkig2H6dtR8hlndskzoaEwKe1jkk2pGlaS6+NwITbVIzjiYcnzAtxZ9HLGNprCJJwh7CRAfSkN6pZECKorBAar6kDkTCq-OACsRCGz8yAHHDktqdLvMDluUgAF7VELjkiqCVAQgwuDai72Eiujk7WmCnve4QvsLvCiLIhZIpoiqIqEsgADUyByyMMOou74KQkSWCXZwACONyxe98MNJu24FnHiQiuHyCW3lQvVXYDh+RkAVRvVnVNbq64OMOPQtFAgsffFvcxgP2R5KkdBYGQeCxXXnA5Dbc-B5CsXIAAhPksfx0gdfluP-eZlP+TH2Ip90MAF+T9fILr17RJ5Pkq9ZyHsWI6PCXdSlLbKhPK+6UDxVFXkrfWfIjgWlYsgY0XB5SuWxipU8rATBXE4A7C85BuK41Uq8fiFNEjCX2pNNBctMEsktAzf6clDQAGY2YFU5upKAmltJGWCAZKoRkTLy3MrkYAAAOIgsw7Ls0qs3XySRfxCyalIeAPQpQME4HASB4izrOEMMgD4FBpGCjDDgXAej7R6CSPBCGuoBhECgBoaeZisCoINHovkliSpO1yNlGyUC66tmgu7PgqV77vxzg9fORdqgSzLu7QeJRp43V+sEp+idcj5Hdl-Mu9QbE4ESL+bh6QYkZFRN0bab58lD1uv9Ep+ptaJFyO7Bue0snOiin6GKjRjT8BSOjZRqjkAGl4LKD2OcGmdSyckIYV0RmVUSj1f+AwhZNx8q3Oqsi4A5FQTAD4Xsej9PTEMr2I8IYzL-mlAYF10D9KqA-fZUIjgVJkrnekAwqioieotIgIJNoUCJEcR4m0spvSpDEU0Eguz9knMORBChJHLM0PBJqFcpxRUNIchoxyEJ0BFHiZKNhBS8ERZC0cKAQBgP4teWKZIRRgDJEQcA0B4C0DAGIIu7EUKUFYFgCgGgKBljACBT8jKFA6L0XLMcEAgghAUAJNIcYhbUsJEAA)