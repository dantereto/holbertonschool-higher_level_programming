#!/usr/bin/python3
"""hi"""


def read_file(filename=""):
    """read file"""

    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end='')
