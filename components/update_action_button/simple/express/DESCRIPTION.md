1. The first button (btn1) tracks clicks and enables the second button after 3 clicks
2. The second button (btn2) starts disabled and gets enabled with an updated label
3. The third button (btn3) updates its own label and icon when clicked

Technical notes:

1. Uses express mode syntax for cleaner code
2. Uses reactive.value() to track click count
3. Uses reactive.effect() with reactive.event() to handle button clicks
4. Shows different update_action_button parameters:
   - disabled: Toggle button enabled/disabled state  
   - label: Change button text
   - icon: Add/modify button icon
5. Uses Font Awesome icon for demonstration
6. Uses Bootstrap button class for styling

To run this app, you need:
- shiny
- font-awesome CSS (included via CDN by default)

The app demonstrates button state management and dynamic updates in response to user interactions.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMr90AGzjIM6FVIAd24Ac2QTdFsoKgB9CSlyWIAjMwpyCNYoUPkISxxsuFjSdApWAAopCh8AXjkwAFUomN8AQUlODIAhNIyAETgYUnqASicIEIp2CM4sVk57ZKgGcpHEBWRNmaxjM3iOpNSKdIhy+uSKCABGeqJ6gGEvTmIAa2R4AEJb5GIvKF1YnUwBcIABabT8Za4UYbLb5XYUfaJCApXqnc6XABM33qfU4WWSPlsyCOJ2+tnxUEJcFsNQAKgwTHAxhAttsEUjOijSeQzsDLgBmHFge7sKAQHLIP7JOBeZAAMj4ZAgMJVEF+zxesTIJkoyBqonEHVkWGkUC8TPKAAYWQoAAJiBIyODqOh0OCSe2O40uuCySjlBFYEFXFn2OjIWKrdasrYa17a0i6ihzOAUcrxrU6yhYHLpkbIADUyFDsM2rgAotBqSSsX46FQGMgBT8nq89KQIyGy3wI5nE8nc2nVsgAHwGgUxtls-KRaJxJ2HNF8kHYwjICkEok1ABi5tYcCI0tlNTo9SrVKJ9cbyBA-ezKbzqwAvq3NawvmBbRAHUapCa4DdD0KC9P9nXUf10yDEEBQLBRw0jaMe1cJp518HlWWPOVxWJKBbFsAB6YgxQlXxnnIHsIDgIJYiw-VkDPEUSJyYkQGgwUX2QKR4A-epKOo2JyNZA18gobJWB2DM-gBIE6CgUFWFIJ5iTk0FliYIJWFBJgxKoVUZ1mOcWk5Jdjl5DEICFdcsJqKiaKwoghNsgShO-X87AcLAqA0ECPIjDhgm1NsXgqNYezECgTAYVlGJ6MzWSuN9XhpW97yTHMnxGV9uLgVh6jAZ8iHAaB4FoMAxAAR0sMR4EoCSKB89cwGVKgaBQMAFBgGJvFIapOGSBQ8gEaEIHQHD-nGacptQZ8AF0gA)
