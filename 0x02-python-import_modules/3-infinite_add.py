#!/usr/bin/python3
import sys
if __name__ == '__main__':
    suma = 0
    cont = len(sys.argv)
    for args in range(1, cont):
        suma += int(sys.argv[args])
    print("{:d}".format(suma))
