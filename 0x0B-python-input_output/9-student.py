#!/usr/bin/python3
"""create the class"""


class Student:
    """Instantiation"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """retrieves a dictionary representation of a Student"""
    def to_json(self):
        return (self.__dict__)
