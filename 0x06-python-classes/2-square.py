#!/usr/bin/python3
"""class square"""


class Square:
    """int: Module level variable documented inline.

The docstring may span multiple lines. The type may optionally be specified
on the first line, separated by a colon.
    """
    def __init__(self, size=0):
          if type(size) is not int:
               raise TypeError('size must be an integer')
          """ckeck error cases"""
          if size < 0:
               raise ValueError('size must be >= 0')
          self.__size = size
