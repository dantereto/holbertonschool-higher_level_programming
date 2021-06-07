#!/usr/bin/python3
"""start the function"""


import json


import os


class Base:
    """start"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries is 0:
            return ('[]')
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = (cls.__name__) + '.json'
        list_o = []
        if list_objs is not None:
            for i in list_objs:
                list_o.append(i.to_dictionary())
        with open(filename, 'w') as f:
            return f.write(Base.to_json_string(list_o))

    def from_json_string(json_string):
        if json_string is None or json_string is 0:
            return ('[]')
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            from models.rectangle import Rectangle
            dummy = Rectangle(1, 1)
        if cls.__name__ == 'Square':
            from models.square import Square
            dummy = Square(1, 1)
        dummy.update(**dictionary)
        return (dummy)
