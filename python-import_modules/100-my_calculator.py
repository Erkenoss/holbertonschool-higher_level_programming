#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    count_args = len(argv)

    if count_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    prime = int(argv[1])
    second = int(argv[3])

    if argv[2] == "+":
        print("{} + {} = {}".format(argv[1], argv[3], add(prime, second)))
    elif argv[2] == "-":
        print("{} - {} = {}".format(argv[1], argv[3], sub(prime, second)))
    elif argv[2] == "*":
        print("{} * {} = {}".format(argv[1], argv[3], mul(prime, second)))
    elif argv[2] == "/":
        print("{} / {} = {}".format(argv[1], argv[3], div(prime, second)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
