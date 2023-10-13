#!/usr/bin/python3
"""Start methode"""


def text_indentation(text):
    """start of text_indent"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    display_str = ""
    is_new_line  = False
    for char in text:
        if char in ['.', '?', ':']:
            display_str += "\n\n"
            is_new_line = True
        else:
            if char.isspace() and is_new_line:
                continue
            else:
                is_new_line = False
                display_str += char
    display_str = '\n'.join(line.strip() for line in display_str.split('\n'))

    print(display_str)
