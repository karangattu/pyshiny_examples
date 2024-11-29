Here's a Shiny for Python app that displays a table with pagination and sorting, using made-up data:



Here's how the app works:

1. The `data` variable is a Pandas DataFrame containing some sample data.
2. The `app_ui` defines the layout of the app, which includes a single card component that will display the data table.
3. The `server` function defines the logic for the app. The `data_table` function is a reactive calculation that returns a `DataGrid` object, which is used to display the data table in the UI.
4. The `DataGrid` object is configured with the following options:
   - `width` and `height` are set to `"100%"` to make the table fill the available space in the card.
   - `filters` is set to `True` to enable filtering on the table.
   - `editable` is set to `False` to make the table read-only.
   - `selection_mode` is set to `"rows"` to enable row selection.

When you run this app, you'll see a table with the sample data, and you'll be able to filter, sort, and select rows in the table.