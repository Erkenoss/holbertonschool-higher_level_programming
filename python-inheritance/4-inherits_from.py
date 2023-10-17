#!/usr/bin/python3
"""Start of a function inherits_from"""


def inherits_from(obj, a_class):
    """return True if obj is an insstance of a_class ddirectly
    or not,from the speecific class"""
    return isinstance(obj, a_class) and type(obj) != a_class
