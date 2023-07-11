#!/usr/bin/python3
"""
returns dictionary description for json serialization of an object
"""


def class_to_json(obj):
    """
    returns dictionary description for json serialization of an object
    """

    return vars(obj)
