This app demonstrates:

1. A single action button that triggers the modal
2. A modal containing four different modal buttons showcasing various parameter combinations:
   - Basic button with just a label
   - Button with an icon (using Font Awesome)
   - Button with custom styling (using Bootstrap classes)
   - Button with all possible parameters combined

The parameters demonstrated for `modal_button` include:
- `label`: The text shown on the button
- `icon`: An icon to display (using Font Awesome)
- `class_`: CSS classes for styling
- Additional HTML attributes passed as kwargs:
  - `style`: Inline CSS
  - `id`: HTML id attribute
  - `name`: HTML name attribute
  - `type`: HTML button type

Technical notes:
1. Uses express mode for simplicity
2. Includes Font Awesome for icons
3. Uses Bootstrap classes for styling
4. No external data files needed
5. Minimal components - just what's needed to demonstrate modal_button functionality

To run this app, you'll need:
```bash
pip install shiny
```

The app will show a single button that, when clicked, opens a modal with four different modal buttons demonstrating various parameter combinations. Each button will close the modal when clicked (default behavior of modal_button).
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMpwR6KAHM4yUnQpclYFSxxfOAB9QIpWAAopCgAbOABeOTAAWVJbKGTkACEzCnJkABE4GFJMojpOZOSoACNUtIAVBhM4AEonCFcAQVtbZAAxchFBgHc4VmZ-AGE3NzDOLHZxWyiySmoKeIVkY+RwgAl2rIAZeIByAB5k7gBrUThkjLBWClxUjjhPJlkOwxHRPuwKBR0KxEAB6WHEWwQABWrCwxGSpBMtjoTTE6OYsKgyKgGlhT2arFhdEmAFooLN5vBYQA2LAAFiwACYEboiY0sDBuOjdJkAHy3PoQKUuZCLMRQKjIKDIXYUKDcBzIGkMZAUTbIZolcgKaacfWndbEKAMWzxHqII4ncLW21RTZQewMQ7ZXL5CpVGpgKUnS1YYxmKISYIQKJGyHkQ4QUOhzIcUjTWrIJ0p7NgNzsDPIHJ5ZJZnMpjFQXRRT7NCgQWnafg23gwWkAZkyFZlEAAAgrJDI4Oo6HQ4JIFAPxEPZOpZJR4hGKFh09MpfY6CoM1FqqX7Y7kyc9-60mGT8kk7njuF0D72lw9BfkPZqhBvgxFXMX5wxw59sgz7xqUya7PUPgmJ+MahMGBAVqGSRtJkJb+sUCbJpU1S1PBJziKwuA7JirDpJ03RwUeuY0qQVAMGkwA4bm4S2DIV7XmxriFNWnDEIBfoFMBJoUWxKbhBecbGhArHCcJmScaw3FFBJ2FCdJuZVjWnzwLSXLdipqk9ORqkpgxwmuCh-EScgZoWtxglGaGol8eJ6FSfZDnrKw3iSSZbk3us6o+GinDxOprC1pkdBQLS8xPKMkW0sQmzEK8WkAIyZAZPm+bJlnWewyAAJK7LpvkppleluaF4VgPWjbcDSgFwNpJW+eVpVZbmrhuD8qSjEBSkVcJjmls5IGue1+Y9XAoxoSBymlaGVV1g20UmMQxBzE+TU6WAHVlYZ2WDex4wmI02riBQkHTbxpaGgNpXDfko2JntbHhJ5UDeUdvnhAFQUhU0GkRVFMWcHFIPqrqaUZQdC3GWAYynQUYwXVdM1Kbt33SW1cOqoDYXLY20w2hA3A+PNuNg58dBI1E46KmjcYNi1bk45V+PVbYtK4poyDIiY3y-rgCWTPstLULYLPCSG14ALo9hWj3JFEa7xBevZDCMbALKqouUHqpB6ga3h+Ka5r5eETS4FiFA7KQyQmDAsbTJ+d4OhWeVhq6dru4NLo2tsHpej6BXvhQXRDiEGUmZkixPMlRv+AJyYtKQsgG9u0zKjd-qe8xf42CIydsFNaJS6mYAPv4z7WsmzT+BipDEaMzS8Bi3HPGTyo8AEW76knEl6EIeMd13NvyfYic58kWCZGAAC+stAA)
