#!/usr/bin/python3
"""
 2-matrix_divied is module that contains matrix_divided function
 This function divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
     functions that divides all elements of a mtarix by div
     Args:
      matrix: list of lists of integrs/floats
      div: integer of float that divide all  element of materix
     Returns:
      returns new matrix
    """

    new_list = []
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(message)

    for element in matrix:
        if len(element) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            for i in element:
                if not isinstance(i, (float, int)):
                    raise TypeError(message)

    for element in matrix:
        element_list = []
        for i in element:
            element_list.append(round(i / div, 2))
        new_list.append(element_list)

    return new_list
