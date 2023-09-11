#!/usr/bin/python3
""" checks the instance of an object """


def is_same_class(obj, a_class):
    """ checks if an object is exactly an instance of a specified class.

    Args:
        obj: the object to check
        a_class: the class to check against

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
