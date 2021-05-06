#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for num in matrix:
        new.append(list(map(lambda n: n ** 2, num)))
    return (new)
