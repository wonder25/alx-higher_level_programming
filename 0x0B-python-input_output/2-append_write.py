#!/usr/bin/python3

""" append to a file """


def append_write(filename="", text=""):

    """ Appends a string to a UTF* encoded file and returns 
    the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as textfile:
        return textfile.write(text)
