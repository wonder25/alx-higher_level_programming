#!/usr/bin/python3
""" MyList inherits from list, gets all the properties and methods
of a list then uses the function print_sorted to print a sorted list
"""


class MyList(list):
    """ Passing the base class list to myList """
    def __init__(self):
        """ initializes the object """
        super().__init__()

    def print_sorted(self):
        """ it prints the sorted list """
        print(sorted(self))
