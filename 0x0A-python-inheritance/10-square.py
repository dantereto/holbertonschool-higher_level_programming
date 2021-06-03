#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle


"""create the class"""


class Square(Rectangle):
    """start"""

    def __init__(self, size):
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
