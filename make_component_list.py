# read documentation_express.json and iterate over each dict and if it has a key "express.ui.*", then add it to the list

import json
import sys


def make_component_list(filename):
    with open(filename, "r") as infile:
        data = json.load(infile)

    component_list = []

    for item in data:
        # if filename contains express
        if filename.endswith("_express.json"):
            if "express.ui." in item["File Name"]:
                # just add the term after "express.ui."
                component_list.append(item["File Name"].split("express.ui.")[1])
        elif filename.endswith("_core.json"):
            if "ui." in item["File Name"]:
                # just add the term after "express.ui."
                component_list.append(item["File Name"].split("ui.")[1])

    return component_list


listy = make_component_list("documentation_express.json")
print(listy)
listy = make_component_list("documentation_core.json")
print(listy)
