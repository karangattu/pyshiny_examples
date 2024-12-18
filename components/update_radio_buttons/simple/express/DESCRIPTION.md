This app demonstrates:

1. Two radio button groups - one for fruits and one for colors
2. When a fruit is selected, it updates the available color options and label for the second radio button group
3. A text output showing the current selections
4. Uses `reactive.effect` and `reactive.event` to trigger the update only when the fruit selection changes
5. Uses `ui.update_radio_buttons` to dynamically modify the second radio button group

The app follows these principles:
- Uses express mode syntax
- No external data files
- Simple and clear demonstration of `update_radio_buttons`
- Proper reactive programming patterns
- Clean layout using `layout_sidebar`

To run this app, save it as `app.py` and run it using:
```bash
shiny run app.py
```

Required packages:
- shiny
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkTEQAJnAZETnBQoDEyAMqx0AGzjIrUCigFRgcKPQBeZGA5MABBTB8YohiAIShoaCTkGIB5BnSAc3lCbLAAWULSGIBdBTIvIQiomIAlOCssmIBNOC8GgHdOsDzC4uSwAHExahqnCFcK7mQAVQBJBQccKCKAfVJ0MIAKKQofcNaoK05SZBSzCnIV9H8qZAAROBgqsABKOf7OBR2MhNl4oLhSGYdqxODYAEZQBiHH6IBTIdHIAFAkGcLAw+GI5GoiAY0k4rDGKH5K6kHZw+7kViHNFk1kxEKA6G9OCSISdEmsskxNzcyTIKDIABiDFCqJKLMFGOI7FInGIcFY4Q5YQICsVbFFVCs5ziCWKetJfwFbOtZM2lIoO2p1zpDIgTItgpi9SEXJ8vIY-P1GJiAGFSA0GMgcgdru65clbYrlar1ZqfQxWLqk4LWIb2ia2h0wJ70Va9QsoEt0OlesgyJRqBQ9QABSw2BhYKgaZu2mx0A3+qTkHbdihE0uiOAUEwMEl0bqQwc8o3IEAOrDav0roTIgC+4usa43Ge3Af3MTmrmWzwCvgzyH2w-dyAReasj-nMsBy8kcYUbbiH+sjqHQdArgBYgSFIIFwLIlCHBuW55kOQhWv2yA7BOtqcAOSHfo6KE7kiPzIOEkQxPE3jFMSiqbCYt5UE6lwuvSFAPO6zI5myYCnkRAZJJOpJgnCvQmlRPjIOGkasAmQlKiqaoauE0RgEWQxTHAMzymAPR9KQgxgNU2bBui-FGoW7SXtxyBWqSvS4XwECmBQm4EWeDwkWRFFgGkGRBEgk70YxcDMTSrrsYyXGmaUfGGnyhDyeiIliak6TpVJEaNHJNmkimSmaqpekDDUJmmeZBbdL0JUljZdkYg5eHOWYbmhB5u6keRpQjBARQxLRgrBS8oXOrSbEcR6uUhrxWUMO1gaJVNyVQKJXgmj1RSZTJOUxflaYqbk+S9cUxlJb+FmHaM1mKvV6K9HmKDIJWvVVDZQ13mFrFupNMXerN82CUtyApWtMQVC9W3ZYDu2Kftqmadp4zFQZQwbSdZXBhVxoxAjEDXYKPxgHuRDgNA8C0GAYgAI4OGI8CUKwXY9iUM2NjQKC1TAATeKQpycHCCgQCYAi4AoNbWFArBzDFRPVEAA)