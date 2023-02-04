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
    width(self)
    width(self, values)
    height(self)
    height(self, values)
    x(self)
    x(self, values)
    y(self)
    y(self, values)
    area(self)
    display(self)
    __str__(self)
    update(self, *args)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize instance of a class """

        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getting width values"""
        return self.__width

    @width.setter
    def width(self, values):
        """ setting values of width"""
        if type(values) is not int:
            raise TypeError("width must be an integer")
        if values <= 0:
            raise ValueError("width must be > 0")
        self.__width = values

    @property
    def height(self):
        """ getting height values"""
        return self.__height

    @height.setter
    def height(self, values):
        """ set values of height"""
        if type(values) is not int:
            raise TypeError("height must be an integer")
        if values <= 0:
            raise ValueError("height must be > 0")
        self.__height = values

    @property
    def x(self):
        """ return values of x"""
        return self.__x

    @x.setter
    def x(self, values):
        """ setting values of x"""
        if type(values) is not int:
            raise TypeError("x must be an integer")
        if values < 0:
            raise ValueError("x must be >= 0")
        self.__x = values

    @property
    def y(self):
        """ getting value of y"""
        return self.__y

    @y.setter
    def y(self, values):
        """ setting values of y"""
        if type(values) is not int:
            raise TypeError("y must be an integer")
        if values < 0:
            raise ValueError("y must be >= 0")
        self.__y = values

    def update(self, *args, **kwargs):
        """ assing argument to each attributes"""
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.__width = v
                elif k == 2:
                    self.__height = v
                elif k == 3:
                    self.__x = v
                else:
                    self.__y = v
        else:
            for k, value in kwargs.items():
                if k == "id":
                    self.id = value
                elif k == "width":
                    self.__width = value
                elif k == "width":
                    self.__height = value
                elif k == "x":
                    self.__x = value
                elif k == "y":
                    self.__y = value

    def area(self):
        """ calculating area of rectangel """
        return self.__height * self.__width

    def display(self):
        """ print in stdout The rectangel instance with character #"""
        print("\n" * self.__y +
              "\n".join(" " * self.__x + "#" * self.__width
                        for i in range(self.__height)))

    def __str__(self):
        """ print an [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)
