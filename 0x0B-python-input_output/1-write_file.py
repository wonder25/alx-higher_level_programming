#!/usr/bin/python3
""" wites a string to a text file """


def write_file(filename="", text=""):
    """ writes a string to a file and returns the number of 
    characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
