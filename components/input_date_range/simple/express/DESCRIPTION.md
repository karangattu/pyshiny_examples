This Shiny for Python app demonstrates several key features:

1. **Date Range Input**: Uses `input_date_range()` to allow users to select a specific date range.
2. **Synthetic Data**: Creates a sample sales dataset with dates, products, and sales values.
3. **Dynamic Filtering**: 
   - Filters data based on the selected date range
   - Allows selection of product categories
4. **Reactive Outputs**:
   - A data table showing filtered sales data
   - A text summary with total and average sales

Key points to note:
- The date range is set to the full year 2023
- Users can select a subset of dates within that range
- Product category checkboxes allow further filtering
- Reactive calculations update the table and summary stats in real-time

When you run this app, you'll be able to:
- Select a date range using the calendar picker
- Choose which product categories to include
- See a filtered table of sales data
- View summary statistics for the selected period

The app leverages Shiny Express mode's concise syntax and reactive programming model to create an interactive data exploration interface.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5dKCAEygGdk+7LgB0IDJq2QQAro1wD+EdKIBmzUjGQ8qFBnGTiWbbXF3wiZuFzgAbClFGr1m3gAs6EeYcnM4UYroAbnBOGshuHrhYcAAe6L68-N5sHujSFETSdES+3HDMjhAAxMgA4tT5UFThuJSupnTE4VA2cPzaDhBKWMycXBpYvHBWABQALABMAJSivPasAPomyAC8WlUN8CMTAAwTAMxEAIzHMxDUXEsbq+s6ett7h8hHE0T7R2cmC70QAOb6a3QXCwXx+-xGcygrBWkMWJiIFxWFyuVCIajgAEcVgByAAi2LOsxabRRUBuQKwuKqUAAYr0tiBRMhmchsSZsShQZx-gQmSzsfFSFxpAEOVJsD9+jAsMRXKRGnARsBsQBRVoBdRiYi8bFEbEAYRspAo7j+utZACFSKQANY6vU06TMMQUJ1wbEAXSIrQgIy5fzgUymvIgLNZvGJOpQ3UlA0lHgoIyOOx2xxTqeQPr9G2+3MDZwAvoTisgAMqm+QAQUwyAAqgBJATcMv5YLMZAAGVIv0aoiyOCg-wWpHQFF4I10FFaK2EYFLkeQVPsi+uACU88gaXQ7PlZ8WAO50E3Ifs2KC4UjpBa8OjWABGUJGU0QfOZh+P-Zv98fz9fYeQJRLvoYL6Kk6R-mG-ZgRQKJwLmAYjBB-7MrO-r-LORBIchs6lrYcABCu1TrgGGHIFh-6whQM5gLsBwALQ7EcDFHKR5Fhois60fsdEvHR7ysaGyH-jAHjUVxzHMQJQnCVAMRiY8PETHxLFgORZzSeRJQAArqMKBHEBsvwsPIKjblQBSCchUFKFesr4Tad6kDECy-Oo0joIhlnSWRYCCnpMEGVQRnMHQbRSd5KFznhBE6UKIpsPqhksKFvDhRFsrysQbQwpGpLKn58Welg0hiBi0iKlMWAUKQNh0HMT4hhFzJDOqVBcDlrS8HlAq6YVHrFaV5VPlVNV1Ym6lCcWYYlKuFz5MgJr6KZO6+FwtxkvYd6tH+AACuTWMwILUgsaiwCEXnWCozSdQsm2tE+L5edNyD6uQbYpDZxjXCBC2kLcmzndJlGwTcJiWDKGh3h4irQUdVDweCUzADsXr-eDIkQFV9xBuRyLLGsYN6BDMBQ+cIyw2hFXAEcqOE-AWAwLJWNbDjT0sppm5mfNHTIA+QxreQ-3ID9fThNFbXsL1+lJSFYVs8yy3mVYpI3BGN0dMAbEshCuUa2yGyesgAB8azAyYUzIAAZGR8v-jr6vUsq7IesgAA8ax4xsFvW1rzL2ySesFaK-V1R45OfTgUsBTLKVPqz0keuR5G+K6zrIIr+TKx0hTPbNeTtrwsiM8w8iQrocyNKlXl7XNh1UDEFB-pd4RF1CuDXvYY4PRzr0QO9BifULP3VWjejkWb1wExs4NkCT0Ph2kFBw3BIFPsjtPT0TGPMxVE3IZ71RT3c9Oz6TMMR5Ta800QdNwAzTOWHHSe2yUW4retvN8FYyCC8sIvNi1fCEsg5sECnAYKKVyIZ1WirU2utHa+2QP7LqetnbG1NvMGC5srY2yakgtWAdHb6yoIbd2yAD6BhwYg5B3UQFFVDr6WGICFhgIgW0OOe9-yJ1tuRaq9gbDXgXGsaBWciEEJ1P1QuMAnzkSgIEX4gjOo3BEZcPW4iirwE4DInhtsU5OlDCoWcAAVY0LQyyRhQAAEhAHwloii2iIAIFgCYKgCzCFEJWNsg59BUm3PIecnUrEgDkQo8RjjnGuNnGAAsRBwDQHgLQMAvgyp0F8PASgvAqoN0ICQcgVAaAoFUhARmFB0BGinHQO8ogZByFEBwbgfAc5NWiR6IAA)
