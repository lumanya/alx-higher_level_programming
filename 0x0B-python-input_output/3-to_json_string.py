#!/usr/bin/python3
"""
Module 3-to_json_string

contains to_json_string function
that returns the JSON representation of an object(string)
"""


import json


def to_json_string(my_obj):
    """
     convert python data objects to JSON repesentation of objects
     Args:
      my_obj (object); python objects
     Return:
      return the JSON representaion of an objects(string)
    """

    return json.dumps(my_obj)
