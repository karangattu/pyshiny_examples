import json
import re
import sys
from pathlib import Path
import pandas as pd


def extract_sections(text):
    sections = re.split(r"={16}", text)
    return [section.strip() for section in sections if section.strip()]


def extract_details(section):
    controller_name = re.search(r"# (.+?) {", section).group(1)
    attributes = (
        re.search(r"## Attributes\n\n(.+?)\n\n## Methods", section, re.DOTALL)
        .group(1)
        .strip()
    )
    methods = re.search(r"## Methods\n\n(.+)", section, re.DOTALL).group(1).strip()
    return controller_name, attributes, methods


def extract_documentation(filename):
    """
    Extracts documentation from a text file, parses it, and saves it as a JSON file.

    Args:
        filename (str): The name of the input file (without '_docs.txt' extension).
    """
    docs_dir = Path("docs")
    input_filename = docs_dir / f"{filename}_docs.txt"
    output_filename = docs_dir / f"documentation_{filename}.json"

    # Read the text from the file
    with open(input_filename, "r") as f:
        text = f.read()

    if filename == "testing":
        sections = extract_sections(text)

        # Extract details and create DataFrame
        data = []
        for section in sections:
            if "## Attributes" in section and "## Methods" in section:
                controller_name, attributes, methods = extract_details(section)
                data.append([controller_name, attributes, methods])

        df = pd.DataFrame(data, columns=["controller_name", "attributes", "methods"])

        data_dict = df.to_dict(orient="records")
        with open(output_filename, "w") as outfile:
            json.dump(data_dict, outfile, indent=4)
    else:
        # Split the text into sections based on horizontal rules
        sections = text.split("\n---\n")

        # Parse each section
        documentation = []
        for section in sections:
            if not section.strip():
                continue

            # Extract file name and content
            lines = section.strip().split("\n")
            file_name = lines[0].strip()
            content = "\n".join(lines[1:]).strip()

            # Create a dictionary for this section
            section_dict = {"File Name": file_name, "Content": content}

            documentation.append(section_dict)

        # Write the JSON file
        with open(output_filename, "w") as outfile:
            json.dump(documentation, outfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_documentation.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    extract_documentation(filename)
