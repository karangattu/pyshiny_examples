This app demonstrates:

1. Use of `navset_hidden` with three panels that are controlled by a radio button input
2. Each panel contains different content (a data table and two different charts)
3. A reactive effect that updates the visible panel based on the radio button selection
4. Sample data created using pandas DataFrame
5. Proper use of Shiny Express syntax

Key features:
- The navigation between panels is hidden from the user and controlled programmatically
- The content switches based on the radio button selection in the sidebar
- Each panel has a unique value that can be referenced when updating the navigation
- The app uses Matplotlib for creating simple visualizations
- The layout is clean and user-friendly

To run this app, save it as `app.py` and run it using:
```bash
shiny run app.py
```

Required packages:
- shiny
- pandas
- matplotlib
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5dKCAEygGdk+7LgB0IAM2akYyXgAs6EXMgZNWyZnCjEKdAG5xREqTPmKscAB7oNvfipZsF6AK4UiG7nGZFndUaIBiZABlWHQAGzhkHgooUV4oSN4AfRioZABeISwAEShYgDFmWDgAChBRZCrkYTAYcgpZWpRgWoApTlqiWoK4ACMumrAAWShmQdqAQWsJkahcWoBdAkrq2o19CGcDWmAARgAGI4OiPYAmY6IATkvkPYBWW73Do+XVqtrnCDoKXmbkfZHU4Xa4nO6PU6HRaiAC+AEp-Fs6DgoABzODJUjoX6lHQUSIZWoACToXC41GQADkoLo6Kj8nRyMgcnB6oMxHRwuEoH0CQAVZjbBEQUQAdx+smQviwvFJ-TGpThiHeUuRTlcyWKXEZyT6rgo5F4pRV1SGtLgouSFFw6B2KwgptNtWCcEi2mQADU6BauibqsRZKQ6MQ4LwMq0wHlYsg+TzIrMAEpwTbbZAAYVkYwoswAqt9funM6wlvbHdVeK64No4FxCZH8ulY7ydirhWKJaqsNBdBWKMl5GTqKVSXWYFAFMkyJRqNmwEqVUEAAqcV3IMQsaIN5CxZsq8WNTvd5IcCCu0qU8hwIi6RLbOsn117Wrzh1l5AAAQ85OYWDSyQkJR+lU5JiJusRWnGZQvm+joaBQzjMA6CRJKkDaIqaS4ruEa4bhs1CpgGWZ7h20pHg+4Tnpe163nA95YWcz7Kq+ZaftQ344OEpDZsxjogeoyb4RiERcYqTEwaa9hqGOFDCfidB9DgNqcWwggRNx4nVByqJEFAFiZOw4QUDKzh9LJRrChpVS6VgfQKshoaobEEb1JQTRgMsMiJA5aQRnhWw7IsFmWdZvZWj8kTGiMDSyOEShJimOxBRpIVwH2uDcn0Z61PFgnIKUAAkCJzkBsGpQhDpaeh1SYae2HrswUr5vwhHFjx+6SqRNLHlhlGntR4R3rU5EAMyMSVrGeD+sklXxXw-CksmiSVEmMA4yDSbJ4TyYpskCPwanLZpdI6XpWRqcZpnKeZh1WRYHEifZKQ+bULmNCWnkoc9YBzb871jswADWXgZAA5KQINJeJKV9niEW1MM0WxcgebzSEpDhCIxU8TB0PJOlPJZWAKO-Vjln8fBiFrnSiKsVoOj6OYYhiFW3F8ckS08RWbo6EyWTqkZ5qWtatqKiqdCgVzLOMg6GRZLUUaNpBzQldKzjoDEGLdkaL3jhAk4NDOgyS9WtZDVhT6k9UrrizIlbaNLmRy2AOX+YWRFICryJqxryRa5FY4TlOVCUEbdtUKbYDkQxltVK6FZiW+qvq-kms0trdS6-r04h4QtvczWdG1aNc5gDCRDgNA8C0GAGgAI6+Bo8CULwWAUBYFC52AQcztXogbcpW0DBAWyMAsEAnjwfwitjb6l4sQA)