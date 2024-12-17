This app demonstrates several key features:

1. Uses `ui.panel_title()` to set both the page title and window title
2. Creates a synthetic dataset without external files
3. Uses a sidebar with a select input to dynamically highlight different columns
4. Renders a data frame with markdown-style highlighting
5. Follows Shiny for Python express mode syntax

The app allows users to select either the "Age" or "Salary" column to highlight, showcasing basic interactivity and the `panel_title()` function.

Key points from the function reference documentation:
- Used express mode imports
- Followed best practices for data creation
- Used `@render.data_frame` for table rendering
- Utilized `ui.panel_title()` with both title and window_title parameters
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBf0HDk6KHah6vb204OuECYCvD4Q6AoKAMTIAMJiUFRsuJTscFLEyLaJUArhWAwetsxYrHBwtgAUACwATACUCtkUUMgAvL5YACI5AGKF8JUgCsijyADkAHKwcOMowOMAggA2nMSzROMAQqQARuObsexQDKsbEz3SnLYHEwCisuMAugQjY0sA5rMo+YV2JX9bNwKJVagBWIhgiHIMH1V4QMYTADKUGWJ1wc2QvyKAKKwMqYIADMTCUQAIy1EmkmGNCAAX1p0WQSPSyAoaTcUC+bM4FGWcGQJlY3A+nIgcGWAH0pHz5EFODgPBLpbz+ZU5GA7gJlqRcOVkD0OLtSCc-IRkAB3bjFC0q2VtDVa9A6vUCpEtCisDWMiAxeLiJKtYX2XYnS289h8cJmZBkShMZZeiBW9mChXBuChhiVeqIN6jSxYYxmSVlfmSdUIxFjDVluCSCqSsjLYIQDVEfPVjUs8siWKkFswBEUUjIAASnA+7FWU4o7eQncRxHYpDWcFYbWAGsWX3n3dR6I1T07PpiXU4rGdUF47IFzVaLV2-IUAAEbPYGFh75LGDMmnA6GQOBtV1cppSgJ84BzPMq1GWxAI6e8sDIPAc07LgpxndgKCbAd2ijUwKFKCV6yoWxcMHCA0NghcaJiRZbFsWNyCBKRyFRNgKFwVYIFFUMyiY8g2BIhsmObVtO04QCMOnSdsIo9oOm3XckEXMZ4IWHdZiefCNM+bSsAwZ1cEqNEYF2bJkA0FA6A1AAqOyQA0OkHO9TsJSk5AZKwnDm0UhcwBRNEGFwDUYOrdS6AWIL0WeXSovGGKQueQzMGWEyzIs1prOQWywAcgASJzEAIFy7LcmjOzECgTAYBF4MiX1kAAJRMYcOSMsA6SIcBoHgWgwDEABHSwxHgShWCwCgNAoc0wDjKgaBQMAFBgRJnVIPlOF2PJgjwBR3E8JM1IirqniAA)