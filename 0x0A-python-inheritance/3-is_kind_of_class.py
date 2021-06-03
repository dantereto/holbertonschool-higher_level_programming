#!/usr/bin/python3
"""create the function"""


def is_kind_of_class(obj, a_class):
    """returns if the object is an instance or not"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
