#!/usr/bin/python3
"""Creates class Base"""


class Base:
    """
    creates class Base

    args:
        def __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""

        if (id is not None):
            self.id = id
        else:
            # use type as __nb_objects is a private attribute
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
