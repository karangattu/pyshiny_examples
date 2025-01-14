This app demonstrates:

1. All parameters of `update_accordion_panel`:
   - `id`: The accordion's ID
   - `target`: The panel to update
   - `body`: New content for the panel
   - `title`: New title for the panel
   - `value`: New value for the panel
   - `icon`: New icon for the panel

2. All parameters of `update_accordion`:
   - `id`: The accordion's ID
   - `show`: Can be:
     - A list of panel values to show (`["sec_a", "sec_c"]`)
     - A single panel value to show (`"sec_b"`)
     - `True` to show all panels
     - `False` to hide all panels

The app provides buttons to:
1. Update all sections with new content/titles/values
2. Show only sections A and C
3. Show only section B
4. Collapse all sections
5. Expand all sections

The app uses minimal components, focusing only on what's needed to demonstrate the accordion functionality. The data is generated within the app (no external files), and the example is self-contained.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkTEQAJnAZETnBQoc4oAczgB9UugqsAFFIUADZwALxyYACCxGQMVpzkyAAicDCkkUR0nMHBUABGoWEAKgwmcACUThAAxMhRVlbIAGLkIlEA7nCszHDIAMIAyoPIdEJ8ZBCszpxY7OJWnpNUlP4KyBvILgASxQCyADL+AOQAPMHcANaicMERYKwUuKEccHAUkcjsYnT37BQUdCsRAAehBxCsEAAVqwsMRgqQTFY6HkxHDmCCoFCoBoQRd8qwQWNKABaKBdHrwEEANiwABYsAAmcG6TG5LAwbhw3SRAB8xyqEEFCg6nAo7C2szyuERFCWpGCJhgEE8HQYGH8oqs4rCAEYQYyKoh1ps6v0xFAqMh8mYKOQ9OgoBBbiaNqLxZK4VB4v4ja7NhsXMRvYt5lAbAw1mB+m0mMFpmBBQGAy5jGZPBIpORPDaAeQoyZ0FZLV4oLlMshIgBVIsl+q5ZCDOCSRJTCvwqC6Tz3GAk3WRJPJwOzNNyzOtnO2-ORDikDoZ4gVyKDdhz5DkYK8KLIABkA3beS7Pb7A-9KZHEFMY5b2dzdogUdn8-yS7AK7XG94ACED53WN3Il7ftEzPTZU0vdNx1vKcHxnVd5wgch5EIStowVPIgT6KJyxQjsj0Ak8QIgIdhywUcFyzFU72nB54IzHCiEiABRLQnSabDgl-fCwCA08IH9M0LStCQ4gSJJHWdTjiM2d0JSDENfWNaSh3k+JPDDCMoxiUTWxSNIMiIkjkFkz0RKEMSH04Kx7hEisYBMYIpHQIpSnKP1lKM4yxTk2YzPiCcJNuKMmxvYiograQy3Ke5WGbDMByUzySMiAB5BhODcbgy2QZZqBEMYGEbZtKPqSJQKHcrkxMlw-IszxAuCYLit0n8UMixVwhnOKX0TRKkuTVL0sy6Bghyto8tGcYQpK1rKoDOaZO80zYnMgKnSC5dmqSfoIqizqHjixdeoWiqwDSjKstG3LKEmwrpt0nawGqOomLoOhiuQO1kBsdIpgodUrULYspAgNwxsoPKiCCUIiDYiZyAUAABC0W1kdQ3uKpGUakNG4FkVZRywIGS3o4JBRsOhkE8RSBOQGtgb6WLQvqLyPWdDpwZWcxPrFUJkDhzhJn9FxiaoBcdOzBq1g8gMrJs2JMkqihvQ8CgYriqBFZlzZq1rKgmmu-Kpq2sKtaM6H9oAOTgDn7qSbdil55CCEqwXyDCFxlbcWFOH8PD-3uOgoBJHoLiaIOQ+Vhg+IDQcNlp+m6yZmbWYlKETEeZB2c5vLhdmUXSxW-zJfWxrXesyJbMIJWVfedXiBzM3krARP9Zzm6CqK5nZo8uPKw8upW8Zk2BlTrObfbkQ4fa8o86JvXC4llUpfL+Wjpd7WNij1X66WJdN9QoeDfGjvjeZx6N6Mmf9qZpZPHZsre+e5BXveyRPtIFQPwgTc2BNvRtxwx2hAZG4hUZwHRm-D4IDsYyAgXjPK-hCZPgXOTOAlNqbuXPPPBm4tVo0SrkQJ8YRgBdQbprFCZC95gAALrClqC-DG78vpPnXD-XgycWpYzATjeBTDoGgPHLjfGFAkEQQoFgFB+Q0EYJph5EWC88HF1gmgBWKFiFUJ6vQl6-CP5jVyBgWK-MGycPtNwoRfCoHmPAeoERYirySLoohZ0MiqZyOwQXJRFkoyEK-h0MIzQyyxW0YwqBejNASSaGWUapi2wwJ4XAyBmN4kWNsYg5BdFomuMwX1Uinjaqth8Wooh8EShlEqM-BoTRZRXj0aw4gJgGCWCnkXCybBlZUG4dYWwWAqAaGgRTfmsRPCPBLO4zYYgKCNOInQSI-RGnNKGUvdpJYUAgEJiJX0ABfSIYAtk0KAA)
