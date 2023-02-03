#!/usr/bin/python3
"""
 4-print_square Module that contains print_square function
 that prints square with the character #
"""


def print_square(size):
    """ print a square with characteer #
       Args:
         size: size lenght of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for row in range(size):
            print("#", end="")
        print()
