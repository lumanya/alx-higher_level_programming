#!/usr/bin/python3
"""
Module 2-is_same_class

contains function that returns True is the objects is exactly an instance
of the spcefified class, otherwise False
"""


def is_same_class(obj, a_class):
    """
    Return True if the objects is eactyl an instance of the specified class,
    otherwise False

    Args:
       obj (instance):  instance of a class
       a_class (class): class
     """

    if type(obj) is  a_class:
        return True
    else:
        return False
