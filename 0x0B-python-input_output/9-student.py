#!/usr/bin/python3
"""
creates class student
"""


class Student:
    """
    creates class student

    args:
        def __init__ - constructor
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
        returns dictionary representation of instance
        """
        return vars(self)
