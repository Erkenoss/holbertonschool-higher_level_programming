#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        lenght = len(my_string)
        for i in range(lenght):
            if my_string[i] == 'C' or my_string[i] == 'c':
                continue
            print("{}".format(my_string[i]), end="")
