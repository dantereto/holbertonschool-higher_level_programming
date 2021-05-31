#!/usr/bin/python3
"""create function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""

    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
