#!/usr/bin/python3
"""start the function"""

import csv
import turtle
import json
import os


class Base:
    """funcion principal prueba"""

    __nb_objects = 0

    def __init__(self, id=None):
        """funcion principal prueba"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """funcion principal prueba"""
        if list_dictionaries is None or list_dictionaries is 0:
            return ('[]')
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """funcion principal prueba"""
        filename = (cls.__name__) + '.json'
        list_o = []
        if list_objs is not None:
            for i in list_objs:
                list_o.append(i.to_dictionary())
        with open(filename, 'w') as f:
            return f.write(Base.to_json_string(list_o))

    @staticmethod
    def from_json_string(json_string):
        """funcion principal prueba"""
        if json_string is None or json_string is 0:
            return ([])
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """funcion principal prueba"""
        if cls.__name__ == 'Rectangle':
            from models.rectangle import Rectangle
            dummy = cls(3, 7)
        if cls.__name__ == 'Square':
            from models.square import Square
            dummy = cls(3)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """funcion principal prueba"""
        list_l = []
        filename = (cls.__name__) + '.json'
        if os.stat(filename).st_size == 0:
            return []
        with open(filename, encoding="UTF-8") as f:
            data = f.read()
            string_r = Base.from_json_string(data)
            for instances in string_r:
                list_l.append(cls.create(**instances))
            return (list_l)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """funcion principal prueba"""
        filename = (cls.__name__) + '.csv'
        with open(filename, 'w') as csvfile:
            if cls.__name__ == 'Rectangle':
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            else:
                fieldnames = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for data in list_objs:
                writer.writerow(data.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """funcion principal prueba"""
        filename = (cls.__name__) + '.csv'
        list_l = []
        if os.stat(filename).st_size == 0:
            return []
        with open(filename, 'r', encoding="UTF-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                for key, value in i.items():
                    i[key] = value
                list_l.append(cls.create(**i))
                return (list_l)
