#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    dirs = dir(hidden_4)
    for i in range(0, len(dirs)):
        if '__' not in dirs[i]:
            print(dirs[i])
