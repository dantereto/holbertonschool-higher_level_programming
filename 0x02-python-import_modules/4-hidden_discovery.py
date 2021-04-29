#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    dirs = dir(hiddden_4)
    space = '__'
    for num in range(0, len(dirs)):
        if space not in dirs:
            print(dirs[num])
