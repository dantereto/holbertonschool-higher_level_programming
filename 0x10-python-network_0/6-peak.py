#!/usr/bin/python3
"""creste function"""


def find_peak(list_of_integers):
    result = 0
    if not list_of_integers:
        return None
    i = 0
    result = list_of_integers[1]
    n = len(list_of_integers)
    for i in range(1, n):
        if list_of_integers[i] >= result:
            result = list_of_integers[i]
    return result
