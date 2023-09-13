#!/usr/bin/python3

""" append to a file """


def append_write(filename="", text=""):

    """ Appends a string to a text file """

    with open(filename, 'a', encoding="utf-8") as textfile:
        return textfile.write(text)
