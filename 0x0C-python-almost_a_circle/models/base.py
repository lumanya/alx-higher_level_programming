#!/usr/bin/python3
"""
 base is Module contains base class
"""
import json


class Base:
    """
     Base class in which all classes inherit from this
    Attributes:
    __nb_obejects (private): private attribute
    method:
    to_json_string(list_dictionaries)

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize instance of a class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return []
        else:
            return json.dumps(list_dictionaries)
