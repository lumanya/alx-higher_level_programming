#!/usr/bin/python3
"""
Module 5-save_to_json_file

contains save_to_json_file functions
that write an objects to atextfile, using  a JSON repesentation
"""
import json


def save_to_json_file(my_obj, filename):
    """
     write an object to a text file, using a JSon representaion
    Args:
     my_obj (object): Python objects data structure
     filename (str): filename
    """

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
