1. Creates a slider control that ranges from 0 to 20 with initial value 10
2. Creates two numeric inputs that will be updated based on the slider value
3. Uses a reactive effect to:
   - Update the first numeric input to match the slider value directly
   - Update the second numeric input with:
     - A dynamic label that includes the slider value
     - The slider value as its value
     - A dynamic range that's ±5 from the slider value
     - A step size of 1

4. Shows the current controller value in text format

The app uses the express syntax mode of Shiny for Python and demonstrates:
- Input controls (slider and numeric)
- Reactive effects
- Dynamic UI updates
- Layout with sidebar
- Cards for organization

To install and run:
```bash
pip install shiny
shiny run app.py
```

Package dependencies:
- shiny
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkTEQAJnAZETnBQoDEyAMJioVZFDb90ADZwPpjINjDkrBQMXtwA5sgm6FZecAD6ECbwDJzECg44UHHppOgUrAAUUhRBALxyYACqyanIAHJZtrnIACJwEQ0AlE4QAO6cFOyJnFgBULikZmmsnDYARlAMFYOICsj7yOOT01gr65vbuxAHNyfGS6wBq7YVDWSUTAFBDA1EDW7kaKkL62X7IGDcWoABiIMCgGlqACYYchpFAAiY4LUAIxQ4bXW77Ar3CgZTo5YivMDcDowNagwjIBoASQgphEmTpDKIeL2hLubKWnK6lIaNKy9IYiLBLMFHIltmQ0sZvIgfP2RymBWImysl3Vt21urS7HENi2DT6EQgURiUnIyFIdESLSoZOyuSGBpu3oOAAFLOasFQNBRffsbM6KKH9QT+QcxBQTAxrnR-oDPt9UejMXxWCgQCSsO8gSCtoMAL4NEYB8SSGRwdR0OhwSQKSPINKxm4aZC1Phy4sZ4HfbYG1zNFLeOicBhRZDCikD9nICikcFeYhTEuZxVojHyOMnJJT9KL3JU8Vcn6M-eY2oafE+o8T13BVit8hWBfk7qa8GkFYnAznA35zPSAQ+NYohQBAxTIBsH7fg6O4jqCR4FCeqTuiKrxHj61IQLSkrKgQ4bIOBcABLUaZgMRiqUZBIAaFWhDkXeWIaGR+EHBCEAPsgAC0yAAKzcfGcIIr2ADUonifyURwOgOIGoMYAVkQ4DQPAtBgGIACODhiPAlCsMGoaMmAJbUBQukKHCFCBKQNScGsCicngCjoLBKSsCM8Y3OpAC6QA)
