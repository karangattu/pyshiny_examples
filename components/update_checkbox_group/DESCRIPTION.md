This app demonstrates all parameters of `update_checkbox_group`:
- `id`: The identifier of the checkbox group to update ("checkbox_group")
- `label`: Updated via a text input
- `choices`: Updated via a multi-select input
- `selected`: Updated via a multi-select input
- `inline`: Updated via a checkbox toggle

The app allows you to:
1. Change the label of the checkbox group
2. Toggle between inline and block display
3. Change the available choices
4. Change the selected values
5. See the current state of the checkbox group

The update is triggered by clicking the "Update" button, which applies all the current values of the control inputs to update the checkbox group.

This implementation:
- Uses express mode
- Doesn't rely on external files
- Uses static data defined within the app
- Focuses specifically on demonstrating `update_checkbox_group` functionality
- Includes only the UI components necessary to demonstrate the updating functionality
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkTEQAJnAZETnBQoDEyAJIROUqABtkxdlJOYjhWBQBhAAkAeTdwgFEAZWQAXmRgOTA3KhYAQUyiTOy4FgAhAuQinORwiqqS5AARTIBdJwhXcLEoKmQKdjhkOk4GVhEAuGIAawAjUg1kAHMmE3Q+9h7kAHdOHz8ZwdWrHrgrBQcsYzMAfQnpuY1r5dJVgAoFZE-KsDvZ+aeVugCh8vplwgN7vNkABxQHIV47PbIA7II4nKwASmBEC+-kCwVCKSisQSiQIIM+rDgPkmVCsKQyWWq+TALXJOK+3B83DgKQAYr4qQosRAXDVyBQmD49BRSMgbDByGMGCdkL4-GjeugoCr4FRRudOJcIKYKNcqBoKO9IHAttcfFADj46mAAHK25AAGUd1Iq0l8Jl5mQAquhjnSvT7nWARRcrmbfg9rVyeebSItFjSXQAVdOZwYebkQQaNTisdAO3B+gO8gXSuAisUAWRMPikAFoqTTJEMhMhi1s8UEQmEIHGTTcu7TOAAvODvDmfTID274kfY3GZRLU2nId2D8HD0Ibr4BI+sIkxOJJdm4qeSU6XklJYCIABMbIpyBgrakFd52YMIGwrtK4LZtpwnY7j2dB9gObDQRG-o+IGo7jqa1z3lIc4LpuNp2lhpwnkuYDbt2Ij7sgABqNZhIQX5ngSF7EteZJfoR9KMsUeStLeXw-hB-4pIBwEQI2HTIKUZiyjisp9AwnAZrY6yHGGJyGsaGESFI5DXDM0nkNamryIQ3yhuGgzgpMfwLLCLxAjG7QAALdJIMhwOodB0LSCgueIbmyOosiUK88ZYMZIo2HQyDXK8GKIF+rjmaq-SDImULPKs2xeOwapIoIuicDMNLINqupwPqo64hcxmrtZDwAvZuG4py9KZOljyZQ5fEtcgDpOikYUrv11JxT1LWMSOg0ThQWArpNoRjV+d6IY+Q22phq1WEti4tSmxbTaaxpFnAaYZjScVfuJriluWlb+CYDCWCIYzqRAfnWLYWAWhQChRQ9T3UGayGBnFCW7WIFCPTidBgo9z0IeRnDkCgIBhR1jVvBiAC+mRgNjLRAA)
