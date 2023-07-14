#!/usr/bin/python3
"""Create class mylist"""


class MyList(list):
    """Create class mylist"""

    def print_sorted(self):
        """Prints list sorted in ascending order"""

        print(sorted(self))
