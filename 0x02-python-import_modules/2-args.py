#!/usr/bin/python3

import sys

if len(sys.argv) - 1 == 0:
    print("0  arguments.")
else:
    print("{} argumets:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{} arguments : {}".format(i, sys.argv[i]))
