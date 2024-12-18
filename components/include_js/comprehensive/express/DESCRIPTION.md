This app demonstrates the three main methods of including JavaScript in a Shiny for Python app:

1. `link`: Links an external JavaScript file
2. `link_files`: Links files with potential additional imports
3. `inline`: Directly includes JavaScript content

Additional features:
- Radio button to select inclusion method
- Checkbox to enable additional kwargs (ID and class)
- Text input for optional script ID and class
- Buttons to interact with the included JavaScript
- Reactive text area showing method details

Key points about `ui.include_js()`:
- `path`: Can be a file path or string content
- `method`: 
  - `'link'`: Recommended for most cases, allows browser caching
  - `'link_files'`: Allows additional file imports (use carefully)
  - `'inline'`: Directly embeds JavaScript
- Additional kwargs can be passed for customization

Note: The JavaScript functions (`showAlert()` and `changeBackgroundColor()`) are placeholders. In a real-world scenario, you'd typically have more complex interactions.

Installation and Execution:
1. Ensure Shiny for Python is installed:
   ```bash
   pip install shiny
   ```
2. Save the script and run:
   ```bash
   python app.py
   ```

Package Dependencies:
- shiny
- pathlib (built-in)

This implementation follows Shiny for Python express mode guidelines and demonstrates a comprehensive use of `ui.include_js()`.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZdKCgCwBsBLAI2Q8Y6UgwrIACuw4AdCI2bIAzhx4Rcg4aPEM4UYhR4A3OHIUsVa3FjgAPdLqVLNIsYIjoArhSKeeRXQgAEzgGOTkAYmQAYV12OGQoZVxKDjhDYmQAKSgjKABlYgYedHEySmoKOQArJQB9cqpKZABeZBkwDq6IAHoe5HzYdC4EnLzC4tLkOk8IAx5yM1n58mUOUgB3AEERsQAKAEpkEDlkM8Tdij2AcgAJOC4uUmmmFjViLk8QoOzcgqKShQAITXA4AbjkAF9wvJloZVsQOFAIABzOAAIX0AGsUUxZkFoqQngxDsdTucgqRiJ54JQsHxSEFrEoKLgRvTsbjSPjCcTWu0IOchchrhFrsgANTIACy0iwdCeoj2ss4WAYyMpMEOACoAIwANgA7MaAEy6gCsBywFFI+QoxVRewN4KhMPKSiJcCwTxRNzG-0m4joPBGyCeUG+yk8xGIcCcM0euBBLogXU6nVTED8OCgaLqpFKSj2hgoIxaHQAknNPiFsvlkAAROAwcgs9Xw1NgA4wqKxPRURLIKhadUMDTB0M25AhFsQNvxaYhhLvT5KBaZ4foOq1OoThJtKScPZ1XdLk9WtiBcT9Dqbuoz0hYWrdO87vdYDbFKh1Ki2K47xpKm7TMNh4ThkGzLgoFwbkKDqNcQj4KASQORByTOUDwOzBC4CQlC0MFYUzmzNQvDg9UggWOo+G8G05z2dCiPODp4E4RkOiIRimPaMAqw+L5RnraV0nWIIOIFbihWADpeAgLFxJktQsVPEYlAUsA1Fk0wwAAXS485gO4-TiJ4LBSO8Bo0mILEGVsBiwE8JQ4DqLENmQlE1MIHiAFUnOQLYgkojsoC4ZAAGk3IYDyOkMpjjOQXtyCC9cQvcMjplERJArAlLQvYe1+G8ON4swjgINMtgIAeBokpy8gQvs8yKCwRznNc9zPNQ+KhRIjwLN-K4Oh3HgxK8joJkBZAKwbcThn0OB1i4EIGHLMAAHlSly5QASmaaYu685erIn87EGsAAKgpx1ImqZokuzyiDm2NFuW1aNuC0KlB2sp7v2zMhSiWU1FYZEHiHZ4Hzne0FyyesV0c9dEmCdwqHVFZ-vOUryqwYhkKCQ4CO47NcYYII6jSCNQns-0bvEPjV0RptZ3nDs-qMwiiKidFaNWKcCpRNEGF+cZvumOF1zUjnhSOiz9A7aieYgeyVE2OoQtCKoxrAfJ1g2fzLjZpiZbguX1wVig6PsxFkTzMhiXU6IkVRBJMWsrl8RiIlRENoj4qiLY4nBtZNjrdx+LXVYQgoKAQ0l7iAAFAmW61TvikI6GQHdWNE+90hjrgiy6qXuOzxl+SarBS-x2LJOnPPY-5OgOmEtighQEAq+hcIM1rs4DrOKIJF0S8EnaqLnB4DPETgazbMEZxp+suAxOLpix48-kQGhVeiMntLvBapyXMijyCf74U94r4bq8J3vuPXpRgGuEbrh08u+ua6-DnPoVL4-p96gfCgE4M+O877IAfk-IBTg6iv3fmRABDR7rfzAUKc+UQmatmhgOSidA6ChEqGHBmqwq5x17nvKurQ2iKTkh0W+4DsbwxCNuIsr56h7iIFXFo1xZJYmuEQbU2oH413AVHfOzgJTULAAAGSUsvZAp1QjQFCjTUWe5uh3weBQkSZcWhSN4SpYqSAf6HVMkw5ytRizNi3G+JcnCdFBG4QYvcSh+HIEEcIkxZwxEN0kTxWRcl5EuOQFjEQTRDCpQjMleqoUhCuAoJ5c+DwnIoASu4LSXjGHVgEiwvYAFyDhPsa3bhmk1BwDcR4k+SgRF3x8QXSUUiqxaR+KowMyBALNEoroAwXBcAaN7ufXQFBPAMEFHUyWkRkAACU9DzBMAovBM8ElB35oLYWAZJozDmB2SWidZmGBMDYRZBg5B7NNocuAJhKB7ArirDYatLjAXTsgOooCAbIAACqqGcBsbkS0hy4HQDwXGiYhzFAFqEIcaRg7bEuKSLZ6N3BQuXNkyMsNGJsCupmM5cyvRwGOVUCAOKDl4quVcCu1tnY1WJE8-FLy3nnCiF8ngPy-k-FZECkFvSwU8AhULTgCRKVoldjiPEwReRKiOAijsSKBVEIEi0-IGLgFKDAJCIg4BoDwFoGAXQABHPwuhaQJOtH+LyYAOkUB1XIGA7BhikFLPwOQWZhB9I8BqYBMI75qp0kAA)
