#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None:
        lenght = len(my_list)
        if idx < 0 or idx > lenght - 1:
            return my_list
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
