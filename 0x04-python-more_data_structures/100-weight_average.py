#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    val = 0
    val2 = 0
    for i in my_list:
        val = val + (i[1])
        val2 = val2 + (i[0] * i[1])
    return(val2 / val)
