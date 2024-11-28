import re


def extract_code_and_description(response):
    """
    Extracts the Python code block and the description from the response string.
    """
    code_match = re.search(r"```python(.*?)```", response, re.DOTALL)
    code = code_match.group(1).strip() if code_match else ""
    description = re.sub(r"```python.*?```", "", response, flags=re.DOTALL).strip()
    return code, description


def create_app_files(code, description):
    """
    Creates app.py and DESCRIPTION.md files with the extracted code and description.
    """
    # Create or overwrite app.py
    with open("app.py", "w") as f:
        f.write(code)

    # Create or overwrite DESCRIPTION.md
    with open("DESCRIPTION.md", "w") as f:
        f.write(description)

## USAGE shown below
# # Extract code and description
# code, description = extract_code_and_description(response)

# # Create app.py and DESCRIPTION.md
# create_app_files(code, description)
