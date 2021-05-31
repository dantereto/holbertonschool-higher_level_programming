#!/usr/bin/python3
def class_to_json(obj):
    class_obj = getattr(obj, '__dict__')
    return (class_obj)
