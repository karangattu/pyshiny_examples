\n{df.to_string()}\n```")
    else:
        # Echo user message with some additions
        response = f"You said: {user_msg}\nThis is a demonstration of the chat component."
        await chat.append_message(response)

# Update chat parameters based on UI inputs
@reactive.effect
def update_chat_params():
    # Update error handling mode
    error_mode = input.error_handling()
    chat._on_error = error_mode  # Note: This is a demonstration; normally you'd want to recreate the chat

# Display current chat state information
@render.text
def chat_info():
    messages = chat.messages()
    return f"Number of messages: {len(messages)}"

```

This app demonstrates:

1. All major Chat parameters:
   - id
   - messages (initial welcome message)
   - on_error handling
   - tokenizer (default)

2. UI features:
   - Auto-resize toggle
   - Message transformation toggle
   - Error handling mode selector
   - Sidebar layout
   - Responsive design

3. Chat functionality:
   - Message transformation for both user and assistant messages
   - Error handling demonstration
   - Different response types (text, formatted code, data)
   - Message state tracking

4. Interactive features:
   - Real-time parameter updates
   - Message count display
   - Various response types based on user input

To test different features:
1. Type normal messages to see basic chat functionality
2. Include "error" in your message to test error handling
3. Include "data" to see formatted data responses
4. Toggle the transformation switch to see message formatting
5. Try different error handling modes
6. Test auto-resize functionality

The app uses Express mode for simplified layout and reactive programming while demonstrating all available Chat parameters and features.

Installation requirements:
```
pip install shiny pandas
```

Run the app with:
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAEyiooEt5kf1SDCmw5xu8ADoR+g4eigR2AZ2RQV6VlMbNkSgBZcIuPjAFDkDOFGLcAbnC1MW+w7ixwAHuktKVM84boAK4UREFcRJaKcAxSUgDEyADKsOgANnAiFFDIdILIxHocyPC+UADmcEpShlzcUGkA+qVKFVXIALzIwFLIfcjhWDBQDADWrKQA7hAAFL39CxJgSysQCwuJAOpwaWS8FKTIAMJFwgAicDCHAIKYAITz68gAKgYqrJeH+lMqtiNcpCCKjoVgoQR8yFIdGQFD0mSSBiMx1OBWYAgg1AoWEe6wAtMhriFSLifFwAF4ONZPZD456kUbUZBpHh1apUp74gCyVValRhDAUSjyDGG3HIOIW+LOXDoIKiwh86KUmWForZ1OQK2Wy3ZyAAlFIALpxCCJI6WUSqAoowxKbIQYiZSZ1PSqNJpVR-LhpKAAIwyyHkAvgVAYbMKxS6gxOHDmuq4rA6Sw+V0aEYoSwIOJabSUHVq9SaOcqSizuvIjRiTAYSbQRMzfTNCmQvsyAHIoES20QOzYgg1u8g261pNwKYP8m2ghAiooMqw21IDRApIN5JVGqR0BQlHGFtwKBlawjXMjihcrpmcXRvT7-XAOs8GEE4GWFjf3X6Ms1SL7vQ+nxfJcTWdWEBi4LAlATOBfRGGY9UQHFBkCEJGiUUDCjmOsDkaUkKQbJYAFFoHvAkiRJKpyQcQgXmfOBlwWZCIGCCg0IwvQsIoAUICFQQYGaHlcwIsAn0FVVkG5MoSwbQD6KQiCUNY5UMhsPdqSWKtBEaWdWGZCByivXVFjAQiGGrZAAAkFF0wwDMICV+hAByniWTsDiWFAlkJdz7KM9S0D7BoPM1MBrkCtJDI1YyRzqKjgqWFJRzi3yov6JZpx0+d4rAABVGdrKynUNQAXzfallLgGw4ETVz6yK-plwSZBpSUdIoGMWFMnTZAcoASSkdMsHCNS+jax09FINIPhrJZnlwdBMlwQEGBKQS+ThSwsC2yL+mdVhYVrABGAAGY6AFIdr6OEuHKPQKFrNzSEu3Jb0fOjgJXU1aLEviBmVFbFL4aFqC-aqpAAAUGrifpFRogRiRpFKkD5oWhnjVUR5iQhmKgPAoBCcRlZAIFIYRFKwNHeNh4sqngxC-L6SwwQYNZcYzXUcUSa5WFYGEeCqbJTBhQ54ZWmn1X6JnwTWOgllAdhOH5rAScmeDIK4uhxDgGY2zOizEDOzkDaSNs9WKw1kBANnitWJrRPR361Cgu0FAVKolXaImQfvTQIEh04Ke4qn+KdrgXcoXD3fIZVkbgVGg4xxVo+1tmCfjaESbJrGsUpjHxbp5yLDEaWYU8dnFl1LmedyPiOG4fThdUXww-tN3WuTiXGeLlnchWIJWAADgAZgcfvWEOgA2ZAACprmb8OKGnlArbLm2dSaqy50yUXdCCX0YDDqDo4hwaK1FtC94P9m1FwB02Dj5BMrgC-97qAvdXPmAlHKTprQ4Ib-qYxYvBHEnNkg8CCD6KgbAZRykxEXduPFMgUHmu0WCypebkD+jEPg2dCbQg0mZQQSxcHYIYM0b+WA0hTBiO-DUiQLzR2htAzSK1Mq2ULgKMOmRCIeEdNuAEsxZpvD4CoHIVA7TIFYatKS1EGJpXTiFBWUASGGDIRQ8oVCaEMDodSRIAAlburM-SQJGFkFRDM2DQi6BoLAZwOBQAAGLBm1k5SxCw2zXDbCgbilQZiHSIAAFj1GVVKbYABC3juhtg8IONsuA4lkjbMaSxxV5FPCgJMKAdQ-5YgwAtRQAlZEzFlmACyMQ4DDmQEtcE5jEJSBAKwOgFNSBoS4rZeCa90lSLSMqem9DkCEUKIcTqMjeSZFgsQUYyBQKuiUMwTIUAeaxXIA0VElAy6cKjkg3+pSACagJdDZNYMvT+38bZSFeGHURVooKmADJVCaCCPbYnqhkrJOTBr5OoKwIp4yZhJyQY1L6OUNCWmkewhuVwPgzLhGsCM+kwZ+wtDYLg9h3CykquzFGAwwVUErEQ8hkLyi6L6KfCABLzJdHJqw7SBUOl6jAKVS2kBYAIBQGASwABHcIlh4CUCUBTPGNEwBkA2TQDlUhRTpFJsyX0UgIBBFMLgKQ8hFBqBNKlPoTLDRAA)
