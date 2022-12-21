#!/usr/bin/python3
"""
Module 2-square

Defines class square with private attribute size and validate size
"""


class Square:
    """
    class Square definition
    """

    def __init__(self, size=0):
        """
        Initiliazies square

        Args:
            size (int): size of a side in a square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
