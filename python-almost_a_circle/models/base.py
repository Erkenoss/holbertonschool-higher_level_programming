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
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances who inherits of Base
        """
        filename = type(list_objs[0]).__name__ + ".json"
        json_file = open(filename, "w")
        if list_objs is None:
            json.dump([], json_file)

        if type(list_objs[0]).__name__ == "Rectangle":
            new_dict = [item.__dict__ for item in list_objs]
            json_string = cls.to_json_string(new_dict)
            json.dump(new_dict, json_file)

        json_file.close()