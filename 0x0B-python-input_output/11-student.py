#!/usr/bin/python3
"""
Module 10-student

contains Student class
with public instance attributes: first_name,last_name and age
and public method to_json that retirve  a dictionary represenraion a Student
instance
"""


class Student:
    """
    Attributs:
     first_name (str): firstname
     last_name (str): lastname
     age (int): age
    Methods:
      def __init__(self, first_name, last_name, age)
      def to_json(self)
    """
    def __init__(self, first_name, last_name, age):
        """ instatiate objects of the class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieve dictionary repesentaion of Student instance """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic

    def reload_from_json(self, json):
        """ Transfer all attribute of json to self"""
        for k, v in json.items():
            setattr(self, k, v)
