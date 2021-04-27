#!/usr/bin/python3
def remove_char_at(str, n):
    cont = ''
    i = 0
    for i in range(0, len(str)):
        if i != n:
            cont += str[i]
        else:
            continue
    return cont
