This app demonstrates:

1. Basic parameters of Progress:
   - min (default=0)
   - max (default=1)
   - session (optional)

2. Core methods of Progress:
   - set() - Sets progress value with optional message and detail
   - inc() - Increments progress by specified amount
   - close() - Automatically called when using with context

3. Key features:
   - Progress bar visualization
   - Message updates
   - Detail text updates
   - Different value ranges
   - Incremental updates

The app shows four different progress demonstrations:
1. Basic progress bar with default range (0 to 1)
2. Custom min/max range (10 to 50)
3. Using increment method
4. Multi-stage progress with message updates

Each demonstration shows different aspects of the Progress class while keeping the app minimal and focused on Progress functionality.

To run this app:
1. Save the code to a file (e.g., `app.py`)
2. Run with: `shiny run app.py`
3. Click the "Start Progress Demo" button to see all progress demonstrations

Package dependencies:
- shiny
- asyncio

This implementation:
- Uses express mode syntax
- Avoids external files
- Focuses specifically on Progress functionality
- Uses async/await for non-blocking progress updates
- Demonstrates all major Progress parameters and methods
- Keeps the UI minimal with just a single button to trigger the demonstrations
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkTEQAJnAZETnBf0HDkUVrgjFOpBQoDEyADKcCLoUADmcMik6FLkrAoOOJFwAPqxFKwAFFIUADZwALxyYAAKTBE6egAicDC+hMh0nPn5UABGhUUAKgwmcACUfhCBAMJiUFRuyO24pGbIAO6cFOwzxFAMVgora8jJm9vZdCZtaazEYtS9-XBE7HCcEewUJWAAzAAMX+gapUROFZ3kcrABGUqDRAKZCwg6cLCgtKPKA2BjZUoVUhVOC6ZB1BqQmFw5LGMxpCTxCBpDpmCjkDFgVgULYUAHIUpBFmuLE4vEExpEYjtXRpd4wAC0HyJEGJsPGk2mUAgMTMphEW3EzSEbBZFBMiRVcIAApY0VgHHLkDY6LqpgbslCrXDRKETAwVckrDJskD3sz7YkwMNZUbYabqOaqBo2WHkBHKTI4OpZJRfRB1VgA8IQy73J5iNa4LbtNjqmkbA1HdC4y7AgLkGCUAAhdycQulvl6PbrG1QM4iGDcIpfIgwKAaIoQ2twnvwrC86qOtx6dBN50uuFrrOhbLwXSpd6t1jt5Cd6rIbJfZD0xvDJo2Fmtd5c1ncCJYT8yzc-7UMPh8CqDDKlE2Rgl8Tozr+W5gjuFC+gA9OBubQb+UBLFAqwrgWPhZoUcDoFeWAAEwoahm4bvK+L1KQyDESgYwGvSLBDiqypWMg44aMg0hQPkAyGtBc7JIuuI5KxU6jpxE5FAArBBK5nvRlGbugxFwXuYmHqUjHMsowEQFEl7gTetHyfeRCPph+TvFixBie+n5YN+5F-gB3CiCBcBgVJslgkQAAskGuap6msLunCWaE1lFHQnJUOgyAgJwAC+LkhbC6GYRqHheLhrD4YRXwkWRGUqfWNHIB8KAAKonoZgFXPU1AiHOxBMcosALJQgm-sJCKiboy7uGe1UqS66AfBp+6sNpYB1e+jViPAlDslZz7xW+DXcE1K0iJWjSldBdA6pwgGeYZ3mycFGWwpNWA7URxFRU+NlxWAACSXjLS1SWcAA1GCaXBuNaEYVh+Z5aQeFwART1Ha55XUQ0yABSgACyA6cOghQHOgVhTLiyyrOsM2pMgxDsF5vU-v1C6VEuElSVxkkKSN6Bo6DsIBlEehFMgwClF9qycHxnAAF7vuymJMPZuhS00pQAGLcGLkuGaUAC6XNngF01aVE7yY-kUgSjz0TnmJa3Rc+5usMAXyawjP4nf+QIaEQ5vndQJjwMBVDZHbN23dmIj8+7yAAFRVdKUGoa77lAV5gfcuYdquP9MfB7dW56+F8GRUWr2xaUIDmylKBcgRf1m6ngPA87GVZRDuXeNDBWw0VWBgo3IUqWI+oehyYAAIJtGeDNiUWDQQMy-s+LPFPMDjoRwFYACEpQjIEI9WBxUCuqwA56N6rA41AvCalAuwk-OoInGc+QXE1Nx9AMDxPC8bylMRPx-OyfpSigmIpCGsLpDhbCsMicQaJGQACVcTH3ShyOMEZrC2CwNGWMLobSH2PtWFSnBbRkgoFmVOy4AB8yAvhgNcgPd0KoZZlingdWeFB57kGQFTPQHRYYqlDmvZyYB+5uiHjpfI7YADWN5HjIFpBQekbEOikFkKZdOIg1gW0nniVhc8pgLyEWAFKmsgA)
