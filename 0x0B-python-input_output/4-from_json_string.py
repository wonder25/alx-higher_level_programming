#!/usr/bin/python3
"""
converts json string to python data structures
"""

import json


def from_json_string(my_str):
    """
    returns a python object representation by a JSON string
    """
    return json.loads(my_str)
