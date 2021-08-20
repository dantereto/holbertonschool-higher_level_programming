#!/usr/bin/python3
"""create function"""


def find_peak(list_of_integers):
    if bool(list_of_integers) is False:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
