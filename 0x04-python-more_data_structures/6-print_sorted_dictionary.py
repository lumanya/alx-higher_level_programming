#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    new = {i: a_dictionary[i] for i in sorted(a_dictionary)}
    for key, value in new.items():
        print("{}: {}".format(key, value))
