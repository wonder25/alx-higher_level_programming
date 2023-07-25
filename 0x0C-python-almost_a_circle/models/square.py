#!/usr/bin/python3
"""Creates class Square"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
        Args:
            def __init__(self, size, x = 0, y = 0, id=None)
            def __str__(self)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """Gets size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
