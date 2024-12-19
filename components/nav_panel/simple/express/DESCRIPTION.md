This app demonstrates:

1. Three navigation panels: "Overview", "Data", and "Analysis"
2. Use of synthetic data (sales data) generated using pandas and numpy
3. Different types of outputs:
   - Plots (bar chart and line plot)
   - Interactive data table with filtering
   - Summary statistics table
4. Basic interactivity with a region filter dropdown
5. Layout customization using `ui.layout_columns`

To run this app:

1. Save it as `app.py`
2. Make sure you have the required packages installed:
```bash
pip install shiny pandas numpy matplotlib
```
3. Run the app:
```bash
shiny run app.py
```

The app will feature:
- An Overview page with visualizations of revenue and units sold
- A Data page with the full dataset and region filtering capability
- An Analysis page showing summary statistics by region

This example follows Shiny for Python's express mode syntax and demonstrates common patterns for building multi-page Shiny applications.

Note: I forgot to import matplotlib earlier. Here's the missing import that should be added at the top of the file:

The app showcases how to:
- Create multiple pages using nav_panels
- Display different types of visualizations and tables
- Handle user inputs
- Use reactive rendering
- Organize content in a logical structure

All of this is done using synthetic data generated within the app, so there's no need for external data files.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5dKCAEygGdk+7LgB0IDJq2QQAro1wD+EdKIBmzUjGS8AFnQjzxLNszhRiFOgDc4q9Zp17cWOAA90J3v0OS96aRSJpOiITbjhmUVEAYmQAcWpwqCotDTgtXEptOAtiZB4KKFElLGZOLg0sXjg4LgAKAEYAJgBmAEpRXigAGzheAH18qGQAXiEsABEkqAAxUvhakFFkZeQAcny4VZR0LiwNvtKIAHM4Wt4C1mHVxoAGFoBaG-rH+tWiai4r24em++bXohqOAARyu41WrQISxWqxM1hkmxQxUO5RgWAgLBg3QaN1xRFuNyIzQAbABWSHQ5araRiCi8LZSbAoioovQUWqkwnIeqcolkikQFZrExHOjkBnIsoVYjaUh0YinYCrAByRm0bzWAGVSP51URVgBRPgUDWrADqvRNAF0+eTRABfdoQaLITXZdhQE7IUjoCzkXiiII4T1wPo+um1CwUHrDYRgTXdXrISY6ABGpCgzBEhGQKjoXS6UFTMYAKsxpHAnS7lVBLHQjkkxYKOBA4F0AxAAO50CjaZBB6CWPottu1OMAeWszDrcE7cdaiEp-boWG0jTH8cT-En4Rnc7ATqF3d7y6whdwOoofTIXVkEF4tRvfW7XF7vGGwGJRGJVoXS6FAACoRcOEOBdKQFD-isIEqMgcLUBWw7geyf6CkK6HLDA5C9l0uAHHA8IViMWhbgMUxYEc6jSOgqa4GcpGDEqGyrFaewUFgWGZK0SrwQiLEcaYEC1IeGHoXmRxEFALjEegXTsbw0iprJEEPiJokrFJWCppmtScTheG8RWWB6CBLhEHp2i4fhhFwFgljdBWvBqepAguJU2R9C4hapqOqwALLYeqznqZpVRXrg3m+QAglOIbIAASgRCGbMFokmBQ0jMIK4mRGhGFAR8oHKZBeXoTB-a0v0xXCYupXqRZVk0j2-CjJ0PT9IMFFUTRdFtb0ZEFExSSbKxr4cYF3HUpV-EKTAwlQRh4mSdJoyyfJinFapC3oZp1UNXhTV0sZYRmcg+19IdvB2Q5vTmZmADW4RXKQELbUKoUeV5Ra+QFmSvXVokfeFkVdLUqwlhB3TIAAqtNqUYelmXZfWuXHn2A61sOnCjnGkwFPOtVCkGvj+H0VQ9OYG4ik2fR5nJ4RxkQcZuhTbCJaK5CM8gb0ucgMpygq77AHGUUFnGVrIAA1MgXR0Oc9HtQNUA8XAHMQPxTXAhWwmtM5S4FWEzB7FMtNzDYpXlX1-QFMWpyoepdCwST7HU+QtP5lQzDCSMowi2LSA88siNZSRiuDNtweClbSvANHjGwqrTYsT7yDOyUidu3TnvCVaqM9ujK6DljragyL0C4bwcsE0uQbaM0G7s02UMAArhComKcAq85LvrwGgTbPRLuVrsQGTshYswdH26Js0T-IrUMeRlE6j1YMjxCWCekcCyB8KSV8SgSrwJwpqzSxUIAxhU3NQyR+CafsgsdtjolDq3C1I08NaOPmZODed4tWQEqGKRwEr7wrKaCGBQuhgJsqaEBMNpr6igVDWGN9c6XzgtkJG38YBzzAPaIg4BoDwFoGAEwWs6AmHgJQK6FAXAUBzGAMglBqCMJQGAUQWIKDFVlqmIosg8CiBbDwDsu8CFWiAA)
