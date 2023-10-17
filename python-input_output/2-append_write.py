#!/usr/bin/python3
"""start of function append_write"""


def append_write(filename="", text=""):
    """append text in filename"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
