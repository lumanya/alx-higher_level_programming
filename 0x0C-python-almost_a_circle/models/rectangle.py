#!/usr/bin/python3
"""
 rectangle is the Module that contains rectangle class which inherit base class
"""
from models.base import Base


class Rectangle(Base):
    """
     Rectangle class inherit from Base class
    Attributes:
     __width: width of rectangle
    __height: height of a rectangel
    __x: x
    __y: y

    methods:
     __init__(self,width, height, x=0, y=0, id=None)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize instance of a class """

        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ getting width values"""
        return self.__width

    @width.setter
    def width(self, values):
        """ setting values of width"""
        self.__width = values

    @property
    def height(self):
        """ getting height values"""
        return self.__height

    @height.setter
    def height(self, values):
        """ set values of height"""
        self.__height = values

    @property
    def x(self):
        """ return values of x"""
        return self.__x

    @x.setter
    def x(self, values):
        """ setting values of x"""
        self.__x = values

    @property
    def y(self):
        """ getting value of y"""
        return self.__y

    @y.setter
    def y(self, values):
        """ setting values of y"""
        self.__y = values
