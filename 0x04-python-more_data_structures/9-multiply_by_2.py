#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = {}
    for keys, num in a_dictionary.items():
        copy[keys] = num * 2
    return (copy)
