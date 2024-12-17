## Technical Description
This Shiny for Python app demonstrates the versatility of `ui.modal()` with the following features:

1. **Dynamic Modal Configuration**:
   - Toggle easy close
   - Enable/disable fade animation
   - Full screen option
   - Adjustable sizes (small, medium, large, extra-large)

2. **Two Modal Types**:
   - Employee Information Modal
   - Department Insights Modal

3. **Data Handling**:
   - Synthetic employee dataset generated using NumPy and Pandas
   - Displays data in a DataGrid
   - Generates modal content dynamically from the dataset

## Installation and Execution
```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install required packages
pip install shiny pandas numpy
```

## Package Dependencies
- shiny
- pandas
- numpy

## Key Shiny Express Features Demonstrated
- `ui.modal()` with multiple configuration parameters
- `@reactive.effect` for event handling
- `@render.data_frame` for table rendering
- Dynamic UI generation
- Sidebar layout
- Font Awesome icon integration

## Modal Parameters Showcased
1. `title`: Modal title
2. `size`: Modal size ('s', 'm', 'l', 'xl')
3. `easy_close`: Allow closing by clicking outside
4. `fade`: Fade-in animation
5. `full_screen`: Expand to full viewport
6. `footer`: Custom footer configuration

The app provides an interactive way to explore different modal configurations while presenting synthetic employee data.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBf0HDRUO8ycHX6d7ah6Acjotl4uIhAmArxBEOgKCgDEyADKuJTscFLEyP4UUMgA5tQOUFLkCnFYDH7MWKxwcLYAFAAsAEwAlAp5BQC8wbZYACJlUABiNfDNIArI88gA5ABysHCLKMB0iwAKDqzkyCCcAL6LyHRCfHwQbhDFzQCMRACsj50AugRzC4sAgsUNsgqjUPDBqn5uBQngAOIgANherwADJ1vrdfikoAAbKAMXBAkG1cGg2xQ5oAZmR1ORREe7RptOQL1R6IWS2GcF8wnglCBpLqxHYpE4xDgrGawEWAAkAEqLIiLACSABUFUssdjxerFgBZPEAayy3EKOvG3HcYsWX2QBr6LO6EBOjqSyB2UGKyDIik4hRMNXKEAUlhwHrgAH1SOgKBKpBQtX05GBdaR-NjUsKAO7EALyQgXTjY3EAIwTKoYJjgLogyT+tlsyHG5BEf0z4uYcGQAGEUilg5wsJkoLZw96qJRmj95iHpSrdQAZZqLAA82O4BtEcGxibArAouC1HEaFCTyHYYjoO-YFAo6FYiAA9A-iLYIAArVhYYjY0gmWx0XExC-ZgHygN8oA0B812LVgH0uSgAFooDbA54AfeEsAAdiwZFn10UCiywGBuC-XQkwAPkWR1q2SFJOHsYs8WQTNOAodhkBgVMcS9cg6F9f0yk4Q4o0DVgFBYtjkBDVh6LgRiGGaTpECnKSB2MMxR0yYgDWLUgNHDQomBMdBJwxdl5iTTi00jaMhIgMT8xU9kkxTNNu14-iAzspM2XM+ZZjMvyFiTcRWFwUcfwaJMUCTABRAJeC7SK818oLgrAOhhzzGKwHGLLkD+CB+EEipCCcoKkzoEwi3DVhiDEahouQJNxmq9MUnqxogzAcr5hOFTHWcwKQ3Uihaq3OBJFMtLLK47Fas4AAvFLmsC5zkzm1IlpW3rkGAJMHKISyfOasBsROpMNHOsAPgGlSVJGuINIkQNw2LMwKHISddyzcMrJxC6wBSLNkFcgH82-AJWHDHdiwoCAEO0Yr8STQaFke0wxpeuy3o+r6Dt+7hLj+ubAeB0hM2QJVFFIUHSYh3FdBhpM4YRonSFRhIa1BqBuB4yhqBEPFxGY1j2N6ZB8lLeQIAAARsewGCwXpw0YNYejgOhkDgAQf1wRpwylrVFOUwKxAof1bl6LnkjB9NiggUpAwuEwIEkby5bEbHZHUOg6Emk9PfEd2fbgWQJ1G+pfv+7FHXsLXwxNlTkmGdJYFFHFsV4b0+L9MQOM2xiGgbQ4TAaBg2Am93yDEwKWAGEMY+moKQ3YClvti3XSH1ztOXyQsHLRXaQxMugkxVUh8nTTv0D1xp7yOLUIGaXpOn6sAh7W9GB1HpNOW5CheRjFAQB1LA3xFZfeilfe8UPwXrSwV3OAAR0rRS19R1LzN25Iu3IMkgZuKXEng4ZARcmjIEOEKSaOk9Lil2iAqgDA+iNzmrjG8+MwBJVIFFDefAtYhQShFXBeZgSTxuDcTGRF0EiTshKToq00ppS3A0ZAyxyBwG-kNNKttNo508iVW43I1jINrmlOMCY4pdx7lTGmDAYBCJ8rtGSy0+iRxjgtZailuELFCuFb8pCdz6JIXgyhGjaG2RrjoxBWUdyZXsKePmFjrJ0OsZvNKVUap1QahAexbVaqdUamAcxT0KA0NcVY+yik7rDQHJojgFNmgwBonIy4dM3ISXFpwP2DhBb81zgJQMCh5bBykKHXJkgSlexDnAdQ4doSR0SZmcM7MSZpjjprZAiclIqXrqpCJOJm5+RDPkQon4yTSGGcw0ZHpPycGaJDJm9igiZQQkKO+iNOArT3AeOA9jmwIVUXAFAFIxAwAANw8R-AwFAiRqSYWLH7C5X9drslbq0b6t8eT5OGJwPcDBODvWKRvXRIyd4rzGDfLkd8j6P2kDiSso5fyUAYVgT6tUKCAvuB-MF5ldlSLAFQDQFAkJrkKBAFAYoBYMCub4esJoUAMnQBoF5PUt7zA8UFSR+y94wp+ZQORMlCjXkOio7aO5DrzFoooosbBtq7RMYYhofRyyVjxQ4-ZaqZbsjRtOeJ6DmnJM6GAE4RBwDQHgLQMAYg36cHOYLT8FASX5jAGOQW1qFCKNvD+eMQLKhRDwAoXwdgAhc2YQsU1HwgA)
