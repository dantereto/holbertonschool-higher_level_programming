#!/usr/bin/python3
"""create function"""


def write_file(filename="", text=""):
    """ writes a string to a text file """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
