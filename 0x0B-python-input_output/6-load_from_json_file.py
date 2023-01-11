#!/usr/bin/python3
"""
Module 6-load_from_json_file

contains load_from_json_file
that create an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    create an Object from a JSON file
    Args:
     filename (str): filename
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(f.read())
