This app demonstrates:

1. All parameters of `navset_card_tab`:
   - `id`: Used for tracking selected tab
   - `selected`: Sets default selected tab
   - `title`: Adds a title (via header)
   - `sidebar`: Demonstrated in second tab
   - `header`: Adds header content
   - `footer`: Adds footer content

2. Different types of content in tabs:
   - Interactive plot with slider control
   - Data table with filtering
   - Static statistics display

3. Reactive elements:
   - Slider input affecting plot
   - Category filter affecting table
   - Display of currently selected tab

4. Layout features:
   - Sidebar layout in second tab
   - Responsive design
   - Card-based interface

To run this app:

1. Save it as `app.py`
2. Install required packages:
```bash
pip install shiny pandas numpy
```
3. Run with:
```bash
shiny run app.py
```

The app will show:
- A tabbed interface with three tabs
- Interactive controls
- A mix of static and dynamic content
- The currently selected tab value
- Header and footer content

Each tab demonstrates different functionality while maintaining a consistent card-based layout. The app uses synthetic data generated on startup rather than external files.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5dKCAEygGdk+7LgB0IDJq2QQAro1wD+EdKIBmzUjGS8AFnQjzxLNszhRiFOgDc4q9Zp17cWOAA90J3v0OS96aRSJpOiITbjhmUVEAYmQAcWpwqCotDTgtWHQAGzSeCihRJSxmTi4NLF44OC4ACgBGACYAZgBKUVyoZABeISwAESSoADFi+GqQUWRJ5AByF2mUQuLuMogWGChM6oAGIlrdra3mggmp6dx5qWwl0pgsVeZ1zZ3kPZeDo5PJ6eIkuABzFjnBZXEplYjaUh0YhwarAaYAQWmRGmACEkTMAMLTAC6+0OogAvq0INFkAAFKB-NKkdAWcj8FQsZAAIzgFCozAEmFMS2hoiCOEpcAA+jSKLxqhYKNlOsIwAA5KCWCpsDFQZhcZAAFSgzOQvTgMFIcqIKjomUyuplWuY0jgxNJGJMvwEUiVKuFPw1wryeoA7nQKNoBBaBJYoOarWkOCM2eFeKIA0HkALoMq2Z71Vwfbrqp9kHQuLKwL6VbUTVNK5WYgB5Wl0cgbZAASV6yEZnIoxWIAGs9H8tHBsuYqshffmKsOqEW5b7y4Qq1MYgaVFBpJk2JO4CPNeOIJXtKYuOFi2qNcgABJH8IVya1+uNzLIQ9QY+csiUagUfOM0gc09ZsggykH+N4LneyB1nS0BPr+HLIB+VCUKIzSIPmMSDHQzC8GwvrsJwQ75kmwapkqwocBAQ55mAKJ8FC5KZH+FbhpkdrFnOcqofmlYCr4-jCrwmSFuE1FMHo4oVnK8qyKynKkCo7CQpQCYLrUzxqc8ACs+L7ouyDcVMAACoRvjgjHfrpi7HgpvA-OyIlcZZemTPu3R8RQOBKeK1TEs5lYmBQ0jMPu7RYOapDEMAiAQNiZl-uUdkctUszomc0wOk5MQAMrbuQu66vhlFPsRWjCcy6pEYGJF0HcZEUVRcr9Hk2pRsxGxsbOur1JxaFOZWJUCpauCkPxvBleqPm9X5UwDTVY3HuVzCTQZ028Uoo1DtuFB5n101VnKdnCmaG5gccu17VMcqYSdnJqlQALMLgJorRdCEQlCcC8J0wByvCFpytiyAANTIEJOHVO0cJ2f8gI4lg0hiAAjnaPm+a9kxo9NL2VsZ1Cme0R2xtjUzWWOUbLedflcAp3ShWQeA+cTi50Ap7lYIdx1Jc0yAAITdL9-1IEzVM08g1PAOL3y-A95yA50bnrR5HPmlz2LC-5bJBSFKiRJl2q6OeeH1ZklXJqRljkQRmxylleQWDhUIqUQLEdSWuqND1L242EzDw3QL2kzhSQSo5F1B+KwraBQMBPt0P2U85AraI01FNXwbLILbSR0A7xAqR8Cd6QKeR-Lw8ObPH6OLsXlJl0J1Q62AACypj7gAGigICQylsXwJwk1YPUKgEpxZ1V1WNel1g9eNy3nDIAAmp33ey1gfcQAPQ8j2ABfjzxNUl3XdAN3KGIsCYlrQcvAxwnMsVkMwS0rziqGD8PnHq1M2KY35auF5MAUtYphqjqP4AAZHO20ABU4deCR2jpkDKy4c5ZCgPIIMaRiBBVCNKeQW4dxkz1C7GwEBvamSoC4CygdNo7hzMyCmGtArBXbKfbBX5Mh4JodOQhnc2aljZLUHy28wAEiIOAaA8BaBgBMMjLChovxlwoJQhcYBEJfikaIdYFAsh-iEsyAosg8CiAojwBMJJ-6oAJNiIAA)
