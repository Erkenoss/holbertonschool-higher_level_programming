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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return a dict in format json"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save a file"""
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            dict_list = [obj.__dict__ for obj in list_objs]
            json_string = cls.to_json_string(dict_list)
            file.write(json_string)
