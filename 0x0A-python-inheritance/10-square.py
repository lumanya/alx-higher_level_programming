#!/usr/bin/python3
"""
Module 10-square

contains parent class Rectangle
with instation of private attributes  widtha and height, validated by parent

contains Square class
with instantiation of private attributes size, validated by parent
with area method
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherit from Rectangle
    method:
     __init__(self, width, height)
    """

    def __init__(self, size):
        """Validate and initialze widtha and height
        Args:
          width(int): private
          height(int): private
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
