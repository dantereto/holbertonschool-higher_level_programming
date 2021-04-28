#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    suma = len(argv)
    if suma == 1:
        print('{} arguments.'.format(suma - 1))
    elif suma == 2:
        print('{} arguments:'.format(suma - 1))
    else:
        print('{} arguments:'.format(suma - 1))
    for args in range(0, suma):
        if args > 0:
            print("{}: {}".format(args, argv[args]))
