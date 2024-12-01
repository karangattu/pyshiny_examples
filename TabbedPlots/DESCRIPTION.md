Here's a Shiny for Python app that displays multiple plots in a tabbed layout using the function reference documentation:



This app uses the `ui.navset_tab()` function to create a tabbed layout with three tabs: "Scatter Plot", "Bar Plot", and "Pie Chart". Each tab contains a plot created using Matplotlib and rendered using the `@render.plot` decorator.

The sample data for the plots is generated directly within the app, without using any external files.

To run the app, save the code in a file (e.g., `app.py`) and execute the following command in your terminal:

```
python app.py
```

This will start the Shiny app, and you can access it in your web browser at `http://localhost:8000`.