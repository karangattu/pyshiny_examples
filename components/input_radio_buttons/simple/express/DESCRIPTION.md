Let me break down the key components:

1. Data Generation:
   - I created a synthetic DataFrame with employee information
   - Used `numpy.random.seed()` for reproducibility
   - Included various data types (strings, integers) to demonstrate flexibility

2. UI Components:
   - Used `ui.page_opts()` to set the page title
   - Created a sidebar with `ui.sidebar()`
   - Used `ui.input_radio_buttons()` to allow column selection
     - The first argument is the input ID
     - The second is the label
     - The third is the list of choices

3. Reactive Output:
   - Used `@render.table` decorator to create a reactive table
   - The function dynamically selects and displays the chosen column
   - `input.selected_column()` retrieves the current radio button selection

This app demonstrates:
- Synthetic data creation
- Radio button input
- Reactive data display
- Express mode Shiny for Python syntax

When you run this app, you'll be able to select different columns from the radio buttons, and the table will update dynamically to show only the selected column.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5dKCAEygGdk+7LgB0IDJq2QQAro1wD+EdKNEAzZqRjJeACzoR54lm2ZwoxCnQBucNRq279uLHAAe6U735HJ+9NIoiU244ZiJpOhUIAGJkAGFTKCptXEodOEtiZB4KKFElLGZOLk0sXjg4LgAKABYAJgBKURyoZABeISwAESSoADEi+CqQUWQx5AByADlYOAmUYAmAQQAbOmI5ogmAIVIAIwmtuJ0oZjXNyZ6rOi5DyYBRGwmAXQJR8eWAczmFuoBWIgAZgADECAcgaqCIX9Xu8xhM4nQKLh5shFlM4AB3ZAATRYAGs7hMAMqcZADTjEOi8MhE47rKCfUhE3a8CjkInEswUCgrOawiDjSaklanFELP7AqVQgDskqlRAAbNKoQBOFVEAAcKueogAvk0IKJYgAFRlwZCWXkW4rZOA05h0dCWciiCI4c0AfVIzt4VStfLawjAACUoFw6KRkNsAuzBV04DBSMHDcbkMSbnA9qdkJikTpkEUI1G9rHyLxRHmKAX3bxM9nmFUGog4ch3X4Ap6i5HPaWeeWqq2hcHynyLJVPWQVrIjYRkEPxsHjqRSOUBMgpzPLVGI7x0KLcC25wuxsBgzN4MGiMGlt8r-OwIjkffgyKxcHdYLxqmYsgALJQPoG7kFQlACIkogAALBFwoRYLkex8s0cCqNk1L7lAuCei0TYtl+YyxAA4hklrpNocBjlQXDAdOMCCuomiFuGkbIH2cYVvh5GUROU7tMgHYUGUFFwOOXCTqQtEQE2ratrEIYZNIzCCtWFotOosy5vmyDkCs8gqVxIlUTRM6tqYFCKYKLTAMAo6GTxEnPM8YB6kQ4DQPAtBgKYACOESmPAlC8PBrgUHOYBkJQ1ChSgYCiDAST7qQvJ0Hs+SyHgogcNwfBREKeXjM5zxAA)
