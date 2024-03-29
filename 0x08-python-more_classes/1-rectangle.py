#!/usr/bin/python3
""" Creates class: rectangle """


class Rectangle:
    """ Empty class rectangle """
    def __init__(self, width=0, height=0):
        """ Initialize a rectangle

        Args:
            __width(int): width of rectangle
            __height(int): height of rectangle
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ Gets the height """
        return (self.__height)

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ Gets the width """
        return (self.__width)

    @width.setter
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
