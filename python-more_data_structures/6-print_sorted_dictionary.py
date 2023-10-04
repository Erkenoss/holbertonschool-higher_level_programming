#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        for sort, sort2 in sorted(a_dictionary.items()):
            print("{}: {}".format(sort, sort2))
