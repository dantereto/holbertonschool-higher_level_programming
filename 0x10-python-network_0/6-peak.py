#!/usr/bin/python3
"""creste function"""


def find_peak(list_of_integers):
    result = 0
    if not list_of_integers:
        return None
    i = 1
    list_of_integers.sort()
    result = list_of_integers[-1]
    return result
