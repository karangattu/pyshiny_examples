## Key Features Demonstrated:

1. Used `navset_card_tab` with multiple parameters:
   - `id`: Added for reactive tracking
   - `selected`: Set default selected tab
   - `title`: Added an optional title

2. Multiple `nav_panel` with different content types:
   - Plot rendering
   - Data frame display
   - Detailed data table
   - Performance metrics UI

3. Interactive controls in sidebar:
   - Region selection
   - Metrics selection

4. Synthetic data generation
   - Used NumPy and Pandas to create realistic sales data
   - Simulated monthly sales and profit across different regions

5. Reactive filtering and rendering
   - Dynamically update plots and tables based on user selections
   - Show currently selected tab

## Installation and Execution:

1. Ensure you have the following packages installed:
```bash
pip install shiny pandas numpy matplotlib
```

2. Save the script and run it using:
```bash
shiny run app.py
```

## Package Dependencies:
- shiny
- pandas
- numpy
- matplotlib

This app showcases the flexibility of `navset_card_tab` in Shiny for Python, demonstrating how you can create interactive, multi-tab dashboards with various types of content and dynamic filtering.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQEsZ1SAnC5dKCAEygGdk+7LgB0IDJq2QQAro1wD+EdKPEs2MKBXQAbUhW10ARjlw69C9toqiAZs1IxkPKhQZxkqyc7iv4RX3BccFZQorb2jrwAFnQQ8p5szHBQxK4AbnDhDsjRsbhYcAAe6Em8-AkeStIURNJ0REnccMxhEADEyADi1M2a7ry4lFE+dMROmqEQSljMnFwOWLxwgQAUACwATACUot78ALxCWN4A+rMQAOZwK7wUUKz7AOQbAAwbAMwAtC8AjN8-jyI1C4T1eH0+Pw2n3eAKIdjgAEcngBZR47CC8KDaOC8E7OKDIQ7oLhYAAiEwAYrN4CsQKJkAzkI9yVRHig9gR6YzHgAlOAXOjkNlSbDneYwLDEKKkUbXYCPAByaiigKZAGVSNUVURHgBRPgUVWPADqOMNAF0iLw6AAvOD7bEQFZ7LZbTkQRnqrE44XTMULMWxCgrACsL3DLyIrwjkZytvtjudfV4rvdnseAAV7DY6IaUH65gG5kGVj8Y0QwxGrfGHdQk1QU+iAL7o0QdNU+dhQK7IUjoVzkXiiOo4btwE59ii8FZchmufT24RgBVQNIdtgAYXuXGQABUoIZkGrpQB3Yh8TKEZCz5A57TaA-Y-a75jSTIQVvtZAbpJ9ARxoJDHuW8WEqKhZlSOgMmQMhKHsbQhwgE9cyiZAR2tQD7hWLZEBvEdYnQaoTiWbFUhnD1PUZJckgFcglyIG9PSXDtSLYPlaIgejrwoyiYOlWVeH2YAlwAQXvJdzWQABqZADFuG5vVxfF5XYwUIEec0sGkMQETfbC3UYxkSLgVJAn2UTxLAG90U9fCqgoE4pRMgBrQxSEKE4LnsaR0HI3iGSXeAKGYUYhyvQyArAFiTLYZEfBC4gwoYnjKKlGViBxITmMUrilyzUgc2sMBLQinJghiszhKinLwrAfLCok6zWg6ZEoFiZAVzXTst2YHd90PZCKFQtJ7kFaR+A4akfGaRDBtQkdoDSJYHPPXqTjuQw-MZOgQUCtqIBORblq45AOhErguFiC4BA9ABJUkQOYZBf0g6DgpSZyrpvYzTN26rsX4AB5DJmDSOg4BPE6OlJOAbCgaQrDK1jAmQDab3nJ9soB5ByWiNztyXBkOkB-s1KxVHc2xUQcJvdtFOQYHmjBiG9wPG85rQugsEWk4OAgYIZ3+nEGZB5nIavEbtDfcywExAGJ1F8HxZplLPQAAUaIJmBwXRrFVxkghsHJFN53XsNw-XeLvcDAjxCZCWN+X8UlPtcGw0rPToI2COqGZ+TU7DkAAQkOCztCXC3-Kj286CsZpbfxB3rfjrg7buYBk6SVPlN5f2hUk-ZDh9ig-Y47DzQ9qjLconQS5zC5pCSFZ6+tO19lLWMADZXUrhkvevIWwsqSpCJLoKEunFXo-82udb0ZvY5t7OJnlFk4A0uFF5TtOoHlNVFI32SD2CJ594B1UNGYZzmieUg0V7jwjby7Nc0J9ri6wcfQvNh-PVnsxgyZwTivZkfRD5AOXunTML8LREAfIYE+0CCq5gvvca+zAni8HvtXJiODGSzwxtcGwWNhZzGQPVXMe5Nb8FpB-GiActhNmQKpcgOwwA2WnpYEuhR4ECyXGvJcHDp6z1wLw7QgsRIwE1JQQRD9Z7YiuNwd2eCGSz0KK4Ygzlpz2DuAOCA+w1ghiEdHAhdALhRAcg+XAmpgzGKjkkCgjcPSzwuMQGwyjabMLztAbQyAABCv5nLzBPB6fq7MUKc25quXmnA+FgBYT4-xgTgmcQlliaW1FvFYhOIYZJpAQmCMjv5DWwJmjHAmCcOwsB3xR0Ns9LJ2hiKyEvm7KenCIE7wdnLHEO8XZ4GUZwx+I9fb0PIIHEOA8xLhyQL-RkHTE6HHmSvJZUCEkaUJEXeypcGEVxUdxQZvBmn3HkIsreWdeleU1OgQwbtc4cTRMAPeB8dQUItJpQ5MABmcIcU4nIRzmC4FaJ6aGPg2rYh3CyAkYSUocwWtEvmcSYZ3FjijSFXFJYZLAEEZF4Kd6FNKiUpo2t8SVKmqVOpNgEaNJJRtbEP89krIJIcbpSkJh9NaQ-fudDvHjNDmAKZEdZkMkZUnM5wD06MpUt49Zhdhkl1GU6LYuzBkPx+cwD0jKgWMg6BmZoNgWAaAgBlZAcVgqhVZoYcJQ1Ik8wReIvKeqDWcGNaaie6L0mLjAOgR1zBDUZROF-RK+Lq6Eq1lpOg5LYbsB9X68cHyWn0sGSK5lJtnZkH6XY-yXKtkKt5ZMyyRTBnCrFZAplMc47nOUpKu5akZWbNHtssZSqH4PwoHobJLLRUVvFbvR4Z8fTvNkF86eba7iNJKMgtgpzu2lvlK8jSiwh2Zt4quC4AbyBDW0LgYi9Np1Lx3k88+ml4CcGHdHVd66hhbt5jArt+6c7zuPckRVWrp5qo9COS6aQtpFsiVENYgtdXMH1b6517hXWhUEWmX9kS7gXF4Fpe1eyo4jjgwhgwzcly7nbb4-tvAUAABIQCjo7YpRABAsAbBsE2KDQrKKoe7OhugmGwDYbHeQmBhHiM4ZvZO8jlHqO0eQ-5Bj8GsAYeIfykGY4TUbqiFuo8ZHkBEYvVIq926WX8aozR9h0GYOMlE0xljIlpM9mRHJhTryuOqYs9uidhUtOCfYXR5dlFPwdApKQPQzRHoCAurmMmvjYJUHUcOLml8gn5KdEuNosXFPY1xlEfGvU0LWkuB1Vc65vzbgtbIziX4+QpHSO4S6vAdBQHkAVJGFUdxowgKGspIW9Z1J+lQVOG1E2MnfbeJcG5G6NH0PIVrKMNooBAB-DQsRDqrmWthHTYAmxEHANAeAtAwBJF0nQJI8BKAIYoOoq8YBgvUAoGt0QGgtC6wMJaqYsg8CiD5jwRCD8FvmiAA)