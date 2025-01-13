This app demonstrates:

1. All three methods of including CSS:
   - `link` (default method)
   - `link_files` (allows importing other files)
   - `inline` (includes CSS directly in the HTML)

2. The app creates a temporary CSS file with custom styles and includes it using all three methods to show the differences.

3. The CSS includes:
   - Custom card styling
   - Custom text styling
   - Custom button styling
   - Hover effects
   - Combined styles

4. The layout demonstrates:
   - Multiple cards in a column layout
   - Different styling applications
   - Interactive buttons to show the styles work with Shiny components
   - Click counters to demonstrate interactivity

5. Cleanup of temporary files when the app closes

To run this app:

1. Save it as `app.py`
2. Install required packages:
```bash
pip install shiny
```
3. Run with:
```bash
shiny run app.py
```

The app creates a responsive interface with multiple cards demonstrating different ways to include and apply CSS styles. Each method of including CSS (`link`, `link_files`, and `inline`) is demonstrated with real examples of the styling being applied to Shiny components.

The temporary CSS file is created and cleaned up automatically, making the app self-contained without requiring external files.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=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)
