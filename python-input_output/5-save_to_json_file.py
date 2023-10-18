#!/usr/bin/python3
"""Start of function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """write my_obj in a text_file with JSON representation"""
    with open(filename, 'w', encoding="utf-8")as file:
        json.dump(my_obj, file)
