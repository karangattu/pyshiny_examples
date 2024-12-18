This app demonstrates several key features:

1. Uses `navset_card_pill` with an `id` for tracking selected navigation
2. Creates three nav panels:
   - A bar plot of sales by region
   - A bar plot of sales by quarter
   - A data table showing the raw data
3. Uses synthetic data generated with NumPy and Pandas
4. Leverages Shiny Express mode rendering
5. Uses `@render.plot` and `@render.data_frame` for dynamic outputs

To run the app, simply save this script and run it with `shiny run app.py` or execute it directly.

Key points from the function reference documentation:
- Used `id` parameter to create an input that tracks the selected nav item
- Utilized `nav_panel` for each section
- Kept the layout simple and focused on demonstrating the navigation

The app provides an interactive dashboard where users can switch between different views of the sales data using pill-style navigation.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5dKCAEygGdk+7LgB0IDJq2QQAro1wD+EdKPEs2MKBXQAbUhW10ARjlw69C9toqjRAM2akYyXgAs6EeasnM4UYhToANzg7BydXd1wsOAAPdB9efi82d3RpCiJpOiIfbjhmGwgAYmQAcWp8zThnXEoXOADiZB4KKFElLGZOLkcsXjg4LgAKABYAJgBKUV4obTheAH0WqGQAXiEsABFNKAAxLvghkFFkU+QAcgAlOABzOnJzlGBzgDk1F3Oic4BlUnSPr4AUT4FE+FwA6vNQQBdZAAKmQAGYCCczucAIrSKCsfKPZDPdEARjBGOJXyJJIpRFRZ1pdNOGLGlKZ5JZF3RbJp9O5GMRlL55IF7L50JREFpP1m8zxHS63F6cq47goQwArAAGTXqohjLWaoiEyaiAC+UwgohK3wa7CgN2qpHQAXIvFEWRwtrgCwdFF4QwC+jgq2EYG+Uv421chlI2JEYDNFuQAGEfFUBFIoIF+mxiDHkAB3OgUFzsOjabQuiAFovIN3QTMNBY55hcBboUvaIZ0LhBsAzOaLOvBiaILlV4u1jOtzhwDvB0P95CGeTXO7kIcj8XcgACuS4+Rwumsm-pe9syB8q4grcPQ2HXO559u9yvffma2cYaWOywNwc0nQS5DFcT4PBMzzztK0J9LIt73tyth0DcRBQDE746BQ0GGGYPqwceD6PpeCyvrwB56EMADW7jduchjYmCKGrChZr4WcKF9A2-pzEBAAqeizMgEH8EuyArs+5zMSxAgxOxFALLg2hQIYM48Xx2gCWG4lwfSPgUNIzDighNyFLSY41nQWB1lOEDKXOYaLvImLYlQBRxhuD47tQe7MKRR4PqeyAAI5YjizDXmRd54Q+QVOfkRF2esxFfq0P5-gBuBAY5IXieBGlQbwMESSxhnIah6zoZh2G+oV+HRSFcX9j5FFUasNF0SVjExNVD5sVmCycXAKmtGpgn2cgmXOZpkXcj1DbyYpynnLxQ3qf2k2SY+un6cghnGWcpkToEVk2WA2ytMg3GKXM65acgHl5N5ywLPYsAhFNpz+YlrSGFxEXrTpeniolyxgMaRDgNA8C0GAPhBXQPjwJQJEUDEFCECQ5BUDQKBgKIGhaIeBiGO0sh4KIHDcHwu0sSD0JAA)
