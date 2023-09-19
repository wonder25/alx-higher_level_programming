#!/usr/bin/python3
""" base class """

import json


class Base:
    """ base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes class """
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects
