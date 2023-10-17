#!/usr/bin/python3
""" module 1-my_list """


class MyList(list):
    """start of class MyList"""
    def print_sorted(self):
        """print the element of a list in sorted order"""
        print(sorted(self))
