#!/usr/bin/python3
"""Start of function load_from_json_file"""
import json


def load_from_json_file(filename):
    """create an object from a jsson file"""
    with open(filename, 'r', encoding="utf-8") as file:
        objet = json.load(file)
    return objet
