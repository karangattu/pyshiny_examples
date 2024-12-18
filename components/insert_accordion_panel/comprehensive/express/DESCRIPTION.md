This app demonstrates:

1. All parameters of `insert_accordion_panel`:
   - `id`: The accordion ID ("main_acc")
   - `panel`: The panel to insert (created using `ui.accordion_panel`)
   - `target`: The target panel to insert relative to (can be None)
   - `position`: The position to insert ("before" or "after")

2. Features:
   - Creates an initial accordion with one panel
   - Provides buttons to insert panels in different positions
   - Each inserted panel has a unique number and shows its insertion position
   - Uses reactive values to track the number of panels
   - Shows markdown content in the panels
   - Displays the current state of the accordion

3. Different insertion scenarios:
   - Insert after a specific panel
   - Insert before a specific panel
   - Insert at the end of the accordion
   - Insert at the start of the accordion

The app uses express mode syntax and doesn't rely on external files. All content is generated dynamically within the app.

To run this app, save it as `app.py` and run it with `shiny run app.py` from the command line.

Package dependencies:
```
shiny
```

This example provides a complete demonstration of the `insert_accordion_panel` functionality while maintaining a clean and user-friendly interface.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAApQA5nGSl0U8j06IWQAIzgKKgZkABsoXFIzBUscLzgAfT8KVgAKKQoYuABeOTAAQWIyBltOcncoCDgY5AAROBhSUqI6Thi40MKigBUGEzgASicIVwBZKG5kCSqauopSPghWBxF0Bqa9bjWFAHdOCnZkFKWhFYgczlsSsBh5iHSlrt90amHRicQFMggchTudLpwsNBpOldo0YjlSgBJCBnThQZoeOGlcYAiDA-HIUpDLgHPTnHzcVHo5CwppYZAAVS2yHJYTMa02YSapGOLPWUFstmQHTENL2MVYWFKU1cAGFyBQmM1QuzAhtFshiFBqiczhcUlrqjkcYDgQbtbZ0uxxPYGAiwPLKEr6liwJM8cDTUDXAAhVWctbIewdTaKqBUIOcOh0BzUIybba1PGCViowJekF68FYOIJMzpMgxEwwN7HBgYHKnWznIoARgA9AAmE0egnZ4z5iQBN4qyLke0Cy1QOhRT6lMqCl1NZBlEcObEZ-EpDsUd6SJPpXscgeCzdwYJiMflSeY6c+-dCeRuxdmiErtfdzf+neW6i2I8ToWn5rh5AAUTsBdWwJZcIFMVcuw3Ld+1KQd0lYChtQoD8T3FRYRAAZUQ4QgJcZB5RMSgHGQA9LhRABHMYxThZBoHgVgFFpGIC0SIjoiKURxHXWQsGkdExhyWt3QUAABMRIJ4-cY0kUTxO4uB1FkSh7jAswsDg4condew6EWXcmPeOc7RbfEyEIkQOIMsy2KwbwKGNDM5XEiNGl5JjMzBMgiMoDNXJhNCOKuSobg3JiEWA-E6FKb9kBAayKAAXy6G8gRSF4GAAa1sHk7iisBpXyiLgWcErWlwOjOGIKdmji1jEpS5BiU4PR3OOKADgTYQ4CFAAqHrNIcPqWWtFltTs6i6QagBafDnO69CaVIVNuxQAbHCKoEZpiiBi3CBgUFq8yko2wl8rO8YCAavii2KPKDMOygksK-F3XxRzkGRLZhGGnx3LWn6SM4BgEImmIM1Ar6IOC6pQvFcK2yBUoXm4NdiGSk6-KYy6TuwuynmRKkMXFdGEcW5akyeNbpWA17gSsuqHCwLZ7Pi5AAGpkCEqYxK4qRJOjOAZIgHmJIUuAlPsld1N3cIDwmBQdL0y0DNly9jVxUy6uQSzxRY8zGbshzgKc8QXLgNy0NBC4vKoHzgMxgLs2uGHyH8uF4YRvKYoe+rCAatLtSynKcjygqGpK1wWnK2BKuq2L4uO0mmpay32o2SH5r61WxCG1lcYiUGpROmbZTmoVfxTNMIBQbP5GLuOdpgPaDoThqw7dbHSeusYiju3WfaejNacR42Ps6kRWXc2uAZ6YGdmJ4CIe2VGQtdsK2+eV5UZJhGHbhTuEfzih8ZRKRqW-He20r7snlr6mXozen9YYJmIhyVmOa5iBZN5mQxYFoWIt5KKTjCpcC0tXx2G0vuJWbsmjpDfOrDMrMdZwj1jZQ2w9kAm3DD4VyoMPLWwVHGXy5s4HNEChCZ2txyEezbF7NCA9L4gQhOlIOxxcrt3DqVKOFUqre1bidZOBC2odQzuXCeI0+pvj6kXUmJcy4LWvkmFAb5poN12g4FudVE4I3bhdK6-FbqlHuq3Z6wIsHvU+tsAGf1JE+DfMgPIY0IhFAAHLkDgEQZR5BKZGSAkuO848V4uzeOvE6SMt4fD9hjMhWMGpH3cZ4g+V8lpVz8aOcxQIsFPxsszd+WtP7CWFnJPm-9pLIRKb-SSEswFqTgghJC0DdJwQMo04QSDgIoNBugqItk35YJwWbC2NEraamIXbfEe9pyUPUtDGh4TSYMJokwmJpMA6ZWyhwkOXCToRzKnwuOTChEkhEWnbg4iFqsj6u0igsj1Gl1NvNCuaSVpsGwpU+RGim5aPjjojeBUDEnW7sYsApj-lZOQJY0e1jvqTzQr+VktynGJI8Y0bxryKalDvteReQTIYhIWXDDeyM3jRJSQSaZMQKX4lRckhqPiIC3wvIeSFOTdbxUZvkj+nNimR2augXMmoTAMBsCIahSZ3m4J-nYRmVANCVMVhwHk8FEJUE6fiMQFARV4jykMUgiFmhMT0MQMuB1cl9MwcgGatYnpgASkQcAdEEAoDAGISiQN2hxklBQBVhASATIoLQQqLwKCCoNTETgoQFCNzwIxBoth2pTFJvie1ABdIAA)
