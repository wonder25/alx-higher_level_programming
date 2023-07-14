#!/usr/bin/python3
"""Checks if obj is an instance of a class or Inherited class"""


def is_kind_of_class(obj, a_class):
    """Checks if instance belongs to a class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
