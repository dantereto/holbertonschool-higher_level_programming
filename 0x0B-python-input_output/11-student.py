#!/usr/bin/python3
"""create the class """


class Student:
    """Instantiation """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """retrieves a dictionary representation of a Student"""

    def to_json(self, attrs=None):

        _dict = {}
        if type(attrs) == list:
            for i in attrs:
                if type(i) == int:
                    _dict = self.__dict__
                try:
                    _dict[i] = getattr(self, i)
                except:
                    pass
        else:
            _dict = self.__dict__
        return (_dict)
    """replaces all attributes of the Student"""

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
