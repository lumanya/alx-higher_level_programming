#!/usr/bin/python3
new_list = []


def square_matrix_simple(matrix=[]):
    for i in matrix:
        new_list.append(list(map(lambda x: x ** 2, i)))
    return new_list
