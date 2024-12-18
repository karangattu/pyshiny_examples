This app demonstrates:

1. Basic numeric slider with min, max, and value
2. Slider with step parameter
3. Range slider (selecting two values)
4. Date slider
5. Animated slider
6. Slider with ticks
7. Slider with custom formatting (pre and sep parameters)
8. Date range slider
9. Drag range slider
10. Interactive plot controlled by a slider

Each slider is placed in a card with a header and displays its current value(s) below it. The layout is organized using `ui.layout_columns()` to create a responsive grid layout.

Key features demonstrated:

- Different value types (numeric, date)
- Range selection
- Step sizes
- Tick marks
- Animation
- Custom formatting
- Date handling
- Drag range functionality
- Interactive visualization

All the parameters from the function reference are utilized:
- id
- label
- min
- max
- value
- step
- ticks
- animate
- width (default used)
- sep
- pre
- post
- time_format (for dates)
- timezone (for dates)
- drag_range

The app requires these package dependencies:

To run this app, save it as `app.py` and run it with:
```bash
shiny run app.py
```
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAEyiooEt5kf1SDCmw5wi7TjzHJu8VnAA2FKAB0I-QcIgBXGHmRQAzsgjo1jZskMALLhFx89m5AzhRi3AG5xzTFjbtcLDgAD3RXQ2MNIT5TbQoibS4iVwh5BjU1AGJkAGU4YXQoAHM4ZFJ0bnJDNSScErgAfQqKQwAKbgoFOABeFTBchS505AAROBhSfqI6LgUFKAAjbp6AFQZtOABKTIgAdy4Ka2Q6hdxSeMayBV0Idq3ENWRn5ByAISMuYhNdOAYvqxDdJPF4HI4nLhYYhQBisNoPEEvF51aGwxrWNzpNr9D6GAEAOV+-2+g2Gf36OwgSKRdTs6EuhiBf2xVOpbP6OngxMajLJGUIyERbJeOM+JKZDGQbRgdiIMCgISInigN2200FrOFLxlEB6AAYiEKtfKQj0AIx6g0arVI5WqnoAVj1RpelK1LueAAFUuksFQQhQPWw4HQflyvo07Zt4Y9NTbXBRtAwqXR+vluh44KxkFG4CgQHT4lhOX8I7ysVsAL79XZInKkkZg46GKhmONNiFQmFwhFxmmQ1GsdGY5lpiXIDu5VsUoO0uIUHkSlk2kVgFtwdCLvnqoNItOtvISnd94U6-WGk9sk3mq27l65x0XlfPdfofVYB1Bt3CoPe6i+-1A0vYNQ1fSMVWjXtnxcAokxTNNFDgTNs1zfNCwoLAwPLZkqxrCAhRyAAlKAIFKQFt3bQ5jhRbsY1nAdu2HKAsX6YjSLKBtyTAb82TnekF2whhl2ffoGBI0ot2BAU72eVjxI4xCPC4chj2gs9b2ApFrwtDToIfNoAGYrQAdj1HjqXMvdgL-NI-j9UIgK1eRQzE9jwNVOjNJeBM4OQVMBkUqhs1c0o0PnLAQqaQT4WrMBdnrJDyGC0g9jUDtTigc5LmuW57ljOsxlEcjgUo8EaNhTytXKocMWY0cwFGIrOP5SzkUhdDJNHLzZLACQoqPQgZMFAKM2ERqqGmIazz6toACY9VmgyiDNZatgIKaFR6Gb5sW5bZqIAyzTWoaH22haluQAA2ZaHVa547utYUbIAhyg2ckQqHcyD8ufHzkz8hDRqzD682QAtwr6zqhNwuL8LjHIAEF1HlILivJUrqIYiqoOFaqmJYsAkZ4URs2amdgL4hklyG-oSOJoKocm7rhqJlHgbJwbmfU9auc2nSeb0iDeidAXnzptm1g2HxgIe38fTswC3pDAxkZJr64Eq37YP+-z0yQ1HULB9CsHFtXoph2sXnrccO24YgAGsagxztB013isZqkchLHPkJyo5BVi+R3yaq9r5yh4SV36O3HcZznoP6QOHeMDnRZXbmNtNC005tB8HRzrVX3NAvhRjwxJc2L8gzl-8Fde4D3rL9W3fjbX4JG-XgcN8H+L9IPDAji24ZyVZbFhFwUrS-2MqyhccpgO4W+t32O2IbQW0sOhBBR7hSKFdKPZb-suzRWqCeav3wQAYXXihLAAMW3jhd+KEPcbD-iI5psAt4YFG45LuyMAAAFYkHEBqAOpBnXmWdLQGhOkLR0lpIFInCL0foAASJm0FDAbj6INWGWpZbWXlgweyAYlahl-v-XMR9hR-XbnrZCyBwhfFBhgnuRZqEcEHogAgsVLbPByONMobEyKCX3tPQ+ON3Yn09nVb2DUipiPAdubi9EsAdWit-SGkUAHfyYWNZR8lsHPmmqIOa51lqrRQdqTaZ1drIDNPtZAh1jrM30g4i6F0jriAsTtC6ABOA6ZkHrEK1M9OuFCG7K10fJZuMjW6Jh1oDTu2Y+ouHkmFXucS3LmwEXDAqowxLFGQCotGGRnbVToc8PGZ96rFJKGU+Sh41EPUpgJamzN+isBKY0PREj44iQaiU5p7FWlSVsc8aBak+bIIQfaSxRAAAcZkplsD6ZFCu0siHVxIbXMhisYmhl6SUfp8TaGJK1AwgGHdmGRWyUWU5xRzl5KXEPbIyAr6uCKlAFhChSDCCOBwGChgBBpGMHfAwFSp5lWkT9WpHt8b1QAJKUD+O4LwZRgEAuEJOAa5kOlf2Av0dAuL9EkrAISGAiw-jlFDAIOwrRTFXjsDeSB2k4GQIfPzIMRcLRCnMkKSJZCyWAqFO9WwG9ihiRgDUkwjRGWUGMD0WIvcxWdL5PCN6HA-mqtMBFEirBmDFifgoNoVoVoKqVa0B6sxihEAVMgVVZKMKGG0IsDV9wgwKiwFKigbQJBQCIIsOw5cjIPV9bghcnRuhtH8gACS4NK2V9KwYQEVaQJlhhKyZLSJYG1NR1HARufasAlYiDgGgPAWgYBXAAEckiuHgMqv0AYBRgDIOimgKBYYow1UMRYahOR4DUEUNIRhBE2nLQAXSAA)