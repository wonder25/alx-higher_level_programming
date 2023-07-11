#!/usr/bin/python3
"""
writes a json string to a text file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    writes a json string to a text file
    """
    with open(filename, 'w', encoding="utf-8") as textfile:
        textfile.write(json.dumps(my_obj))
