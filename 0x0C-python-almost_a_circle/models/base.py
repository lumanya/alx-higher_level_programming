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
    save_to_file(cls, list_objs)
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
        """ static method that python dictionary to json"""
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ class method that writes the JSON string represnation
         of list_objs toa file
        Args:
         cls - class
         list_objs - list of instnances who inretits of Bse
        """
        objs = []
        filename = cls.__name__ + ".json"

        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(objs))
