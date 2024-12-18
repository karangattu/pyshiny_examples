This app demonstrates:

1. A simple tabbed interface using `navset_tab`
2. Three panels: Overview, Data Table, and Statistics
3. Synthetic data generation using pandas and numpy
4. Basic data filtering functionality
5. Multiple rendering types (tables and data frames)

Technical description:
- Uses Shiny Express syntax for simpler, more concise code
- Leverages pandas DataFrame for data storage and manipulation
- Implements reactive filtering based on user input
- Uses Bootstrap-styled navigation tabs via `navset_tab`
- Includes sidebar layout in one of the tabs

Installation instructions:
1. Install required packages:
```bash
pip install shiny pandas numpy
```

2. Save the code in a file (e.g., `app.py`)
3. Run with:
```bash
shiny run app.py
```

Package dependencies:
- shiny
- pandas
- numpy

The app provides a clean, interactive interface for exploring the synthetic sales data through different views and allows filtering of the data table by region.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5dKCAEygGdk+7LgB0IDJq2QQAro1wD+EdKIBmzUjGS8AFnQjzxLNszhRiFOgDc4q9Zp17cWOAA90J3v0OS96aRSITbjhmImk6UVEAYmQAcWoQqCotDTgtXEptOAtiZB4KKFElLGZOLg0sXjg4LgAKAEYAJgBmAEpRXigAGzheAH18qGQAXiEsABEkqAAxUvhakFFkZeQAcny4VZR0LiwNvtKIAHM4Wt4C1mHVxoAGFoBaG-rH+tWidBC6Ui5eYfqbm5ENRwACOV3Gq1aBCWK1WJmsMk2KGKh3KMCwEBYMG6DQBgOQt3x-xurRKpGk3FqjShMOWqwpdAovC2UmwqIqqL0FFqAFYiXyiMSaRAVmsTEcvhAWSiyhViNpSHRiKdgKsAHJGbRvNYAZXJFC1RFWAFE+BRtasAOq9c0AXUFAPaEAAvk7osgddl2FATshSOgLOReKJwjgfXA+v6mbULBQesNhGAdd1eshJjoAEakKDMESEZAqOhdLpQDPxgAqzGkcDdEBiAGETEk0gUM1U2AB3RnaKRQSx0I5JSWiLsG5Ch6CWdt9Vu1OhcBNgVvBsCtRC05Ab0c9id9vocCBwLq1RMAeWszH7cA7ibXG9Foe0jRPSZT-HPISvN9X95Wv+WAACQRcCEWCtj0-55HAKhaG+fS8LI2LMLgtR3iKooYcsCEwEh8ijJ0PT9IMWBHOo0joBmKFwnAErkJCWA+kcCyQZhdLwtQ1Ysqq8CcBa2GrPaLGsfSYhMlxqw8VKRr8baQnLK6ZIUnU1JyVoiE5k4ZBdLIED8KMqoAIKWEcyAAEpwAinFGuWpAFF0ZkWRxmxGkZJkAKqicy1m2d0yAeYyzKyehrErCYFDSMwIrYbhG5bt2450Bie4HkeL6TAUyDlqWEGruuwUYY+z6JqZUAdmmUy3pBkHbglWAlrg+rwfOcAZjmqF5SFoo1aGvDNa1zDtapD6Jb4-jwUecDmCe+WdaxibipKfSFl0VDMIm0IzbNGGJp6PTmA5tEQOtQ2sfKirKr8wCJgZxaJrayAANTIF0dDnGccGDKqC10baWAMiC1aoU6W0YcDW2qUB1AgcwexTEtcw2JtmEgTBy2rTUAxTINSOdXQMGjRQJQ0YtaMhKhIyjNdt1ICdmFhRFUUfRVOMhfTkWwYRmMFMABG9FzUBfcTP0U8gBNE4dS1FqtqFBaKcVjrulj7pwqU7QUFjnEqK5oSFhUvjq6uvTkvk6upyGVTjkGQ8EMPgYjIUo1o6v9NFGnYyD5xJHpHN88RIG8MQzB0BmpykmRlIqSzoXZAzTte8AguWc5awMmJtq2mAzpEOA0DwLQYAmADdAmPAlC8GBLgUPmYBkJQ1BVygYCiNiFDoF0tkvRmRSyHgogHjwwZHVHyyZ7aQA)