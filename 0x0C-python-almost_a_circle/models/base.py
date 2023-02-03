#!/usr/bin/python3
"""
 base is Module contains base class
"""


class Base:
    """
     Base class in which all classes inherit from this
    Attributes:
    __nb_obejects (private): private attribute
    """

    __nb_projects = 0

    def __init__(self, id=None):
        """ Initialize instance of a class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
