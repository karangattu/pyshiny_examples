Here's a Shiny for Python app that visualizes disease outbreaks, cases, and vaccination rates using interactive maps:



This app generates sample data for disease outbreaks and vaccination rates across several countries. It then uses the Folium library to create interactive maps that visualize this data.

The app has two main components:

1. **Disease Outbreak Map**: This map displays the number of outbreak cases for each country using markers and a heatmap. The marker icons are red medical symbols, and the heatmap shows the concentration of outbreak cases.

2. **Vaccination Rate Map**: This map displays the vaccination rate for each country using markers. The marker icons are green for countries with a vaccination rate of 70% or higher, and orange for countries with a lower vaccination rate.

The app uses Shiny for Python's reactive programming model to update the maps based on the generated data. The `@render.ui` decorators are used to define the UI components that will be rendered on the server-side and displayed in the browser.

To run the app, save the code in a file (e.g., `app.py`) and execute the following command in your terminal:

```
shiny run app
```

This will start the Shiny app and open it in your default web browser.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5CAV0d2SgGd26ADoQGTVsnRQIAE368B6GSLEs2AM1IAbOlxHrmpGMk06uOLRwDmdCANUSAEnCgUAshiIfmAazjMAYUs+KmZ9Q2M+AAtbHgc2AEFMIgBJCHQOCj4iAHlMjKyiAGU4Pj46ciJmF2IKOgA3OCrqGX8iDjoREQBiZABxan9XOGQ+WHQtEbkKKBF0rGZpGSMsPjg4GQAKABYAJgBKETIOSmY6UuQAXmRgITAAVSKEu6I7gOkoORfkO7c4AA86GRvncAEKLABedC0IIeAGlYQAxRYQYhwWEDZgwaS4WEpGZaXGEH5gAIxaCwgBSGGkdwAuiItK4rjcAMwADiwAE4AAwAdl2RG2AFYsHsAIzCoi7VlYABsrJFRAAtJKsHz2TzxURheKsML+dshZz2cK5XKdbt9bseTyhXrebt2URWVzuTy9i65Vgbdt2QyIFpyCzgMq+XysDzWXKuSq+aKYwKVeKeVbhcKnSrthGubtcyqeVhxbsNdKsKyM4LkOLZdseQaiMWxVy5Ubq+LvXW+W2a5zdhmuQHSJkAEbVKA+AD6xH4F2u8xRyxgCyWtgomxTdurtttRHKELgl0mEE2x1O5z4+0OEHqUGIxFsrgqEEniyoLIXSxWJzomixm0LVkiELWNRjoA8j2oU9h3PUory6WQ6DWWdJ2mKAWSULAABFXCgZFYDgTYQBEZBSJJM8KGYIkUAos5SgIEiyLuJk6goDhWjuFAWIYiAyJJIMIBsNiONoASeL4u5hwoMcXCnGc1j4TjkCkmSJ2nWdskY0i7lve9HzqchX2GJTdIfaADJfN90QgABfa8RAwdBJw6FkOhwKArDgSd1EsOgti05A3KZXApOnbQuBfAB3RZ0E2AK+LcmdmH83i+LS0jEqgZLJyiFxWmYOKwCwpCXDWZA8mk8cfGQDxhDAfZxPStK3KkgpnLoQqVKqydsTqhr4qa3K6CsKIKEuO4DR5dB-heAb0sivyKCicawE3ABSWbUvS-qtuaugsCSlKmr2g6spkHK8v8QqADU7zMp9gwAJWGGqMDuHbjoS-bWsydrCtM-Tnx6t76saz7kCGkaxom21ps28HSIWmQlpW9b4aaj6yOvezZDgdRRn8RoCtsAoiB+ig91KcpyH2RAAoAAWqXHmCwDoAtafGutk4HYtpubkGMa5TF0Zdas2IMZwsy5gDrFUuWFOkiAhUgjEnEIsrG7Zr2O7FfH8adglCFlvD8QJDau-YsE+c6KFITYYBx46-2QScqlISLkFsZAZBKlC0KwOhQkMSK+E2Pndqd7QRawE2rv546JYeiBpeD24wBYwP2PRMBFeQVPmPIISs-pRX46apgMnQS51DuEBU4Aclo3B67pGyUDr93gHrrm1Pk0oW5s5A+8Uwgy-SoFyGrqPzBSMgTzIINmBW6plGJCfk7ueAZB8QPvnQap1Dof4VvUWZQbH5BLetydbftrLTYNjgQn8R2mucVwxYvtDLh95C1lQ3CwA04Z2EtnV46dC6ZxEuAnuckNIlywLeSw9EL6LB9k-S4NowafRHJYJekpsE6ygP8ScysjCXBTIQrGVsZA2ztg7BCx1qhsWYLxNyjgAAqbgAAy9ssCvjgPvHKFAYBaEnGHV+pFGYtH8KzTou0ObIABuZIGvUw50wjmRQWJhp6iwwOLUgktnzS1lsgZU8tc5kJgGrGYrBLha35rrB+xBzbMGNvffwQQn6hDDjQuh9tJFpWdq7PO7tPa8V-qVLy-tA7+GDqHcOCMdFmD0XrAqF8+KJylsAfO6cnygPpG7SKwDIEFJzqXTR4MK4cCrjXMAHdimNxgpRZurd24N2UUnIyVAW4ACpNyIB9OoGya0lF3X0hsdGSTSLrynikrAs9yBxUqdMheLAVpWGqNQO4nt8a5M6RZbp2c6TIAAHzXELHyZAcAtBlUkiiTyUzpl8VmXcPguAziCTARk8uB8j4nzPlQ8GmNgV+JvvQjxzBH7P2YIEvizCOCsMCvtThPC+ECKEaNUR4j4IQAcpgFkSRYqOXapTZgRN9hgBskQcA0B4C0DANUAAjh0ao8BKB8CwBQf4FBiRgDnlQGgKAwAiGxBQCYpAKA6BHHMLgeARBSFkPwBVQYpW4jsC4EcLA8V2HJLgJGnksiMIRlSukQA)