#!/usr/bin/python3
"""class base"""
import json


class Base:
    """Start of base class"""
    __nb_object = 0

    def __init__(self, id=None):
        """Start of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    def to_json_string(list_dictionaries):
        """return a dict in format json"""
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
