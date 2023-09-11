#!/usr/bin/python3
""" checks the subclass """


def is_kind_of_class(obj, a_class):
    """ Checks if an object is exactly a subclass of a specified class.

    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        True if obj is exactly an instance of a_class, False if otherwise
    """
    return isinstance(obj, a_class)
