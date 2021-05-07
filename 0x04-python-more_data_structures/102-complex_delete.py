#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy = a_dictionary.copy()
    for v, num in copy.items():
        if num == value:
            del a_dictionary[v]
    return(a_dictionary)
