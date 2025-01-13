This app demonstrates all the parameters of `notification_show`:

1. **Basic Parameters**:
   - `ui` - The content of the notification (text or HTML)
   - `duration` - Time in seconds before the notification disappears
   - `close_button` - Whether to show a close button

2. **Notification Types**:
   - `type="default"` (default gray)
   - `type="message"` (blue)
   - `type="warning"` (yellow)
   - `type="error"` (red)

3. **Advanced Features**:
   - `action` - Additional clickable content
   - `id` - Identifier for replacing notifications

The app includes:
- Three columns of controls for different types of notifications
- Font Awesome icons for visual enhancement
- Examples of HTML content in notifications
- Demonstration of notification replacement
- Various durations including permanent notifications
- All possible notification types

Installation instructions:
1. Make sure you have Shiny for Python installed: `pip install shiny`
2. Save the code to a file (e.g., `app.py`)
3. Run with: `shiny run app.py`

Package dependencies:
- shiny

Technical notes:
1. The app uses express mode syntax for simplicity and readability
2. Font Awesome is included for icons
3. All notifications are triggered by button clicks using `reactive.effect`
4. The layout uses cards in columns for organization
5. Each notification demonstrates different combinations of parameters
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAIK3byAGLkRbgHc4VmY4ZABhAGVI5DohPjIIVgVLLHZxWwB9RKpKAAoFZCLkVIAJABUAWQAZPIByAB4AG24Aa1E4JoBeOTBWClwm4PS4Cl7kdjE6HrB2Cgp0VkQAemXiWwgAK1YsYibSE1s6JqgxXeZlqE2oDWWWgCNWZbjKAFooIJD4ZYA2LAAWLAAJjWukuTSaWBg3F2ul6AD46gBKBQoiAuZAABSgAHMwlIKENkFA7Mh7KxiAxOOgpOQUpwcLi4JlSDTWHkCUMZgA5UhSOicYhQWkQZAAETgMFIvSIAohUHuXPKDBMcDRCgCnAo7BKDJOuAOFGypCaJhgSTySMQhWKrnCJrNooAjCgAEJQViC5C8-mC4WccjJUXFTXa3W7U62S3W4PFYqpIUMLLpKD2BgFMDuz3Eb18zgCoUi5JgNFxuOpYxmTISEWZe5mCjkDMcUgBOsewUy5C9SLsVvILNen35v0i3qlstFCsQUxGmsBiB1htN3ottv7CA4rs9vsBZDVcg48UmBj+uklm2T6ez6uSBdL+Yrvq7zIQUjZfaseSEbtgXv9gB1LU+zMCJPzCV1l3RC90VjZA7Qdc1kCBFBhwLM9RXKXB0GCS9kFDHUE0jaM8PLBlE2TDIHAzNDRwXZAsJw4sJyvBlKznO9yAfRsIGbF94F0Jltz-XdkEqYJWCZBjsO-Fiy2vKt5y4+tH141cXwCU4IG4Lcfx3QCtJ06ScPHUj4zYmdFM4xcVJ4vjW0yBwmEcPSRP7ABRBhnOM2SnDghDTSQgBmFA3GsvQSS8ABJMUgzjAjwwoki4LIiMk0yFM0wzMKi2JUkYuYsypwsm8lJsqD7LbMrhP-PcgLDHKF1MlLzKwdjb1rWynzXTIxHQE5iG-Ih9L3AAlOB+okcRFV8lrirayyOM6ir1IcvqBuZEx0FsYUht-ABVbbduQcbJsGhUhmajF3NkSgJkioYGD0OIGGQe4OxzN9fULBcgwAATEedZHUOg6DgSQFAB8Q72BuBbooPJ2KwHr3uzNF7DoZBMmS1KvpHH6uLXAo5t-couD0TgIrej7kDx9Cx0IIqyRPDCuiCvD1QgKGgbgEGwYhrnAZh3m4eoBGkZ6jccXRuBMexq08NSOm6MJ3dicnIpejJynabzen6P6KBcGe+InQABjYcHyFsYsCCZ2wWZFLpzY5vzueFvnwbGQXoakWH4cRxbkZfN8P1IL8ZblnHWuVgnFyJpmtfJ3Xvow+69DfZA9nDsIuugu2Sezr9uPILpvCgJovwLjXmdPJ2AFZXdg1wbrF+67Eek3XtjtOBiYyGhb9kXQa9gffZkEWA4l-iJKZSOsej+ae9rBOSbKKpakaTgs5OXQZjoKBXhCFovAP15iE4Bg9jgV5uDiBEGmWTh4QY5OdagZABMkvFkD7sJl4XMiauGs-4zC-kJMATcx4809gLd2Q91BTyDj1TSDBtKbnnvLGMuM9Yq3jmrJm68aj1AaNvPYHpWD70PsfTgp9D4UCpCSHEQxXiaHITADCD8n4v21hTKmqD0FHj-infGGEgFM1Ab0AROlehQJ9jA2W-NvbwInogsWgdZzBwck5IQmDF7hgAarVs6sNZEM3qQneFCqFHxNLQ2Ih8L5XxYRoDhDBWhcOfq-HW79RQ6NesIwxEBxEk0kWAPxsi4KcxbvDduthO6xHiGVCK+VYrQI9oo0e8j0lIM0T1MqeiFZwSVrguOmRV4116LROO+FgLEmsjKJmZUuipCgBmcILRiDtHgAAQi7JMWWMxnBdnIHsQUrQZgVwcAjOojVyA7zGXAWw3TkTjmAZOB2dcFxdF5BAMI8FkCRAoEbPQJhKCcCaDvHOtg5EqNhiPOBg9VGi3yNPNaE0NoFOwTHEpGEykEJJknbxVN1pTQuv-H5DM1llloTMEF50ZoNJJhs1mOz5CRLdo8u5Si0kIOeeLZBL44WbSOlQT5isGSBL+cYxOYBeEiP1nMolXhtRhG0HDAMJg9DkCGkzGFvQiVgsRTXUJ4C8RCo1sip27NIlgAAL5EHANAeAtAwBiAAI6WDEPASgOwKAaAoD+MAOQxYqoUBwhY+xCScHuAoCAZo8AKHQJFD0fka5xjlQAXSAA)
