#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    
    last = my_list[::-1]

    for i in range(len(last)):
        print("{:d}".format(last[i]))
