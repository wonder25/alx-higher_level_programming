#!/usr/bin/python3
"""
Writes a string to a textfile
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file
    """
    with open(filename, 'w', encoding="utf-8") as textfile:
        return textfile.write(text)
