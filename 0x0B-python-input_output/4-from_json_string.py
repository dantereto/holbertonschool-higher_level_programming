#!/usr/bin/python3
"""create function"""


import json


def from_json_string(my_str):
    """returns an object"""

    return json.loads(my_str)
