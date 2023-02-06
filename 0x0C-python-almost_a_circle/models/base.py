#!/usr/bin/python3
"""
 base is Module contains base class
"""
import json
import csv


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
    save_to_csv_file(cls)
    load_from_file_csv(cls)
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        objs = []
        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    writer.writerow([o.id, o.size, o.x, o.y])

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
        except FileNotFoundError:
            return list_instances
        return list_instances

    @classmethod
    def load_from_file_csv(cls):
        """ load data from csv file"""
        objs = []
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dic = {"id": int(row[0]), "width": int(row[1]),
                               "height": int(row[2]), "x": int(row[3]),
                               "y": int(row[4])}
                    if cls.__name__ == "Square":
                        dic = {"id": int(row[0]),
                               "size": int(row[1]),
                               "x": int(row[2]),
                               "y": int(row[3])}
                    o = cls.create(**dic)
                    objs.append(o)
        except FileNotFoundError:
            return objs
        return objs
