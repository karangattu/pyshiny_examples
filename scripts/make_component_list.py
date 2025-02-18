import json
import os
from pathlib import Path

def make_component_list(filename):
    docs_dir = Path("docs")
    filepath = docs_dir / filename
    
    with open(filepath, "r") as infile:
        data = json.load(infile)

    component_list = []

    for item in data:
        if filename.endswith("_express.json"):
            if "express.ui." in item["File Name"]:
                component_list.append(item["File Name"].split("express.ui.")[1])
        elif filename.endswith("_core.json"):
            if "ui." in item["File Name"]:
                component_list.append(item["File Name"].split("ui.")[1])

    return component_list


if __name__ == "__main__":
    listy = make_component_list("documentation_express.json")
    print("Express components:", listy)
    listy = make_component_list("documentation_core.json")
    print("Core components:", listy)
