#!/usr/bin/python3
""" Integer validator """


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """
        public instance method that raise an exception indicating that
        the method area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value. It raises a 
        TypeError execption if value is not an integer, and raises
        a ValueError exception if value is less or equal to 0

        Parameters:
            name(str): name is always a string
            value(str): value is always an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
