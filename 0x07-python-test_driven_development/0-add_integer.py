#!/usr/bin/python3
"""
 0-add_integer is the module
 that has add_integer function that add two number and returns addition numbers
"""

def add_integer(a, b=98):
    """ add two number a and b
        a and b must be integerrs or float, otherwise raise TypeError exception
        with message a must be an integer or b must be an integer
        a and b must be first casted to integers if the are float
        Returns: a and b
    """
    if  not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
