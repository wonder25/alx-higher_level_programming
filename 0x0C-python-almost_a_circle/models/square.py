#!/usr/bin/python3
""" a class that inherits from base """

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square Inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        method constructor class Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Print str method, return representation object
        """
        return "[Square] ({}) {}/{} - {}"\
                .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        size of a square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Evaluate the value of square
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """
        *args is the list of arguments - number of keyworded arguments
        **kwargs can be thought of as a double pointer to a dictionary
        key/value (keyworded arguments)
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[2]
        if len(args) == 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.width = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        dic = {}
        dic['x'] = self.x
        dic['y'] = self.y
        dic['id'] = self.id
        dic['size'] = self.width
        return dic
