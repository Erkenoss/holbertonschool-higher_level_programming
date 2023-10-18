#!/usr/bin/python3
"""Start of the function from_json_string"""
import json


def from_json_string(my_str):
    """Return an object in format json string"""
    return json.loads(my_str)
