#!/usr/bin/python3
"""create the function"""


def class_to_json(obj):
    """returns the dictionary"""

    class_obj = getattr(obj, '__dict__')
    return (class_obj)
