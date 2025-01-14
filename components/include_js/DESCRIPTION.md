This app demonstrates:

1. `method='inline'`: Embeds the JavaScript directly in the page
2. `method='link'`: Links to the JavaScript file, with additional script tag attributes:
   - `async_=True`: Loads the script asynchronously
   - `defer=True`: Defers script execution
   - `crossorigin`: Sets CORS behavior
   - `integrity`: Sets subresource integrity hash
3. `method='link_files'`: Links to the JavaScript file and allows access to other files in the same directory

The app is minimal and only includes:
- A page title using `ui.page_opts()`
- The three different ways to include JavaScript using `ui.include_js()`
- A simple text output to confirm the page loaded

The JavaScript code itself is a simple alert that confirms the script was loaded successfully.

Note that in a real application, you would typically store JavaScript in separate files, but for this example we're using inline code to avoid external files as per the requirements.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDagBM4DADoRGzNlx5Y4AD3RjWrPgKEju6AK4UihzrPkt0UCuwA2nAEY7Bw5AAUb7WbIDEyAGExGzhkKGQYbn4oO2RrAHNQik4KOzhZMxwoRIB9UnQKVgAKZNS4AF5pMABJCGI7Q0lkACkAZWQAETgYUiqASh8IfwAxTgZWE2Q0igBybWJgqjDkcTG4YgohXigIcWQ6TjT9oWRSQwYWqAA3KFaFzgLZACtWHNWL8o8vIpycg7Tfn0smJKMgAPTIKovKrPV7vLAwADW7yKak4EzyiPKABUGIY4AMIH5AoskuxQs1rrd7gV9od0hAXn96chPkz3uDIWhMFhoWBZAB3FLsU7oahFJn-OBEKoC-phbR0RCyZCq-ZYAUMFJwIow-n86BpYS6mp0ZC4M4zMRsOBwbjxZC2dFEWyhJ5U1g0kRS5ACqDabj1RpwPasQzEYhwLR0Qx2Oy4LD9ADcPn1-UG-lqQaarsuNzuWtpUoynCwgYakhyLwlrylhOJrX46COVFUIk2ilIAsd5Li2VCdlIUEk4lkAAEQZIGFhWxRZJIzRQ20U+sqIGrRHAKOd11Vsb3KfmvZ3Y3t2NdQmp1sYQ2Fdp2BeudmEjRRE2AwABfAC6QA)
