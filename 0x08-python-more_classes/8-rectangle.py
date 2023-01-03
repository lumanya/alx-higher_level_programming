#!/usr/bin/python3

"""
Module 2-rectangle
contains class Rectangle with private attribute wight and height
and public area and perimeter methods, allow printing using any given symbol,
delete instance, has public attribute to keep track of instances,
and has static method that returns bigger rectangle out of tow given
"""


class Rectangle:

    """
    Defines class Rectangle with private attribute awidth and wight

    Args:
      width (int): width
      height (int): heigh

    Attributes:
      number_of_instances (int): number of instances created and not deleted
      print_symbol (any type): used to print string represantaion

    Functions:
    __init__(self, width, height)
    width(self)
    height(self)
    width(self, value)
    height(self, value)
    perimeter(self)
    area(self)
    __str__(self)
    __repr__(self)
    __del__(self)
    bigger_or_equal(rect_1, rect_2)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initilize rectangles  """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        pic = "\n".join([str(self.print_symbol) * self.__width for row in range
                         (self.__height)])
        return pic

    def __repr__(self):
        """String Representaion to recreate anew instance """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Delete instance of a class """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        static method that returns biggest rectangle based on area

        Args:
          rect_1 (instance): instance of Rectangle class
          rect_2 (instance): instance of rectangle class
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rcetangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
