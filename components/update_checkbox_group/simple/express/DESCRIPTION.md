1. Creates two checkbox groups - one for fruits and one for vegetables with sample data
2. Uses a reactive effect to watch changes in the fruits selection
3. Updates the vegetables checkbox group:
   - Changes the label to show how many fruits were selected 
   - Automatically selects vegetables based on number of selected fruits
4. Shows the current selections in text format

The app shows how `update_checkbox_group` can dynamically:
- Update the label
- Change selected values
- Respond to changes in other inputs

Technical notes:
- Uses express mode imports and syntax
- Follows Shiny for Python best practices
- Creates synthetic data within the app
- Uses reactive programming patterns correctly
- Properly handles cases when no items are selected

To run this app, simply save it as a .py file and run it with `shiny run app.py`.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkTEQAJnAZETnBQoDEyAMJioVNrHQAbOGQrLygFRgcKAH1idlJOYjg9AF5kYDkwAEFMAPSidIAhKGhoXOR0gHkGIoBzeUIysABZGtJS9IBxKvQ6gF0FWWrqzjho2PjE5BS0sDcoBiYKNrB8pmIyP0d69IBldG4JdiWAFWYvVq2Zk2ITGAAjW3S+iBdkADFOBlYRGLhiAGtbqQNMhqkwTOhkGRKEw-HoKOxAqxfuQrMhyPIIA4sMYzKNfgCgZFQaRwQAKBTISkNcKcCisXIUqk7OABSTIGl0xBtCBUyFjBKsJIc0ZxAUERmUpGsqhWJLTLL+Op5ZZFVWPBQASicmM42IgpiiP3+gI0RLB6HJPKZYAGQ0S3N5zOlyAGcAoUFuAVYXMIEr5osSSVtwxF43pEC1zwgAAFPJIZHB1HQ6L9FtY4HRkJFSRquVbKa52m62CzU3BURzw7ypWWrJFK5M+PqzFhKzm-X7XABVdDBbzwwLBiZGgnA4ng5C3KBI1HkZCYu62NGZmuScvshgRKtUrHgvsjEcms0ki1+x02uCDYb03353nIPwellCp2pl2Xt0er3IUm4EnIPZ-nXEAAggUlVxletN1pVgNT4FdSzXOsGxZJFkAABgAXw3LdcwZO9eRiANBSHUMxTPKkIPLINLztMjEmARBQPAxDIMrODOAQ6VyygrdkFQwJ0KeXlIxeAARThWH8KBeAgzhyHDWNqBsBgsCoDQ0xsFdYgAd0iOSFJzPNeQbFIcQoVtoLpds7yHZImwNLA7Js3kxAoEwGB5Oh0h8sA-W2Vj10rFAQAAciIUKsAAKziMD2PgnCYP42FAlCgA5dFQsw-zAtROyQvC5BIpi7hSTsjjMzs5K0PSzLsrvXz0jATCiHAaB4FoMAxAARwcMR4EoVg1I0+owChKgaBQPyIBgLx-FICgNluBQFzwBR0CKYJwwo+9UEwnogA)
