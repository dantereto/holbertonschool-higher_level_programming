#!/usr/bin/python3
"""create the function"""


def matrix_mul(m_a, m_b):
    """start"""

    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    for i in m_a:
        if type(i) is not list:
            raise TypeError('m_a must be a list of lists')
    for j in m_b:
        if type(j) is not list:
            raise TypeError('m_b must be a list of lists')
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        for element in i:
            if type(element) not in [int, float]:
                raise TypeError('m_a should contain only integers or floats')
    for j in m_b:
        for element in j:
            if type(element) not in [int, float]:
                raise TypeError('m_b should contain only integers or floats')
    for i in m_a:
        if len(m_a[0]) != len(i):
            raise TypeError('each row of m_a must be of the same size')
    for j in m_b:
        if len(m_b[0]) != len(j):
            raise TypeError('each row of m_b must be of the same size')
    if len(i) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    val = 0
    result = [[] for matrix in range(len(m_a))]
    mul = 0
    x = []
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                mul += (m_a[i][k] * m_b[k][j])
            result[i].append(mul)
            mul = 0
    return (result)
