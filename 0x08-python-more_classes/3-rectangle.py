#!/usr/bin/python3

"""
Module 2-rectangle
contains class Rectangle with private attribute wight and height
and public area and perimeter methods and print #'s
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
    perimeter(self)
    area(self)
    __str__(self)
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
            raise TypeError("width must be an integer")
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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns area of rectangle  """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns perimeter of rectangle  """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """ Print Rectangles with #'s """
        if self.__height == 0 or self.__width == 0:
            return ""
        pic = "\n".join(["#" * self.__width for row in range(self.__height)])
        return pic
