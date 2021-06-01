#!/usr/bin/python3
"""create the function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, containing a specific string"""

    copy = ''
    with open(filename, 'r', encoding="utf-8") as f:
        for i in f:
            copy += i
            if search_string in i:
                copy += new_string
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(copy)
