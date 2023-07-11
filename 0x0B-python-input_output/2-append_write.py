#!/usr/bin/python3
"""
append a string to a textfile
"""


def append_write(filename="", text=""):
    """
    append a string to a textfile
    """
    with open(filename, 'a', encoding="utf-8") as textfile:
        return textfile.write(text)
