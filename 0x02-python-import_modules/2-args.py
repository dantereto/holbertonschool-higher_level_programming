#!/usr/bin/python3
import sys
if __name__ == '__main__':
    suma = len(sys.argv)
    if suma == 1:
        print('{:d} arguments.'.format(suma - 1))
    elif suma == 2:
        print('{:d} arguments:'.format(suma - 1))
    else:
        print('{:d} arguments:'.format(suma - 1))
    for args in range(0, suma):
        if args > 0:
            print("{:d}: {:s}"
                  .format(args, sys.argv[args]))
