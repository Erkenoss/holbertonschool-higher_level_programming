#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count_args = len(sys.argv)

    if count_args == 1:
        print("0 arguments.")
    elif count_args == 2:
        print("{} argument:".format(count_args - 1))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(count_args - 1))
        for i in range(count_args):
            if i != 0:
                print("{}: {}".format(i, sys.argv[i]))
