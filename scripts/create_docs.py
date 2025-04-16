import re
import ast
import textwrap
import json
from pathlib import Path
from typing import Dict, List, Optional, Union
import argparse

# --- Helper Function ---


def _extract_signature(
    node: Union[ast.FunctionDef, ast.AsyncFunctionDef], lines: List[str]
) -> Optional[str]:
    """Extracts the full signature of a function node from source lines."""
    try:
        # AST lineno is 1-based, list index is 0-based
        start_lineno = node.lineno - 1
        signature_end_lineno = -1
        def_keyword = "async def" if isinstance(node, ast.AsyncFunctionDef) else "def"

        # Find the actual 'def' line start, skipping decorators
        current_line_idx = start_lineno
        while current_line_idx < len(lines):
            if lines[current_line_idx].strip().startswith(def_keyword):
                start_lineno = current_line_idx
                break
            current_line_idx += 1
        else:
            # 'def' keyword not found after initial node line (shouldn't happen often)
            return None  # Indicate failure

        # Find the line index where the signature ends (ends with ':')
        current_line_idx = start_lineno
        while current_line_idx < len(lines):
            line_content = lines[current_line_idx].split("#")[0].rstrip()
            if line_content.endswith(":"):
                signature_end_lineno = current_line_idx
                break
            current_line_idx += 1

        # Ensure the signature end was found reasonably before the body starts
        body_start_lineno = node.body[0].lineno - 1 if node.body else len(lines)
        if signature_end_lineno == -1 or signature_end_lineno >= body_start_lineno:
            # Fallback if detection fails: try just the 'def' line if it ends with ':'
            if lines[start_lineno].split("#")[0].rstrip().endswith(":"):
                signature_end_lineno = start_lineno
            else:
                # Could not reliably determine signature end
                return f"{def_keyword} {node.name}(...):"  # Placeholder

        # Extract the raw signature lines
        signature_lines = lines[start_lineno : signature_end_lineno + 1]

        # Dedent and clean up the signature string
        if signature_lines:
            signature_code = "\n".join(signature_lines)
            try:
                signature = textwrap.dedent(signature_code).strip()
            except Exception:
                signature = signature_code.strip()  # Fallback stripping
            return signature
        else:
            # Fallback if lines couldn't be extracted
            return f"{def_keyword} {node.name}(...):"  # Placeholder

    except (IndexError, ValueError) as e:
        print(f"Warning: Error extracting signature for {node.name}: {e}")
        return None  # Indicate failure


# --- Main Extraction Function ---


def extract_function_signatures(xml_content: str) -> Dict[str, str]:
    """
    Extracts function signatures from Python code embedded in a Repomix XML file.

    Args:
        xml_content: A string containing the content of the Repomix XML file.

    Returns:
        A dictionary where keys are function names and values are their
        corresponding signature strings. Only functions with docstrings are included.
    """
    output_dict: Dict[str, str] = {}
    file_pattern = re.compile(r'<file path=".*?">(.*?)</file>', re.DOTALL)

    for match in file_pattern.finditer(xml_content):
        file_content = match.group(1)
        try:
            parsed_tree = ast.parse(file_content)
            lines = file_content.splitlines()

            for node in parsed_tree.body:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    # We still check for a docstring to maintain the original filter
                    docstring = ast.get_docstring(
                        node, clean=False
                    )  # Don't need clean version

                    if docstring:  # Only include functions that have a docstring
                        func_name = node.name
                        signature = _extract_signature(node, lines)
                        if signature:
                            output_dict[func_name] = signature

        except (SyntaxError, IndexError, ValueError) as e:
            # Ignore files that cannot be parsed or AST processing errors
            # print(f"Skipping a file section due to parsing/processing error: {e}")
            pass

    return output_dict


# --- Main Execution Block ---


def main():
    """
    Reads the Repomix XML file, extracts function signatures,
    and saves the result to a JSON file.
    """
    parser = argparse.ArgumentParser(description="Extract function signatures from Repomix XML.")
    parser.add_argument(
        "xml_file",
        type=str,
        help="Path to the Repomix XML file."
    )
    parser.add_argument(
        "output_json",
        type=str,
        help="Path to the output JSON file."
    )
    args = parser.parse_args()

    xml_file_path = Path(args.xml_file)
    output_file_path = Path(args.output_json)

    repomix_output_xml: Optional[str] = None
    try:
        # Read the input XML file
        with open(xml_file_path, "r", encoding="utf-8") as f_in:
            repomix_output_xml = f_in.read()
        print(f"XML content loaded successfully from '{xml_file_path}'.")

    except FileNotFoundError:
        print(f"Error: Input file '{xml_file_path}' was not found.")
        return  # Exit if file not found
    except Exception as e:
        print(f"An error occurred while reading the input file: {e}")
        return  # Exit on other read errors

    # Proceed only if XML content was loaded
    if repomix_output_xml:
        print("Extracting function signatures...")
        function_data = extract_function_signatures(repomix_output_xml)
        print("Extraction complete.")

        # --- Save the result to the JSON file ---
        try:
            with open(output_file_path, "w", encoding="utf-8") as f_out:
                json.dump(function_data, f_out, indent=2)
            print(f"Successfully saved extracted data to '{output_file_path}'.")
        except Exception as e:
            print(f"Error writing output to '{output_file_path}': {e}")
        # ----------------------------------------


if __name__ == "__main__":
    main()
