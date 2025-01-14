This app demonstrates:

1. All parameters of `input_task_button`:
   - `id`: Unique identifier
   - `label`: Button label text
   - `icon`: Custom icon for ready state
   - `label_busy`: Text shown while processing
   - `icon_busy`: Custom icon for busy state
   - `width`: Button width
   - `type`: Bootstrap button style
   - `auto_reset`: Whether to auto-reset after completion
   - Additional HTML attributes via `**kwargs` (class_ in this case)

2. Key features:
   - Custom icons using Font Awesome
   - Status display showing number of times task has run
   - Simulated long-running task
   - Proper button state management

3. The app is minimal and focused on demonstrating the task button functionality without unnecessary components.

To run this app:

1. Make sure you have Shiny for Python installed:
```bash
pip install shiny
```

2. Save the code in a file (e.g., `app.py`)

3. Run the app:
```bash
shiny run app.py
```

The app will show a task button that:
- Displays a custom icon and label in both ready and busy states
- Shows a processing message while the task runs
- Automatically resets after completion
- Keeps track of how many times it's been clicked
- Uses Bootstrap's primary button styling
- Has a fixed width and custom CSS class

This implementation provides a complete demonstration of the `input_task_button` capabilities while keeping the app focused and minimal.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAApQA5nGSl0U8j06IWQAIyhWTmI2ClwAG25PBUscLzgAfT8KVgAKKQo4uABeOTAAFQiAa2QAITMKcmQAETgYUlKiOk44uKhQwqKyhhM4AEonCFcAQVtbZAAxchEpgHc4VmYfAGEAZR2+CGQKdh8TqDnWOElOcmTOLDPbdLJKagochWQv5BSACTKALIAGRyAHIADwJCDVMRxEpgVixQocOBwCilZDsMR0eHsCgUdCsRAAemJxFsEAAVqwsMQ4qQTLY6L0xLTmMSoJSoBpiQlQqxicFKABaKBrDbwYkANiwAHYsAAmMm6Dk9LAwbi03SlAB8oPGEANLmQWzEUCoyCgyGIUAYcwa1qWUG4vhMDCOVTC9UaUDsMXNJlYChWnGOP3uNrtOROnE8ePhAGYAAxJ9AaUqjRCfb4pSNPR4OD7lT11fGNFptDPZr7V5CuFpdCA+Y7Nz2hb0QWspYxmdIUKrpdtliAfQ7fcecWzw-usSqDiidwi18e9UJwOGlABKJkOFVnHWX3yi5CKKX7nhpnBydIirHS8LoUGFGwSc0fwvQvVwGYIh6+q-XQdA1weE3CYYh1kiCBPCwWCDzHccvmPCAgNYECzy8S9r16XR71Kd8X0nZACPQbgm3dEjuB-P9rRwu94VCBcPwYfhbV4GBhQTUpayNBDkAAARsewGCwKgNHRPj7DoD1Z3SREA1yTMaLIHcRCKA5TAoUSB0YkcDUQo9pJUyhkCKdSkyzPiDK+MQKDdQ5Sj3ap2AiCBQREeThDgOZcDRbirO+Wz7OIxzPRcvQ12oUQd2QEBjIoABfI5+HWfzjQAUToOgrhEB0XLsQojhOGTKgUQTxGuWR1CynKyrNSq4HUWRKByHstJnOddINKTMV9WxCj7KociUvj+EEYRkvgWtXB2fgTF6C0rXpaDhWGCAIESEraykeAsFYQo4HQHIFVGMAEoAXSAA)
