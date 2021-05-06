#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return(list(map(lambda sec: list(map(lambda num: num ** 2, sec)), matrix)))
