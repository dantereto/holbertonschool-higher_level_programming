#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cont = []
    for i in my_list:
        if i % 2 == 0:
            cont.append(True)
        else:
            cont.append(False)
    return(cont)
