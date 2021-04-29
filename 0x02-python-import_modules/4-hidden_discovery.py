#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    dirs = dir(hidden_4)
    for num in range(0, len(dirs)):
        if '__' not in dirs[num]:
            print(dirs[num])
