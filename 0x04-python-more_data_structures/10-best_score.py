#!/usr/bin/python3
def best_score(a_dictionary):
    maxi = None
    if a_dictionary:
        maxi = max(a_dictionary, key = a_dictionary.get)
        return (maxi)
    else:
        return
