#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
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
        
    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
