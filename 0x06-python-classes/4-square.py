#!/usr/bin/python3
"""
This is a module for a class square
"""


class Square:
    """
    This class defines a square
    """

    def __init__(self, size=0):
        """
        Initializes a new square

        Args:
            size(int): size of the new square
        """

        self.size = size

    @property
    def size(self):
        """
        Get the current size of square
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return current area of the square
        """

        return (self.__size * self.__size)
