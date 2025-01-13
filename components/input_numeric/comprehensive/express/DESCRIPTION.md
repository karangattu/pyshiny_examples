This app demonstrates:

1. All parameters of `input_numeric`:
   - `id`: Unique identifier for each input
   - `label`: Display label
   - `value`: Initial value
   - `min`: Minimum allowed value
   - `max`: Maximum allowed value
   - `step`: Step size for increment/decrement
   - `width`: Custom width of the input field

2. Features:
   - Basic numeric input without constraints
   - Constrained numeric input with min/max values
   - Stepped numeric input with specific increment size
   - Custom width numeric input
   - Real-time validation of inputs
   - Calculations using the input values
   - Responsive layout using cards and sidebar

3. Technical aspects:
   - Uses Shiny Express mode
   - Implements reactive rendering
   - Shows proper error handling
   - Uses Bootstrap cards for organization
   - Implements input validation
   - Shows real-time calculations

To run this app:
1. Save it as `app.py`
2. Install required packages:
```bash
pip install shiny
```
3. Run the app:
```bash
shiny run app.py
```

The app will show:
- A sidebar with different types of numeric inputs
- Main panel with cards showing:
  - Current values of all inputs
  - Calculations using the input values
  - Validation status of all inputs

Each input demonstrates different parameters and constraints, and the app provides immediate feedback on the values and their validity.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMpwR6KAHM4yUnQpclYFSxxfOAB9QIpWAAopCgAbOABeOTAAORN4Bk5iZABJCFMRABE4GFJMojpOZOSoACNUtIAVBhM4AEonCFcAYTEoKmQoNk57ZqgGZCbcUjMFAHdOCnZkcIWliijWKbgZhniexAVkS+Q1ja3OLAPp2dPziCv35FcAISgDwohcg4CnxSss3h9LuFjGYogC8gV4hcIR8phkwDM-rUkcirk1mnBkmifn9kHCgYVoRQseCcZdpFBkt00gBGAAM2I+fRpHw571cOXhFNBIhumxg3AA9DAoBpkGQIKwKAwoNw4ryrlDhbDAfliIjuTjUZl5Yrldw4LZqbTcS0CWjBiElSqIBbSTrgZTkPFWQBaNmsvqEdUQ+mM9IAVlZBGDH3FEDSUZj72lGhZrPZBquXJxMf57qFZWu602irg6EmAC95JnIfdKdrBfrrZcjWBS5gLVbm3i7Zk3FQO7Y3YKQYX4u20uHA9Gax9Q0zmeGZ83kHGE8vmym04nZ+8J+GY9nkbnkALyaOzEXbsQTIrlGtbBsY5qyg3yU3m62b3eYFEH0+g13G18UJTJBlvCh7ymW4yV1C8qUAld53SAAmJckyuf92DRRdWXQDRMkPfo+WQABZZ1kG8F1kivTYRkkGR-F2MpQm5UU7iwYhZlsF5n3uLiGFsKJ2HEewTjAkwGBsEQADUGW6UIwCPCEYwAARsMSsEsGN7DoFRSBWKJkISM4MMuMQKEkt5wgoXxWCwWwZA-FdaywWyfHs9BnJc94bLsh4lXIHxETAYlgRKMoUEyHoiDM2lTXiSksAxBEemUlyYri3z7nczzvJ81zcoCpgIGCsDHTNF0hwiy9vT9dMzmQaLYqA60EqSk0nXNHi0qyrMNx8vyPJwfKCqG+zTSCkL+zLdBXRqkRxwHSdGuaprWvipVEuFALZotU50pXTKNuytz-K8vqIXG4qpokn9kAAdWgzYFqipSWoKj52p279IN-LCDsu5BDuRdKOSGbj9LWUq5QZG8mmCBVaOQDZ-EpVj3nY8IBJ614cWx7jhNEhwQsGOGTARzgQmimM1I0hwtM4HS4D0jgDKiLjknh0YqYVXiNosqyOKKxzpFG61rouk7kWuybSum3IAj0hkaPRt6YvWz69y2pKUr1HpkAAangziKudfaDeNoHDR29s5p6o2Td+5g-2ewHpcuY7Psl8WXNlwL5cyABBWRlT8JXxkaeDWHVj6tcuBKmBMOx4m2spkt+VLHY6s3utOR3reRJK7Yt7Ofogl2AbS5AJWQAAWIgUN6j3gbirlweQMnBKh7gfGQUMph58g2FsyyMcw4sOJx-n8f4wmRKgMSQoW5A5OSQfEfcUfbxp2c6eoTTtNnXSoaMhkN95mfNzgXRIj0NJkGAABdOK4qGETiAAa2QPX4Lizg9K60zvrPgegsjkDgHjAq8Bb5+HshgOaKdMhhQLJeTgegqhBFwLvFcb9O4f2-p1SqrpKT-0AT9XOVV87oNPBAqBPkYGsDvlgBBB9SaUJIcKUByBMEUGwUpOKBIAFOw4Q7AAPMgVkAQ5g5wVF1KhBsAB8yB-T0Jcow5hrCkFgAdHI4hQ5PQ0N2BHZUpV-B1X9IGEGKkNrvzgF-Eee0DHCjISbEuDsaHgJdGolcGi4EsI7Nomag54LcN4fw6xHwhHkPTu4-OABSZA4ZkAAEIH6sh8dfWBN8AmIJ4n2Ac9tQk0IgKQEQEwYAUykOgVIEcDwCI2ngwYBC5QVxYFhP+G1hEdTaa7R87BqFgLoUDPxOStH5J0W0os-TikYIEHwnBzZXGlJEKMmOQNBYMGsjlc6IUg5R3RuMMQ-dz62BSbUEeuA2jGlIMkIQKAfBiGoAAbkWdaAkrBIEbM8ELa6otfYrh9pkNeF9h7oNYApc4hBLnXLAGQO5DAUBiFsK896hdCr+QpvEYA1117xBgKwHwBs6BCFXISkEq4b5MLgU-SJOIehgAAL5EHANAeAtAwBiAAI6WDEPASg9kKAaAoNCuF5AqA0BQGABQ0oKA1LKevZoCg4R4AUFRWwvxiLNiZU-IAA)
