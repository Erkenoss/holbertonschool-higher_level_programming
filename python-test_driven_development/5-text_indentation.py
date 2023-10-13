#!/usr/bin/python3
"""Start methode"""


def text_indentation(text):
    """start of text_indent"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    display_str = ""
    for char in text:
        display_str += char
        if char in ['.', '?', ':']:
            print("{}\n".format(display_str.strip()))
            display_str = ""
    if display_str.strip() != "":
        print("{}".format(display_str.strip()), end="")
