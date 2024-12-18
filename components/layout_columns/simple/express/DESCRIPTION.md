This app demonstrates several key Shiny for Python features:

1. Uses `layout_columns()` to create a responsive grid layout
2. Generates synthetic data using NumPy and Pandas
3. Creates three cards with different visualizations:
   - A bar chart showing sales by region
   - A pie chart showing profit margins
   - A data table with the raw data
4. Includes a dark mode toggle
5. Uses `full_screen=True` to allow card expansion
6. Leverages `@render.plot` and `@render.data_frame` decorators

Key points from the function reference documentation applied:
- Used express syntax with `input`, `ui`, and `render` imported from `shiny.express`
- Followed best practices for data handling
- Used `ui.page_opts()` for page configuration
- Utilized `layout_columns()` with cards
- Demonstrated reactive rendering

To run this app, simply save the script and run it with a Python interpreter that has Shiny for Python installed.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5CAV0d2SgGd26ADoQGTVsnRQIAE368B6GSLEs2MKBXQAbUhW10ARjlw69CydooiRAM2akYyPgAs6EHqonM4UYhToANzg7BydXd1wsOAAPdB8+AS82d3QOCiIOOiIfWThmGwgAYmQAcWp8zThnXEoXOADiZDkKKBEIbGZpGUcsPjg4GQAKABYAJgBKET4obTg+AH0WqGQAXkkZLAARTSgAMS74IZARZDPkAHIAJTgAczpyC5RgC4A5NRcLoguAZVJ0z7fACi-AoX0uAHV5mDvgBhagULraC4AXQIp3Ov1m8yegiwXVkvQJMncFCGAFYAAzUylEMY06lEckTdEQc6XAAKDlsdAoCwAslBmPcILiOvjur0OKJbCwYENKVhKeSiIqxirkMyRABfKYQEQlDlQW7VMgQHm3DhdALkERZHDGuALUjoCh8IYBfRwVZCMA-bECHauQykIXKQjIHnabRQQxzVYAFWYHDgeoNyAAgjIZM0hQBrZAwUgyaoUUi3W5zO10LCpdJLfMLIsloZ0GQ+sByZh5pvFkJgNPFZAAGSguH+bAA7ryXMgyNouBA+CJpxRZ-aY+P6-PF+6JogMWdV+ua8Qw0NbBxows+MQfNRE8nUwe2ezzvaz8wZAt6lAS8whl9f05gEQweBue5bQHQ83xg9kAAFcn-HBdGsV832aOBbGcAMFjMMl9zgjDLAoLALStOALzoW4+DoAAvb0hgADiIAA2CY9WIt8dFIwwhSGGYQIbVoXggh5RTRHChOWF5gJxFFOK484eKwT05iGa47nE2ZkDkgQOXyWVmA0CBiDgC5FKUkisBiGNDDgbQNLEx5LKUlTcDshyNL05AhgAEgmCyiIwlSYkaPN3QcVobQgVYRi1dClJ8CgrTZFTbmIWwhkHdlj2QD9z0va9b3vWKkxTQjEvZAqvx-Xx-0AsAuVIHk2EFYV3GXaCqvOYLkEQ6hkPwvqS2w+IWt5PDUOyl8rLOFTyJ8KiaPoxiWOQdjXK4lT0DoSjBPmYSoBeZrWoFIURVRIg+rm5BPO0PhVgOxYZM0yCJOunrbrOKB0hdfxVguABSABGLAQdsIGgaCr7uKsVTeXUi5Tt5ZB2pFUDwK0lybvOZLUusjKspy848pq4Yiu0G87wGMqn0qrjybqv98kanydlaZAE1jKtuq4vqBryZgsGWBZ7FgEJYdGqTDtaONKIZub8eYNlnqOsBtSIcBoHgWgwB8ABHLIfHgSg+FUsKIzAM0qBoFAwBEDQtFQgxDHaLg8BEKRZH4Qpbo1lEgA)
