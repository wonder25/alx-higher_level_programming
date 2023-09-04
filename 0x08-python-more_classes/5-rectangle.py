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

    def area(self):
        """ Calculates area of rectangle """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Calcualtes perimeter of rectangle """
        if (self.__height == 0 or self.__width == 0):
            return (0)
        else:
            return ((self.__height + self.__width) * 2)

    def __str__(self):
        """Prints rectangle using # shape """
        my_list = ""
        if (self.__width == 0 or self.__height == 0):
            return ("")
        else:
            for j in range(self.__height):
                for i in range(self.__width):
                    my_list += "#"
                if (j < self.__height - 1):
                    my_list += "\n"
            return (my_list)

    def __repr__(self):
        """Prints string representation"""
        num1 = str(self.__width)
        num2 = str(self.__height)
        return "Rectangle(" + num1 + ", " + num2 +")"

    def __del__(self):
        """ Prints string before deleting instace """
        print("Bye rectangle...")
