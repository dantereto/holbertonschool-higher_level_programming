#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_c = my_list[:]
    if list_c is None:
        return
    if idx < 0 or idx > len(my_list) - 1:
         return(my_list)
    list_c[idx] = element
    return(list_c)
