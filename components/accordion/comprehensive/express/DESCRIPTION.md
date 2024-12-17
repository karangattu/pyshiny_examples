This Shiny for Python app demonstrates several key features of the `ui.accordion()` and `ui.accordion_panel()` components:

1. **Multiple Accordion Configurations**:
   - `multiple=True`: Allows multiple panels to be open simultaneously
   - `open=["Sales Overview", "Data Filters"]`: Specifies which panels are initially open

2. **Panel Icons**: Uses Font Awesome icons for each accordion panel

3. **Dynamic Content**:
   - Synthetic sales data generation
   - Filtering of data based on region and product selections
   - Reactive data tables and visualizations

4. **Accordion State Tracking**:
   - Shows currently open panels
   - Provides a reset button to return to default panel state

5. **Reactive Components**:
   - Filters dynamically update data table and plot
   - Accordion state is tracked and can be read reactively

### Key Shiny for Python Features Demonstrated:
- `ui.accordion()` with `id`, `multiple`, and `open` parameters
- `ui.accordion_panel()` with `icon` parameter
- Reactive data filtering
- Dynamic visualizations
- Synthetic data generation
- Font Awesome icon integration

### Installation and Execution
1. Ensure you have Shiny for Python installed:
```bash
pip install shiny
```

2. Save the script and run it with:
```bash
shiny run app.py
```

This app provides a comprehensive showcase of accordion functionality in Shiny for Python, demonstrating how to create interactive, dynamic interfaces with rich, responsive components.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzhExEACZwGAHQiNmbLjyxwAHujGtWfAUJHd0AVwpFrndf0HDRUJcyfnX6d4qimAcjoil4uIhDWArxBEOjqmiz+VFLwZuHIyXCpcsg5ygA2FFBhFsgwUBToBaQUBZwARji41bXIQdUU6uoAxMgAyriU7NmcxJmVUMgA5tQqlZzk6sp0M3MMlXAA+qxQBXCsW8lQABSRMFvUFAycBwC8AKwADACUiOrIn8iqYD8-AOLrTZsIYUEZSca7famY5YP6-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-s-HYofxg5XTxZSJBSFkHoOgdAlHqHU2JrTcBZCUAJl6ve-HRNkogFFepWwcN63ygZLIVmv3Zx+PR1zKmqYcDDGzDmXNeYO0Flov+jTAGWJeGAGiRBwDQHgLQMAYgJGcDEPASg60KAoedmAUqVAaAoERCBxV511DnDwOoC2-hn6WuizyIAA)
