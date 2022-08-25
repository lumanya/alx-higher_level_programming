#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv[1:])
    print("{} {}{}".format(length, "arguments" if (length) != 1 else
                           "argument", "." if (length) == 0 else ":"))
    for i in range(length):
        print("{}: {}".format(i + 1, argv[i + 1]))
