1. A simple food selection interface with grouped choices (Fruits and Vegetables)

2. A checkbox group that controls which food groups are available in the select input

3. Use of `update_select()` to dynamically update the select input options based on checkbox selections

4. Display of the currently selected food

The app shows how to:
- Create grouped choices using nested dictionaries
- Use reactive effects to update UI elements
- Use `update_select()` to modify select input options
- Filter data based on user input

The code follows Shiny for Python express mode conventions and best practices by:
- Using express imports correctly
- Properly structuring reactive updates
- Using in-memory sample data instead of external files
- Following proper function reference documentation guidelines

When you run this app:
1. You'll see a checkbox group with "Fruits" and "Vegetables" options
2. Below that, a select input showing all food choices grouped by type
3. When you uncheck a food type, the select input will update to remove those options
4. The selected food is displayed below the inputs
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkTEQAJnAZETnBQoDEyAMqx0AGzjIrUCihkAFo-TklOcigGXgB3Tgp2ZABzJhN0OCtkYnZScLhWBRy84gLkAF5kEAVkWuQ5MAAxBgcKQtpqiDru+rRMHwaUBoBBfvlCGp7ahoAjKGhoQd6AIXm1hqJJqYaheeTxobAAeQY98a3kAF8CC4aANTh9wJmfdpROqemwYmimCiWGgBhX6kf4TLqfBqlHwxAFgQFwGG4DYXboNHwUCgmUpwgAycEx2POENqlwUZIgLmQAEkIKYRDk4MQANYzUgaFJpdDICikbLkChMLxsRFMox0swKBxYYxmAD6jJZbI0ctSpHSAApbmA6KRSFY5RRcBl2jcSb03KLJMhdfqecayryVKRYogUebivlWOVgA1mq1Tb0Hk8oC8Cg0ALpm7qsK1UKw+v0tBKB+6PAmh16RhQASicEFclp81tlIkSAWQ8S8wpmvnS-njUs4MolFDlseLFC15oatqsqZ7YCLYptev7bvB3U9pW90-DEDzlIL7lysR57F8xBMDEsIg7YsiS4AApYbAwsFQNP9rHA6CLO5k5X2NTm3eaxFiGF06A0AJrq+8xUyd5SywPtWBfMkwHzVwAFV0AbXx9xLVtkDmWMsnIbINyVdlAIichCggE9xAiWR1DoOgxQUGw7zlF8326VwAHECXw+NRztI0TQuZD40NB09EqUC+wEk0X1uc1XGWBwvCyCA4DXOc9CscIpCiGI0KgDDkCwvjDyI7oFNiBVci9CoqmZRBpFHBhkGZAgbO4bCSgKGUqBgCCcz4O9mT4Lo+MfbiCgpNEpOQeDEPXJC438+kLmlesAjgds427T5enA90MuU8pjNM1zDLqHMwGuKpIFgBAUDAMQAEcHDEeBKFYC8r0IEgBWoChaGgiAYACbxQS8TgZgUCATAEZE6XmfwiNRT5SojIA)
