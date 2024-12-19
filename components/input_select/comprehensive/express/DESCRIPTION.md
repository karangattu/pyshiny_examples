This app demonstrates:

1. All parameters of `input_select`:
   - id
   - label
   - choices (including nested optgroups)
   - selected
   - multiple
   - selectize
   - width
   - size

2. Features:
   - Nested choices using optgroups
   - Dynamic updates based on user preferences
   - Interactive controls for all major parameters
   - Visual feedback showing current selection
   - Documentation card explaining the parameters

3. Layout:
   - Uses `layout_sidebar` for organization
   - Cards for different sections
   - Responsive design with `fillable=True`

4. Data:
   - Uses made-up data for US states grouped by region
   - Structured as nested dictionaries for optgroups

To run this app, simply save it as a .py file and run it with:
```bash
shiny run app.py
```

Package dependencies:
- shiny

The app provides a complete demonstration of the `input_select` component with all its parameters and various configurations. Users can:
1. Toggle between single and multiple selection
2. Switch between regular select and selectize.js mode
3. Adjust the size of the select box
4. See the current selection and settings
5. View documentation about the parameters

The app follows Shiny for Python best practices and uses the express syntax throughout.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMqx0AGzjJbUCihkAHdOCnZkCDhWKls2CgYTSRMxZDohZFJ0CgBzJhN0VgUYgOjkAF5kEAVkWuQ5MABRKBjkAGFSFooGlGqIOoH6sAA5AE0eoeG4YORRoQBrBoIawdqG4YApCfXp5A2HVjhcJZXVhraAFW2wDogoyU5iMwbT5ABfZf66hoB1aJEOl0Jn1VmswD8AILXH4tVQ5CjkE5fM5gADyACVrqixDlEYRXgNzlDaOcoF5OOkGBBOFAXsj3p9CWAALKcWzBf7AgnfFnDa6su7RUiBJGgoY-ACS0M4rDIEFY3FFoIaEuJKBVpGCtLArzeCj1EBc7jgInQUByviyUnIRQglhw5rgAH0rawABRSCg+coNYxmJ2HHySZAAETgMFISzSnC8XigACNvRdEnAAJROCChcLIe1x3Ckf0K+zxqAMN2pxCvLMRe1FuAlssV7m1e3sAAsbvO5ASpC8yAAClAol4Gun6QN7X6KE7iOw4MR5vHSBpO2AYCYvFJvPJCENGtBE7515vONu2HAg9bDbvpGSTHBygAxMmHMdiycQUzT2fzxfL1eBvOUgAF47kQDQAKqHOel6cKBWAAFZFDed4Ps+Xivs2OacFgU5Ona8AMI8AFwWBQxuKRyBunOnA5OwRj9GE4asOmKFePe5QAKxvsq9LVthWDEKWtjlpW451PaQkMLYTpzlA9hlg0ABCLSPMal6jlhrgqQqxAwUBIRhBEZJ9maDCwCaBxYQAAjYClYJYWH2HQ+mSE6U6iVhAxiBQKT9B+X4BheQGduJYq1GyPpgCUVBKuFgxxvGF5RW07CkKQ0ExXAbosZW+JheFs6kI80TlFlrCMvFgyAZIcC2FFYwNHwLkQMKfCfmYWDHluPjlsgF7QcA6zjLuRINAAupVVV1N1p7elOXUbj12WplN02uSBD4LTVm3lmt00KqBZUJG622keWqbNZEbXbcFDygX1A2+MM5BwPtVWhLY4RRQAjAADH9ACkdLTWOVZGQJUkiU2BWScJsniApq5uHdsTIAAaqhOWsTxqy2dQ9lUBo3QFc5G11U6t7sStYnTT5flpA0cwmOTti9NtgRUOWeo6oafEQ3D0mebDOFQwj8kOKubQpDYIgoxQUgQDkyG44M+N2A4DmcE5cAuU8DCy0FCvcMrwsHSaivKxUVRecqLJLXNvgo7BeIoDEZYLbN24Xe98UNM7QGUcypD2BM7unR1FBYDt52pqttsohRoFURS10iDHoGsW7J1nQ9ce++FvxsuE1z-UDINVQa00J6IJoM-agTK1gtgyKF60SThjesDgYht+3gwvE4YCIcVEBusAdANCA8xvL00g82kGTzEQ0jteextK93TEwO6qbjaroM12D-PZoL0O06CZ-i0jDQhqQTzwJQAScHiB8d11pbzLYmpjy8Oq82KZwQCBylgslQBgegwwRnlAkUobMsJYQAFTIEQYgtkqCUAXDnO1L8fB7CUApJwBwVEGhZU0gVZBqDEoXgwcgLBvhqF9g4D-ZACZSCyGQOEXwU4kEoMQUVEqrBaEQj8I8K8pZeCkD1mlQRVF+JRBiHVeIiRkipEpJkbIeQCyFDfrUShiCdp1VofQ9qYQaSxl4IYuIVN7zY14agr2PhaE-DnFwhgyBHG+BjjaVhqQTKajqvYgxqNSLONcXOdxCIcyZRCfBJCQTPrhGMdgxJEQpGcOwVOEhYAy7AzALolBfDDpwFocMEwMAkruPSdvPQUTmEzDdMEOc-RWoMQ2pRCM9gCl-1HGAD4VRIAWVoGAMQABHSwYhH4UG7hQYmu4wByioDQFAvMYABG8MKck8YFAETwAoM0dgWgZmmn08aQA)
