#!/usr/bin/python3
"""
Module 1-my_list

contains My_list class that inherit from  list class and has a public instance
public instance method print_sorted that prints list
"""


class MyList(list):
    """
    Inherit from list

    method:
       print_sorted(self)
     """

    def print_sorted(self):
        """print list of ints all sorted in acending order"""
        print(sorted(self))
