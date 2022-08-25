#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, div, mul

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = argv[2]
    if op == '+':
        print("{} + {} = {}".format(argv[1], argv[3], add(int(argv[1]),
              int(argv[3]))))
    elif op == '-':
        print("{} = {} = {}".format(argv[1], argv[3], sub(int(argv[1]),
                                    int(argv[3]))))
    elif op == '*':
        print("{} = {} = {}".format(argv[1], argv[3], mul(int(argv[1]),
                                    int(argv[3]))))
    elif op == '/':
        print("{} = {} = {}".format(argv[1], argv[3], div(int(argv[1]),
                                    int(argv[3]))))
    else:
        print("Unkown operator. Available operators: +, -, * and /")
        exit(1)
