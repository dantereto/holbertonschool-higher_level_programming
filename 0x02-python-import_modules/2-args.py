#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    suma = len(sys.argv)
    if suma == 1:
        print("0 arguments.")
    elif suma == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(suma - 1))
    for args in range(0, suma):
        if args > 0:
            print("{}: {}".format(args, sys.argv[args]))
