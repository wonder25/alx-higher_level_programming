#!/usr/bin/python3
"""
This is a module for a class square
"""


class Square:
    """This class represents a square"""

    def __init__(self, size=0):
        """
        Initialize a new square

        Args:
            size (int): The size of the new square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
