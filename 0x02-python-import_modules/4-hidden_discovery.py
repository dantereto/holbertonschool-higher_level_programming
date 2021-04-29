#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    dirs = dir(hidden_4)
    sep = "__"
    for num in range(0, len(dirs)):
        if sep not in dirs[num]:
            print(dirs[num])
