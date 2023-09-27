#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count_args = len(argv)
    add_args = 0

    if count_args != 1:
        for i in range(count_args):
            if i != 0:
                add_args += int(argv[i])
        print("{}".format(add_args))
    else:
        print("0")
