This app demonstrates several key features:

1. Uses `update_sidebar()` to dynamically control sidebar visibility
2. Creates a sidebar with an ID (required for `update_sidebar()`)
3. Provides buttons to open and close the sidebar
4. Uses synthetic data to populate department information
5. Shows the current sidebar state
6. Uses Shiny Express mode with decorators for rendering

Key points from the function reference documentation:
- Used `id` parameter in `ui.sidebar()` to enable `update_sidebar()`
- Created reactive effects with `@reactive.event()` to handle sidebar updates
- Used `show` parameter in `update_sidebar()` to control visibility

When you run this app, you'll be able to:
- Select different departments
- See employee count and average salary
- Open and close the sidebar using buttons
- See the current state of the sidebar

The app follows the technical constraints:
- No external files for data
- Uses Shiny Express syntax
- Demonstrates `update_sidebar()` functionality
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMJioVNszhtclOxwUsTItl5QCvboUMLwlHoAvMjAcmAAylAANnCsaURpALKxANbB3ADm+chpAKIQFdxwDpXVaQBi3FAQxPKENWAAEgBKaQC6CnACWaS4zQD6ZCYJyMnAACwArEQAzAAMRADs28gATCenexPQsgxQFXDzrNmxnLmrKQAcm3u-Rz9-ZAARkuvwOyAAnADwQA2aHXBSWHD3R6kdAUVgACikFByiTSABE4DE4tQRASoBwAEakWK2NIASicEFcHnE3igbE49ipsWQAHdOBR2MhunwIELONk2BQvPIIILhcgkaxuXBeQxMdz8WBVTzYtU0dQdfZWCUKGjGYgFMhbcrOFhjGZ5ndbJxSPMqWYLRAsTa7QG0tEKE84DlJG0IAHAxkw3BJMgiSSKPEKJHo3biOxSJxeqxEtFYimyXko3amRAXMhitxkGRKGTRZ4FIqRUislBcKRnWQsiYYL7MQzrWXbQABGz2BhYKgaNOjsJwOjIKboGZzR5LShDkcZ22sOOSOC2ebBj5OihYYOh8MUIf+jPcewaD6F0kJR12TSYg+34+n4kKArPdRGCEwGCjOg0gAOX7KkHGQUhl1qaZZmaVgUBAVd1wWLcMWAJ9NDGABfNIHxqBcJ2oKcZ00ecA3sZcoGkConheBhcB3ciA1-eMqBPM9kgvK9AJvPj7wXANCJfZI32LD9pJ-Q9+IA9FgL3MQKHAyC0gAQVuFFkEyDsOJQAASEBmIcFE2JMt5WAIr8NDGRACFIsBmVcAAhb1yD0C063ICgmCyLl9UcCAkQveYJCkchPV8iBMTSI0ICeNUNTaMAAHl0GoIyMoNMAKyiiBTBDWL3TSr0KB9ZKwGIGYD3S8KsrcJq-HSQrHGKzzkGGcRJBkPwlzoPj-NIZV0HCbw9XVPlpE4VUqU4LIhVwBQqMq2R1DoMaIwgLahp2uBZG3YTUpa+aGArRjkHmLiFyRExprlK6NXqubMv6DhSH5RIABUGBMOAK02zxjrgXb9vnI6pBOs672ExrSGar7Ylupd7segNnteqh3tiT7uuqX7-vabIDzBllkFyuLoCyFB0mzfk63AmwRHRhgZTlcHqIcWi5yiLGuaeWUqBxu1NO05AoIybqeaoTDhK5od3LAYiiHAaB4FoMAxAAR0sMRU1YGc536BqgrJPWFBgLw11IXFOCpBRIoEDayu6cJS24vcNbGIA)
