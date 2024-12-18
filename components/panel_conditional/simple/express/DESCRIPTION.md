This app demonstrates several key features:

1. **Dynamic UI with `panel_conditional`**: 
   - The breed selection input changes based on the selected pet type
   - Each breed selection is conditionally shown only when its corresponding pet type is selected
   - Uses JavaScript condition `input.pet_type === 'Dog'` to control visibility

2. **Reactive Output**:
   - The `pet_details()` function updates dynamically based on user selections
   - Uses `req()` to ensure a pet type is selected before showing details
   - Selects the appropriate breed based on the pet type

3. **Synthetic Data**:
   - Uses hardcoded lists for pet types and breeds instead of external files
   - Provides a realistic selection experience

Key Shiny for Python concepts demonstrated:
- `ui.panel_conditional()`
- `@render.text`
- `req()` function
- Reactive inputs and outputs
- Express mode UI construction

When you run this app, you'll see:
- A sidebar with pet type selection
- Conditional breed selection based on pet type
- A text output showing the selected pet details

The app provides an interactive way to select a pet, with the UI dynamically adapting to the user's choices.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMJioVNrkrs4UsTItl5QCugBAPoUuBF6ALzIwHJgACKkAOYpRCluXtnIKQBCnAy2BSkAYpwcKQC6CraZkQBGYnC2CUkpADJQbVBNjoSFYADiDjBQEMgAyv7o-mUV46QANvYzAEoBDJxwssM5YAAKpKS2a-JgDRDEXq3tnciJyWCznLBwrNfHJw6sT4QFYAWSg3Dg7nOwJGxWoGSga3qChapVsjzgHS6bxOUAYTAoKzy0AYuCJpGIAGsvPskbCwNU7uxkYoauwMViXt1Vhs6GyVkUAhQwvSxiZMGT6QBBCAZOBrPm1G5OCCuXFytgBcUKSw4KByyKkdAUVgACikFCu8RS-xEs3lcEkQhSAEoVa4wdxkABVACSCgA7pwKOxkLq1lBcKQzJFAfYWnjTS7EApkGnkEGQ2HOFg43AEwwkymZunS65qgxWCIrrI1pqrpJOOQULbkAAVWLyEultO64wxhiDJutMwUchm1M9qcpCIUaKdirdqfplL2hsiVsdiKL5c94jsUicYjfeKz+dxSdTt3ApdlqF2YNN6B19DTeXIOhCZBtTG2euOqRyG-KAfj-IDZ2QGJt1vdNM1DXVXwgeVIjIB9AOfU0Un7CgcCiKDIXiQjkAAcnSDJiNdYtd1LPsIFMOdB1sYcWlHcdMJg6jRiaDIOXKWEOOo1cHUkZAyOQIonh3Ti9wPI8T243jWEvajr2U0s4OzPUkLWFDyCY9DEUwsBsNwud8JeIjiLyCgKLAZM1OXWj6MiRjmNYiAJwE3cUnuOcfw6KTpJXd5hJEazxMk-igtLfdD2PVh4l8xSHKvFVdw0hC3x01D9KfQysLosxTPPAjLJKMpbPsrz0ycgch1IEcKDHDz2Oi4LUTKXjAuioT13EtEIt-bqgtiuSEo69F-M6FKe1UgSMpzRDkJyx9yHy4zCpws9zMIxJiOqDhKqo6TaoY+rGuazy2rTFJFXZKbhuk3qAOQA7Qwkoaouu0b4viO7kuqtM5rvAB5Mx6OQPFxGUgABGx7AYLAqA0Qkl3sOhkDPexhU4NYzSq3dXAANURTgQm8EMvEhzGAkgzs+D0H51wCgSxAAR1NEzts7JNr28gTXFSAJJghb8nmA0DkHA2n8JmqauQAOXILtd04DGubwnmXQs0YyJSSG7D4TasAUqaixm0t5cSEzTaeJMZvlNWjfo4r8KTHXcnyMADb-EykrNgnpKt52iv9u2+eXR31eN7mIndojijRfXpl942Jt483AbF38uRM9OA4dtYnY1sytY9hl+W9lOQ5w-6A+Ozjg5Muvw5mmbXB2CgTAYGZsfBPGZrELue4-FIAE1o3-SQOmpkApoAX2QEAS5KpN55SMB56IcBoHgWgwHZywxHgShWCRlGRjAVCqBoFAwAUKYKHQNZSEtTgWgUCATAEMk6JTkC0rSU3nUIAA)
