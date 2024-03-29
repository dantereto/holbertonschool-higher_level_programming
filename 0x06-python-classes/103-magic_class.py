#!/usr/bin/python3
import math
import dis
"""square class"""
class MagicClass:
    """start"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(raduis) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
    @property
    def radius(self):
         return self.__radius
    def area(self):
        return self.__radius ** 2 * math.pi
    def circumference(self):
        return 2 * math.pi * self.__radius
