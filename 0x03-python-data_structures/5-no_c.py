#!/usr/bin/python3
def no_c(my_string):
    cont = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            cont += i
    return (cont)
