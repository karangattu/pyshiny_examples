1. Use of `input_date_range` in express mode
2. Synthetic data generation using pandas and numpy
3. Interactive filtering based on date range and category
4. Display of filtered data in both tabular and plot form
5. Proper handling of date objects and conversions

Key features:

1. Date range selector with default range spanning all of 2023
2. Category filter dropdown with "All" option
3. Interactive data table showing filtered results
4. Time series plot that updates based on selected date range and category
5. Responsive layout using `layout_sidebar`

The app creates sample daily data with:
- Random values following normal distribution
- Three categories (A, B, C)
- Dates spanning 2023

The data updates reactively when:
- Date range is changed
- Category selection is changed

Installation requirements:
```
pip install shiny pandas numpy matplotlib
```

This provides a simple but functional example of using date ranges in Shiny for Python while following best practices and proper date handling.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAEyiooEt5kf1SDCmw5xu8IuLis4AGwpQAOhH6Dh6KBHYBnZFF3pWy1UOQQArjDx7dEdMsbNk2gBZcIuPlbXIGcKMTcAG5wDkwsru64WHAAHuh+2romwu7o5hRE5lxEflpwDMrKAMTIAOLUBaLOsOiycCIKynZYDJqszFjacNIAFACMAEwAzACUyuxUugC8yIZYk3AA+m0QAOZwvdoKQtMA5IMADCMAtIf9Z-17RNSs+0enQyfDV0SMcACO+wAie+NaHCgyFm82+gIAYm14L0QMpkPDkHtFnsUIttAQ4Qi9kEoLJzHAUWZsKsOjAsBBBDBcQNDociP06ch6hBemjRqMMRAEYjiKI1oJcISWiTOsQXKQuMRNsA9gBBa6IgBCCr2AGE9gBdIjM1mibTs5QAX3+JWQAFUAJLIMjeCDUCjaZTZHBQDZLUjoB29bgUerTRRgMFUZAAJU0G2Q3zgMFIAbeXFksigACM-QAVBj4k0QADuXAoLmQzqTuFIGSW2i4MmTUAYvVGiEx8LzBaLXC6VbgNbrDab3LbWDS5cWK3Dmz7-YRAZHqw2cYnk+QAYAynI4IFI9Uw+tQoQF5PtrWKNNFlJeg9hgR+leOfv+7cT6Izxer4MCC9b1zF9y6JSOP6wFwIDcBOGAYBOVgjDAO9-m-O9nSHCgKzXQIuAAL3HL9v3hANeSofkGFwecsOwlcUOEVU+QFYjsIRMUJSlbRpmAANZUTAMNWQABqJkuG2XUFBlPC4AIwUNSwcwVA+fF60-Wj4W6epAmkAC2NkAMYKKEiAAE8hkBgFkBJZGFgUISJkOhkDoBMqD8VglkmKB60bEjuVKCphALBpFl8Mc+DsDJkBxPE4F0dprXIEJTAoUhGjEHgzO-Q8hAc6oQVYLAYtSzgEoE+L4CwG1k3cTZEMMqhRx3etgEOLU4qkLAYHcTLcvZWDF1ubKGnSzLSC6s9TwSwrmGKu1ejKmcx2q-o6sGgqmogFroTau871KcEbIKRogRrbpWGQcg4t8nc71YSzZkcljXMXASoBlZFOIAPlmZKkMWUZkAAMiXa7J1u+7RE1ZAAB5Zk6967w1VbfuQUpZUwWRPGE0SrM2hg+EsilhFY9joJhrhLLK5GBXrZAAEJZhx9SkDvbkzuBNg6GAM6hKowigemWYibZ3B6yhmHuTvPwKHMBguTOrTuV024ChwWRSAoPsLOQKRkIYLhQqWOoFectbyjEVH5AKaRttO87Dds6Rsqc9rJz11U-GqLy5nlxX8e8UwqQobXfS4ZMcFwH2bBdt3v2stYiCgWIGbqCgunMZMfe0etoe-An-PSOPicI0nOaXMA1IDFz5Nh5AAAVXeQfwxWtHnkBbQtWAJuhjcoCL5cKAWEV-dG8P87bWfwgVNQkqSZN7LvJzw62GZZlm9mzsTgVmPD+ZL7ko7lnXp8upFAbqnfARlYL8U1bUUzkaY8Nt7DN-qDYtBTmG5G6Yv5NKCuFecdw1nqWuh8IrTBEm8fasiZnvKgZ9GbH1xKfDUN84Iw03t0JCPp6i9D2GmBKyBVzq1CuXV2fw7zILEEsWISZkxyAwUGAkCDgGxC6KQ3AFCqF7AAGqwNoanRcpQQwK2qLEE4Uc+JMgvrIXQPdkCUIoLZXw-h2DFVkPmIiMNY5YFiNwYgABrZOTAFDcHINMAALAAVjofCNR3A1guCQiWMsFAn6IO-MLUWXJw5gENEQcA0B4C0DAH4aSXA-DwEoNoTKGjCAkHIFQGgKA8Zex9ko5MzRLB4GUBoAEjoIBAPhB4jUQA)