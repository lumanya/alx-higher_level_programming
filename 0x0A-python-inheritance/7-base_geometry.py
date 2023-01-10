#!/usr/bin/python3
"""
Module 2-geometry

contains public instance method area that raise Exception if called
and integer_validator raise exception  if value is not int and less
or equal to 0
"""


class BaseGeometry():
    """
    Method:
     area(self)
     integer_validor(self, name, value)
     __init__(self)
    """

    def area(self):
        """  raise Exception if called  """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raise Exception if value in not int and less than or equal to 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
