Here's a Shiny for Python app that displays a message if required inputs are missing, and uses made-up data:



Here's how the app works:

1. The `app_ui` defines the user interface, which includes three input fields (name, age, and city) and an output text field.
2. The `server` function contains the logic for the app.
3. The `@render.text` decorator is used to define the `output` function, which displays the user's input values.
4. The `req()` function is used to check if the required inputs (name, age, and city) are provided. If any of the inputs are missing, a `SilentException` is raised, and the app will display a message indicating that the required inputs are missing.
5. If all the required inputs are provided, the app looks up the corresponding values in the `data` dictionary and displays them in the output text field.

When you run this app, you'll see the following behavior:

- If you leave any of the input fields empty and click outside the field, the app will display a message indicating that the required inputs are missing.
- If you fill in all the input fields, the app will display the corresponding values from the `data` dictionary.

Note that this app does not use any external files for accessing data, and the data is defined directly in the Python code.