This app demonstrates:

1. Basic modal button with simple dismiss functionality
2. Modal button with an icon using Font Awesome
3. Modal button with custom styling using Bootstrap classes
4. Modal button that's controlled by a disabled state
5. Multiple modal buttons in the footer

Technical details:

1. Uses `ui.modal_button()` with all its parameters:
   - label: The text to show on the button
   - icon: An icon to display (using Font Awesome)
   - class_: Additional CSS classes for styling
   - kwargs: Other HTML attributes

2. Features:
   - Responsive layout using `layout_columns`
   - Dynamic disabled state toggling
   - Font Awesome integration for icons
   - Bootstrap styling classes
   - Multiple buttons in modal footers

3. Installation requirements:
```bash
pip install shiny
```

4. Package dependencies:
- shiny

To run the app, save the code in a file (e.g., `app.py`) and run:
```bash
shiny run app.py
```

The app provides multiple examples of modal buttons with different configurations, demonstrating all possible parameters of `modal_button()`. The buttons trigger modals with different styles and behaviors, and one button demonstrates dynamic state changes.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQss4oAczgB9UugqsAFFIUADZwALxyYACypLZQwcgAQmYU5MgAInAwpJFEdJzBwVAARqFhACoMJnAAlE4QAMTIAIK2tsgAYuQizQDucKzMcMipyCasw5xkEKzOnFjs4rae01SU-grIW2PzABLlUQAy-gDkADzB3ADWonDBEWCsFLihHHBwFJHI7GJ0D+wUCjoViIAD0oOItggACtWFhiMFSCZbHQimJ4cxQVBoVANKDLsVWKC6N0ALRQfqDeCggBsWAALFgAEwQ3RYwpYGDceG6SIAPhOdQgQoUvU4FHYOywRVwSIoK1IwRMMBm-jFtglYQAjKCmTVEJttk1ElBWFNkNk4gliilyIati5jGZPBIpORPDbAeQNo92KReh7TVNcshIgBlP29JJB4jIGJWkMI02sTwPGDFUkAZkiQu2oYgeaa8fiyE9qQLYolfGm9qlTvlrs47rL3treciHH9nimdsI+bz7bAEf9cdiJcrkoAkjW+23tkndKnIums5Fa7ntrWi2PrbaK+LJcRxqkWAvZgXto6IKYG5ImxAPXuNheB6HfV2j09mCG51tw5HkAAYWPZQw2eUJ2mLYIfxfAczyXMAV0zUsKAgUleigBgIG4Nw11gjc-1g7crVLPdkAnZBbE4VgSggtgKCgKhayvG8XTvZsn1-N9OwDKiaNKOBbBg18-yHACoOQfxJ2wqR4mCXh0mo2jBLqWdYLzeC0wzbMwHXeomkAsRGOGIy71kZBpHiaoRlIZBViYBI+OU9onmMhQnIE5ZXKoZAwluRtZCwSylTgfxKmqEUIAAAVMqRArgOg6DgSR3IS5BPH8fVmPmEx0DiKg2LdB8WwgH0eM8DyIJDSrBLCGqvIYqgsA8ChMsippylINw3FCSilM8+jjOQOBZAYXhkImaZbHPGLxDMuB1ES5LPjsNKMqy2DYpkBbuGCzh8q8IoqAYfxMwIvr+IgzxvIWiZWogUgRHq67GoWlq2vqWaAoWhKkpS6Ktvi2R1nrLByuKGMhXsOh0syg1YJYPyXEteJnxEt9yi4PRqOQKBSxjC0d3Ig9cbYfh0F6viuV0UivQgXIuKCMpIhNM1Yyghn1O2ElHocMJkZ3R86Z9RTWGp2YwHO86Bata7I38GBIq++bFr+lblbin7gda0Hyp7YVUph9b4bzRGpRR4I0ZEyJMZxi2Tj0ErvlNXGC31zn0aZ8JIgkijp17AguJ547+fmC2hfLK30dEwDEQmD3o62fXQ6wfYjlOM5ODsopdAeOgoFJQZLnafPSQ0GBMKufkzlBTgBXOvMpeyzlBZ4hWlcBn6lv+jXtvUbX-F1yMVhAxXDdhjbTd882dyjgcbaxwmSPYF28c-E96JeQTafLBPXy9h5gK-FgOcIIPSF5hgU-Dkq5-RyIAHkAGk9+jzTImKVDC5MYhiAGCWuJN1gjLeIct-Tt0+p3VWy0FC9yBtQHW14zBg2HvVKGa04a1jNiAy2XEF52yJhhPQPECxKBYHjJ2EpGI2W6q8C6zlBpMTPlzLYB8bZdR6sMUWDDT6BxYcgYOfNgBcTzDgiOrZ+H3zAAABQYPwTCuBX6Jy2O-MAn80LaHkWNC0cBSRMjwso5ANQ+GGLEbfER1shzJXIHEMaSjlGqPUYXaxdgFEGOUQ3bYABdPSwCw6t3lmPemjQMjUQplAXgR4GA2BEDdWBNh7AMCwFQDQK1oYqC7M9G6mDNofBMFhARkRuEDRuigEAWTXrNQ+JlAAvpEMANSiDgGgPAWgYAxAAEdLBiHgJQOEFBUl9jAKsBBbSFAVyBIiEInBigKAgMqPACh0BQFceeCxWwGleKAA)
