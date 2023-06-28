#!/usr/bin/python3
"""
This is a module for class square
"""


class Square:
    """
    This defines class square

    Attributes:
        size(int): size of square
    """

    def __init__(self, size=0):
        """
        This initializes a new square

        Args:
            size(int): size of the new square

        Raises:
            TypeError: if `size`is not an integer
            ValueError: if `size` is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """
        Get the current size of square

        Returns:
            int: size of square
        """

        return (self.__size)
    @size.setter
    def size(self, value):
        """
        sets the size of the square

        Args:
            value(int): size of the square

        Raises:
            TypeError: if `value` is not an integer
            ValueError: if `value` is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculates the square of size and returns value

        Args:
            size: self.__size

        Returns:
            the current area of square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Print the square with the #character

        Args:
            int: self.__size ** 2
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
