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
    from_json_string(json_string)
    create(cls, **dictionary)
    load_from_file(cls)
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

    @staticmethod
    def from_json_string(json_string):
        """ return the list of JSON representaion json_string
            Args:
              json_string: is the string representaion of a list of
                          dictionaries
        """

        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return an instance with all attribute set"""
        if cls.__name__ == "Square":
            dum_instance = cls(1)
        if cls.__name__ == 'Rectangle':
            dum_instance = cls(2, 3)
        dum_instance.update(**dictionary)
        return dum_instance

    @classmethod
    def load_from_file(cls):
        """ return list of instances """
        list_instances = []
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                list_output = cls.from_json_string(f.read())

            for instance_ in list_output:
                list_instances.append(cls.create(**instance_))
        except:
            pass
        return list_instances
