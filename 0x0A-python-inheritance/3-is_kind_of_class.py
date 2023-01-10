#!/usr/bin/python3
"""
Module 2-is_kind_of_class

contains method is_kind_of_class
return True if an object is an instance of, or if the object is an instance of
a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Function that check if obejcts is an instance of the given class
    Args:
     obj (objects) : object
     a_class (class): class

    return:
      True if the objets is an instance of the class
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
