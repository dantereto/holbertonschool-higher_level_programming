#!/usr/bin/python3
"""create the function"""


def text_indentation(text):
    """start"""

    if type(text) != str:
        raise TypeError('text must be a string')
    for ch in range(len(text)):
        if ch > 0 and text[ch] == ' ' and text[ch - 1] in '?.:':
            continue
        print(text[ch], end='')
        if text[ch] == '?' or text[ch] == '.' or text[ch] == ':':
            print('\n')
