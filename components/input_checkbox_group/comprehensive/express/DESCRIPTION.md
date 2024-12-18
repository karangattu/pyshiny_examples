This app demonstrates:

1. All parameters of input_checkbox_group:
   - id
   - label
   - choices (both as list and dictionary with HTML labels)
   - selected (pre-selected values)
   - inline (boolean for layout)
   - width (CSS width value)

2. Two different ways to specify choices:
   - Simple list of strings
   - Dictionary with HTML-formatted labels

3. Dynamic updates using ui.update_checkbox_group()

4. Different layouts and styling:
   - Inline vs stacked layout
   - Custom widths
   - Color-coded options
   - Card-based organization

5. Real-time display of selected values

Technical notes:
- Uses express mode syntax
- All data is created within the app (no external files)
- Demonstrates both static and dynamic checkbox groups
- Shows how to handle both simple and complex (HTML) labels
- Includes reactive updates based on user input

The app creates a comprehensive demo of checkbox groups with:
- Basic usage section
- Styled options section
- Dynamic control section
- State display section

Each section is contained in its own card for clean organization, and the layout uses ui.layout_columns() for responsive design.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMqx0AGzjJbUCihkAFo-TklOcigGXhgMdG4Ac2RpKC8TOD0KUmQACQAVAFkAGWQvKAAjOC9WBWJ2UnDMgH1bcJEAXmQQBWQ+5DkwMVtBlEssVnQoCAAKQYAlOBHCNgpcHw7Bsi8hFGcAMX2ABhOjgG5BgEoCXv7BxLFqUeRxyem5sABxR4hBolY1hstqQdgw9icAIIQk4XMDXW59QYVdLyWivKazQYAIRRf1W6zgmzA212yGcpyOUNh8IgAF8nBBXG5+N5fF5OADkKQ6Mh6o1iJk6g0mqxmuzOV1gIMAPLoKTkZAQvEyuWRCDILHKsCy+XqgDCWp1auQABFBgBdBnjKaJODNUhy1gzKQUIFgPXsODEADWFVIGmQ31IJnQprgMFIeLonC85WRhPyDAylwZAHdOBR2C9OFhyrhgxRmtsTDAIE7LogEWTkABRDSeHzIACMKCxUFY4RerCgtuQ6czyCC4pE01sg9jyCmDFgcCoDFq6v6-az42I0VsMwrVf62awa4Ytmanqg9gYHzbHeIyA9Xt9-sDTBDV23-XGxjMRc9Pr9GmaD2D6BzIuO4gXwthEhU7bhH+j7oH8L6gXG1REh6pCkKwvgwCYXhSKyXKquQrCVoQCEgXyIodORAqisONzAaB-QYT4khLB0UragR6pKisKq6hqFp0QxIHcOyECEvsaQYYJQlLpwtiZkSADMJzoBogykSmvz0TuAACNinlgVAaBQpH2DykGXs0OjYRQm6VtpDGcDy74UFgFnQf+IZ2aRQliBQJgMOqdCDAAmsGbDVF6VC2CgIAAOREHFWAAFaNLMLluVBxAwQBm6XPSYA+f0fkBeqgwAHKkJmSQRcx0XqVpO6uHWDa+AATCgACqHYQMkBQlGUlTVHoy5hBEUQxIOdh8BAolslA+ZmFWo2ruu3kOX0q0Hke4inh8biAks15fneAZBk+cKkW+ECmIW9S3j+OVeUVfRyUSAIEoenlwSRG0gUhXgoQ06G+CS87EdJMm8sK1GUTDLRtJIkMyUxUWsexwwCS9M1zR0iYZMjQnpvJ7BEk2JwAKQNUJmmkXp1AGUZJl-WZ+I+Ie1k4etUOvc5N1mBMh1fbB3M8zuJWBcgwXuiCQh6KjLExd0CXIElqXcDMGUfezT2AZc+XUzzEtlWAlW8rL861WjywMq4Jq4NAMCdiG-hUMgmitQoK05vuG5bvRW2Hsee2DPbjudnq5AUEwXjPvRVauJHlAx3odBCC86CuzVmagydP7IN9y0ZiuOZ5gWRYgiWZai6B123c0rD9vUHwmBhzQidwqJEIM3W+B3YmDYtJkrKkKIdBJNRwJpQl1x+EAlg44QfMTmbNKpWoAOpyQOMyqSmI9pBkHTKUcRBOxAHTk6fyBxBoHQABwnLT9H0xIUiyOodB0FFVas80NcgXGC7AIdp7rfn9LrICYskRZV1vBP6O5+6Egyq3O0SDNyEwYivUm0sQAZWwWvDQm5aTr0Kn9Z+TIGipl5AFGwIgAQgK5DyNIXgZq3QXN7Pca1-Y7kDjtE8DgPh6lodQEQB0QFxx3FWemdgHBYEsL-OAPIOCkFTA3QIVAAHi1nKVXcgREisCwG0aQUCebjH0YYwC0sLydm+ikQ+cBYoZXctlb6xCriYNrjmCxOAZjSwOp9AusF7EoicfzVy2sliQINnCTxgDvE9ksX4wYABJWandB4FjCbdeRbd0ExJpGLcxiTfHSy3iTCKFApC9WyQLAhqliGkMKQxS4YBaREHAI7BAKAhhwAAI6WDEPASghiKDGRWMSKOojaBkLiBQbwVV2QVAUPPAQuAFAYn8AubGbTzRAA)
