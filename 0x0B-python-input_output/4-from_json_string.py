#!/usr/bin/python3
"""
Module 4-from_json_string

contains from_json_string functions
that returns an objects(python data structure) repesented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    return an obejects(Python data structure) repesented by JSON string
    Args:
     my_str (str): JSON
    """

    return json.loads(my_str)
