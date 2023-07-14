#!/usr/bin/python3
"""Creates class square, child class of Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Creates class square

    Args:
        def __init__(self, size) - constructor
    """

    def __init__(self, size):
        """Constructor"""
        
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Computes area"""

        return (self.__size * self.__size)

    def __str__(self):
        """Prints friendly format"""

        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)
