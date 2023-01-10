#!/usr/bin/python3
"""
Module 4-inherits_from.py

contains functions inherits_from
Returns True if the objects is an instance of aclasss that inherited(directly
of indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
     check wether the objects is an instance of a clas that inherited
    fro sepcified class

    Args:
     obj (objects): objects
     a_class (class): class

    Return:
      True if objects is an instance of a class that inherited from the given
      class
    """
    return (type(obj) is not a_class and issubclass(obj.__class__, a_class))
