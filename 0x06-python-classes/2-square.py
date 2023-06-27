#!/usr/bin/python3
"""
This is a module for a class square
"""


class Square:
    """
    This defines a class square

    Attributes:
        size (int): Human readable string describing the exception
    """

    def __init__(self, size=0):
        """
        The __init__ method is documented in the class level 
        docstring or as a docstring on the __init__ method 
        itself.

        Both methods are doable but should not be mixed. Choose 
        one to use to document the __init__ method.

        Args:
            size (int): Description of `param1`
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
        """
        Private instance attribution: size
        """
