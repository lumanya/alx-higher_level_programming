#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is not None:
        return max([x for i, x in a_dictionary.items()])
    else:
        return None
