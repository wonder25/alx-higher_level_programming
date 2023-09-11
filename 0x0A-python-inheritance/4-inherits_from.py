#!/usr/bin/python3
""" Only sub class of """


def inherits_from(obj, a_class):
    """
    Function to check if an object is an instance of a class that
    inherited (directly or indirectly) from the specified class.

    Parameters:
        obj: any python object
        a_class: any python class

    Returns:
        True if obj is an instance of a class that inherited from a class.
        False otherwise, or if obj is an instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
