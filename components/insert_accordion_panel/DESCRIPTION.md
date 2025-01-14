This app demonstrates:

1. All parameters of `insert_accordion_panel`:
   - `id`: The accordion's ID
   - `panel`: The new panel to insert
   - `target`: The existing panel to insert relative to
   - `position`: Where to insert relative to target ("after" in this case)

2. The app is minimal and focused on `insert_accordion_panel` functionality:
   - Only uses necessary components
   - Creates static data within the app
   - No external file dependencies

3. The app allows you to:
   - Start with one panel
   - Add new panels with a button click
   - Each new panel includes a title, value, icon, and content
   - Panels are inserted after the first panel

4. The code uses express mode syntax and proper Shiny for Python conventions

To run this app, simply save it as `app.py` and run it using:
```bash
shiny run app.py
```

Package dependencies:
- shiny

The app will start with a single panel and allow you to add more panels by clicking the "Add Panel" button. Each new panel will be inserted after the first panel and include a star icon from Font Awesome.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkTEQAJnAZETnBQoDEyAMpwR6KAHM4yUnQpcj0oaz4IYgAbExtkADFyEQBBAHc4VmZ5CAccXzgAfUCKVgAKKQoouABeOTAAEVxoGE5iZGTiMgYrTnJkergYUjqiOk4oqKgAIyrqgBUGEzgASgVc9nErArJKagpShWQj5FyACTmAWQAZUoByAB4o7gBrUTgo2rBWClwqjjhPHVkOwxHRPuwKBR0KxEAB6WHEKwQABWrCw0VIsTokzE6OYsKgyKgGlhTymrFhdCSAFooOlMvBYQA2LAAFiwACYEboCRMsC0IOjdHUAHy3VYQCUudpWKzIKDICpVNacLDsDkHBpNWCtdqdIQ9PoABTC736g2GYClEFcyVlyBsrGIDE4QV6EBV-KgDGeVlIqQgmrqwYgAGEnsRXhQNsgpmYKH0pu9-YrSPL7RA4KlkN5M1E9AnFTGJF1DRAHdqWsQoBNcFgFABRCTsZCZ7O5s2pcZRYFQWTytgUb18Hby8LEEzfZQ7KiUesesDBq1OG3IABC8b6he4rFsXlN+c9xjMBQkwQgBTjkPIB3LxzqUFlBQ7URGyEO97AdrlADks8gTTzN8PyOaIoF0ApPimCgIGpbR+G9XgYCmakAGYQ2tVwAEkIE4KQa3lfVundNhPBMdAFC7aMTlVEsDXdUpOCsT46OI8gChsIY30Cah5kWFZEBA5AqJbXJWLLZ8D1vY4ZPfMAcLwzgCMA95gLvWTkGkGslk+F8AEYRiEmTWnIaozkuG4Hk4ZAwN0T46CgalMieOUHOpdgslFe5YU4MUJRk5ZBPU2S6jmLg9E4AsYzGBhvhzA9hLwlsGX8bhFIImc9hDaVQ0xXYGFTZBngBdBFQYCRXlIOh0xsOUX1YBQX22PKRGqN4zxkOAsC0mI4FKPTrQAATEDrZHUOg6DgSQFGG8RJE69RZEoRiIFMCgsEfLYXwlGxqs2go20kvNSkCoSJwYSwKGakxKGQNqmrIG71r8fZ-OOB6WqwXd9nOy7rtugBqZABqEoTXFDEaqFbf8XxspIsuCw7YbasSiIkl9pI05A6DqFSexAX69n+kQgb0gBfQzgpknqdJxsAXwJkwLqJx7AeBinCCM44TIgMzVXOa47nuazbNYezHOcpjsYlocGC8ny-IILmjlyGBvV9f1AzppdleQZx9eQXLdluqkCrx5BGeZyhieQUmKap+8HaOMLIr4PQrErVoayiXhNrgOVMpNoR4rzVsTGQ2wLcJ63WZJ9n5yx5BqWQLCjEiGJHTYLJsaENXIX9xVNAoXXk+ScJOJCChyqoPQ1Z9P0AzYcjBGEXWdeXYK3qOMGU4gXdhCLfw2xD1TgtyHc91PNH3SO95MY0piWOn9iK8pxOX2qJGDyVp3FW9F7dIPAywD4aro6u2O7ravTkHeXdsbqBnz+Jjmd-X0hWEU0yHzoKg5cXTuK5XD1EiugSYvBoz+HPmHCOBUqoj0PBAWa1hbBYCoBoYuKDqofSerYE6QUZJiAoEzcsdNQxM0ujApMcDsEHhhBbHBc4XonQ5mAMmABdIAA)
