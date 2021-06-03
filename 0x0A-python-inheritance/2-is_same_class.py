#!/usr/bin/python3
"""create the function"""


def is_same_class(obj, a_class):
    """search the obj"""

    if type(obj) == a_class:
        return True
    else:
        return False
