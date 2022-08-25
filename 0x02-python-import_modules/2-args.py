#!/usr/bin/python3

import sys

length = len(sys.argv)

if length == 1:
    print("0 arguments.")
elif length == 2:
    print("{} argument:\n1: {}".format(length - 1, sys.argv[1]))
else:
    print("{} arguments:".format(length - 1))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
