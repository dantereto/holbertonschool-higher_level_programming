#!/usr/bin/python3
def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    if type(matrix) != list:
        raise TypeError('matrix must be a matrix (list  \
        of lists) of integers/floats')
    new_l = []
    size = len(matrix[0])
    for i in matrix:
        if type(i) != list:
            raise TypeError('matrix must be a matrix    \
            (list of lists) of integers/floats')
        if len(i) != size:
            raise TypeError('Each row of the matrix must have the same size')
        new = []
        for element in i:
            if not isinstance(element, (int, float)):
                raise TypeError('matrix must be a matrix  \
                (list of lists) of integers/floats')
            else:
                new.append(round(element / div, 2))
        new_l.append(new)
    return (new_l)
