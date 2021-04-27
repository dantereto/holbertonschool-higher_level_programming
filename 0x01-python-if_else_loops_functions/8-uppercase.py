#!/usr/bin/python3
def uppercase(str):
    cont = ""
    for i in str:
        cont = ord(i)
        if cont >= 97 and cont <= 122:
            cont -= 32
        print(chr(cont), end='')
    print()
