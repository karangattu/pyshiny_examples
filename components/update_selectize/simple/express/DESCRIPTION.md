This app demonstrates several key aspects of `update_selectize`:

1. Initial Setup:
   - Creates a nested dictionary of states grouped by region
   - Uses `input_selectize` with multiple selection enabled
   - Demonstrates the ability to use nested dictionaries for choices

2. Update Mechanism:
   - Uses an action button to trigger the update
   - Demonstrates updating:
     - Choices (adding new regions)
     - Selected values
     - Label text

3. Reactive Display:
   - Shows the current selection dynamically

Key Points from Function Reference:
- Used `multiple=True` to allow multiple selections
- Used a dictionary with nested structure for choices
- Demonstrated updating choices, selected values, and label
- Showed how to use `update_selectize` within a reactive context

Execution Instructions:
1. Ensure Shiny for Python is installed (`pip install shiny`)
2. Save the script
3. Run the script with Python
4. Interact with the selectize input and update button

This example follows the best practices outlined in the Shiny for Python function reference, particularly for the `update_selectize` method, showcasing its flexibility and ease of use.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMJioVNrkrs4UsTItl5QyHRCwXAw5KwUDF6c5ApxXnB6ALzIIArIechyYACiUHHupKUUhSg5EPn1BWAAcgCa1Y1NcADuyC1CANaFRLkNeYVNAFLt493IEw6scLhDBXWjjW4AKtNgbuQQcJKcxGaFI3kAvgTnjQDq6SJ7le2163cAgju3paoA5hTJQirN6FADyACUdqCxL9AcM1qNCm5PrQkVAADacCIMCCcKBnBHIK43QoAWU4ti6DxeN3qZKaO3JEAOrFIFHxQNp+UKtwAkl9OKwyBBWNwVlyxmBeSiUIVeaQuhybhcFCqIC5kAAFKC-ODIKQUdF6qB2KJChicdBSZIQSw4HVwAD6pCtrAAFAajRlCgBlOBGo4ALz1AFV0CFvAARaKkQoASicEFcvNxUgxbH9hykwb4EFMIi6nAo7GQ2jg9jo3HLyGI7FIx3SCjtxjMjsWAezcDdJLA3CLePRbfZVFY4sJctTA+QPuH6WnmaOcOB+VSI-h9RgJnRUnQXs2DBM8ggCfVSeQACEzAC6gD9RbfrqGMgTOG0k3OFgWxRHRJrRBHQARle5DdmAL4Rk6AEUOqnJgGGEHzh2nDBvGiauOC1D2E+xZ6icDA2CI7ZZkkp4AAKeEcsjqHQdBZgoFbII6bpxogNyuLc-g3v4yBARQ158HoxCYsQ-TlhYr7eDhGZITmX43F+WDgWkgHQcxJKEnaSlUG2C6dt2hJ0r2k4YkOaSjpyBn5K4ka+LAxwYuivC6gcCTeLW9bEHOAGlNW5BsMweroqQvzHBKNZ1g2rAZK8bzcs0swYSFsQ0pZsWNJsAAaOybJopRjmliJgAAYgAMjsRVBRaIT5QVhluKCOx7JVUC2LGYBhfUapvMSqXIK4fodsgYSsCYAGLCIpB0Pq3EHD07mRWFRGSOWGTAIUmXisVZVgAAutcvWuPBaTTYFUAAf6+qkCoCr+fAxbcL84UmrqthheiZ3+hkdCFEdVC2NOs56G6bjCaJ-0gApWmQapcYXPq-DpAm7WEieGoYXYDgnTWJj4dQhG6SRCjkZhDhYFQGhVBjU0cAqOlISBLE3GIFA43U327DjBGIcR5A1ApfZpoOq7pMxKpgGAVzZJAsAICgYBiAAjpYYjwJQrBkxTQJgMKVA0HLCgwF4u5spiAEKLaAjLHmJohKOp61RLO1AA)
