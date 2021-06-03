#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
