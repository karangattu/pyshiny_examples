Here's a Shiny for Python app for a bike and pedestrian route planning app:



Here's how the app works:

1. The app has a UI with a panel title, a column layout with input controls for route type, maximum distance, and maximum duration, and two output elements for the route map and route table.

2. The `server` function defines the logic for the app:
   - The `filtered_routes()` function filters the `routes_data` DataFrame based on the user's input selections for route type, maximum distance, and maximum duration.
   - The `route_map()` function creates a Folium map and adds markers for the filtered routes, with different colors for bike and pedestrian routes.
   - The `route_table()` function renders a table with the filtered route information.

3. The app is created using the `App` class, passing the `app_ui` and `server` functions.

This app allows users to explore and filter bike and pedestrian routes based on their preferences, displaying the routes on a map and in a table. The data is generated within the app, but you could easily replace it with real data from a source like OpenStreetMap or a local transportation authority.