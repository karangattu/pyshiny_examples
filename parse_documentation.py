import pandas as pd
import re
import json
import sys


def extract_documentation(filename):
    """
    Extracts documentation from a text file, parses it, and saves it as a JSON file.

    Args:
        filename (str): The name of the input file (without the '_docs.txt' extension).
    """

    input_filename = f"{filename}_docs.txt"
    output_filename = f"documentation_{filename}.json"

    # Read the text from the file
    with open(input_filename, "r") as f:
        text = f.read()

    # Split text into chunks for each file
    files = re.split(r"(?=File:)", text)[1:]  # Split by "File:"

    # Initialize lists to store data
    file_names = []
    usages = []
    descriptions = []
    parameters = []
    examples_list = []

    # Iterate over each file
    for file in files:
        lines = file.strip().splitlines()

        # Extract file name
        file_name = lines[0].split(": ")[1].replace(".qmd", "")
        file_names.append(file_name)

        # Extract usage, parameters, examples, etc.
        usage_start = [
            i for i, line in enumerate(lines) if line.strip().startswith("```python")
        ]
        if usage_start:
            usage_start = usage_start[0]
            usage_end = [
                i
                for i, line in enumerate(lines)
                if line.strip().startswith("```") and i > usage_start
            ][0]
            params_start = [
                i for i, line in enumerate(lines) if line.startswith("## Parameters")
            ]
            if params_start:
                params_start = params_start[0]
                description_lines = lines[usage_end + 1 : params_start]
            else:
                description_lines = lines[usage_end + 1 :]
            description = "\n".join(description_lines).strip()
            usage = "\n".join(lines[usage_start + 1 : usage_end])
        else:
            usage = ""
            description = ""

        usages.append(usage)
        descriptions.append(description)

        # Extract parameters
        params_start = [
            i for i, line in enumerate(lines) if line.startswith("## Parameters")
        ]
        if params_start:
            params_start = params_start[0]
            params_end_list = [
                i
                for i, line in enumerate(lines)
                if line.startswith(
                    ("## Returns", "## Notes", "## See Also", "## Examples")
                )
            ]
            if params_end_list:
                params_end = params_end_list[0]
            else:
                params_end = len(lines)
            params = "\n".join(lines[params_start + 1 : params_end])
        else:
            params = ""
            params_end = len(lines)

        parameters.append(params)

        # Extract examples
        examples_start_list = [
            i for i, line in enumerate(lines) if line.startswith("## Examples")
        ]
        if examples_start_list:
            examples_start = examples_start_list[0]
            examples_lines = lines[examples_start + 1 :]

            # Remove unwanted lines
            unwanted_prefixes = ["#|", "## file:", "\n"]
            examples_lines = [
                line
                for line in examples_lines
                if not any(line.startswith(prefix) for prefix in unwanted_prefixes)
            ]

            # Remove ```{shinylive-python} and closing ```
            examples = "\n".join(
                [line for line in examples_lines if not line.startswith("```")]
            ).strip()
        else:
            examples = ""

        examples_list.append(examples)

    # Create DataFrame
    df = pd.DataFrame(
        {
            "File Name": file_names,
            "Usage": usages,
            "Description": descriptions,
            "Parameters": parameters,
            "Examples": examples_list,
        }
    )

    data_dict = df.to_dict(orient="records")

    def has_all_values(data):
        """
        Checks if all keys in a dictionary have corresponding values (not None).
        """
        # iterate over all keys in the dictionary and return only those that have values for all their keys
        return all(data[key] for key in data)

    filtered_data = [item for item in data_dict if has_all_values(item)]

    with open(output_filename, "w") as outfile:
        json.dump(filtered_data, outfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    extract_documentation(filename)
