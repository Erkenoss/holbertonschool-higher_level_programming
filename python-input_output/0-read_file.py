#!/usr/bin/python3
"""start of function read_file"""


def read_file(filename=""):
    """read a fle"""
    with open(filename, encoding="utf-8")as f:
        read_data = f.read()
        print(read_data)
