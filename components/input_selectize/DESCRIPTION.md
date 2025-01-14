This app demonstrates:

1. All parameters of `input_selectize`:
   - `id`: Unique identifier for the input
   - `label`: Display label
   - `choices`: Using a nested dictionary for grouped options
   - `selected`: Pre-selected values
   - `multiple`: Allow multiple selections
   - `width`: Control width of the input
   - `remove_button`: Show remove button for selections
   - `options`: Advanced selectize.js options including:
     - `placeholder`: Custom placeholder text
     - `plugins`: Using the clear_button plugin
     - `render`: Custom rendering of options
     - `create`: Allow creating new options

2. The app uses a simple text output to display the selected values.

3. The data is created as a static dictionary within the app instead of using external files.

4. The app is minimal and focuses solely on demonstrating `input_selectize` functionality.

The app will show a selectize input with grouped options, multiple selection capability, clear and remove buttons, and custom styling for the options. When you select states, the selections will be displayed below the input.

Technical notes:
1. Uses express mode for simpler syntax
2. Avoids unnecessary UI components
3. Demonstrates all available parameters of `input_selectize`
4. Uses static data defined within the app
5. Provides immediate feedback through a simple text output
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMqx0AGzjJbUCihkOiE2QKpWBVZwuD0AXmQQBWQU5DkwAFEoaOQAYVJsinSUJIhU8rSwADkATWLKqrgAd2QaoQBrdIJkipT0qoApev7m5AGHVjhcLp7e9NyAFWGwfIgIOElOYjN02eQAX26y1PSAdViRfML60t6+sFOAQWXT7NUAcwpyGeO5sAB5ABKy3+Yne30Ie3K82etHmUC8nBCDAgnCgu1+ByO0LAAFlOLYmhcblCTniqst8WtYqRAj87pVTgBJF6cVhkCCsbj0u7pJmwlB80hNdFgPb7BQSiAudxwEToKDvXykdBSciRCCWHCKuAAfRVFFYAAopBQfHF0m44D5NgAvXwAETgMFI6QAlE4IE1OBR2MgtV4oLhSGZdVz7AAjKAMI1uxB7b2+-2cLDhuBRmNx0kpVwAIWyWzY1o2UntyETfoRXmQCoYsDlE2zyawxlDkxtpbgRqb5QJFrA0QC8khmIZgYj1v7uXYpFIkzCQ6NrCzI4Z5WIM62sTig4i2LXKXbJbgtjiwH6dUIlVysIAuvuDzATF4pN44HEFgwTHAH2uDZx1TiW4DwqdJvAkOAZy8exHDhMArQ7BcIiwFCeRAslvBMd5uEiWhzzAYgfGjXUIzML5pTAe8e15MAbBg+otQAK1YXU4GkBFu1HdDUgAchAf9yBQOgTAgTZyCNH1nSIWJiAwOA3USMQKBMFFKgAHlsGQAD41OiJgIHeLT0mQABqZAZLkiSqBgLBx2tBSzPSNSAHo9PIQyXM06QjLAABufZ9h46jeg9LjeilBlQr2VxcSgbgaygdYvATH0-S1WSGFsWN4zC5sMtsXV2HEGDu3g4sxLKQFYmfQ13SbJsAAE6IcLAqA0IpcvsOgiw7ACIGy4K+G6iBaT4CBTAoVMYgG3KGSUlSyn6UgkNiHrj1sDF0Pm1S6HSNoTDWyQTxKHiiB4rBGNIbgJPGswpsXN03QlMAwH2W8gA)
