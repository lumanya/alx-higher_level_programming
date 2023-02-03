#!/usr/bin/python3
"""
 3-say_my_name is a module that contains say_my_name function
 that print "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
     this function print "My name is <first name> <last name>
    Args:
      first_name(str): hold first name
      last_name(str): hold last  name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
