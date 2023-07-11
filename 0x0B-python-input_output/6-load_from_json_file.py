#!/usr/bin/python3
"""
creates an object from JSON file
"""

import json


def load_from_json_file(filename):
    """
    creates an object from json file
    """
    with open(filename, 'r', encoding="utf-8") as textfile:
        return json.loads(textfile.read())
