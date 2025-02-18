import os
import subprocess
import re


def read_success_rate_file() -> float:
    try:
        with open("passing_percentage.txt", "r") as f:
            passing_percentage = float(f.read().strip())
            return passing_percentage
    except FileNotFoundError:
        print("Error: passing_percentage.txt not found.")
        return None


def run_tests():
    # Run pytest against the 'AIprentice' folder and capture the output
    result = subprocess.run(
        ["pytest", "AIprentice/", "--tb=short"], capture_output=True, text=True
    )
    return result.stdout


def parse_results(output):
    # Use regex to find the number of passed and failed tests
    passed_pattern = r"(\d+) passed"
    failed_pattern = r"(\d+) failed"

    passed = re.search(passed_pattern, output)
    failed = re.search(failed_pattern, output)

    passed_count = int(passed.group(1)) if passed else 0
    failed_count = int(failed.group(1)) if failed else 0

    return passed_count, failed_count


def calculate_passing_test_percentage(passed, failed):
    total = passed + failed
    if total == 0:
        return 0  # Avoid division by zero
    return (passed / total) * 100


passing_percentage = read_success_rate_file()

if passing_percentage >= 80:
    print("Creating tests for AIprentice apps.")
    # Create tests for AIprentice apps
    subprocess.run(["python", "create_apps_using_llm.py", "testing", "sonnet"])
    # run pytest
    output = run_tests()
    passed, failed = parse_results(output)
    passing_percentage = calculate_passing_test_percentage(passed, failed)
    if passing_percentage >= 80:
        print("PROMPT files are of high quality.")
    else:
        print("PROMPT files are of low quality.")

else:
    print("Insufficient success rate to create tests.")
