This app demonstrates all the key parameters of the modal component:

1. **size**: All possible sizes ('s', 'm', 'l', 'xl')
2. **title**: Both simple text and custom HTML with icons
3. **easy_close**: Both True and False options
4. **fade**: Animation control
5. **footer**: Various footer configurations including:
   - Single button
   - Multiple buttons
   - Custom styled buttons
6. **Content**: Both simple text and complex HTML content

The app shows five different modals, each demonstrating different combinations of parameters and features. Each modal is triggered by a button click.

Key features demonstrated:
- Modal sizes
- Custom titles with icons
- Easy close functionality
- Fade animations
- Different footer configurations
- Custom styling
- HTML content
- Font Awesome icons integration

The app is minimal and focuses specifically on modal functionality without unnecessary additional components. All the data is generated within the app itself, with no external file dependencies.

To run this app, you only need to have Shiny for Python installed and the code in a single file. The Font Awesome integration is done via CDN, so no local files are needed.

Installation instructions:
```bash
pip install shiny
```

To run the app:
```bash
shiny run app.py
```
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQss4oAczgB9UugqsAFFIUADZwALxyYACypLZQwcgAInAwpJFEdJzBwVAARqFhACoMJnAAlE4QAMTIAIK2tsgAYuQitQDucKzMcMh0QnxkEKzOnFjs4raeQ1SU-grIi8guABKFUQAy-gDkADzB3ADWonDBEWCsFLihHHBwFJHI7GJ05+wUFOisiAD0P8S2CAAK1YWGIwVIJlsdByYjBzB+UCBUA0PwOuVYP36lAAtFBOt14D8AGxYADsWAATP9dIjslgYNwwbpIgA+bYVCCchTtTgUdjLMY5XCQijTUjBEwwCCedoMDD+Xm2fnnACMAAZ1QBSSJlRALJa8-mCsFQBi2fx6g1LJYuYhmqYTKD2BjzaKxeLIACiGlg6BuuutNuQRoFdodnlysVwlv1EGDCeQNQAwmIoFRkLkzBRyHoc8h7KlhhR5RnbJw6HQHNQRKk4gkhpk3CZS5xc0HEybjGZPBIpORI9nyG6OKR2p5WDB4sF0shIgBldhj5DzqfZZAxeuz8FQXSec7wHGU5AwXJHwPxzu2sbdsV9tsyrMfYeRUfj+DlqWzhdL9obuCfiwm7xNuOR7gecBHieZ6UheV7Xlgt69pID6Ds+EAjr+niwh435gIuy4bGaHgbh6M6EMgO7gZEh7Hqe55gJy8GLC4SH3gOT45hhr5YRo5FED+y4+iWUDIERDAkcB-GUWBrD7jRkF0TBcHMaxECmHeKEcUO3EXFhxAmJczB4QRf7JoZOZAWRoG7nJEFQfRsGMZUAACaYobI6iVnAkgKG54geXA6iyHMt5YG+E5rsEnL2HQKhjpF06eHW8SxkGLBhCaKXBPMl4JpEhRcHonB6KJk7TieZEhnyAqMhA-CejMNZYOkHZLEEBQLlFpFboQbWLKwnAAF7hK+rV5cG4isLg0wQqw4TFKUBD9X0pCkFQDBhC42VoVxbrJnN8gUVRdmRLkFAQDi81DHEDC4CpixMQhO1vv4MDchA-n3p5cDeb5n3uVIP0hRQ-hhRFH6cFKMW-fF74AVDMDJWRaUTRlWUoytBVFXwpUngjUqVfWyD+LFUAmMEIiDSNZTVcaokdb0UB2Kt60OC1fUTTajPnFEBNWb1y1c0s1OjWAMDjZ2U0zeCpDzWETTxPNQudv0bObcAK02ttZG7S+YDJszxCnDZ1FgOdl3XeQt28LRuoq6pYw7Zx+sAPIANKm6d5sXTi2gNXdD3BgAukGT0sU7uuve9rmAzIQW-VW-1fYFwU1mD6lmOFWE4eUCixXD2HEV42Woza6M6-WuWdtjJW48gom50Tnqhg38acEMfDxvyvSMxzDsJjzLgUO4oLltI1eO1gI9uKCnD+Cd8lgHQUBXRKnCNCvOLEJwDDgpB3D9PjDFlAPV6ROJklVa3ACSQyRCtp8raL5z8St0uzXLC0lHAZ82mrG0tqR3rHrXSABxdafAKAAEIg7hwxiA6OH0U5AwTn9B4AMAqoLTqFTOFBs4JT4jDOKEU+LIyrlaNGyBMqV1SljMAhU6512ZsgTQIlkBN2ynTAUEBSB9GdEzeqU5+wQH7itHmkRhLyjEsXHqIFOadhfpEPiktEwr3sArJWv8VoAIcEAhkusXa6QOl-OBQZaHBAnL+N6yC44-XQX5OxCcQYZw0gQ8cBkjIxzsLDCKnjLLkNSpQ8u1CEF0OFhHaeo8sDj0nvBYe0T2AABZ9oWWUMmVoNZ7ZawQjPUE6A3SML0FwwsuYRJUG+NkiJwYEmzywBTOJzFIl5KwAcVJXjkBrE2JRTJlAqlNO1mMFpbTIjmQ6Zca43A3D9IGc06JIzogUykP6XouiGCZh0iMRif8p7DPnpEAAcnw6WMlTHOWqTaJ+FyRZXE6mAMgEIGAoCqJSYgABmOAABWdUABuB+1SrmdiHkM6JsSclzLqfPRe5wt7dAOJvVeHgzTHycoC5ioy0kC3kTshMEy7kPKEM8t5SSACcAAOWwuQ-lgEfjitgw0xYSwUYmD+st5aK2CMrHRa1AGa2uZE52Ol9pGxNsdWSS8LZXR8tbM0ttFIzPicA+IoC3TzigLIL2ErfasBMMQY2LJzmdlDhNeBFirFjhsWAAAvsHIAA)
