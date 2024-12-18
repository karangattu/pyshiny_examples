This app demonstrates the following parameters of `update_checkbox_group()`:

1. `id`: The identifier of the checkbox group to update
2. `label`: Dynamically change the label of the checkbox group
3. `choices`: Dynamically change the available choices
4. `selected`: Programmatically select items
5. `inline`: Toggle inline display of checkboxes

Key features:
- Uses synthetic data (pet categories)
- Demonstrates dynamic updates
- Shows current state of checkbox group
- Uses reactive programming principles
- Follows Shiny for Python express mode conventions

### How to use the app:
1. Initially, you'll see a checkbox group with some default pets selected
2. Use the "Choose Category" radio buttons to select a pet category
3. Click "Update Checkbox Group" to:
   - Change the label
   - Update available choices
   - Select default items
   - Toggle inline/block display
4. The state displays will show the current configuration

### Technical Notes:
- No external files are used
- Data is generated within the app
- Uses `@reactive.effect` and `@reactive.event` for dynamic updates
- Demonstrates multiple ways to interact with and update a checkbox group

Would you like me to elaborate on any part of the implementation?
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMJioVNrkrs4UsTItl5QyHRCwXAw5KwUDF6c5AroAQD6xF5wAOZCnHB6ALzIIArI5chyYACysDBQADasVSjAVQAipNlVRFVuXj2VYAASQqzyhEMASlAARrOcFINVAKINcOjsUJRVALoEZRVVAEKcDLbNtG1gAApQDExLk6tQ2evLt9TZlhAfAPIAdwaHwAyuh7kwAXsDhAKtMNlJ1pdWlUQdAANYTXpgAAynAAXvdbB8PKQyLZOO9nmAAComYRU7FuLbwdbJMC7BQAXycEEsOFecDSpHQFFYAAopBR1oU+v5iOjZqQNMgAOJMEzoZAAVXQIW87WipCqAEpeQDFuxkPyGlBcKQzGlWJx7LN7uKTYhDuULRQrfzna73Z7vXDkK4AJIQRacRrIYjyxXK5DZDVa31Wt3OoIJ0icYgFUNw-nGR0JuAKpUaNKph3ocVFsPlKrcGONNKpMXLWFNsOouDrSTIKNthrIG4BS69Hu9iq5-MFQrXTrdan9J7Yu4PUgboZoqCY6GNpvjQdUWxLjpdEkDDnH5Bm34zsOuNzkeKkJrhSL2GIQOIJFIEDZNaepZMg4IJPAVAMM0z7FpwWClhQaQSFI5BpLMZgUOQDZgJq+pCrMFC-NSuqEe4iZVmqaamve96uAAgrYFLodAY5kJQTBfjhUR-gB4EUnQdAONQIgEeBrAFtADBJHBs4lhApgoQkFKkJh2GxA28G9lUmRULkDC4E6A4Vru95wnKpCkOM7hZIZuDdrOcLzgWrCFA0nBxOKnYZPZeQFFgmK4BKJqPrO4W6Tp5SKcpGRUcqeHcJ5EBCjh2RvFiQw0l0mXDhAKVZdIjQmHAhQAGKNOMj6hq4fxmMpyD3OIyC8RwpAAvG9I2CIcRZKGGbWohmTnB6XrRUNWAjbYaT+FA9gMHhzIVkmKrqnWyAghQ-VgJFTb3gAAjYC1YFQGhLBN9h0PGCXVn1VBjRZFRiBQ9KwnQ-ZnnAtgoCAyFIdGUjtp2oXIJEADkABy5BwODPJgLyrhTOIkgyHAyBwMJZmtaQoEUeWlbJrWmoKEdKNSLI6hY5IpOeKjlNwLIlDiv9ElUJhJGPldeNZPFK1VjWaaPc+riGvx8TgcVskOnobPo5BsABA48kVPyct84T1bE-WDHIMcUDZnwtgQfciswfeLqymArZAw0HaTj09ETa4OJzAOJtQUrDDIAAtMEviwPmjQNLwCbbNk6O2rMA73lHA6FB9nxinwsJ-UpZhTf5RkmWeHpcnZBlCI5hBO7Or7sHmbke2bDi+-70AwEHDQhzd4fo65BTIFm31g7Cp5mT3+k5EX94d+5vlD4Z+SsMA-2T0XOdmR6+yl72rggqZkg9wr0G137-dDnQZxxK1AK44s0Qqyem-noUE9Z9Ps-pxQmeF9nB8UMvwCIAATCvE26yjIVauu9vZ+3SnlbuxtyA3X5sqC2BVuBlX+slJBaQIHrA9KGGqEA6qiiSOxFAzFjZhGOrXNqFdOrEG6mJNg21vBQDoDBHmVBabUBOmdC63N1b2G2pSUK404QvTesgbSs5E7rmHkZX6c8s7GQ-nnOQTgEYTUTkApBMjn4A0Kug3KmCTQ8mUfeCRNDKCbRvgQzRykAajntmKD0YNvZQxhnDKo2CwBciIOABuCAUBgDEAAR0sGIeAlBWCnXOpMMAnEqA0D8QoeoFB0ANB3J5WYCg+QCEckpbYIQ4JPXKB43YQA)
