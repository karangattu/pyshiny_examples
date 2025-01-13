This app demonstrates:

1. All parameters of `update_date_range`:
   - `id`: The ID of the date range input to update
   - `label`: The label text
   - `start`: The start date
   - `end`: The end date
   - `min`: The minimum allowed date
   - `max`: The maximum allowed date

2. Features:
   - A dropdown to select which parameter(s) to update
   - A button to trigger the update
   - Visual feedback showing the current selected dates
   - Notifications when updates occur
   - Random date generation for dynamic updates

3. Layout:
   - Uses a sidebar layout
   - Cards for organization
   - Clean separation of controls and display

4. The app allows you to:
   - Update individual parameters
   - Update all parameters at once
   - See the effects of the updates in real-time
   - View the current selected dates

The app generates random dates within appropriate ranges for each parameter, making it easy to see how different parameter updates affect the date range input.

To run this app, simply save it as a .py file and run it with `shiny run app.py`. The app will demonstrate all possible ways to update a date range input using the `update_date_range` function.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAEyiooEt5kf1SDCmw5wi3eKzgAbClAA6EfoOEMoEVs0WNmyAM4ALLhFx8YAocgZwoxbgDc42pi0PHcWOAA901vXrMLYWN0AFcKIlCuImsNOAZFRQBiZABlOGF0KABzOGRSdG5yALpBZChkYmkbCGRpKFxScMUonBy4AH0Cij0ACm4KaoBeeTAAEVFkACV1XOQAVXR2KmQxuBhSUaI6Lml6gCNhgBUGULgASkSIFIBha0mKvS4pfagGZAB3LgoDSvIKJjSPSKL4-ZCtJ4vN69c6IRTIBHgrhYAwAFl6oxu-0ByAACuoZKNLrVEfDEa0QuEOnoZHA7BiSYjSWAsmoYB0KKQOqElqItmSmQjRvi2Rl4shOQteVR+YzBSABYKmaMDoTaKNFss8gAZKD7NUERVKoVgPRyISjFAa6V5VLm4QTGWEI3G0bUViW5DWrXIACiGlWfOdcuNXrAMGMnu9kwAssZA07DSHXeGoF4o2BNbG0wmnMHQ8q0HsM1mVgBBPZ4t6wMUMYFgF0IgC+iuJyrlFIgYQoHVsRQgHX24U5EAZodGPK1g4oEFl47AZcw0lMpbzSdDVSg-g6IzA+xnAFpfDw3rhRq2rikY1B42RKNRhG8bCDvr9WvVGlSyNJQjAIH1YUVUE32RYg3lYGE4WTBFWjAhhWA6AwbCkBgMTAAB5BguGyYwoGkXNplmPIAEku2aMA22NTtuw6Kc1AgXIxwLE06KIgBGOdmLDdJqjsAiZgYtdG0FM03goIYtV6AAmAAGKSAGYiDYpTznXLj3Qk0RpLkxTkDYqSiHktjVOEpkIwgTSqG0hSlJUtTmJgNNLLgazUSUgzkCMyilWJIDXyRLA4IgwDoICoLEOQ+I0JuUIGFiYQADU8LOetvMFAABWIUKwKJhKkOh9AMUgPg6exkrgACoK4kQqACIY+DIigsFYwS2JhUzES4AqtQCLgAgAOXIOAquqxFrAoWLalGQaaoq-RaTsOAPQbUKmXGyaArkbI9Garh7CY0bNpyHb0F6OhRjtMTcxQEAeuAGSAF0Wwo+zRtaLaTrO0Z-VYa7kFu0Q9GANinqJDqEV865kAAMVCCA7C4cgJVIZBcggeJJnozQWB6xR8qsdRsdorTRKEIh3RCpkJE6fUKA+OBqGQer3WQA99HtRV2FwPRBwyenGfq6nebphmIGahpgTlLHmGJ7mmYJjRmCwLH6MYrmedp-mIDS9aGFqUnhAAaglHglpkORenVoZpfZdXIZSX06DoOlhElAxCeqcEbUlzKbARxxPCdl3FF9vs9rgTxHEoXpKSaydRGnbW8bgAqOkgxVWVgeXY7aNkOS5eOrLS14aWJlZ6sk2SbL0lTFUVLrkEzlghnqlU9TVEalVaQvOhaxjwbDPu4A4-MuNVaQhnOzMbV+3V9Xw3oQBt5XCeMChemUvSZJk84m0uFbQzSxUZAbpumdb00OaQYT0ZKg35ZtsuXMrnTbL01TZus3SADZDJ3tKmTdxtE-DoqsXID1GEPEer1QwGyGLfakHNQpHzlCfAqZ8W5hndJaG+cASos3qo-SSL9q4AHY7KfyrrpfShljIAPJMiHuICwEHQLJAhOYDoEDw0gg7ByC66oOkKfaszcL7mRwaFBB5kH6ExlsQrSVcPKb2MkQEh1CVL0Jgow4BQ9WHzigZxByxh4F4I6OI-hcpj5CPQSI8+YZHLpmvpI0xDiZGK1tlpEhbka7v1UQouS3iaGeTocJIBU5dEQLAAY0eDknJSLTMJFBTI0GN1sZg0YeFpASNDAg++hDZEeKsmot+KjKGv2QL-Ty-9cH4IDPk9xT9Lb+LIRQ4pekPJeU0cgKR8Z6lE3kVZRRJSP5tOUecLp8SvBuP6Z45pgTWlzPcrQ8ZwlQnaPCRwoieiUzRJgcacek9MTMHQNUFYq5kCL2XljNeG8lLb13vvPZSo4G5PtE8wUPDTHuneWZYxPSIA-MRA4kxJUHGJMvMgMsrBfoQFINwHYYF+wBElIYYqnx3YUAAOQBH1MYbIXstQeggKHf2EcU7OzsCHe4pLI4Phjo1HKwD9xJziAVVFJVYXwq4IixGo5KaIgwQ1bsudYD525DadqHZkScq6tyjgvLqRFQ+NshEU9Vy-RAE3JsqTRRUFQnoR5eVYryvIEMRSwkKC4HQHAXc8B-DtHPHKc4YAmxEHANAeAtAwDWAAI5RGsPASgO0KBeAoIQEg-wHxesUI5CgJy4VCP2IoCAv48CKCyBoLcVxqouoekAA)
