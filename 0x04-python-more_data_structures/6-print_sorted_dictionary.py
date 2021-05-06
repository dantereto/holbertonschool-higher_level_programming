#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    data = sorted(a_dictionary.keys())
    for i in data:
        print('{}: {}'.format(i, a_dictionary[i]))
