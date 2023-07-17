#!/usr/bin/python3
"""Create class myInt"""


class MyInt(int):
    """Creates class Myint"""

    def __eq__(self, other):
        """magic function"""

        return super().__ne__(other)

    def __ne__(self, other):
        """magic function"""

        return super().__eq__(other)
