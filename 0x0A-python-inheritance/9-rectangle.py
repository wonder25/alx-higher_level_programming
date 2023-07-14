#!/usr/bin/python3
"""Creates class Rectangle, child class of BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Create class Rectangle

    Args:
        def __init__(self, width, height) - Constructor
    """

    def __init__(self, width, height):
        """Constructor"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes area"""

        return (self.__width * self.__height)

    def __str__(self):
        """Prints friendly format"""

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
