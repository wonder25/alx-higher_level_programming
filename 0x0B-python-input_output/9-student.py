#!/usr/bin/python3

"""
create class student
"""


class Student:
    """
    Creates class student

    Args:
        def__init__ - constructor
        def to_json
    """
    def __init__(self, first_name, last_name, age):
        """
        constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns dict repr of instance
        """
        return vars(self)
