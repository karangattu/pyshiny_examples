1. Creates a basic page with a button
2. When button is clicked, shows a modal with a table of sample data
3. Modal can be closed by clicking outside or using close button
4. Uses express syntax for simplified code structure

Key features:

- Uses `ui.modal()` to create modal dialog
- Uses `ui.modal_show()` to display the modal
- Uses `reactive.effect` and `reactive.event` to handle button clicks
- Creates table content dynamically from sample data
- Includes a title and easy close option
- Uses Bootstrap classes for styling

To run the app, save this code and run it with `shiny run app.py` from the command line.

The modal will display a nicely formatted table of the sample data when the button is clicked. The modal can be closed by clicking the Close button or clicking outside the modal (due to `easy_close=True`).
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQss4oAczgB9UugqsAFFIUADZwALxyYACypLZQwcgAInAwpJEAlE4QAMTIAMJiUFRssOihyHEUUAqspaGelVDIYcggCsgdyADkAJJULACCXSgAjAAMYwTtnb39yABCw8gATBNE0x2zKflLAMwTCgC+WbkDtrbITQBGZhTkyHcqpADuyKlxwc6cWMZmnhJScieG4UO4QfyRDgvSLrMAAZXYLyScCqnGCrBhyGIwSguk8ETAVwoEAAtNp+FAGLgMickpxWGUoLwrrjOMQ+Io0hAAAI2ewMLBUDQUBT2OgPYX+dKIDaiFEmBgQZB0SIAFVIVQSnH6rBQIFC4NqAnqjXSxzAtJiH2Q7CgdlCDGQCl54kkMjg6jodDgkmdhTdsnUsko-l+FCwUOemTscHFnilMqVnVyBXExXe8Sx5ColFlZEo1BELRcqvcABl6RQIUnOp0XOxdhCwH1tslUeiMlMa7XkC4qm5WIKoFdQtWe+PkMA++5BxQGP4p99+7PbP4ANbpCxLmeC1fSdIAXXSyqEyDXBGkHJKxq8jR+OqlB67E572NxrHxkSqI7gD2HoRJVg504dA4FsSJZVrTdILrb4M2CYFbnIJs8mCUhWHkMBoyg2VZRTQpijtC5IzeWJ4llFhizgsjgjHCd8xzcwYI6IJQgJOE6l-RIimqQhmOQcRWFwTxsXQ8JVQYEx5G7bDYKweDPEjfwYHSMBDiIcBoHgWgwDEABHSwxHgShZ2FQgSGzQsdIUGAijKDVgk4K4FAgEwBGpCB0CI3EshfWs1IPIA)
