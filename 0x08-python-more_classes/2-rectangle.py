#!/usr/bin/python3
""" Create class: Rectangle """


class Rectangle:
    """ Empty class Rectangle """
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
    
    def area(self):
        """ Calculates area of rectangle """
        return (self.height * self.width)

    def perimeter(self):
        """ Calculates perimeter of rectangle """
        if (self.height == 0 or self.width == 0):
            return (0)
        else:
            return ((self.height + self.width) * 2)

