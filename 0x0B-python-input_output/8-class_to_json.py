#!/usr/bin/python3
"""
Module 8-class_to_json

contains class_to_json which return dictionary discriptions with simple data
with simple data structure
"""


def class_to_json(obj):
    """
    Returns dictionary description with simple data structure
     (list, dictionary, string) for JSON serilization of an objects
    Args:
     obj: python object
    """
    return obj.__dict__
