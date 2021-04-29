#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    dirs = dir(hidden_4)
    for num in range(0, len(dirs)):
        if dirs[num] != '__':
            print(dirs[num])
