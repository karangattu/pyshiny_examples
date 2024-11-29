Here's a Shiny for Python app that allows you to zoom and pan on an interactive plot using the `render.plot` function and the `click`, `dblclick`, and `hover` options:



Here's how the app works:

1. The `app_ui` defines the layout of the app, which consists of two cards: one for the interactive plot and one for displaying plot information.
2. The `server` function defines the logic for the app:
   - The `plot` function uses `render.plot` to create a simple sine wave plot with some random noise.
   - The `plot_info` function uses `render.text` to display information about the user's interactions with the plot, such as the coordinates of the clicked, double-clicked, or hovered-over point.
3. The `click`, `dblclick`, and `hover` options in the `output_plot` function enable the interactive features of the plot, allowing the user to zoom, pan, and hover over the plot to see the corresponding coordinates.

When you run this app, you'll see an interactive plot that allows you to zoom, pan, and hover over the data points to see their coordinates displayed in the "Plot Information" card.