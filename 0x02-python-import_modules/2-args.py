#!/usr/bin/python3
import sys
if __name__ == '__main__':
    suma = len(sys.argv)
    if suma == 0:
        print('0 argguments:')
    print('{:d} argguments:'.format(suma - 1))
    for args in range(1, suma):
        print("{:d}: {}".format(args, sys.argv[args]))
