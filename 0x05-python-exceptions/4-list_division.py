#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    copy = []
    for i in range(list_length):
        try:
            copy.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            copy.append(0)
        except TypeError:
            print("wrong type")
            copy.append(0)
        except IndexError:
            print("out of range")
            copy.append(0)
        finally:
            pass
    return(copy)
