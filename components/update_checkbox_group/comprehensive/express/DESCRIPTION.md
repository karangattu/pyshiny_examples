This app demonstrates all parameters of `update_checkbox_group`:
1. `id`: The target checkbox group's ID ("demo_group")
2. `label`: Controlled by a text input
3. `choices`: Controlled by a checkbox group that filters available choices
4. `selected`: Controlled by another checkbox group
5. `inline`: Controlled by radio buttons
6. The changes are applied when clicking an action button

The app features:
1. A two-column layout using `ui.layout_columns`
2. Cards to organize the controls and demo area
3. Real-time display of selected values
4. Notification when updates are applied
5. Styled choices using HTML spans with colors
6. Reactive effects to handle updates

To run this app:
1. Save it as `app.py`
2. Install required packages: `pip install shiny`
3. Run with: `shiny run app.py`

Package dependencies:
- shiny

The app provides an interactive way to explore all parameters of the `update_checkbox_group` function while maintaining a clean and intuitive user interface.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMpwR6KAHM4yUnQpclYFSxxfOAB9QIpWAAopCgAbOABeOTAAYXY4YgBrACNSDWQAcSYTdGQAETgYUkyiOk5k5KhC1LSAFQYTOABKJwhXLLEoKjZmf1ZYdFTkWwmoBWJ2Uk5iOD005BAFZEPkTLFbTJRw1m8IeMyAJTgzwjYKXC7MsmShFGcAMV+AAxAgEAbkyAwIByOmR8Ymo52Ql2utzAFTg8OerFe7zAn2+yGcQIAgkSgWCwBCoYdMp1+gikVAbpkAELJOmY7HpD6kL4MH7AgEk8mUiAAX2GrgAMlBcKQzMgKLlkABVACSyDgqXglFCEAA7pxFYjOFh2rKzFFPiYYBAEp8ogbbIrWGlgAA2IhugC6A0QVIJyElcDoIitNuQAFpkFlyBQmMldUdkAajeFiFAGLZ4r7-Um0xnbFFclB7AwUTHKPHQhTc9CIEmk1KOprkGRKzza4dwsYLVQNBQURA4Hqou1CpqmscwAA5YeB5vJSfSKBsrnZdakVj+PEMVh+mv1hvUw9H0brTbbVux+Od41YHsUS25ArFDRRWFy9C3E9H6G489bFEW6pJIQhNLeSaZB4IGhgBl4UKQfAQMQbL2PukI-r+rZwS6yScFi8RrBsWysFg+RwLgCQDCKWFJsBeRULYaR4QRREXqR5GUdmNG0Yc3B4UOPR9PImFHEMonHlhrjQQxjxXu2i4SXeD5PnkRQlO+lRfhBf70ZIjxAZqDFgYQOnUmAAAKYgRnpoY8kIe7gUpSZsSRzH4QOrnbGRFFUTxvH8dw6S9HSSniVht6uKqEACdu14dkp3YQKYj4MCWnCkFEhRmAhtrfrx5mBUOlrxYupnOX+NT4fMMpIbFAD8TkFdhxHbGk+xgHG7IoJkACa2yTpkdArluCKZNOjRgKKGHNbZjwZGAw0JvIYC3uFv6RSq6BLJM2UULlt5JSlUQSMEEBZTl5D5QVmRVDt0SFBQEBNTdYDKttEz+DkamvuUWkvbxKFQLoUQLY9EARto-AZrgmRrcMjbIHcnA+OwdlsuGUZ1A02E-SUyAflU-opuwd7ppm2Z+olJrk4Wxalii2OId9L74xUn7grem3dEqax46UhPVHqcAAORtMg46Ih9UgQD4h0mipfOs2+gvXbxmT2A0mkc+VzWZDkpCbnFvKObrBVeS6FszQVc1McAJyPJkXrw0pm1uOseqtiYDA2CIWKfbeAACNillgfYULe9h0F7PvUI+tkZTcOYVYctvILsD5YJrmWq+tAXRxApB+0Z+m2FTzVJmIFDe-W42ITuei23DKeiJ4NfIHQUEl4xV4mygIAi0QItYAAVhsNy2wM4qrc9IzIAAEoytgLHdn16HquT1ntuV8HoKGbORZwQMH4iSDIcDqHQdAMQoJ+nef6iyJQ8SZ6vVBZU94lR8gUSU-6rhlE8AqXm3tfYvE+gEaObY4w8kTEcIcI4xwtgzslMwWAEGjgXNmf0tsnytR2EhFKWAvKGRgkIbBP5tDRDTigohuDbLkLzrvKIRV-C0LQawkqClszp12JkLqK1-T-2QL8VoVAGAtXYhLYGclyBsG7onf0LRkjiIMhbdOex8goAtsAfIXoO5CGQPkJC8iYJqJwuKH8wj3r3WAduZ86kBZaWTIaUmK5kjIG8GleA4i4FdhNG-aIStHHayqGrBsGt6g53+mbI8SDkhpAwfE62R4LZpGUaowsVtby2zSFQ0hslbApIbKwtI+EWExSCv6Jhwj3akE9oXKQLR0xnX9OERpnBmkTETkBD25YHG-UFlLe6tgACEk5XjoDXPAXQkRwRTSIOAaA8BaBgDEAAR0sGIbUcQw79meLiWMcdVkKBgBMeYRc8KFAUBAa0eAFDXCWLqMyqBRReiAA)