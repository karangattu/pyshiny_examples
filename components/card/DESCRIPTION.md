This app demonstrates:

1. All possible parameters of `ui.card()`:
   - `id`: Unique identifier for the card
   - `full_screen`: Allow card to be expanded to full screen
   - `height`: Fixed height
   - `max_height`: Maximum height
   - `min_height`: Minimum height
   - `fill`: Allow card to grow/shrink to fit container
   - `class_`: Custom CSS classes
   - Custom style attributes

2. Card components:
   - `ui.card_header()`: Header section
   - Main content area
   - `ui.card_footer()`: Footer section

3. Both static and dynamic content within cards

4. Minimal use of other Shiny components

The app creates two cards:
1. A demo card showing all parameters with static content
2. A simple card with dynamic content to demonstrate render functions

This example is self-contained and doesn't rely on external files or data. It uses minimal additional Shiny components while fully demonstrating the card functionality.

To run this app, save it as `app.py` and run it using:
```bash
shiny run app.py
```

Package dependencies:
- shiny
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMpwR6KAHM4yUnQpclYFSxxfOAB9QIpWAAopCgAbOABeOTAAYSgGW2QAETgYUkyiOk5k5KgAI1S0gBUGEzgASicIVxy85AB3Tgp2ZCgq5EFdTjr-bwZYTwdQiH7B5HDiXNt4hWQdvlsMsHsSqPW8su3duhMqqNZiMWpG5rgiZFcAQSrSXuRT-IpSMgav5NN47HB-oCrqM7g8IBcduw4JwfOwKAcAMwABix6A0ZV2b3cnl+G2QSJRaIRyAqVSeLVehN2Hy+Pz+yAByB8TF6AHoOAxuABrDlQga-cgUKDcBzU4jVXRRA4wXAAWgALJkmUT3rZ8sQTKwASwsm43L8Faw4ItWohqV0yUioPZHBBCWsNlEnS6tm7tchMt18kUSuc-drMg0uHojiEKLMqHoRslST0ZnMqAxQmBqe1wwH8w6ejVSLZeGRKNQKNTwjBckLbN8IFsc63qVHOHpOxykcg69wJZXKAE6D3-H8sO3e+z2FA9NJcpxSIaxrkMws2CTuPKTLZuD47fnqQAqGnXZK3e5wR5NFrIVXDVl6UFQOz70VnmFX6gn8nI1HogA5NiuIaIB96bnENKcBoEJ-pS1b5qetLJPS-gPsm3x6OynLct8-LsIKEBCr+8pzqwSqASqGrgRherYYaxrIKa5pkbo1rUpkXFgHm9rMWSdCkKQmY1pwWB-FEgnCQ4vr+gG2RkgAYkJImENShJsRRBxUBoFCqjAZgQlx+a8Z0yDvBAwlIgwqb5Bw3zvmW0AwJwxCDlQlAKMsQwenksm7Jw+yZE5sCuScGxhoS0IXrC14QGhBDUhSAEHAATDieKRbsmlKpkMB6ZqOYQLaoniZ63oyZkBS4M5rnMZKVaFMUpQ8Zx+YAAI2C6WA6YhhL2KOIUucQJwNZQ8QlfmhJiBQJgMG6kbRrZKhYeS3wftuyS7v4Q11RWHkiIa75dQ4Z4QJIS4QNmYAAL4ALpAA)
