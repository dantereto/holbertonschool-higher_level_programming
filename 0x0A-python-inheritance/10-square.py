#!/usr/bin/python3
"""create the class"""


class BaseGeometry:
    """check the area"""

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
"""create a class"""


class Rectangle(BaseGeometry):
    """start"""

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def __str__(self):
        string = '[Rectangle] ' + str(self.__width) + '/'
        string += str(self.__height)
        return string

    def area(self):
        return (self.__width * self.__height)
"""create the class"""


class Square(Rectangle):
    """start"""

    def __init__(self, size):
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
