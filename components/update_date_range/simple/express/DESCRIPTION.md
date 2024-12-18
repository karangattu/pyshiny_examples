This app demonstrates several ways to update a date range input:

1. A slider controls the window size (number of days) in the date range
2. A "Center on Today" button that centers the date range around today's date
3. Shift buttons that move the entire date range window backwards or forwards
4. A text display showing the currently selected range and its duration

Technical description:
- Uses Shiny Express syntax for simplified app structure
- Demonstrates use of `update_date_range()` in multiple contexts
- Shows how to handle date arithmetic with Python's datetime module
- Uses reactive effects with event binding to handle button clicks
- Includes some basic Bootstrap styling for buttons

Installation and execution instructions:
1. Install required packages:
```bash
pip install shiny
```

2. Save the code to a file (e.g., `app.py`)
3. Run the app:
```bash
shiny run app.py
```

Package dependencies:
- shiny

The app will run and display a user interface with date range controls and buttons to manipulate the date range in various ways.
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAEyiooEt5kf1SDCmw5wi3eKzgAbClAA6ERs2QBnABZcIuPjAFDkDOFGLcAbnEXKWGrbixwAHuiOrVu-cK3oArhSJGEFIMRD5ciooAxMgAynDC6FAA5nDI3BTSlhBhOMlwAPqk6BSqABTpmQC88mAAIqLIAEpQECnIAKro7FTItXAwpDUAlBEQ0QDCRg1QatJcwWmkyGSUTNJp6qndqQwtbQDuWqyk+2pcAF5ZOd5++apzwaU1h0EndxeWhMg19T0vx6dVB9kKV2LhVCMvjAtJUAIxEGBQRyVADMAAYiGYoNIfHBKgB2EYQKLISbGHozbaGPapG4URTXCC+Cj5bb5XatOBPCDIXnfMBsjkpGoERR8-lxTKmEQ9IWfUU8vmqORCSrbLAUUhg0pDZAAWjSPDgUlkUFBUHBBKGCvF1FYatEGq1Fp1iiJJLJ02QACM-JqeZrltQqAwNlsGnLkORFmCGVwsHT8iZuOR8r6KP6nmBiMG4Ax8prY18auNc6HowAVZ24EXLaRQNz5apgb0UCB6lw8KAMGtgd1jUlTCk+v3RwO2OjCSPekwAa323dYqjjCaZt2TXFT6czNQnLJnxFntZq8h8ACZvWiAKynuhwNF0WKaSfIABCc9rxHrjebMD1Z+GUYJiHVIZm3Mclj3alOWQOhBAXBhWBXRMNy3UcICzPd8jghgEKQ4swBiZ9hAAMXgxdvnPfEoFhW97zoT9v1UJsaj-AC+1GAABKZTC4CwHDoO9TEUbjjF4-i4AsShSjpLAc0oPMC2rIkpEffIdUQMU+X+E5kEqPg1woLAdP2d5Lh1ZAAHpLOQADFV5HIfC6URWRcuVuXFcUakFGkRS0zy1BVCgHSoJ1tV1A0JGNGQ5HNS0TOtfzPLtEK4DCl1dQAakNSQYrNMFVEqBKkv7USNwkwS4GEiAyvEtLJODGTDKwLCD1nFS4DUjSkuIHwGECFllW7YR9NknzOR1YA0QAXR6vqBvyO09IM5ksHGlJJthWb7OQEzltKXr+uDRagn1ZZ5uOoahCGNaLWXHaksc5yqFcl73KSryBTc3zCA+pUgsqQ6Fqu4RIqNE1YoKoqjhORKdttIJAYuygTtYM6ooh-K7uh159iJcVSp48x6sq6rauJhwpIoJrVqwnC8I6rqhk0nagcuoLlrG76JqGKbtvFNmUaW0bmvWrlea2pK9v0g7kZZJaDUFwagpugqkse+MnLZMWPIC-kxb8+H-uGpGjpRkHkGyjG8riwqEptPWUqV1HLZy6LTVtnGAXxvl+2iWouFUdB6x0JW1BkKqU2JGrAmCDUnHpIJOvDqUqFYdkaW6naQaIYWVr8W63szn3eSMCg+p5BjCIj0xjWglIUBAEGAF9FmQEA7Vb0oQFKO09RB1W7td2FW4KyEwGbohwGgeBaDAIwAEcwiMeBKFUDVHAoL5s3IKgaBQMBFERChg9IDIuG9RRsj0GsmRadh7r+gKJ+moA)
