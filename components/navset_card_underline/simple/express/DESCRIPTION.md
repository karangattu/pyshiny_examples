This app demonstrates:

1. A simple dashboard layout using `navset_card_underline`
2. Three nav panels: Overview, Revenue Trends, and Unit Sales
3. Synthetic data generation using pandas and numpy
4. Basic data tables with different aggregations
5. An interactive filter in the Revenue Trends panel

Technical description:
- Uses express mode for simpler syntax
- Creates synthetic sales data with date, revenue, units, and region columns
- Uses `navset_card_underline` for navigation with underlined tabs
- Implements reactive rendering of tables based on user input
- Includes a selectize input for filtering data

Installation and execution:
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

The app provides a clean, professional look with underlined navigation tabs and demonstrates basic data manipulation and display capabilities in Shiny for Python.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5dKCAEygGdk+7LgB0IDJq2QQAro1wD+EdKIBmzUjGS8AFnQjzxLNszhRiFOgDc4q9Zp17cWOAA90J3v0OS96aRSJpOiITbjhmUVEAYmQAcWpwqCotDTgtXEptOAtiZB4KKFElLGZOLg0sXjg4LgAKAEYAJgBmAEpRXigAGzheAH18qGQAXiEsABEkqAAxUvhakFFkZeQAcny4VZR0LiwNvtKIAHM4Wt4C1mHVxoAGFoBaG-rH+tWidHC6Ui5eYfqbm5ENRwACOV3Gq1aBCWK1WJmsMk2KGKh3KMCwEBYMG6DQBgOQ-3xhNaJVI0m4tUaUJhy1W5LoFF4Wyk2FRFVRegotQArETeURidCICs1iYjl8IMyUWUKsRtKQ6MRTsBVgA5IzaN5rADKZIomqIqwAonwKFrVgB1XpmgC6AoB7QgAF9HdFkNrsuwoCdkKR0BZyLxREEcN64H0-YzahYKD1hsIwNrur1kJMdAAjUhQZgiQjIFR0LpdKDpuMAFWY0jgrogMQAwiYkmloJYqmwAO4M7TIclccJdPQ1ZAFdNBiCd-U9ugYqCt7J9YjZrh9Xv9we1OhceOQWcJ1qIGnICfdkMtvocCBwLq1BMAeWszEsdDg7b3B+FIpWIe0zRvieT-D3uET4vnuh4iuBKwAAKhH2zBYCOPSQcsfYqFoAF9LwsjYswuC1PuyGfiYFDSMwwqdD0-SDFgRzqNI6DpnhcJwOK5CQlg3pHAshGfrC8LUFWzIqvAnDmlhMCrHaPG8Ws9KMkJqwiZKhriZJ0nLC6pK9pSjoyZ+h7HlOM6WOenBXn+ABKcAIlWyAVtQPxvoRIa+P4mFXnA5h0AAXqc6nIAmYoSu5PTmAmQp6RBiYeeYyBWaxEDhf5coKkqvzAAmACCRYJjayAANTIAO5xnBhgwqkFbE2lg9IglW+G6TJjW8YRMEOeECElkhH68ahyD8YifSIacBE9ZFXBoaMFG9AMUxYGQeD4f5dBoa5FAlCxwVVKFXKtMgACEoxZTlSD+SKE0jHkKjABNFWbVVIyjGtG0JSFnm7Ta-nEaRwoTZ1hY8q0wAqhs5oDYJhqVZKNqfWNekGV2Rlnhe5kJgAqmIbBJpRTlw1+04-n+GMMvwupdFwyCMXF92JWAzX6XjyxtWE8HDYRfVyf0w34e+kUrN9ZHoZRs0FDgVikBQQ1dX5jORZY3RVr8dKY0yEV85+eh9i4VxQ28Z0rJxKjksQwwqqphpKeaMB6FbUAuGpssiiSdEUlSYBOkQ4DQPAtBgCYdV0CY8CULwCEuBQeZgGQlDUBHKBgKI2IUOgXQSwO6ZFLIeCiBePBjv57s2kAA)
