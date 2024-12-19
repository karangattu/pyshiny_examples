Technical description:
- The app creates a simple interface with three sliders:
  - Two control sliders for setting minimum and maximum values
  - One main slider that gets updated based on the control sliders
- Uses `ui.layout_sidebar()` for a clean layout with controls in the sidebar
- Implements a reactive effect that updates the main slider whenever the min/max controls change
- Shows real-time display of all slider values

Installation and execution instructions:
1. Save the code in a file (e.g., `app.py`)
2. Make sure you have shiny installed: `pip install shiny`
3. Run the app: `shiny run app.py`

Package dependencies:
- shiny

The app demonstrates proper usage of `update_slider()` while maintaining a clean, responsive interface. It shows how to dynamically update a slider's range and value while ensuring the current value stays within the new bounds.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkTEQAJnAZETnBQoDEyAApQA5nGRSKAGx8oa2R-KFxSM2RSdClyVgUHHC84AH0YilYACj9AgF45MABlf04bBmQAVXQrKCpkABE4GFJCojpOfzCAI3yAFQYTOABKJwgAd04KdmQksIizVNYyuG6oBizhxAVkXeRJ6dnOLGWbNY2tnb3r1wBhcgomfzZS8uQ6IWQYbgB6GCgNLManU4AkINdrkljItWK9bFlCt8IKlpFB-G1kIUALLcfgmFgANTRQwxSLyAAYiP8NHkAKyU5Co-xDCmjcEQ3ZQiCmChLOEbREAlFojHYgF4wnE+SEL7cOkM6l5ACM5IZTJZKvJbI5uyuHNcWKg3BeKwq0zq+06z26PhMwKoVj1EK5PL5poR7J1e0F3Dd5VFnq9mLAhuNJVNAaDezJDKdXsVmqIcZ16rg8uTuzZTtcDU4rHQ82QxBMDEsIlhpsZUrB1wAApZylgHE6bHQVKRxsLmaDNttA9cxBQS+CkhQvKwsFYZB6o5zjmPPBP2AAWBFgW4lsvIInd1jbMDDAgZ53z8c4LJ0bHGndDFAgaEULBIrubAC+hUPx8hp8X58vIYBbcpTvB8nyFJk3w-I9+x1Ucz3QC8xTDfkgO7EDuTMMDfQrcpIIPY8swgVwAFE6DoOBJF8UggVqepph8f5jRw2x9nYahZQgP5ALISgnj0Yh2GCbwFHrcRJBkOB1DIiiKAUVtkFSXsnSSO1aLSZiBRg3UwEY5ENLaY8yVA58IM-LSvgBPJjPAtFNmgr1XAAaTgOB0CLTdqBEVM+DbA5VGQCA4HGUQhLgIhSHohhJlYHxiDCAQqI4riNGPVM8mpLIkSyazsP5Oy+Awx9qRfYZDwKnkn19UztT2YYwFfIhwGgeBaDAMQAEcHDEeBKAnCgNAoGUwB4qgaBQMAFH+CgCwi0pugUCB8TwBR0GCWowS-PZ6oAXSAA)
