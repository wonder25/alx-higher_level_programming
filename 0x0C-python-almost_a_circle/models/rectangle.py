#!/usr/bin/python3
"""Creates class Rectangle"""

from .base import Base


class Rectangle(Base):
    """
    class Rectangle

    Args:
        def __init__(self, width, height, x=0, y=0, id=None)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
