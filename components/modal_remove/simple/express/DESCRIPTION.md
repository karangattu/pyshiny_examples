1. Creates two action buttons - one to show a modal and one to remove it
2. When "Show Modal" is clicked, displays a modal dialog with a message
3. When "Remove Modal" is clicked, removes the modal programmatically using `modal_remove()`
4. The modal is configured with `easy_close=False` so it can only be closed via the Close button or programmatically

Key features:
- Uses express mode syntax for cleaner code
- Demonstrates both `modal_show()` and `modal_remove()`
- Uses reactive effects with event handling
- Shows basic modal configuration options

To run this app, just save it as `app.py` and run with:
```bash
shiny run app.py
```

Required package dependencies:
- shiny

The app provides a simple demonstration of programmatically removing modals, which can be useful for workflows where you need to control modal visibility based on application state or user actions.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQss4oAczgB9UugqsAFFIUADZwALxyYACypLZQwcgASnAwpLLIAKIasOihkUR0nMHBUABGoWEAKgwmcACUThAu7ABM-pExcQnJqelZOXlgDRDOnFjGZp4SUuSepWYU5O1gHKQA7vnIkQDK7OvInfGRwy4TFFOSnLPzFIsQy2K98oRbYD1pcAexR0ONAAJiaYyODqOh0OCSBQA8SXWTqWSUfxnLCrNbDex0ZCefx1RAKZAE5AsMLIFypLrtCCE6mvSpcPScPRQInfBLwXTuT4UdhQETEKBU0qfR4fWzIbSkNwMWAwXmcfnFXBYfL4mkEoIVSIASQMwgFIiicA5HhVVLVyHErFwnmIwVIrHCADF4g6CKq1XRSKQqAwwmTWXMFktIgBhO0O47u5DDan+rqeVH+GDDKGA2EguBgiEUVMwqRwuAIihIiCmChYEWyOpbOyZrE4vFmglx+KeStwHH-Gz2BhYKgaHO1zEwVhuBtRsQUEwMKmh4LygDWyAA5Lt9odgsvkItkLZGbkoLxmeT4rvOPFJVhkGHFyv3ukN1ud+2+CIJVKZXKFcElZEwABfIhwGgeBaDAMQAEdLEeag-D7AcXjAMhKFgsCFFlChcm9edSgUJoBFwBR0AFOJWEac0aQAgBdIA)
