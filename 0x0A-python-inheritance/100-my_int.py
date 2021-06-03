#!/usr/bin/python3
"""create a class"""


class MyInt(int):
    """start"""

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
