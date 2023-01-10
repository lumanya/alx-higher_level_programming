#!/usr/bin/python3
"""
Module 2-is_same_class

contains method is_same_class
returns True is the objects is exactly an instance
of the spcefified class, otherwise False
"""


def is_same_class(obj, a_class):
    """
    Notes:
      use type() to get specific class
      use isinstance() to get class and any parent classes too
      use issubclass() to get what objects is a subclass o
    Args:
       obj (instance):  instance of a class
       a_class (class): class
     """

    if type(obj) ==  a_class:
        return True
    else:
        return False
