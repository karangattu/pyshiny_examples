from anthropic import Anthropic

text = "{.doc-section .doc-section-returns} {.parameter-name} [:]{.parameter-annotation-sep}"

client = Anthropic()
token_count = client.count_tokens(text)
print(token_count)
