#!/usr/bin/python3
"""Function that prints names"""


def say_my_name(first_name, last_name=""):
    """Print a name

    Args:
        first_name(str): the first name
        last_name (str): the last name
    Raises:
        TypeError: if either or first_name or last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))
