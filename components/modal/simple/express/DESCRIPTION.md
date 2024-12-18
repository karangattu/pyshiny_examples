This app demonstrates several key aspects of using modals in Shiny for Python:

1. **Modal Trigger**: An action button that shows an initial modal with employee selection
2. **Modal Creation**: Using `ui.modal()` to create modals with different content
3. **Modal Footer**: Adding a close button with `ui.modal_button()`
4. **Easy Close**: Setting `easy_close=True` to allow closing the modal by clicking outside
5. **Dynamic Modal Content**: Showing employee details based on user selection

Key features highlighted from the function reference:
- Used `ui.modal()` with parameters like `title`, `footer`, and `easy_close`
- Utilized `ui.modal_show()` to display the modal
- Used `ui.modal_button()` for the close button
- Demonstrated reactive effects with `@reactive.event()`

The app creates a simple interface where:
1. Clicking "View Employee Details" opens a modal to select an employee
2. Selecting an employee shows another modal with their specific details

Enjoy exploring the modal functionality in this Shiny for Python app!
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROcFCgMTIAyrkrs4U4sgAmUClGR0hyBQuyJqw6AA28hBwAuGkuHBwAPpePsgAvMjACsi5yCBykLDytIUAguGcxHDIAFKk7BCs5IVEhR5w6FDC8JSFKIX2UJGsrciFrMPduP3IAOwArAAMKwC+BDl5BUXws4UAQqQARg4wnEFj7Z3dFL0Ue2AAst0A1q7cAOaXYJPh07MANgAHCslutNrlttBdqUwABhdjdSo1fZMADuEG+HS6PWo91hAFEIB9uIkGJ9vr9-rQAJzLNYbCB5fKFaElAZgAAinCg0GQAAVyRBqljrri+rCABIAJUpUwYM1ocwATKDwUytqzig8CUFechJSYJW0wNibncHgBJAAqcr+CtmQPpYIUAF1rBA7PyoB8aqR0FJyKMIJYcD7kv6KKwABRSCiRdKFAmxeKJZCc1xQTjhPSPUhecLpmKkQoASg9dme3GQAFVLcg-rhSGYFKHjGYkhJAxAkkczBRyNGJuxSGikjB88NvgA1ThwNHIZMRVM1DM+bOjMDlzGe5B5guBckfX0MEJ0OhwSQKAACYi7Mjg6nPl-uEFv4kkD-Usko0fbFCwDhR3HSdwm3Do6GQJJo1LRAIWQOw4TvKhkF8CcDzRc52BCFMEhqbh-AYGBvE4FoNVyFhMlDdDhiHcjmWQUN0CHMB7DgSJJFQpkYmXPDAlIZBpDnBcOnXHM4K3RkGLyNsIFMCgklYdiXzo6TpMKHi4jwxTlKvQhxnotTxnhEdSCUxdcMSS5DLUkAeOAAByNkHNdFB7Kc4oXL8AIeL4bjLOSVIoFWeDmVLKS1LjBMkwC5BLUUIRiO7VpQryfxSCoBh0mo0De37QdCjhOIlLLCLpPEVhcCSYhirgdJrQYEwojC+CcoLRSRzRaMYG3WxkGlagOlPTSV08TMN2QNEXCZfURr4zg9CUjiqA8G870-WQnwvK833WqRNrgH8KD-OSzHUAKdOW8C4EgoCxzmxIUnGnMYLg+jOEg-9zt4x6lpU2DUtyOwADFuA8QJgj+yQ4HBh64AcvRRKzHNAbYXSVqSXzMmiDRjtR5lo18wicPQPySa0x6gr4SD3Oc10MkyL64cu-7woMozmQAOXIZq1O3IzUY+tHlphzGBDejm8kQ5Cal8JGJpo8J8byeWcxAg8qM4LBFdUyWGNDHwPlYLAPBkXW9bUg2fWN5i6EKTnihQEAoYx2nPNdELJOVyWraNnBoztrkxVuPEnZd0X3LNcUKBcz3wu9jnfZtgPBnlXAUAAEmd9GI4ERyqQVFzEAIOOyothjWAoXBorAKhcYAWmGTgPggFBqkoOAGAAbkKBOwrLi2orqwO12RvRiezkWPDF9BHLpz2B719LMuyrXFbyigBwgFiirMkp45syXWE4AAvOrChgXvD4Y-m9ba4YOtHaNVdYdXhlLMB1nyHYEBQMAxAAI6WDEHcY2FBcb6TAGQDuNA-4KCSsueMnAjgKBDAIGYcleReGDAnT+rogA)
