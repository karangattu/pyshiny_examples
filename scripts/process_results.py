import json
import os
import sys
from pathlib import Path


def process_inspect_results(results_dir):
    """Process Inspect AI results and generate summary"""
    results_path = Path(results_dir)

    # Find the latest results file
    result_files = list(results_path.glob("*.json"))
    if not result_files:
        print("No result files found")
        return

    latest_file = max(result_files, key=os.path.getctime)

    with open(latest_file, "r") as f:
        data = json.load(f)

    # Extract key metrics
    eval_data = data.get("eval", {})
    samples = eval_data.get("samples", [])

    total_tests = len(samples)
    passed_tests = sum(
        1 for s in samples if s.get("scores", [{}])[0].get("value") == "C"
    )
    partial_tests = sum(
        1 for s in samples if s.get("scores", [{}])[0].get("value") == "P"
    )
    failed_tests = sum(
        1 for s in samples if s.get("scores", [{}])[0].get("value") == "I"
    )

    pass_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

    # Generate summary
    summary = {
        "total": total_tests,
        "passed": passed_tests,
        "partial": partial_tests,
        "failed": failed_tests,
        "pass_rate": pass_rate,
        "quality_gate_passed": pass_rate >= 80,  # 80% threshold
        "details": f"Complete: {passed_tests}, Partial: {partial_tests}, Incomplete: {failed_tests}",
    }

    # Save processed results
    with open(results_path / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print(
        f"Processed {total_tests} tests: {passed_tests} passed, {partial_tests} partial, {failed_tests} failed"
    )
    print(f"Pass rate: {pass_rate:.1f}%")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_results.py <results_dir>")
        sys.exit(1)

    process_inspect_results(sys.argv[1])
