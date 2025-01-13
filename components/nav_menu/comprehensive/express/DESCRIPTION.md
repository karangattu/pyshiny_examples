This app demonstrates:

1. All possible parameters of `nav_menu`:
   - title (required): The menu title text
   - value (optional): A unique identifier for the menu
   - icon (optional): An icon displayed next to the title
   - align (optional): Menu alignment ("left" or "right")

2. Additional features:
   - Uses Font Awesome icons
   - Includes dark mode toggle
   - Shows reactive values
   - Uses markdown for content
   - Demonstrates nav_spacer and nav_control
   - Uses different panel configurations

3. Structure:
   - Basic menu (minimal parameters)
   - Menu with value parameter
   - Menu with icon
   - Right-aligned menu
   - Complete menu with all parameters

To run this app:

1. Make sure you have the required packages:
```bash
pip install shiny
```

2. Save the code to a file (e.g., `app.py`)
3. Run with:
```bash
shiny run app.py
```

The app provides a comprehensive demonstration of nav_menu's capabilities in Shiny for Python's express mode, with clear examples of each parameter and their effects on the navigation interface.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMInWFZW4DKv5G9kGCgAazg+Mgg9GCEI6U5WTgAjABt5CEssdnFbAH0oqkoACgVkcuQsgAkAFQBZABlSiArW5DkwDq6WtvKAHlTuUNE4VIBeDq9cdI44OAoO5HYxOgmwdgoKdFZEAHpd4lsIACtWLGJU0hNbOlSoMXPmXahjqA1dweTWXbpyCgBaKAAdzgrGYcF2ADYsAAGWEHXTPVKpLAwbjnXQdAB8ZV6yD6U3SOJ6eIqWDoUH+YMGtmQIGQv0oVM4AC84CgAIxYABMYhgAG5gvcAObcf4MTjCjYoACs6A0goAvrjen1doS4MTSV1Op0ScgAJQKI0QBRZdBQYVwPKkdAUVjNVpSCjpNYAOSg0mQdWoJmQABE4LEOgQVQzOMioGk4GMagwTBkTS53GIoFRkFBkNAEsK05xyMhkvdkEDOBR2MhbJw6HQHNQRNm8vBMshNLB0DMFKXy5VOFhs6x5nkiwxis7XR0PV6fS2AKIadudsAGxBhsOuABCUCSxCznqbvpLZYrx08InHGVa3YrWUbzZMpTAW533t9HRXYavx97-f3FogoyPgAClAAGpMgHLvqu+qklkIQMKEtikECECPs46HIM+nC7jOfr-MgIFgRB76fniHQ1FweiJBmhbbthe7SAeLbXsgp5eDRF7IBaDCwPMDhYN0pIsbef6gYBHSEaMyDclBpG9HB9yIchqEdOhm50Thh74ZJ4EycucltB0ACCECkOWDhcWJ4HcIEOS0S+94CXq67IFOwSHix0hQKkCaWTx8BUI4+rCX2d6+o+uFHj2ABq3kJiGyBeT5MYdElCZMSYskwRUIW-ox-7iWAOnIEZCVpSlYAFakeRQFlpKtApCFIShaEYbFyWvi22lWSVJHZb05GUe5LbsNuNGsOgcDENW9HlX5vGBWw8xOQZrSrRUAACNj2AwWBUBoCz9W09h0CoyF5OVxQfkdpJiBQJgMC0dAdB4DA2CI96JXF7JfclGXdC5bmfSx2HkGGuVhZkjpkWAkUsQAklECUGaDEBjFkFCWmcnDFBc26sHkawUlSpA0gylJWvcfWtNdQnfiJ+VWY+vjzFIEDCnokHLtB9UVI1SktapGGIwWkX4SzmzcBzxH6TdFSDdRn2jXomaUwwkTkCtR0Q6JYHM6zUt6HptO8z+8ECypYBqcgIstGLyAS2z0vG+t5TGaZ5nq4Okvs3oVVa4DnrDX6LESlKIjeZKEDNodX49gzGXQwNYAAEqShsJWDMKAG0rhyNHZH2drGHGwhijUTo32mMc1gON47ohMdMT1KcLSxP3EwQLiunCyyzTPN4jrjN6x0afhwRPVcybvP881lvW2PGyAlnOedXhE9EVPrvtGAFGK4e1GF6vQTmaIPda3T8ehbrhWLyIxXGwPM99ubc+ta4d-L1HcC51pG9SS7OWbswAmTMjkdWJcARHx-pZMCAd9SuDcMwDsmgGLByihWby4FuILQcKwcG9Nr6MXvEnNoF41hIIEOkdMedCAGXKmsMgVC+L-ToUdVGlc9pY1rrjO4DciaUhbm3QRmNHDLlDAXFeax0h0F7mGaebQh55Cqo+ShKD0zFS5kQBhHQmHqOtFPJ+9VZ7KXfu4ZB1CIj200dTU2CsYiHnsLEaIFAeJUBVsiLipBdApHSPNAKeDVx6lNmbRSb8dSCVNgAKkCGWdIKAXoWL4mvSJvMYnlQSWAPRljWHbxiajFAXhiyozyRmFemSZFyKATvHUJoQnby2tQHae1NCx1NidM6QIChJKoBdb6V0jEhLug9J6iTmHpk+hk5A2SWH3lSSE9o2tCF5WUUzMZ+j-66TKt9RhPTrSP23iYwWVsMJqMsWvZA3UiKAPqSAj24DYFSRsqfGZEzDxtmYfA1orgjK2FpJmbMbALTEAsr8dWyRWYWQSKwEw3lkBCFzBAVkeYwb6gThNCQDgrpOAQSVP5NFAWFCYOBFithFLBFIPYQIpBhTCnSAQq+KyiWkwGQZLIxgzB5DJQhJslK4BXTAIqIg4BoDwFoGAMQABHSwfJ6xnAoAdQgJA-j1nFQoEIWxLguhSAoTIAhcAKH-GS-BppqmCoALpAA)
