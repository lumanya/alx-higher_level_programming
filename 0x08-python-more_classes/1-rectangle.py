#!/usr/bin/python3

"""
Module 1-rectangle
contains class Rectangle
with private attribute wight and height
"""


class Rectangle:

    """
    Defines class Rectangle with private attribute awidth and wight

    Args:
      width (int): width
      height (int): height

    Functions:
    __init__(self, width, height)
    width(self)
    height(self)
    width(self, value)
    height(self, value)
    """

    def __init__(self, width=0, height=0):
        """ Initilize rectangles  """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets  width if int > 0  """
        if not isinstance(value, int):
            raise TypeError("width must be and integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter return height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter set width if int > 0  """
        if not isinstance(value, int):
            raise TypeError("height mujst be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
