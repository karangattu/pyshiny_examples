import os


def process_input(input_str):
    # Process the input here
    output_str = input_str.upper()
    return output_str


if __name__ == "__main__":
    input_str = os.environ["INPUT"]
    output_str = process_input(input_str)
    print(output_str)

    # Write the output to a file
    with open("output.txt", "w") as f:
        f.write(output_str)
