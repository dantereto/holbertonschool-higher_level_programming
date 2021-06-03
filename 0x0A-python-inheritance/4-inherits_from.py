#!/usr/bin/python3
"""create the function"""


def inherits_from(obj, a_class):
    """check the inherit class"""

    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
