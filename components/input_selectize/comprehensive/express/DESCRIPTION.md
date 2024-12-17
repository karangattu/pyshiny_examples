This app demonstrates multiple ways to use `input_selectize()`:

1. **Basic Selectize**: 
   - Simple list of industries
   - Single selection
   - Basic dropdown functionality

2. **Company Select**:
   - Nested dictionary input (with optgroups)
   - Multiple selection
   - Grouped by industry

3. **Advanced Selectize**:
   - Custom options
   - Placeholder text
   - Maximum item limit
   - Ability to create new items
   - Multiple selection

4. **Remove Button Selectize**:
   - Tickers as choices
   - Multiple selection
   - Remove button enabled

The app includes:
- Synthetic data generation
- Multiple selectize input configurations
- Reactive outputs showing selections
- A data frame output filtered by selected tickers

### Key Features Demonstrated:
- `choices`: Different input types (list, dictionary)
- `multiple`: Single and multiple selection modes
- `options`: Custom selectize.js options
- `remove_button`: Optional remove button
- Reactive interactions
- Data filtering based on selections

### Installation and Execution
1. Ensure you have Shiny for Python installed:
   ```bash
   pip install shiny
   ```
2. Save the script and run it with:
   ```bash
   shiny run app.py
   ```

This comprehensive example showcases the flexibility and power of `input_selectize()` in Shiny for Python.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5ZqCAE1JgB0IDJq2QBnCszoQA5gIBmzXsgq50U6ciEs2AETrEKRADJ1xRAKqDyAgVpHpOXKKOTPk6LvMUwxACym4moza7HBQBnQAbnBeSqL+ELhYcAAe6Mxwoi52bFLoAK6GodxwzET5dDYQAMTIAOLUpVBUYriUvnAU+shOFFACXHByyNKNHFQA+mSMnHSZABQAlMgAtAB8yHoGwOJlm-oUOxJEuwC6p4gCyNfIfGB3dw0QTS1QyM-icFw9B3TkUMxAqRhtMHIJMiNFPl0F9kAAjQJSLj5XZJB73e4QG6abgoiRzFwAXmQICu2JudwAKnBiL4IKQADakaS4O4oUlY8lcu4AQR5AAUjGzbmAeZgGXBkABJCDELB3AhkrnYu4AWQAygAxSnCtX6RSiYFsADCLGEzT+EAVt05yopYDqAHlHXUhbReQz0L4oHDOtLZfLCEq7SKeaqAFoAOV1opgUAAXuQsNN-XKHrbyQBfRUZlVgTVSTjEGK0Dkh+0AKX5qpjVdVLGknGQxu9oklADJm6RAzny9c7gAhHnGmMDzgAa2QwOQPPgkmI-SDueVj3VMbqjK4cax6vCvlECuDdrVa-dYHrzEbO76EAlrMxduzR-tAAkwgyKL4FxlhWW+3cK0jCta1IOlDSxTsK1AiBwMPZduTAflNQAURjfk5DoeNSlTHtnwQ8xIxfGNLDoKguDfKAP18eooXQOC+xFVUACUAGkY1VUpiEnTtTUDPDkEzYNBIzDIKHyZgsSRPFJEyKpaieF5JQ4bg4goUguPcUo5BYbdix6Zp+hKYZRmecY4AmcR1PHCYYWYbTmF0uB5lBWZMhQLZDl2IgPKOPYzlOZZ1ncLgsB0AzNQ4eBLgzdFHjGZpJVENpP06bpLI02z7Mc-S+j4jFg16N5iWAU5g3snFkVRIgXMSCYuAOHFkBqgksFIuAYFEJZortcqui40oiGgeBGpq3A6oOVqqA6rr+OxQqsAwGFuHmP8GOuABySl9HHUp1pQPqdrKWblXW00ZkSPb3lgOBezWjaZUqiRcEuqSquOrl1v5ec4EuqFluUngYCwfJBCy+YAFYAAYiChyHFiIAAmeH3vJT6tJ0osfpQP6uHmAHeGB0GdPmFYEeh5AAGY4cRxYUczWmRM6cSsQ8ULwsipzCoZgRamNDIEvcKBRindAunIFxHGUUiJQECocCF8zSFFzqugoCVCTudU4AlCIsP9Ao2HVXxSAAdwXNtrQwhkGR9dXKWYfI4G5mp6nilpCoEZqIWJEzFKmXgwQJJYBHS6yuGGH23fM0ObPRhzMecgPXNEZ3anVOhBjhAFkBN0jqMiAE-hRMRtZpLo9byQoDwgXPP2QOXRAzuAs+YGaM1qMdG+IEudfLyVK7YWvqMbxgJWQBlTAoYM5YHizS91pz+LuLOu7n3vrSXsBO+6LXe8wksiH42lSH0TJCQn8RE-OlqdtwTrFmR+DkBgfIPzodB1c1SiLYzZ3sTT+efcc55x+BEf4gJkDzCVhQaQtEGbYhnhAA2a8y773mJvUaKCDAbyfprQBXZr6yUIDaO0x9T6iEJF7UQt0uQvzfh-OAhJ7aO2DH-G4AC956yHk1PEShoGWmrggugrUkGFCwX3dBuC0BcALrKL44icHHlFDIzG3xd6oKwoo5UZDiwUKoTQ8kdCugMKYQ7G6-F+Hi0JKtEMdwP7hDgMbBkgxmAxnUQYJqSdwSiCwL4+i-4wBxhSFKKaB5aAUwMUo4g-MqDCmYZKZAtQeTW1Nk1GJ6h3hwBNpoUJ-FhLYjYdcDhGjJTcIyDAUg0R4SFDUlaDMiDkFtk4YvKR5TKnR0AVohC7igHcKYu1dpyABw1OsMQo+xtyGEhjuHYAm1tq7VOFgNSF8KBLEiTcIx787ZmPWdcNp0QJhwhGRAUxLDf5yWQKqKAUhPGUGoGwAEYQBDcLljbXApAxFkAZPkGAME27-32KIexgQmll1hK9fEskMwAAEMglGYEs1IU8MyDGGPEU2EwIUyXvt1ZUolmbIDkHg3usIHrSQJOyAeWAV76HEUsQSmJgy1D0ECt5PcwXfCocGWF1AXGIpSMiuaQw-AYqof85UoKDCwmJFSzBkrVnLBYMgEqR8vEEgmCs5AxUUajUJUqrFiIsTythCjcquqblUKwKMVZBqiAgHplgAu3yFjwOVKVJ++KJKEuJRyghgc3IknWkQdaWAABWJ8IBX39aIDVk9FgMqqACo2qTQ6aTshjORermDsqld8A6pRBE3B5fCrAhUJgKGugVYVMdMoZuLOKrkxrvgytERQLA+yOm9yWFObNKqn50GGPSNgTbcXlk9UatSXE6pEo9UzL10y5BHCstO2ZW1+rMHWos0wUh5hNsWO6plyBk3ZKgCouR3x5X7x6J0a5DJC3XGLXyqgAqq3DFPbI4sXBxF1RvXQO9DbyRNq1TiA2C0z2frpYq3t7q7Tju9coj9sIemWnZEG5AIbw07r3QysA2YSSQGurQMAGQACOFRyn3J8RQAVxCwBkDuTQFAmI4wUA-qQNWdA4QCAgD8vAAgwROGrijXDpwgA)
