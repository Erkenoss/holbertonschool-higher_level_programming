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
        if list_dictionaries is None or (isinstance(list_dictionaries, list) and all(isinstance(item, dict) for item in list_dictionaries)):
            return json.dumps(list_dictionaries)
        else:
            return f"[]"
