#!/usr/bin/python3
"""Start of function write_file"""


def write_file(filename="", text=""):
    """write text in a new file"""
    with open(filename, 'w', encoding="utf-8") as f:
        write_data = f.write(text)
        return write_data
